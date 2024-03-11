stream_address=$1
stream_port=$2

if [ $3 ];
then no_ros=--no-ros;
else :;
fi

. $DANCEVISION_SCRIPTS/get_local_address.sh
local_address=$(get_local_address)

cd $DANCEVISION_APP/client && npm run dev &
cd $DANCEVISION_APP/server && rest-api --address $local_address --port 8000 $no_ros --stream-address $stream_address --stream-port $stream_port &
