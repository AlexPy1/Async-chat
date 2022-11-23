import subprocess
import os


def more_clients(num):
    for _ in range(num):
        a = subprocess.Popen(['python', 'r_client.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)

    return


more_clients(3)
