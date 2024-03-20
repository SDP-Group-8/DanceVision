from typing import List
import paramiko

BASHRC_CMD = "source ~/.bashrc"

def build_command(cmd: List[str]):
    return " && ".join([BASHRC_CMD] + cmd)

def run_command_in_session(username, password, command, address):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(address, username=username, password=password)
    return ssh.exec_command(command, get_pty=True)
