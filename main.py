"""
Python Messenger
Author: Oliver Sader
"""
from networking import MessengerSocket
import messengerUI
# from dataclasses import dataclass
# from tkinter import simpledialog
# from tkinter import scrolledtext
# import tkinter.ttk as ttk
# import tkinter as tk
# import threading as thr
import socket as st
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# import json
# import pygame
# from IPy import IP
import sys


def main():
    serversocket = MessengerSocket(st.AF_INET, st.SOCK_DGRAM)
    bound = False
    while not bound:
        if len(sys.argv) == 1:
            port = messengerUI.PortWindow().get_port()
        else:
            try:
                int(sys.argv[1])
            except ValueError:
                raise SystemExit(
                    'Usage: Messenger.py <Port: int> [Port must be integer!]')
            else:
                port = sys.argv[1]
        try:
            serversocket.bind(("", port))
        except:
            pass
        else:
            bound = True
        root = messengerUI.MessengerWindow(port, serversocket)
        root.focus_force()
        root.mainloop()


if __name__ == "__main__":
    main()
