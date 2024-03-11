get_local_address()
{
    local_address=$(nmcli -g IP4.ADDRESS device show wlp2s0)
    echo $local_address | cut -d "/" -f 1
}