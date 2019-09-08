#!/bin/bash

docker rm -f servo

docker build -t therauch1/servo .
docker run -d --privileged --name servo --restart=always -p 42069:42069 therauch1/servo