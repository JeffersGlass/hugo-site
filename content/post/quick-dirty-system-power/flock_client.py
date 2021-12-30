"""
This is one of a pair of programs meant to allow one computer to shutdown many computers in an exhibit context.
This program ('client') is meant to run on the singular computer that recveives a set signal to shutdown the exhibit. This signal may come from a button or switch, a system log (Say, via UPS), etc, which then runs this script.
The server program should be running on any computers that need to be shutdown in this context.
This client program steps through the list of provided servers and tells them to shut down, then shuts itself down.
"""

import socket
import os
from time import sleep

socket.setdefaulttimeout(10)
PORT = 1933
MSG = b'SHUTDOWN NOW'
RSP = b"SHUTDOWN CONFIRMED"

deviceIPs = [
    "172.16.0.2"
]
attempts = 0
MAX_ATTEMPTS = 5

print("Client program is contacting remote computers to shut them down")

while len(deviceIPs) > 0:
    attempts += 1
    if attempts > MAX_ATTEMPTS:
        print(f"System could not shut down the following IPs: {deviceIPs}")
        print("Shutting down self in 15 seconds")
        sleep(15)
        break
    for ip in deviceIPs:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"Attempting to connect tp {ip}, attempt {attempts} of {MAX_ATTEMPTS} (timeout is {int(socket.getdefaulttimeout())}s)")
            try:
                s.connect((ip, PORT))
            except TimeoutError as err:
                print("Connection timed out")
                continue
            print(f"Connection successful, sending message: {MSG}")
            s.sendall(MSG)
            data = s.recv(1024)
            print(f"Received {repr(data)}")
            if data[:len(RSP)] == RSP:
                print(f"Received shutdown confirmation message from host at ip {ip}")
                deviceIPs.remove(ip)
            else:
                print(f"Got some other message than we expected from host at ip {ip}: {data}")
    sleep(1)
else:
    print("Successfully shut down all remote IPs, shutting down self in 10 seconds")
    sleep(10)
os.system("shutdown /s /f /t 10")