import subprocess

def run(command):
		proccess = subprocess.Popen(command, stdout=subprocess.PIPE)
		return proccess.stdout.read()
