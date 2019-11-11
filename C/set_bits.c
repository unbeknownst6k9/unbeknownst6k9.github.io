#include <stdio.h>

unsigned long int set_bits(int action, char character, int position) {
	int a;
	unsigned long int change;
	change = action;
	change = (character << 1);
	change = (position << 8);
	printf("the bit wise is %ld\n", change);
	unsigned int Amask = 0x1;
	unsigned int Cmask = 0x7f << 1;
	unsigned int Pmask = 0xff << 8;
	unsigned int act = change & Amask;
	unsigned int word = change & Cmask;
	unsigned int pos = change & Pmask;

	printf("the action is %d, the character is %s, the pos is %d", act, word, pos);
	scanf("%d", &a);
}