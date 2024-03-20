import argparse
from typing import Callable
from multiprocessing import Process

from dancevision_startup.commands import build_command, run_command_in_session
from dancevision_startup.get_hostname import get_hostname

import sys

pi_username = "pi"
pi_password = "raspberry"

def launch_chromium(address, port, on_command: Callable):
    cmd = build_command(
        [
            "export DISPLAY=:0",
            f"/usr/bin/chromium-browser 127.0.0.1:{port} --use-fake-ui-for-media-stream",
        ]
    )
    stdin, stdout, stderr = run_command_in_session(pi_username, pi_password, cmd, address)
    on_command(stdin, stdout, stderr)

def launch_server(local_address, address, port, on_command: Callable):
    cmd = build_command(
        [
            "cd ~/Stream_Client",
            f"echo 'const ADDRESS = \"{local_address}\"' > address.js",
            f"python3 -m http.server {port}"
        ]
    )
    stdin, stdout, stderr = run_command_in_session(pi_username, pi_password, cmd, address)
    on_command(stdin, stdout, stderr)

def launch_video_streamer(address, port, callable):
    hostname = get_hostname()

    p1 = Process(target = launch_chromium, args=(address, port, callable))
    p2 = Process(target = launch_server, args=(hostname, address, port, callable))

    p1.start()
    p2.start()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--address")
    parser.add_argument("--port")
    args = parser.parse_args()

    def read_output(stdin, stdout, stderr):
        stdout.readlines()

    launch_video_streamer(args.address, args.port, read_output)
