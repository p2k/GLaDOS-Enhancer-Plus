
====================
GLaDOS Enhancer Plus
====================

-> `Quick download of the current version <https://github.com/p2k/GLaDOS-Enhancer-Plus/raw/master/glados_enhancer_plus.user.js>`_ for returning users or people who know everything about Userscripts.

Introduction
------------

**Hello folks!**

This is a collaborative effort for making a good countdown aid which directly enhances the official `GLaDOS@Home status page <http://www.aperturescience.com/glados@home/>`_.

The Project has been initiated by Aubron and p2k, both participators in the `Valve ARG <http://valvearg.com>`_ `IRC Channel <http://valvearg.com/wiki/IRC>`_. Due to its nature, this project is quite short-lived, but if you are a JavaScript developer and have some spare time, feel free to fork this project and make your push requests.

For the first release, the two scripts developed by the initiators will be merged. After that, more features will be added as we see fit or as your suggestions fly in.

Features
--------

- Updates all displayed bars, text and values every 30 seconds (via Ajax requests to the same site)
- Shows the percentage done in decimal numbers within the progress bars
- Does not modify the original countdown and does not intervene with Valve's JavaScript code
- Instead, shows a second countdown next to it, based on the percentage done and the time passed with linear progression
- Also shows the time difference between the official default release date and the calculated release date
- Highlights the current community focus
- **NEW in v1.1**: Removes the banner on top of the page

Installation Instructions
-------------------------

This Userscript will work with Google Chrome, Firefox and Opera.

*These instructions will work for other scripts too. Just open the correct URL to the script of your choice instead of clicking the hinted links in the following text. Note, however, that not all scripts will work in all browsers like ours. If in doubt, use Firefox which has the most support for Userscripts.*

**Google Chrome**

Most straightforward install. Just click `this link <https://github.com/p2k/GLaDOS-Enhancer-Plus/raw/master/glados_enhancer_plus.user.js>`_ and follow the instructions given by Chrome to install our script. It is treated like any normal extension. Look it up in the extensions list (Window -> Extensions) to uninstall it.

**Mozilla Firefox**

You need the `Greasemonkey add-on <https://addons.mozilla.org/firefox/addon/greasemonkey/>`_ to get any Userscripts running on this Browser. After you've installed Greasemonkey, click `this link <https://github.com/p2k/GLaDOS-Enhancer-Plus/raw/master/glados_enhancer_plus.user.js>`_ and a small window should pop up where you can install our script. Greasemonkey comes with its own menu where scripts can be deactivated or uninstalled. Open the add-ons list (Window -> Add-ons) and find the Userscripts entry on the left, next to the monkey icon.

**Opera**

For this browser, you need to create an empty folder somewhere on your computer (e.g. make a folder called "Userscripts" in your documents folder) which should hold all Userscripts. After you've done that, `download our script <https://github.com/p2k/GLaDOS-Enhancer-Plus/raw/master/glados_enhancer_plus.user.js>`_ and save it into that folder. Next, open the JavaScript options dialog (O menu -> Settings (or Preferences on Mac) -> Advanced -> Content -> JavaScript options) and select your created folder there. To uninstall, just remove our script from your folder.

**All browsers**

At this point, our script should have been installed and is ready to run. Hit up the official `GLaDOS@Home status page <http://www.aperturescience.com/glados@home/>`_ to see it in action.

**And one last thing**

The script might change at any time within the next hours (well, until the project will eventually die after the release of Portal 2). Revisit this site every now and then to look for updates.
