#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int N, M;
	int sum1 = 0, sum2;
	int card[100];

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		scanf(" %d", &card[i]);
	}

	for (int i = 0; i < (N - 2); i++) {
		for (int j = 1; j < (N - 1); j++) {
			for (int k = 2; k < N; k++) {
				sum2 = card[i] + card[j] + card[k];
				if (i == j || i == k || j ==k){
					continue;
				}
				if (sum2 <= M) {
					if (sum1 < sum2)
						sum1 = sum2;
				}
			}
		}
	}
	printf("%d", sum1);
}