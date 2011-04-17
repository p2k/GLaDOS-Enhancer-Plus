
# Copyright (c) 2011, Patrick "p2k" Schneider
# Released under the GPL license
# http://www.gnu.org/copyleft/gpl.html

# For this script you'd need an apache http server with mod_python

__all__ = ["index"]

import simplejson, os.path

SCRIPT_BASENAME = os.path.basename(__file__)
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

JSON_DATA_PATH = os.path.join(SCRIPT_PATH, "glados_data.json")

def index(req, jsonp=""):
    req.content_type = 'text/javascript'
    
    if os.path.exists(JSON_DATA_PATH):
        data = simplejson.load(open(JSON_DATA_PATH, "r"))
    else:
        data = {}
    
    rdata = {
        "focus": data.get("focus", 0),
        "overallRate": data.get("overallRate", 0),
        "gameRates": data.get("gameRates", {}),
        "potatoRate": data.get("potatoRate", 0),
    }
    
    return "%s(%s)" % (jsonp, simplejson.dumps(rdata))

if __name__ == "__main__":
    # For testing
    class EmptyReq(object):
        content_type = None
    print index(EmptyReq(), jsonp="test")
