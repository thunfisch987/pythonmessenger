"""
Python Messenger
Author: Oliver Sader
"""

from . import netw
import messengerUI
import socket as st
import sys


def main():
    serversocket = netw.MessengerSocket(st.AF_INET, st.SOCK_DGRAM)
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
