#!/bin/sh

[[ -f /bin/redis-server ]] && exit 0
cd /var/tmp
wget http://download.redis.io/releases/redis-3.0.1.tar.gz
tar xzf redis-3.0.1.tar.gz
cd redis-3.0.1
make
make install
cd utils
chmod +x install_server.sh
./install_server.sh
