// 2164. 카드 2

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 원형 큐를 사용했다.
int card[500000];

int main()
{
	int n;
	scanf("%d", &n);

	// 원형 큐의 맨 첫 인덱스를 나타낼 front의 값을 0,
	// 맨 마지막 인덱스를 나타낼 rear의 값을 n - 1으로 설정했다.
	int i, front = 0, rear = n - 1;

	// card의 0번째 인덱스부터 차례대로 번호에 맞는 카드를 저장해주었다.
	for (i = 0; i < n; i++)
		card[i] = i + 1;

	while (1)
	{
		// 제일 위에 있는 카드를 바닥에 버리는 과정이다.
		front = (front + 1) % n;
		// 만약 카드가 한 장 남는다면, front와 rear 값이 같아지므로 이때 break 하면 된다.
		if (front == rear)
			break;

		rear = (rear + 1) % n;

		// 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기는 과정이다.
		card[rear] = card[front];

		front = (front + 1) % n;
		if (front == rear)
			break;
	}

	printf("%d\n", card[rear]);

	return 0;
}
