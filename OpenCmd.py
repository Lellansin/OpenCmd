
import sublime, sublime_plugin
import os;

class OpenCmdCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		cwd = os.getcwd();
		path = self.view.file_name();
		platform = sublime.platform();
		
		if(platform == 'windows'):
			# get file directory
			path = path[0:path.rfind('\\')];
			# cd directory and start a cmd
			command = path[0:2] + ' && ' + 'cd "' + path + '" && start cmd'
			# sublime.message_dialog(command)
			os.system(command)
		elif(platform == 'linux'):
			# get file directory
			path = path[0:path.rfind('/')];
			# cd directory and start a terminal
			command = 'cd ' + path + ' && gnome-terminal'
			os.system(command)
		else:
			sublime.error_message('Sorry, this plugin doestn\'t support your system now. :(')


		# dubug info
		# sublime.error_message(platform)
