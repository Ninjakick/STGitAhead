import locale
import os
import subprocess
import sublime, sublime_plugin

class GitAheadCommand():
    def get_path(self):
        if self.window.active_view():
            return self.window.active_view().file_name()
        elif self.window.folders():
            return self.window.folders()[0]
        else:
            sublime.status_message(__name__ + ': No place to open GitAhead to')
            return False

class GitaheadOpenCommand(sublime_plugin.WindowCommand, GitAheadCommand):
    def is_enabled(self):
        return True

    def run(self, *args):
        path = self.get_path()
        if not path:
            return
        if os.path.isfile(path):
            path = os.path.dirname(path)

        settings = sublime.load_settings('Preferences.sublime-settings')
        gitahead_path = settings.get('gitahead_path', '/home/smartone/GitAhead/GitAhead/GitAhead')

        if gitahead_path in ['', None]:
            sublime.error_message(__name__ + ': GitAhead executable path not set, incorrect or no GitAhead?')
            return False

        if gitahead_path.endswith(".app"):
            subprocess.call(['open', '-na', gitahead_path, path])
        else:
            try:
                encoding = locale.getpreferredencoding(do_setlocale=True) or 'UTF-8'
                p = subprocess.Popen([gitahead_path], cwd=path.encode(encoding), shell=True)
            except Exception as e:
                sublime.error_message(__name__ + ' Error launching GitAhead ' + e.message)
