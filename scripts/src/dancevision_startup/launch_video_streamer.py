from dancevision_startup.commands import build_command, run_command_in_session
import subprocess
from pathlib import Path

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

def launch_video_streamer(script_location: Path, address: str, port: int):
    subprocess.run(["sh", script_location / "startup_video_streamer.sh", address, port])
