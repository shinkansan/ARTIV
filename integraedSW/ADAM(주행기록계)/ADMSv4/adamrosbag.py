

class rosbagRecord(QThread):

	def __init__(self, comms, parent = None):
		QThread.__init__(self)
		self.main = parent
		self.working = True
		self.commands = comms

	def __del__(self):
		print("Record End")
		self.wait()

	def run(self):
		pipe = subprocess.Popen(self.commands, shell = True)



pipe = subprocess.Popen(self.commands, shell=True, executable="/bin/bash",
			stdout=subprocess.PIPE).stdout
            output = pipe.read().decode("utf-8")     
            self.cpu_output.emit(float(output))
