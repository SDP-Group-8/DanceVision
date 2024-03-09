address=$1
port=$2

local_address=$(nmcli -g IP4.ADDRESS device show wlp2s0)
local_address=$(echo $local_address | cut -d "/" -f 1)

python3 -c "from dancevision_startup.launch_video_streamer import launch_chromium; launch_chromium('$address', $port)" &
python3 -c "from dancevision_startup.launch_video_streamer import launch_server; launch_server('$local_address', '$address', $port)" &
