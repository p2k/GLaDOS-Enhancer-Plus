
# Copyright (c) 2011, Patrick "p2k" Schneider
# Released under the GPL license
# http://www.gnu.org/copyleft/gpl.html

# For this script you'd need an apache http server with mod_python

__all__ = ["index"]

import os.path

SCRIPT_BASENAME = os.path.basename(__file__)
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

JSON_DATA_PATH = os.path.join(SCRIPT_PATH, "glados_current_focus.json")

def index(req, jsonp=""):
    if os.path.exists(JSON_DATA_PATH):
        data = open(JSON_DATA_PATH, "r").read()
    else:
        data = '{"current_focus": 0}'
    req.content_type = 'text/javascript'
    return "%s(%s)" % (jsonp, data.strip())

if __name__ == "__main__":
    # For testing
    class EmptyReq(object):
        content_type = None
    print index(EmptyReq(), jsonp="test")
