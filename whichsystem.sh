#!/bin/bash

if [ $# -ne 1 ]; then
    echo -e "\n[!] Uso: $0 <direccion-ip>\n"
    exit 1
fi
 
get_ttl() {
    ttl=$(ping -c 1 $1 | grep ttl | awk -F' ' '{print $6}' | awk -F= '{print $2}')
    echo $ttl
}
 
get_os() {
    ttl=$1
    if [[ $ttl -ge 0 && $ttl -le 64 ]]; then
        echo "Linux"
    elif [[ $ttl -ge 65 && $ttl -le 128 ]]; then
        echo "Windows"
    elif [[ $ttl -ge 129 && $ttl -le 255 ]]; then
        echo "Solaris/AIX"
    else
       echo "No Found"
    fi
}
 
ip_address=$1
 
ttl=$(get_ttl $ip_address)
os_name=$(get_os $ttl)
echo -e "\n$ip_address (ttl -> $ttl): $os_name\n"
