#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int ham[100] = {0,};
	int a[10] = { 0, };
	for (int i = 0; i < 3; i++) {
		scanf("%d", &ham[i]);
	}
	scanf("%d", &a[0]);
	scanf("%d", &a[1]);

	int min = ham[0];
	for (int i = 0; ham[i] != NULL; i++) {
		if (min > ham[i]) min = ham[i];
	}

	int m = a[0];
	if (m > a[1]) m = a[1];

	int result = m + min - 50;
	printf("%d", result);
	
}
