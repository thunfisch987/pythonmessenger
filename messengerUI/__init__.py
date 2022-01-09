import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from tkinter import simpledialog
from tkinter import scrolledtext
import tkinter.ttk as ttk
import tkinter as tk


class MessengerWindow(tk.Tk):
    """
    Window
    """
    from .widgets import widgetmaking, makeMessageWidgets, usernamewidget, makeIPFrame, deleteinvIPLabel, checkIPEntry, validmessage, validusername, validIP, configuregridweight, makeTopMost, windowsettings
    from networking import startlistening, listenformsg, Message, sendmsg, send

    def __init__(self, port: int, serversocket):
        self.port = port
        # Ausführen der Init-Funktion von Tk(), also dem Window
        super(MessengerWindow, self).__init__()
        try:
            pygame.mixer.init()
            self.sound = pygame.mixer.Sound("./sound.ogg")
        except Exception as e:
            print(e)

        # Eigenschaftens
        self.windowsettings()

        # Erschaffen der Widgets etc.
        self.widgetmaking(port)

        # Erschaffen des Sockets (IPv4, UDP) und binden an alle Adressen mit gg. Port
        # Starten des Threads der auf einkommende Nachrichten hört
        self.serversocket = serversocket
        self.startlistening()
        self.buttonstyle = ttk.Style()

    @property
    def user_IP(self):
        return self.ip_Entry_1.get() + "." + self.ip_Entry_2.get() + "." + self.ip_Entry_3.get() + "." + self.ip_Entry_4.get()


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


__all__ = ["MessengerWindow", "PortWindow"]

if __name__ == "__main__":
    print("use __init__.py in messenger folder")
