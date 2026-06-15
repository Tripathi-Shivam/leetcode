#!/bin/bash

FILE=${1#spark-local/app/code/}

docker exec spark-master \
    /opt/spark/bin/spark-submit \
    /opt/spark-app/code/$FILE