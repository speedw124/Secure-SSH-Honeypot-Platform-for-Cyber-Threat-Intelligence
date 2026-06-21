#!/bin/bash
set -e

echo "Fixing filebeat.yml permissions..."
chmod 644 /usr/share/filebeat/filebeat.yml
chown root:root /usr/share/filebeat/filebeat.yml

echo "Filebeat permissions fixed. Starting filebeat..."
exec filebeat -e -strict.perms=false
