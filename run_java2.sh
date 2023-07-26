#!/bin/bash
args_single="-Xmx210g -Xms210g -Xmn21g \
    -cp target2/SystemDS.jar:target2/lib/* \
    org.apache.sysds.api.DMLScript \
    -f $1 \
    -debug \
    -stats \
    -exec singlenode \
    -config config/config.xml \
    -args $2 $3 $4 $5"

args_multi="-Xmx210g -Xms210g -Xmn21g \
            -cp target2/SystemDS.jar:target/lib/* \
            org.apache.sysds.api.DMLScript \
            -f $1 \
            -stats \
            -exec singlenode \
            -args $2 $3 $4 $5"

while getopts ":m" opt; do
    case $opt in
        m)
        echo -e $args_multi
        java $args_multi
        exit 0
        ;;
        \?)
            echo "Invalid option: -$OPTARG"
            exit 0
            ;;
    esac
done

echo -e $args_single
java $args_single

exit 0

