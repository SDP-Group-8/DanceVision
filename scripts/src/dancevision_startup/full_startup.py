from dancevision_startup.startup_server import startup_server
from dancevision_startup.launch_command_listener import launch_command_listener
from dancevision_startup.launch_planner import run_planner

import argparse
import time

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--port")
    parser.add_argument("--turtle-address")
    parser.add_argument("--stream-address")
    parser.add_argument("--stream-port")
    parser.add_argument("--file")

    args = parser.parse_args()

    wheels, actuator = launch_command_listener(args.turtle_address)
    frontend, backend = startup_server(args.port, args.stream_address, args.stream_port, args.turtle_address, args.file)

    stdin, stdout, stderr = wheels
    
    line = ""
    while "process[master]: started" not in line:
        line = stdout.readline()

    # Why is this still needed?
    time.sleep(5)

    p = run_planner(args.turtle_address)

    p.start()
    backend.start()

    stdout.readlines()
