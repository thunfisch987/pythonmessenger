import json
import socket as st
import threading as thr
import tkinter as tk


def makesocket(self, port: int):
    self.serversocket = st.socket(st.AF_INET, st.SOCK_DGRAM)
    self.port = port
    self.serversocket.bind(("", self.port))
    receivethread = thr.Thread(target=self.listenformsg, daemon=True)
    receivethread.start()


def listenformsg(self):
    while True:
        jsondata, addr = self.serversocket.recvfrom(1024)
        self.sound.play()
        jsondata = jsondata.decode("utf-8")
        data = json.loads(jsondata)
        if data["name"] == "":
            self.ausgabe.configure(state='normal')
            self.ausgabe.insert(
                tk.END, "{} : '{}' \n".format(addr[0], data["msg"]))
            self.ausgabe.configure(state='disabled')
        else:
            self.ausgabe.configure(state='normal')
            self.ausgabe.insert(
                tk.END, "{} : '{}' \n".format(data["name"], data["msg"]))
            self.ausgabe.configure(state='disabled')


if __name__ == '__main__':
	print("networking")
