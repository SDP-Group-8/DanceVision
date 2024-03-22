import os

from dancevision_startup.get_hostname import get_hostname

def setup_environment(turtle_address):
    hostname = get_hostname()

    os.environ["ROS_MASTER_URI"]=f"http://{turtle_address}:11311"
    os.environ["ROS_HOSTNAME"]=hostname
