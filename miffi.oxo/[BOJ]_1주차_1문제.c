// 2164. ī�� 2

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// ���� ť�� ����ߴ�.
int card[500000];

int main()
{
	int n;
	scanf("%d", &n);

	// ���� ť�� �� ù �ε����� ��Ÿ�� front�� ���� 0,
	// �� ������ �ε����� ��Ÿ�� rear�� ���� n - 1���� �����ߴ�.
	int i, front = 0, rear = n - 1;

	// card�� 0��° �ε������� ���ʴ�� ��ȣ�� �´� ī�带 �������־���.
	for (i = 0; i < n; i++)
		card[i] = i + 1;

	while (1)
	{
		// ���� ���� �ִ� ī�带 �ٴڿ� ������ �����̴�.
		front = (front + 1) % n;
		// ���� ī�尡 �� �� ���´ٸ�, front�� rear ���� �������Ƿ� �̶� break �ϸ� �ȴ�.
		if (front == rear)
			break;

		rear = (rear + 1) % n;

		// ���� ���� �ִ� ī�带 ���� �Ʒ��� �ִ� ī�� ������ �ű�� �����̴�.
		card[rear] = card[front];

		front = (front + 1) % n;
		if (front == rear)
			break;
	}

	printf("%d\n", card[rear]);

	return 0;
}