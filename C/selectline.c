#include<stdio.h>
#include<string.h>

/*should expect user to enter unexpected type one of the possible is to do nothing*/
int main(void) {
  int i,j;
  char c, input, line[15];
  while (c=getchar() != EOF){
    input = c;
    printf("the input is: %c",input);
    c = getchar();
    while (i < 15) {
      line[i] = getchar();
      i = i + 1;}
    /*get the empty space*/
    /*check point*/
    printf("Checkpoint01");
    for (i = 0; i <15; i++){
      if (line[i] == input){
	j = 1;}
      //printf(line);
      //c = getchar();
    }  
    switch(j){
		//if it is in the line then print everything
    case 1:
      printf("Checkpoint02");
      for (i=0;i<15;i++){
	printf("%s",line[i]);
      }
      while (c = getchar() != '\n'){
	putchar(c);
      }
	  //set j to 0 to exit the switch
	j=0;
    case 0:
      printf("\n");
	break;
    }
  }
  return 0;
}
