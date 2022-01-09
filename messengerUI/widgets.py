import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.ttk as ttk

from IPy import IP


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


def configuregridweight(self):
    self.grid_rowconfigure(0, weight=1)
    self.grid_rowconfigure(2, weight=1)
    self.grid_rowconfigure(3, weight=1)
    self.grid_rowconfigure(4, weight=1)
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure(2, weight=1)


def widgetmaking(self, port: int):
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

    # IP-Eingabe
    self.makeIPFrame(port)

    self.ausgabe = scrolledtext.ScrolledText(self)
    self.ausgabe.grid(row=3,
                      column=0,
                      columnspan=3,
                      sticky="ew")
    self.ausgabe.tag_config("right", justify="right")

    self.makeMessageWidgets()

    self.send_Button = ttk.Button(self)
    self.send_Button["text"] = "Send"
    self.send_Button["command"] = self.sendmsg
    self.send_Button.grid(row=4,
                          column=2,
                          sticky="w")

    # configuring
    self.configuregridweight()
    self.ausgabe.configure(state='disabled')
    self.name_Entry.focus()


def makeMessageWidgets(self):
    self.msgcmd = self.register(self.validmessage)
    self.message_label = ttk.Label(self)
    self.message_label["text"] = "Nachricht (max. 1001 characters):"

    self.msg_Entry = ttk.Entry(self)
    self.msg_Entry["validate"] = "key"
    self.msg_Entry["validatecommand"] = (self.msgcmd, "%Ps")

    self.message_label.grid(row=4,
                            column=0,
                            sticky="w")
    self.msg_Entry.grid(row=4,
                        column=1,
                        sticky="w")

    self.msg_Entry.bind("<Return>",
                        self.sendmsg)


def usernamewidget(self):
    """
    Defines the Username-Widgets (and Port)
     - UsernameFrame
     - port_Label
     - name_Label
     - name_Entry
    """
    self.usernamecmd = self.register(self.validusername)

    self.UsernameFrame = ttk.LabelFrame(self)
    self.UsernameFrame["text"] = "Username: (max. 8 characters)"
    self.UsernameFrame["relief"] = tk.SUNKEN

    # self.name_Label = ttk.Label(self.UsernameFrame)
    # self.name_Label["text"] = "Name (max. 8 characters):"

    self.name_Entry = ttk.Entry(self.UsernameFrame)
    self.name_Entry["validate"] = "key"
    self.name_Entry["validatecommand"] = (self.usernamecmd, "%P")

    self.sound_variable = tk.IntVar(self)
    self.sound_variable.set(1)
    self.sound_Checkbox = ttk.Checkbutton(self.UsernameFrame)
    self.sound_Checkbox["text"] = "Message Sound"
    self.sound_Checkbox["variable"] = self.sound_variable

    self.topmost_Button = ttk.Button(
        self.UsernameFrame, text="AlwaysOnTop", command=self.makeTopMost, style='topmost.TButton')

    self.UsernameFrame.grid(row=0, column=0, columnspan=3, sticky="nsew")
    # self.name_Label.grid(row=0, column=0, sticky="nw")
    # self.name_Entry.grid(row=0, column=1, sticky="nw")
    # self.port_Label.grid(row=0, column=2)
    # self.name_Label.pack(side="left")
    self.name_Entry.pack(side="left")
    self.sound_Checkbox.pack(side="left")
    self.topmost_Button.pack(side="right")


def makeIPFrame(self, port: int):
    self.vcmd = self.register(self.checkIPEntry)

    self.BigFrame = ttk.LabelFrame(self)
    self.BigFrame["text"] = "Empfänger (IP):"
    self.IPframe = ttk.LabelFrame(self.BigFrame)
    self.IPframe["text"] = "Enter IP Here"
    self.IPframe["relief"] = tk.SUNKEN

    self.ip_Entry_1 = ttk.Entry(self.IPframe)
    self.ip_dot1 = ttk.Label(self.IPframe, text=".")
    self.ip_Entry_2 = ttk.Entry(self.IPframe)
    self.ip_dot2 = ttk.Label(self.IPframe, text=".")
    self.ip_Entry_3 = ttk.Entry(self.IPframe)
    self.ip_dot3 = ttk.Label(self.IPframe, text=".")
    self.ip_Entry_4 = ttk.Entry(self.IPframe)

    self.ip_Entry_1["width"] = self.ip_Entry_2["width"] = self.ip_Entry_3["width"] = self.ip_Entry_4["width"] = 5
    self.ip_Entry_1["validate"] = self.ip_Entry_2["validate"] = self.ip_Entry_3["validate"] = self.ip_Entry_4["validate"] = "key"
    self.ip_Entry_1["validatecommand"] = self.ip_Entry_2["validatecommand"] = self.ip_Entry_3[
        "validatecommand"] = self.ip_Entry_4["validatecommand"] = (self.vcmd, "%P")

    self.invalidIP_Label = ttk.Label(self.IPframe)
    self.invalidIP_Label["text"] = "Invalid IP !"
    self.invalidIP_Label["foreground"] = "red"

    self.port_Label = ttk.Label(self.BigFrame)
    self.port_Label["text"] = f"Port: {port}"

    self.BigFrame.grid(row=1,
                       column=0,
                       columnspan=3,
                       sticky="nsew")
    self.IPframe.pack(side="left")

    self.ip_Entry_1.pack(side="left")
    self.ip_dot1.pack(side="left")
    self.ip_Entry_2.pack(side="left")
    self.ip_dot2.pack(side="left")
    self.ip_Entry_3.pack(side="left")
    self.ip_dot3.pack(side="left")
    self.ip_Entry_4.pack(side="left")

    self.port_Label.pack(side="right")

    self.ip_Entry_1.bind("<FocusIn>", self.deleteinvIPLabel)
    self.ip_Entry_2.bind("<FocusIn>", self.deleteinvIPLabel)
    self.ip_Entry_3.bind("<FocusIn>", self.deleteinvIPLabel)
    self.ip_Entry_4.bind("<FocusIn>", self.deleteinvIPLabel)


def deleteinvIPLabel(self, event=None):
    self.invalidIP_Label.pack_forget()


def checkIPEntry(self, ippart):
    if ippart:
        if ippart.isdigit() and int(ippart) <= 255 and int(ippart) >= 0:
            return True
        self.bell()
        return False
    else:
        return True


def validmessage(self, message):
    if len(message) <= 1001:
        return True

    self.bell()
    return False


def validusername(self, username):
    if len(username) <= 8:
        return True

    self.bell()
    return False


def validIP(self):
    if self.user_IP == "...":
        return True

    try:
        IP(self.user_IP)
    except Exception:
        return False
    else:
        return True


__all__ = ["widgets", "makeMessageWidgets", "usernamewidget", "makeIPFrame", "deleteinvIPLabel", "checkIPEntry",
           "validmessage", "validusername", "validIP", "configuregridweight", "makeTopMost", "windowsettings"]

if __name__ == "__main__":
    print("test")
    print("test")
