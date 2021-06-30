import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.ttk as ttk

from IPy import IP


def widgets(self, port: int):
    """
            Defining all Widgets

            Seperate Functions:
            self.usernamewidget() -> usernamewidget-Labels etc
            self.makeIPFrame() -> IP-Widgets etc
            self.makeMessageWidgets() -> explains itself
            self.configuregridweight() -> configures the weigths of the colums and rows
    """
    # Name-Label & Entry
    self.usernamewidget()
    self.portvariable = tk.StringVar(self, "Port: {}".format(port))
    self.port_Label = ttk.Label(self, textvariable=self.portvariable)
    self.port_Label.grid(row=0, column=2)

    # IP-Eingabe
    self.receiver_Label = ttk.Label(self, text="Empfänger (IP):")
    self.receiver_Label.grid(row=1, column=0, sticky="nsew")
    self.makeIPFrame()

    self.ausgabe = scrolledtext.ScrolledText(self)
    self.ausgabe.grid(row=3, column=0, columnspan=3, sticky="ew")
    self.ausgabe.tag_config("right", justify="right")
    self.ausgabe.configure(state='disabled')

    self.makeMessageWidgets()

    self.send_Button = ttk.Button(self, text="Send", command=self.send)
    self.send_Button.grid(row=4, column=2, sticky="w")

    self.configuregridweight()

    self.name_Entry.focus()


def makeMessageWidgets(self):
    self.msgcmd = self.register(self.validmessage)
    self.message_label = ttk.Label(
        self, text="Nachricht (max. 1001 characters):")
    self.message_label.grid(row=4, column=0, sticky="w")
    self.msg_Entry = ttk.Entry(
        self, validate="key", validatecommand=(self.msgcmd, "%P"))
    self.msg_Entry.grid(row=4, column=1, sticky="w")
    self.msg_Entry.bind("<Return>", self.send)


def usernamewidget(self):
    self.usernamecmd = self.register(self.validusername)
    self.name_Label = ttk.Label(self, text="Name (max. 8 characters):")
    self.name_Label.grid(row=0, column=0, sticky="nw",)
    self.name_Entry = ttk.Entry(
        self, validate="key", validatecommand=(self.usernamecmd, "%P"))
    self.name_Entry.grid(row=0, column=1, sticky="nw",)


def makeIPFrame(self):
    self.IPframe = ttk.LabelFrame(
        self, text="Enter IP here", relief=tk.SUNKEN)
    self.IPframe.grid(row=1, column=1, sticky="nsw")

    self.vcmd = self.register(self.checkIPEntry)

    self.ip_Entry_1_text = tk.StringVar()
    self.ip_Entry_1 = ttk.Entry(
        self.IPframe, width=5, textvariable=self.ip_Entry_1_text, validate="key", validatecommand=(self.vcmd, "%P"))
    self.ip_Entry_1.pack(side="left")
    self.ip_dot1 = ttk.Label(self.IPframe, text=".")
    self.ip_dot1.pack(side="left")

    self.ip_Entry_2_text = tk.StringVar()
    self.ip_Entry_2 = ttk.Entry(
        self.IPframe, width=5, textvariable=self.ip_Entry_2_text, validate="key", validatecommand=(self.vcmd, "%P"))
    self.ip_Entry_2.pack(side="left")
    self.ip_dot2 = ttk.Label(self.IPframe, text=".")
    self.ip_dot2.pack(side="left")

    self.ip_Entry_3_text = tk.StringVar()
    self.ip_Entry_3 = ttk.Entry(
        self.IPframe, width=5, textvariable=self.ip_Entry_3_text, validate="key", validatecommand=(self.vcmd, "%P"))
    self.ip_Entry_3.pack(side="left")
    self.ip_dot3 = ttk.Label(self.IPframe, text=".")
    self.ip_dot3.pack(side="left")

    self.ip_Entry_4_text = tk.StringVar()
    self.ip_Entry_4 = ttk.Entry(
        self.IPframe, width=5, textvariable=self.ip_Entry_4_text, validate="key", validatecommand=(self.vcmd, "%P"))
    self.ip_Entry_4.pack(side="left")
    self.invalidIP_Label = ttk.Label(
        self.IPframe, text="Invalid IP !", foreground="red")

    self.ip_Entry_1.bind("<FocusIn>", self.deleteinvIPLabel)
    self.ip_Entry_2.bind("<FocusIn>", self.deleteinvIPLabel)
    self.ip_Entry_3.bind("<FocusIn>", self.deleteinvIPLabel)
    self.ip_Entry_4.bind("<FocusIn>", self.deleteinvIPLabel)


def deleteinvIPLabel(self, event=None):
    self.invalidIP_Label.pack_forget()


def checkIPEntry(self, ippart):
    if ippart:
        if not ippart.isdigit():
            self.bell()
            return False
        else:
            if int(ippart) > 255 or int(ippart) < 0:
                self.bell()
                return False
            else:
                return True
    else:
        return True


def validmessage(self, message):
    if len(message) > 1001:
        self.bell()
        return False
    else:
        return True


def validusername(self, username):
    if len(username) > 8:
        self.bell()
        return False
    else:
        return True


def validIP(self):
    if self.user_IP != "...":
        try:
            IP(self.user_IP)
        except Exception:
            return False
        else:
            return True
    else:
        return True


if __name__ == "__main__":
    print("test")
