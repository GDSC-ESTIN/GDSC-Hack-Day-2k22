#!/bin/bash


for (( i=1337;i>0;i-- ))
do
	unzip flag$i.zip
	rm flag$i.zip
done

cat *.txt
