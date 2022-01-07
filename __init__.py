"""
Python Messenger
Author: Oliver Sader
"""

from tkinter import simpledialog
from tkinter import scrolledtext
import tkinter.ttk as ttk
import tkinter as tk
import threading as thr
import socket as st
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import json
import pygame
from IPy import IP
import sys


class Messenger(tk.Tk):
    """
    Window
    """
    from makewidgets import widgets, makeMessageWidgets, usernamewidget, makeIPFrame, deleteinvIPLabel, checkIPEntry, validmessage, validusername, validIP
    from networking import startlistening, listenformsg

    def __init__(self, port: int, serversocket):
        self.port = port
        # Ausführen der Init-Funktion von Tk(), also dem Window
        super(Messenger, self).__init__()
        try:
            pygame.mixer.init()
            self.sound = pygame.mixer.Sound("./sound.ogg")
        except Exception as e:
            print(e)

        # Eigenschaftens
        self.windowsettings()

        # Erschaffen der Widgets etc.
        self.widgets(port)

        # Erschaffen des Sockets (IPv4, UDP) und binden an alle Adressen mit gg. Port
        # Starten des Threads der auf einkommende Nachrichten hört
        self.serversocket = serversocket
        self.startlistening()
        self.buttonstyle = ttk.Style()

    def makeTopMost(self):
        if self.wm_attributes("-topmost") == 1:
            self.wm_attributes("-topmost", 0)
            self.buttonstyle.configure(
                'topmost.TButton', background='SystemButtonFace')
        else:
            self.wm_attributes("-topmost", 1)
            self.buttonstyle.configure(
                'topmost.TButton', background='palegreen')

    def windowsettings(self):
        self.title("Python Messenger")
        # self.geometry("700x500")
        # self.minsize(700, 500)
        # self.maxsize(700, 500)

    def configuregridweight(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def sendmsg(self, event=None):
        """Funktion zum Senden einer Nachricht"""

        if self.msg_Entry.get() == "":
            return
        self.empfaenger = "localhost"
        if not self.validIP():
            self.bell()
            self.invalidIP_Label.pack()
        else:
            self.send()

    def send(self):  # suggested by Sorcery
        if self.user_IP != "...":
            self.empfaenger = self.user_IP
        self.msgdict = {
            "name": self.name_Entry.get(),
            "msg": self.msg_Entry.get()
        }
        self.jsonmsg = json.dumps(self.msgdict)
        # senden der Nachricht an Ziel-Adresse über Socket
        self.serversocket.sendto(self.jsonmsg.encode(
            "utf-8"), (self.empfaenger, self.port))
        # löschen des Inhalts des Eingabe-Widgets
        self.ausgabe.configure(state='normal')
        if self.msgdict["name"] == "":
            self.ausgabe.insert(
                tk.END, f"You: '{self.msgdict['msg']}'\n", "right")
        else:
            self.ausgabe.insert(
                tk.END, f"{self.msgdict['name']} (You): '{self.msgdict['msg']}'\n", "right")
        self.ausgabe.configure(state='disabled')
        self.ausgabe.see("end")
        self.msg_Entry.delete(0, tk.END)

    class Message():
        pass

    @property
    def user_IP(self):
        return self.ip_Entry_1.get() + "." + self.ip_Entry_2.get() + "." + self.ip_Entry_3.get() + "." + self.ip_Entry_4.get()


class MessengerSocket(st.socket):
    def __init__(self, family, type):
        super(MessengerSocket, self).__init__(family, type)


class PortWindow(tk.Tk):
    port: int

    def get_port(self) -> int:
        """\
        Create a simpledialog asking for the port.
        
        If port is None (Dialog was closed) the port is set to 15200
        """
        self.withdraw()
        self.port = simpledialog.askinteger("Port", "What Port?")
        if self.port is None:
            self.port = 15200
        self.destroy()
        return self.port


def main():
    serversocket = MessengerSocket(st.AF_INET, st.SOCK_DGRAM)
    bound = False
    while not bound:
        if len(sys.argv) == 1:
            port = PortWindow().get_port()
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
        root = Messenger(port, serversocket)
        root.focus_force()
        # root.wm_attributes("-topmost", 1)
        root.mainloop()


if __name__ == "__main__":
    main()