import os
import subprocess
import time
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def ip():
    subprocess.run(["netsh", "int", "ip","reset"], shell=True)
def tcp():
    subprocess.run(["netsh","int", "tcp", "reset"], shell=True)
def winsock():
    subprocess.run(["netsh", "winsock","reset"], shell=True)
def flush():
    subprocess.run(["ipconfig", "/flushdns"], shell=True)
def register():
    subprocess.run(["ipconfig", "/registerdns"], shell=True)
def release():
    subprocess.run(["ipconfig", "/release"], shell=True )
def renew():
    subprocess.run(["ipconfig", "/renew"], shell=True)

def restart_computer():
    print("O computador será reiniciado para que as alterações sejam concluídas...")
    time.sleep(10)
    os.system("shutdown /r /t 0")

if __name__ == "__main__":
    
    if is_admin():
       ip()
       tcp()
       winsock()
       flush()
       register()
       release()
       renew()
       restart_computer()
    else:
        print("Solicitando privilégios de administrador...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)