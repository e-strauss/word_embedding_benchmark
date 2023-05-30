#!/bin/bash

while getopts ":m" opt; do
    case $opt in
        m)
        echo -e "java -Xmx7g -Xms7g -Xmn600m
            -cp target/SystemDS.jar:target/lib/*
            org.apache.sysds.api.DMLScript
            -f $1
            -exec singlenode
            -args $2 $3 $4 $5\n"

        java -Xmx7g -Xms7g -Xmn400m \
            -cp target/SystemDS.jar:target/lib/* \
            org.apache.sysds.api.DMLScript \
            -f $1 \
            -exec singlenode \
            -args $2 $3 $4 $5
            exit 0
        ;;
        \?)
            echo "Invalid option: -$OPTARG"
            ;;
    esac
done

echo -e "java -Xmx4g -Xms4g -Xmn600m
    -cp target/SystemDS.jar:target/lib/*
    org.apache.sysds.api.DMLScript
    -f $1
    -exec singlenode
    -config config.xml
    -args $2 $3 $4 $5\n"

java -Xmx7g -Xms7g -Xmn400m \
    -cp target/SystemDS.jar:target/lib/* \
    org.apache.sysds.api.DMLScript \
    -f $1 \
    -exec singlenode \
    -config config/config.xml \
    -args $2 $3 $4 $5
exit 0


