address=$1
port=$2

. $DANCEVISION_SCRIPTS/get_local_address.sh
local_address=$(get_local_address)

python3 -c "from dancevision_startup.launch_video_streamer import launch_chromium; launch_chromium('$address', $port)" &
python3 -c "from dancevision_startup.launch_video_streamer import launch_server; launch_server('$local_address', '$address', $port)" &
