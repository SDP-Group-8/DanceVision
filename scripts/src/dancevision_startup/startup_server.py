import subprocess
import os
from pathlib import Path
import argparse
from multiprocessing import Process

from dancevision_startup.get_hostname import get_hostname
from dancevision_server.rest_server import run_app

def run_command(cmd: list, cwd=None, env=None):
    return subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, env=env)

def start_frontend(port):
    hostname = get_hostname()
    env = os.environ.copy()
    env["VITE_API_URL"] = f"http://{hostname}:{port}"

    frontend_path = Path(os.environ["DANCEVISION_APP"]) / "client"
    return run_command(["npm", "run", "dev"], frontend_path, env)

def start_backend(port, stream_address, stream_port, turtle_address, file):
    hostname = get_hostname()

    if turtle_address is not None:
        os.environ["ROS_MASTER_URI"]=f"http://{turtle_address}:11311"
        os.environ["ROS_HOSTNAME"]=hostname
    
    return Process(target=run_app, args=(hostname, port, turtle_address is None, stream_address, stream_port, file))

def startup_server(port, stream_address, stream_port, turtle_address, file):
    frontend = start_frontend(port)
    backend = start_backend(port, stream_address, stream_port, turtle_address, file)

    backend.start()
    backend.join()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port")
    parser.add_argument("--stream-address")
    parser.add_argument("--stream-port")
    parser.add_argument("--turtle-address")
    parser.add_argument("--file")
    args = parser.parse_args()

    startup_server(args.port, args.stream_address, args.stream_port, args.turtle_address, args.file)
