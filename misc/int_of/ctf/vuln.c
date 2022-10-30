#include <stdio.h>

int main(){
  unsigned char impossible_num;
  int new_num;
  

  
  char c;
  char flag[] = "GDSC{WeLl_That's_a_tRap}";
  printf("Enter a number :");
  scanf("%d",&new_num);
  if (new_num > 0){
  	impossible_num = 38;
  	impossible_num =new_num + impossible_num;
  	printf("%d",impossible_num);
   	if (new_num > 0 &&  impossible_num == 15){
      	printf("\nGood job use netcat to take the flag from our server ");
      	}}
  else{
	printf("try again with a positive num ");
	}

  

return 0;
}
