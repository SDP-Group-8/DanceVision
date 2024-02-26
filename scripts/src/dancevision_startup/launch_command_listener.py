import argparse

import paramiko

from dancevision_startup.constants import AT_SUBNET

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--address", dest="address")
    args = parser.parse_args()

    ssh = paramiko.SSHClient()
    ssh.connect(AT_SUBNET + args.address, username="pi", password="r00t")

    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("chromium-browser")
