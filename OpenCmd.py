
import sublime, sublime_plugin
import os, sys;


class OpenCmdCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		cwd = os.getcwd();
		path = self.view.file_name();
		platform = sys.platform;

		if(platform == 'win32'):
			# get file directory
			path = path[0:path.rfind('\\')];
			# cd directory and start a cmd
			command = path[0:2] + ' && ' + 'cd "' + path + '" && start cmd"'
			os.system(command)
		else:
			self.view.insert(edit, 0, 'Sorry, this plugin doestn\'t support your system now')


		# dubug info
		# self.view.insert(edit, 0, platform)