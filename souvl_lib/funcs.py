import os
import subprocess

def status():
    status=subprocess.run(['mpc','status'],stdout=subprocess.PIPE)
    return status.stdout.decode('utf-8')


def play_pause():
    os.system("mpc toggle")

def prev():
    os.system("mpc prev")

def next():
    os.system("mpc next")

def stop():
    os.system("mpc prev")

def random():
    os.system("mpc random")

def shuffle():
    os.system("mpc shuffle")

def repeat():
    os.system("mpc repeat")
