import os
def status(file_name):
	try:
		file = open(file_name, 'r')
		output = file.read()
		file.close()
		return output
	except FileNotFoundError:
		print("File does not exist")

def main():
	connection = status("STATUS.CFW")
	file2 = open("STATUS.CFW", "w")
	if connection == "Disconnected":
		print("Attempting connection")
		os.system("warp-cli.exe connect")
		file2.write("Connected")
		file2.close()
		
	elif connection == "Connected":
		print("Attempting disconnection")
		os.system("warp-cli.exe disconnect")
		file2.write("Disconnected")
		file2.close()

main()
		
	