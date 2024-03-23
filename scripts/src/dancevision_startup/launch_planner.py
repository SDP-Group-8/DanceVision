import argparse
import roslaunch
import os

from multiprocessing import Process, Queue

from dancevision_startup.environment import setup_environment

def launch_planner(turtle_address, queue):
    setup_environment(turtle_address)
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, [os.environ["DANCEVISION_LAUNCH"]])
    launch.start()
    signal = queue.get()
    launch.shutdown()

def run_planner(turtle_address, queue: Queue):
    return Process(target=launch_planner, args=(turtle_address, queue, ))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--address")
    args = parser.parse_args()

    queue = Queue()

    process = run_planner(args.address, queue)
    process.start()
    process.join()
