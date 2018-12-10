#!/bin/bash

short_file="./passing_tests.txt"

while read -r line
do
    defects4j coverage -t $line
    cp coverage.xml coverage_$line.xml
    > coverage.xml
done < $short_file
