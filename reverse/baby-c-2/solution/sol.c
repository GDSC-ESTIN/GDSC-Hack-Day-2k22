#include <stdio.h>

int main(){

char  even[17]= {71 ,83 ,123 ,84 ,95 ,117 ,53 ,95 ,118 ,110 ,38 ,48 ,68 ,98 ,116 ,115};
char odd[17]={68 ,67 ,49 ,115 ,74 ,53 ,116 ,51 ,51 ,95 ,95 ,68 ,95 ,121 ,101 ,125};

for (int i=0; i<32;i++)if(i%2==0)printf("%c",even[i/2]);else printf("%c",odd[i/2]);
printf("\n");
}

