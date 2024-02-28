address=$1
port=$2

# local_address=$(nmcli -g IP4.ADDRESS device show wlp2s0)
# local_address=$(echo $local_address | cut -d "/" -f 1)

# export VITE_BASE_URL=$local_address
# cd ~/DanceVision/src/stream_client
# npm run dev -- --host --port $2 &

python3 -c "from dancevision_startup.launch_video_streamer import launch_chromium; launch_chromium('$address', $port)" &
python3 -c "from dancevision_startup.launch_video_streamer import launch_server; launch_server('$address', $port)" &
