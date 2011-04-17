
# Copyright (c) 2011, Patrick "p2k" Schneider
# Released under the GPL license
# http://www.gnu.org/copyleft/gpl.html

# For this script you need the mechanize python package installed

__all__ = [] # Locks out mod_python

import mechanize, simplejson, os.path
from HTMLParser import HTMLParser

SCRIPT_BASENAME = os.path.basename(__file__)
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

JSON_DATA_PATH = os.path.join(SCRIPT_PATH, "glados_current_focus.json")

VALVEARG_URL = "http://valvearg.com/wiki/Valve_ARG_Wiki"

class IDSeeker(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.id = None
        self.__inID = False
    
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "div" and attrs.has_key("id") and attrs["id"] == "HP2LYAppID": # This hidden field is believed to contain the correct ID
            self.__inID = True
    
    def handle_data(self, data):
        if self.__inID:
            try:
                self.id = int(data)
            except:
                self.id = None
    
    def handle_endtag(self, tag):
        self.__inID = False

def runUpdate():
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_refresh(False)
    
    idSeeker = IDSeeker()
    
    r = browser.open(VALVEARG_URL)
    idSeeker.feed(r.read())
    
    theId = idSeeker.id
    if theId == None:
        theId = 0
    
    data = {"current_focus": theId}
    
    open(JSON_DATA_PATH, "w").write(simplejson.dumps(data))

if __name__ == "__main__":
    runUpdate()
