#include <stdio.h>
#include <time.h>
int main() {
	unsigned long int change = 0;
	unsigned short action;
	unsigned short character = 'A';
	unsigned short position;

	time_t null_t;

	printf("Please enter action/character/position\n");
	scanf("%hu", &action);
	printf("enter is %d\n", action);
	printf("enter is %c\n", character);
	scanf("%hu", &position);
	printf("enter is %d\n", position);

	null_t = time(NULL);
	printf("original time is %ld\n", null_t);
	printf("hours is %ld\n", null_t / 3600);
	printf("days is %ld\n", null_t / 86400);
	printf("years is %ld\n", null_t / 31536000);
	unsigned int diff = null_t - (49 * 3153600);
	printf("time01 since 1/1/2019 = %d\n", null_t - (49 * 31536000));
	printf("time02 since 1/1/2019 = %ld\ndiff is %ld\n", null_t - (49 * 31536000), diff);
	change = change | action;
	change = change | (character << 1);
	change = change | (position << 8);
	change = change | (diff << 16);
	printf("the bit wise is %ld\n", change);
	unsigned int Amask = 0x1;
	unsigned int Cmask = 0x7f << 1;
	unsigned int Pmask = 0xff << 8;
	unsigned int Tmask = 0xffffffff << 16;

	unsigned int act = change & Amask;
	unsigned int word = (change & Cmask) >> 1;
	printf("word is %d and 0x%x\n", word, word);
	unsigned int pos = (change & Pmask) >> 8;
	unsigned int time_dif = (change & Tmask) >> 16;
	printf("the action is %d, the character is %c, the pos is %d, the time is %d\n", act, word, pos, time_dif);
}
