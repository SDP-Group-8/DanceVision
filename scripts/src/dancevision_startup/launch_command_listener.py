from typing import List
from dancevision_startup.commands import build_command, run_command_in_session

SOURCE_CMD = "source /opt/ros/kinetic/setup.bash"

def build_ros_command(commands: List):
    return build_command([SOURCE_CMD] + commands)

def run_command_listener(address: str):
    cmd = build_ros_command(["cd ~/catkin_ws", "source devel/setup.sh", "roslaunch turtlebot3_bringup turtlebot3_robot.launch"])
    run_command_in_session("pi", "turtlebot", cmd, address)
