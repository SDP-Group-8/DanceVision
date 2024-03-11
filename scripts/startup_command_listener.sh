address=$1

. $DANCEVISION_SCRIPTS/setup_ros_variables.sh
$(setup_ros_variables $address)

python3 -c "from dancevision_startup.launch_command_listener import run_command_listener; run_command_listener('$address')" & 
python3 -c "from dancevision_startup.launch_command_listener import run_wheels_listener; run_wheels_listener('$address')" &
