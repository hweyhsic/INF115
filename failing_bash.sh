#!/bin/bash

short_file="./failing_tests.txt"

while read -r line
do
    defects4j coverage -t $line
    cp coverage.xml ~/INF115/parsing/failed_output_files/coverage_$line.xml
    > coverage.xml
done < $short_file
