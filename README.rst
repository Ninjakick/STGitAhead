Integration GitAhead with sublimtext
====================================

Very simple plugin to open GitAhead (https://gitahead.github.io/gitahead.com/) from Sublime Text (http://www.sublimetext.com/).

Installing
----------

**Using Git:** Clone the repository in your Sublime Text Packages directory and restart Sublime Text:

    git clone https://github.com/Ninjakick/STGitAhead

**Using the Package Control plugin:** The easiest way to install GitAhead is through Package Control,
which can be found at http://wbond.net/sublime_packages/package_control .

Once you install Package Control, restart Sublime Text 2 and open the Command Palette.

Select "Package Control: Install Package", wait while Package Control fetches the latest package list,
then select GitAhead when the list appears.

The advantage of using this method is that Package Control will automatically keep this plugin up to date.

Usage
-----

After install GitAhead you are enable to lauch it via terminal like "Path_to_installation_dir/GitAhead"

Open the command palette and execute the ``GitAhead: Open GitAhead`` command to open the GIT repository
in which the currently opened file is located.

Sample user key binding to execute the command::

    { "keys": ["super+."], "command": "GitAhead_open" }



Changelog
---------
v0.1 (15-12-2021):

* Initial version

License
-------
See the LICENSE.txt file.
