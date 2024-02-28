from dancevision_startup.constants import AT_SUBNET
from dancevision_startup.commands import build_command, run_command_in_session

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

def launch_server(address, port):
    cmd = build_command(
        [
            "cd ~/Stream_Client",
            f"python3 -m http.server {port}"
        ]
    )
    run_command_in_session(pi_username, pi_password, cmd, address)
