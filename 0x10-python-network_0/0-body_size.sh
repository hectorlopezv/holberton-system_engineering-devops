#!/usr/bin/env bash
#how to use curl
curl -si 0:5000 | grep "Content-Length" | awk '{print $2}' 
