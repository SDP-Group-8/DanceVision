from typing import List
import paramiko

from dancevision_startup.constants import AT_SUBNET

BASHRC_CMD = "source ~/.bashrc"

def build_command(cmd: List[str]):
    return " && ".join([BASHRC_CMD] + cmd)

def run_command_in_session(username, password, command, address):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(AT_SUBNET + address, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
    print(stdout.read())
    exit_code = stdout.channel.recv_exit_status()
    print(f"Exit code is {exit_code}")
