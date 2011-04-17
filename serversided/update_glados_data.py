
# Copyright (c) 2011, Patrick "p2k" Schneider
# Released under the GPL license
# http://www.gnu.org/copyleft/gpl.html

# For this script you need the mechanize python package installed

__all__ = [] # Locks out mod_python

import mechanize, simplejson, os.path, re, time
from HTMLParser import HTMLParser

SCRIPT_BASENAME = os.path.basename(__file__)
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

JSON_DATA_PATH = os.path.join(SCRIPT_PATH, "glados_data.json")

VALVEARG_URL = "http://valvearg.com/wiki/Valve_ARG_Wiki"
GLADOS_URL = "http://www.aperturescience.com/glados@home/"

OVERALL_MAX_PIXELS = 494.0
GAME_MAX_PIXELS = 457.0

MAX_SAMPLES = 12 # = 60 / 5

RE_WIDTH = re.compile(r'width: *([0-9]+)px')
RE_POTATO_COUNT = re.compile(r'X *([0-9,]+)')

class IDSeeker(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.id = 0
        self.__inID = False
    
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        # We are using the official data field of hasportal2launchedyet.com here too
        if tag == "div" and attrs.get("id", "") == "HP2LYAppID":
            self.__inID = True
    
    def handle_data(self, data):
        if self.__inID:
            try:
                self.id = int(data)
            except:
                self.id = 0
    
    def handle_endtag(self, tag):
        self.__inID = False

class ProgressSampler(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.gameProgress = {}
        self.potatoCount = 0
        self.overallProgress = 0.0
        self.__inGameRow = None
        self.__inPotatoCount = None
    
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "div":
            if attrs.get("class", "") == "game_row":
                self.__inGameRow = attrs["id"].split("_")[-1]
            elif self.__inGameRow != None and "game_progress" in attrs.get("class", ""):
                if "game_progress_complete" in attrs["class"]:
                    self.gameProgress[self.__inGameRow] = 1.0
                else:
                    pixels = float(RE_WIDTH.search(attrs["style"]).group(1))
                    self.gameProgress[self.__inGameRow] = round(pixels / GAME_MAX_PIXELS, 5)
            elif attrs.get("id", "") == "potato_count":
                self.__inPotatoCount = ""
            elif attrs.get("id", "") == "overall_progress_bar":
                pixels = float(RE_WIDTH.search(attrs["style"]).group(1))
                self.overallProgress = round(pixels / OVERALL_MAX_PIXELS, 5)
    
    def handle_data(self, data):
        if self.__inPotatoCount != None:
            self.__inPotatoCount += data
    
    def handle_endtag(self, tag):
        self.__inGameRow = None # This closes processing already after the game_progress div, but that's ok
        if self.__inPotatoCount != None:
            self.potatoCount = int(RE_POTATO_COUNT.search(self.__inPotatoCount).group(1).replace(",", ""))
        self.__inPotatoCount = None

def deriveCurrentRates(samples):
    ret = {"overallRate": 0, "gameRates": {}, "potatoRate": 0}
    
    if len(samples) > 1:
        # We only take the first and last sample as reference the other samples
        # are kept because they have to slide through the one-hour window
        firstSample = samples[0]
        lastSample = samples[-1]
        
        timeStart = firstSample["timestamp"]
        timeEnd = lastSample["timestamp"]
        timeFrame = timeEnd - timeStart
        
        ret["overallRate"] = round((lastSample["overallProgress"]-firstSample["overallProgress"]) * 60 / timeFrame, 8)
        for gameId, firstValue in firstSample["gameProgress"].iteritems():
            lastValue = lastSample["gameProgress"][gameId]
            ret["gameRates"][gameId] = round((lastValue-firstValue) * 60 / timeFrame, 8)
        ret["potatoRate"] = round((lastSample["potatoCount"]-firstSample["potatoCount"]) * 60 / timeFrame, 8)
    
    return ret

def runUpdate():
    if os.path.exists(JSON_DATA_PATH):
        data = simplejson.load(open(JSON_DATA_PATH, "r"))
    else:
        data = {}
    
    allSamples = data.setdefault("allSamples", [])
    
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_refresh(False)
    
    # Get current focus
    
    idSeeker = IDSeeker()
    
    r = browser.open(VALVEARG_URL)
    idSeeker.feed(r.read())
    
    data["focus"] = idSeeker.id
    
    # Sample current progress
    
    progressSampler = ProgressSampler()
    
    r = browser.open(GLADOS_URL)
    try: # Code is error-prone if Valve changes certain things, but it is highly unlikely
        progressSampler.feed(r.read())
        thisSample = {
           "timestamp": time.time(),
            "overallProgress": progressSampler.overallProgress,
            "gameProgress": progressSampler.gameProgress,
            "potatoCount": progressSampler.potatoCount
        }
        allSamples.append(thisSample)
    except:
        pass
    
    if len(allSamples) > MAX_SAMPLES:
        allSamples.pop(0) # Remove oldest sample
    
    data.update(deriveCurrentRates(allSamples))
    
    simplejson.dump(data, open(JSON_DATA_PATH, "w"))

if __name__ == "__main__":
    runUpdate()
