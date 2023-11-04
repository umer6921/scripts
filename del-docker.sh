#!/bin/bash

sudo systemctl stop docker
sudo apt-get purge docker.io -y
sudo apt-get purge docker-ce docker-ce-cli containerd.io
sudo groupdel docker
echo "Docker deleted"
