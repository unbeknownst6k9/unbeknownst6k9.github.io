#include <stdio.h>
#include <stdlib.h>
int compareAge(const void *a, const void *b) {
	int *a1 = (int *)a;
	int *b1 = (int *)b;
	return (*a1 - *b1);//the opposite will be - (*a1 - *b1)


} //need to have a constant pointer

int compareNewAge(const void *a, const void *b) {
	int **a1 = (int **a);
	int **b1 = (int **b);
	return (**a1 - **b1);//


}
int main() {
	int ages[] = {20,30,10,35,40,25};
	int **new_ages = malloc(6 * sizeof(int *));//array of int pointers

	qsort(new_ages, 6, sizeof(int*), compareNewAge);
	printf("Sorted new ages:\n")
	for ( i = 0; i < 6; i++)
	{
		new_ages[i] = malloc(sizeof(int));
		*(new_ages[i] = ages[i]);
	}
	for (int i = 0; i < 6; i++)
	{
		free(new_ages[i]);
	}
	free(new_ages);
	
	qsort(ages, sizeof(ages) / sizeof(ages[0]), sizeof(ages[0]), compareAge);
	printf("Sorted ages:\n");
	for (int i = 0; i < sizeof(ages)/sizeof(ages[0]); i++)
	{
		printf("%d\n", ages[i]);
	}

	return 0;
}