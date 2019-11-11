/*
Timothy Kwan
3050244
cmpt201
X02L
*/
#include <stdio.h>

unsigned int rotate_right(unsigned int i, int n) {
	unsigned int mask = 0;
	unsigned int b = 0;

	for (int j = 0; j < n;j++) {
		mask |= (0x1 << j);
	}
	b = i & mask;/**/
	i = i >> n;
	b = b << (sizeof(int) * 8 - n);
	i = i | b;

	/*use or to put it back*/
	return i;
}

int parityTest(unsigned int x) {
	unsigned int mask = 0x1;
	int i = 0;
	int count = 0;
	while (i != sizeof(int)*8)
	{
		if (x&mask<<i)
		{
			count++;
		}
		i++;
	}
	if (!(count % 2)) {
		return 1;
	}
	return 0;
}

int main() {
	int a;
	int j = 8;
	unsigned int num = 0x12345678;
	unsigned int new_num = rotate_right(num,4);
	printf("rotate_right(0x12345678,4) is %x\nrotate_right(0x12\
345678,7) is %x\nparityTest(15) is %d\nparityTest(21) is %d\n", new_num, rotate_right(num, 7), parityTest(15), parityTest(21));
	scanf("%d", &a);
	return 0;
}