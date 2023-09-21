#!/bin/bash

# 定义LANIP
lanip=$(hostname -I | grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' | egrep 192.168.3.*)

# 配置iptables
iptables -t nat -A POSTROUTING -s 192.168.200.0/24 -o ens37 -j MASQUERADE
iptables -t nat -A POSTROUTING -s 192.168.200.0/24 -o ens37 -j SNAT --to-source "${lanip}"

# 添加内网必须路由
route add -net 10.0.0.0 netmask 255.0.0.0 gw 192.168.3.1