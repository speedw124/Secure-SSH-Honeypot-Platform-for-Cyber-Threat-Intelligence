#!/bin/bash
# Block suspicious IPs
iptables -A INPUT -s 192.168.1.50 -j DROP

