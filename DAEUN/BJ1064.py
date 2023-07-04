# 백준 1064번 - 평행사변형
# 평행사변형의 조건에 따라 세 선분 중 길이가 다른 두 선분의 길이를 활용하여 둘레를 구한다.

x1, y1, x2, y2, x3, y3 = map(int, input().split())

if ((y2-y1)*(x3-x1) == (y3-y1)*(x2-x1)):
    # 평행사변형이 안되는 경우 - 한 점을 기준으로 두 변의 기울기가 같은 경우 
    print(-1.0)
    exit(0)
    
d1 = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
d2 = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
d3 = ((x3 - x1)**2 + (y3 - y1)**2)**0.5

distance = [2*(d1+d2), 2*(d2+d3), 2*(d1+d3)] # 가능한 둘레의 길이  
result = max(distance) - min(distance) 
print(result)
