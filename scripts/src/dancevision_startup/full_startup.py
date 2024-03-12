from dancevision_startup.startup_server import startup_server
from dancevision_startup.launch_command_listener import launch_command_listener

import argparse

def line_buffered(f):
    line_buf = ""
    while not f.channel.exit_status_ready():
        line_buf += bytes.decode(f.read(1))
        if line_buf.endswith('\n'):
            yield line_buf
            line_buf = ""

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
