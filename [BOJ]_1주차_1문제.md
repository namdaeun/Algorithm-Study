// 2164. Ä«µå 2

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int card[500000];

int main()
{
	int n;
	scanf("%d", &n);

	int i, front = 0, rear = n - 1;

	for (i = 0; i < n; i++)
		card[i] = i + 1;

	while (1)
	{
		front = (front + 1) % n;
		if (front == rear)
			break;

		rear = (rear + 1) % n;

		card[rear] = card[front];

		front = (front + 1) % n;
		if (front == rear)
			break;
	}

	printf("%d\n", card[rear]);

	return 0;
}