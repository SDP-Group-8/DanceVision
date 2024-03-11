setup_ros_variables()
{
    . $DANCEVISION_SCRIPTS/get_local_address.sh
    export ROS_MASTER_URI=http://$1:11311
    export ROS_HOSTNAME=$(get_local_address)
}

setup_ros_variables $1
