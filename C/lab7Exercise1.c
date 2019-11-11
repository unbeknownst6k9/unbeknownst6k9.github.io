/*
Timothy Kwan
3050244
cmpt201
X02L
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
	double price;
	char title[60];
}game;

int compGamesByPrice(const void *a, const void *b) {
	game *a1 = (game*)a;
	game *b1 = (game*)b;
	return (a1->price - b1->price);
}
int compGamesByTitle(const void *a, const void *b){
	game *a1 = (game*)a;
	game *b1 = (game*)b;
	int i=0;
	while (a1->title[i] == b1->title[i]) {
		i++;
	}
	return (a1->title[i] - b1->title[i]);
}
int main() {
	int a;
	printf("check01\n");
	game items[7];
	game tmp_ref;

/*input the data*/
	tmp_ref.price = 22.79;
	strcpy(tmp_ref.title, "Opus Magnum");
	items[0] = tmp_ref;

	tmp_ref.price = 0.01;
	strcpy(tmp_ref.title, "Minecraft");
	items[1] = tmp_ref;

	tmp_ref.price = 7.79;
	strcpy(tmp_ref.title, "TIS-100");
	items[2] = tmp_ref;

	tmp_ref.price = 14.99;
	strcpy(tmp_ref.title, "Trainz");
	items[3] = tmp_ref;

	tmp_ref.price = 0;
	strcpy(tmp_ref.title, "Code Combat");
	items[4] = tmp_ref;

	tmp_ref.price = 7.79;
	strcpy(tmp_ref.title, "Lemmings Revolution");
	items[5] = tmp_ref;

	tmp_ref.price = 64.96;
	strcpy(tmp_ref.title, "Warcraft");
	items[6] = tmp_ref;

	printf("before sorting\n");
	for (int i = 0; i < 7;i++) {
		printf("the price is: %lf the name is:%s\n", items[i].price, items[i].title);
	}

	qsort(items, 7, sizeof(game), compGamesByPrice);
	printf("\nsort in price:\n");
	for (int i = 0; i < 7;i++) {
		printf("the price is: %lf the name is:%s\n", items[i].price, items[i].title);
	}

	qsort(items, 7, sizeof(game), compGamesByTitle);
	printf("\nsort in title:\n");
	for (int i = 0; i < 7;i++) {
		printf("the price is: %lf the name is:%s\n", items[i].price, items[i].title);
	}
	scanf("%d", &a);
	return 0;
}