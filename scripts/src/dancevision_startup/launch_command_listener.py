from typing import List
from dancevision_startup.commands import build_command, run_command_in_session

SOURCE_CMD = "source /opt/ros/noetic/setup.bash"

turtle_username = "pi"
turtle_password = "raspberry"

def build_ros_command(commands: List):
    return build_command([SOURCE_CMD, "cd ~/catkin_ws", "source devel/setup.sh"] + commands)

def run_wheels_listener(address: str):
    cmd = build_ros_command(["roslaunch turtlebot3_bringup turtlebot3_robot.launch"])
    run_command_in_session(turtle_username, turtle_password, cmd, address)

def run_command_listener(address: str):
    cmd = build_ros_command(["rosrun control_listener run_listener"])
    run_command_in_session(turtle_username, turtle_password, cmd, address)
