stream_address=$1
stream_port=$2
turtle_address=$3

sh $DANCEVISION_SCRIPTS/startup_command_listener.sh $turtle_address &
sh $DANCEVISION_SCRIPTS/startup_server.sh $stream_address $stream_port &
