# Challenge name

## Write-up

Solution script:

```bash
#!/bin/bash


for (( i=100;i>0;i-- ))
do
        unzip flag$i.zip
        rm flag$i.zip
done

cat *.txt
```



## Flag

`GDSC{A_g00D_h4ck3r_5hould_h4v3_5Tr0ng_scr1pt1ng_5k1lls}`
