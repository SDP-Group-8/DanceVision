from dancevision_startup.startup_server import startup_server
from dancevision_startup.launch_command_listener import launch_command_listener

import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--port")
    parser.add_argument("--turtle-address")
    parser.add_argument("--stream-address")
    parser.add_argument("--stream-port")
    parser.add_argument("--file")

    args = parser.parse_args()

    launch_command_listener(args.turtle_address)
    startup_server(args.port, args.stream_address, args.stream_port, args.turtle_address, args.file)
