"""
This is one of a pair of programs meant to allow one computer to shut down many computers in an exhibit context.
This program ('server') runs on any computer that is NOT receiving the direct singal to shut down.
The 'client' program should run on the singular computer in the exhibit context that receives the signal to shutdown the exhibit (from a UPS, switch, etc)
"""

import socket
import os

HOST = ''
PORT = 1933
MSG = b"SHUTDOWN NOW"
RSP = b"SHUTDOWN CONFIRMED"

print("Server program is listening for shutdown commands from primary client")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if data[:len(MSG)] == MSG:
                print(f"Got shutdown MSG {data}")
                conn.sendall(RSP)
                os.system("shutdown /s /f /t 10")
            else: 
                print(f"Got {data= } instead of expected {data[:len(MSG)]}")
            if not data:
                break