#!/bin/sh
[[ -f /usr/local/bin/jsonrpcstub ]] && exit 0
	# 
	cd /var/tmp

	# 1:	
	#
	echo "INSTALLING dependency jsoncpp.."
	git clone https://github.com/open-source-parsers/jsoncpp.git
	cd jsoncpp/
	mkdir -p build && cd build && cmake -DCMAKE_CXX_FLAGS="-fPIC" ../ && make && make install
	rc=$?
	if [[ $rc != 0 ]]; then
		echo "FAILED to install jsoncpp. This is unexpected. Contact the owner of the Vagrant file fo help."
		exit $rc
	fi
	echo "INSTALLING dependency jsoncpp.. Done"

	# 2:
	#	
	cd /var/tmp
	echo "INSTALLING dependency argtables2-13.."
	output=argtable.tar.gz

	wget -q https://sourceforge.net/projects/argtable/files/argtable/argtable-2.13/argtable2-13.tar.gz/download -O $output
	tar xf $output
	cd argtable2-13 && ./configure && make && make install
	rc=$?
	if [[ $rc != 0 ]]; then
		echo "FAILED to install argtable. This is unexpected. Contact the owner of the Vagrant file fo help."
		exit $rc
	fi
	echo "INSTALLING dependency argtables2-13.. Done"

	git clone git://github.com/cinemast/libjson-rpc-cpp.git


	# 3:
	#
	cd /var/tmp
	echo "INSTALLING dependency jsonrpccpp.."
	git clone https://github.com/cinemast/libjson-rpc-cpp.git
	cd libjson-rpc-cpp
	git checkout v0.5.0
	mkdir -p build && cd build && cmake ../ && make && make install
	rc=$?
	if [[ $rc != 0 ]]; then
		echo "FAILED to install json-rpc-cpp. This is unexpected. Contact the owner of the Vagrant file fo help."
		exit $rc
	fi
        ldconfig /usr/local/lib
	echo "INSTALLING dependency jsoncpp.. Done"
