#!/bin/bash

echo "GDSC{A_g00D_h4ck3r_5hould_h4v3_5Tr0ng_scr1pt1ng_5k1lls}" >flag.txt

zip flag1.zip flag.txt

for ((i=2; i<1338; i++))
do
	zip flag$i.zip flag$(($i-1)).zip
	rm flag$(($i-1)).zip
done
