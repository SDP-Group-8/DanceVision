from typing import List
import paramiko
import subprocess

BASHRC_CMD = "source ~/.bashrc"
SOURCE_CMD = ". /opt/ros/noetic/setup.bash"
WORKSPACE_SOURCE_CMD = ". devel/setup.sh"

def build_command(cmd: List[str]):
    return " && ".join([BASHRC_CMD] + cmd)

def run_command_in_session(username, password, command, address):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(address, username=username, password=password)
    return ssh.exec_command(command, get_pty=True)

def run_command(cmd: list, cwd=None, env=None):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, env=env)
