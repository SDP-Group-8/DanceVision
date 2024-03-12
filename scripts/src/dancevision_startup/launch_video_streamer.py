import argparse
from multiprocessing import Process

from dancevision_startup.commands import build_command, run_command_in_session
from dancevision_startup.get_hostname import get_hostname

pi_username = "pi"
pi_password = "raspberry"

def launch_chromium(address, port):
    cmd = build_command(
        [
            "export DISPLAY=:0",
            f"/usr/bin/chromium-browser 127.0.0.1:{port} --use-fake-ui-for-media-stream",
        ]
    )
    run_command_in_session(pi_username, pi_password, cmd, address)

def launch_server(local_address, address, port):
    cmd = build_command(
        [
            "cd ~/Stream_Client",
            f"echo 'const ADDRESS = \"{local_address}\"' > address.js",
            f"python3 -m http.server {port}"
        ]
    )
    run_command_in_session(pi_username, pi_password, cmd, address)

def launch_video_streamer(address, port):
    hostname = get_hostname()
    p1 = Process(target = launch_chromium, args=(address, port))
    p2 = Process(target = launch_server, args=(hostname, address, port))

    p1.start()
    p2.start()
 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--address")
    parser.add_argument("--port")
    args = parser.parse_args()

    launch_video_streamer(args.address, args.port)
