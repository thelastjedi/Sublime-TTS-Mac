import sublime
import sublime_plugin
import os

class tts_mac(sublime_plugin.TextCommand):
    def run(self, edit):
        selected_section = self.view.sel()
        to_speak = []
        for selection in selected_section:
        	to_speak.append(self.view.substr(selection).strip())
        x = ' '.join(to_speak)
        if len(x):
        	x = "say '%s'" %(x)
        	os.system(x)
        else:
        	sublime.status_message('TTS: No text selected')