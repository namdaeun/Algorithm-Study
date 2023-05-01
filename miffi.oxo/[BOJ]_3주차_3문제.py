# 1254. 팰린드롬 만들기

s = input()

for i in range(len(s)):
    # 문자열 앞뒤의 i번째부터 끝까지를 슬라이싱하여 비교
    # 슬라이싱한 두 문자열이 같은 시점부터는 문자열 뒤에 다른 문자 추가할 필요 X
    if s[i:] == s[i:][::-1]:
        # 해당 시저에서 s의 길이에 i를 더한 값이 가장 짧은 팰린드롬의 길이
        print(len(s) + i)
        break





# 16499. 동일한 단어 그룹화하기

n = int(input())

# 집합 활용
same_word = set()

for i in range(n):
    # 문자열 입력 받고 정렬
    word = str(sorted(input()))
    # 정렬된 문자열 집합에 추가
    # 집합에는 중복된 원소가 들어가지 않음
    same_word.add(word)

# 따라서 반복문 끝나고 집합의 원소의 개수를 출력하면 단어가 총 최소 몇 개의 그룹으로 이루어져 있는지 구할 수 있음
print(len(same_word))





# 13417. 카드 문자열

t = int(input())

for i in range(t):
    n = int(input())
    # n개의 단어들
    c = list(input().split())
    
    word = ""
    
    for j in range(n):
        # 빈 문자열일 경우 오른쪽에 추가
        if word == "":
            word += c[j]
        # 문자가 단어 맨 앞 글자보다 사전순으로 빠르거나 같다면 왼쪽에 추가
        elif word[0] >= c[j]:
            word = c[j] + word
        # 그렇지 않다면 오른쪽에 추가
        else:
            word += c[j]

    print(word)
