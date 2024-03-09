address=$1
python3 -c "from dancevision_startup.launch_command_listener import run_command_listener; run_command_listener('$address')" & 
python3 -c "from dancevision_startup.launch_command_listener import run_roscore; run_roscore('$address')"
