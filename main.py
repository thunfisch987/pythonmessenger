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
    TODO: export Functions to seperate files and so on
    """
    from makewidgets import widgets, makeMessageWidgets, usernamewidget, makeIPFrame, deleteinvIPLabel, checkIPEntry, validmessage, validusername, validIP
    from networking import makesocket, listenformsg

    def __init__(self, port: int, serversocket):
        # Ausführen der Init-Funktion von Tk(), also dem Window
        super(Messenger, self).__init__()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound("./sound.ogg")

        # Eigenschaften
        self.windowsettings()

        # Erschaffen der Widgets etc.
        self.widgets(port)

        # Erschaffen des Sockets (IPv4, UDP) und binden an alle Adressen mit gg. Port
        # Starten des Threads der auf einkommende Nachrichten hört
        self.serversocket = serversocket
        self.makesocket()
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
            self._extracted_from_sendmsg_12()

    def _extracted_from_sendmsg_12(self):  # suggested by Sorcery
        if self.user_IP != "...":
            self.empfaenger = self.user_IP
        self.msgdict = {
            "name": self.name_Entry.get(),
            "msg": self.msg_Entry.get()}
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

    @property
    def user_IP(self):
        return self.ip_Entry_1.get() + "." + self.ip_Entry_2.get() + "." + self.ip_Entry_3.get() + "." + self.ip_Entry_4.get()


def main():
    serversocket = st.socket(st.AF_INET, st.SOCK_DGRAM)
    bound = False
    while not bound:
        if len(sys.argv) == 1:
            portwindow = tk.Tk()
            portwindow.withdraw()
            port = simpledialog.askinteger("Port", "What Port?")
            portwindow.destroy()
            if port is None:
                port = 15200
        else:
            try:
                int(sys.argv[1])
            except ValueError:
                raise SystemExit(
                    f"Usage: Messenger.py <Port: int> [Port must be integer!]")
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
    # try:
    #     os.chdir("./messenger")
    # except OSError:
    #     pass
    # if len(sys.argv) == 1:
    #     portwindow = tk.Tk()
    #     portwindow.withdraw()
    #     port = simpledialog.askinteger("Port", "What Port?")
    #     portwindow.destroy()
    # else:
    #     try:
    #         int(sys.argv[1])
    #     except ValueError:
    #         raise SystemExit(
    #             f"Usage: Messenger.py <Port: int> [Port must be integer!]")
    #     else:
    #         port = sys.argv[1]
    # if not isinstance(port, int):
    #     port = 15200
    # serversocket = st.socket(st.AF_INET, st.SOCK_DGRAM)
    # try:
    #     serversocket.bind(("", port))
    # except:
    #     print()
    # else:
    #     root = Messenger(port)
    #     root.focus_force()
    #     root.wm_attributes("-topmost", 1)
    #     root.mainloop()
