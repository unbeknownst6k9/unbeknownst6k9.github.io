/*
Name: Timtohy Kwan
number: 3050244
cmpt201 X02L

*/
#include <stdio.h>
#define ROW 9
#define LINE 5
#define FUTURE 30

int count_day(int year);

int main() {
	int i, year, start_year, day, j;
	static int counter;
	scanf("%d", &year);
	start_year = year;
	//get the last digit of the input year
	while (start_year > 9) {
		start_year = start_year - 10;
	}
	counter = FUTURE;
	//print out the first column from 0-9
	printf("\nyear ");
	for (i = 0;i < 10;i++) { printf(" %d ", i); }
	//print the next line to be ready for the data
	printf("\n");


	//print out the datas
	j = 10 - start_year;
	while (counter > 0) {
		
		//print out the empty spaces

		switch (start_year>0)
		{
		case 1:
			printf("%d  ", (int)(year / 10));
			while (start_year > 0)
			{
				printf("   ");
				start_year--;
			}
		default:
			while (j != 0) {
				day = count_day(year);
				printf("%d ", day);
				//increment the year
				year = year + 1;
				//decrease the data count
				//printf(" counter: %d ", counter);
				counter--;
				j--;
			}
			break;
		}

		
		//printout the data for the first line
		
		//go to next line
		printf("\n");
		printf("%d  ", (int)(year / 10));
		for (i = 0; i < 10; i++) {
			if (counter < 0) { break; }
			day = count_day(year);
			printf("%d ", day);
			//increment the year
			year = year + 1;
			//decrease the data count
			//printf("counter: %d", counter);
			counter = counter - 1;
		}
	}
	printf("\n");
	char a;
	printf("Enter anything to exit");
	scanf("%s", &a);
	return 0;
}


#define FEBURARY 2


int count_day(int year) {
	int a, y, m, dow, day, family_day;
	//printf("\npass01\n");
	day = 1;
	//printf("pass02\n");
	a = (14 - FEBURARY) / 12;
	y = year - a;
	//printf("pass03\n");
	m = FEBURARY + 12 * a - 2;
	dow = (day + y + y / 4 - y / 100 + y / 400 + 31 * m / 12) % 7;
	while (dow != 1) {
		dow = (dow + 1) % 7;
		day++;
	}
	family_day = 14 + day;







	//printf("%d", dow);
	return family_day;
}