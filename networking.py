import json
import socket as st
import threading as thr
import tkinter as tk


def makesocket(self):
    receivethread = thr.Thread(target=self.listenformsg, daemon=True)
    receivethread.start()


def listenformsg(self):
    while True:
        jsondata, addr = self.serversocket.recvfrom(1024)
        self.sound.play()
        jsondata = jsondata.decode("utf-8")
        data = json.loads(jsondata)
        self.ausgabe.configure(state='normal')
        if data["name"] != "":
            if addr[0] == "127.0.0.1":
                self.ausgabe.insert(
                    tk.END, f"{data['name']} (You): '{data['msg']}' \n")
            else:
                self.ausgabe.insert(
                    tk.END, f"{data['name']} : '{data['msg']}' \n")
        elif addr[0] == "127.0.0.1":
            self.ausgabe.insert(
                tk.END, f"{addr[0]} (You): '{data['msg']}' \n")
        else:
            self.ausgabe.insert(
                tk.END, f"{addr[0]} : '{data['msg']}' \n")
        self.ausgabe.configure(state='disabled')
        self.ausgabe.see("end")


if __name__ == '__main__':
	print("networking")
