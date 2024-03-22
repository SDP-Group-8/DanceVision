import argparse
import roslaunch
import os

from multiprocessing import Process

from dancevision_startup.environment import setup_environment

def launch_planner(turtle_address):
    setup_environment(turtle_address)
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, [os.environ["DANCEVISION_LAUNCH"]])
    launch.start()

def run_planner(turtle_address):
    return Process(target=launch_planner, args=(turtle_address,))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--address")
    args = parser.parse_args()

    process = run_planner(args.address)
    process.start()
    process.join()
