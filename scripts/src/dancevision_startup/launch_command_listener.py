from typing import List
import argparse

from dancevision_startup.commands import build_command, run_command_in_session

SOURCE_CMD = "source /opt/ros/noetic/setup.bash"

turtle_username = "pi"
turtle_password = "raspberry"

def build_ros_command(commands: List, address: str):
    set_ros_uri = f"export ROS_MASTER_URI=http://{address}:11311"
    set_domain_id = f"export ROS_HOSTNAME={address}"
    
    return build_command([SOURCE_CMD, set_ros_uri, set_domain_id, "cd ~/catkin_ws", "source devel/setup.sh"] + commands)

def run_wheels_listener(address: str):
    cmd = build_ros_command(["roslaunch turtlebot3_bringup turtlebot3_robot.launch"], address)
    return run_command_in_session(turtle_username, turtle_password, cmd, address)

def run_command_listener(address: str):
    cmd = build_ros_command(["rosrun control_listener run_listener"], address)
    return run_command_in_session(turtle_username, turtle_password, cmd, address)

def launch_command_listener(address):
    wheels_listener = run_wheels_listener(address)
    command_listener = run_command_listener(address)
    return wheels_listener, command_listener

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--address")
    args = parser.parse_args()

    launch_command_listener(args.address)
