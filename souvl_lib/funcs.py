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

def get_vol():
    vol=subprocess.run(['pamixer','--get-volume'],stdout=subprocess.PIPE)
    return int(vol.stdout.decode('utf-8'))

def set_volume(val):
    os.system(f"pamixer --set-volume {val}")

def song_seek(val):
    os.system(f"mpc seek {val}%")

def get_progress():
    vol=subprocess.run(["mpc"],stdout=subprocess.PIPE)
    time=vol.stdout.decode('utf-8').splitlines()[1].split()[-1][1:-2]
    return int(time)
