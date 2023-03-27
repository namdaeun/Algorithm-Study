## 9012. 괄호
<img src='https://www.notion.so/9a0cbe928d5f4c1db8f52d12835868ed?pvs=4#7f92a2f69fec42bf9e0b8d72e5df8d3e'/>

```python
def checkParenthesis(ps):
    check = []  # 괄호의 짝이 맞는지 확인할 배열
    for s in ps:
        if s == '(':
            check.append('(')
        elif s == ')':
            if not check:
                # 빈 리스트 - VPS아님
                return 'NO'
            # 닫는 괄호 존재하는데 닫는 괄호 들어옴 - VPS아님
            elif check.pop() != '(':  # pop은 비교문에만 써도 실행됨 
                return 'NO'
    if check:
        return 'NO'
    else:
        return 'YES'
     # check 리스트가 비어있는 경우 VPS
  
    
testcase = int(input())
ps = []
for i in range(testcase):
    ps = input()
    print(checkParenthesis(ps))
```

우선 main함수에서는 testcase를 입력받고, 괄호를 입력받은 배열 ps를 선언 및 초기화해주었다.
그 다음 for문을 사용해서 testcase만큼 ps에 각 케이스별 괄호 문자열을 입력받았고, 
ps에 대해 checkParenthesis함수를 호출해주었다.


**checkParenthesis함수_**
- 열린 괄호가 있다면 리스트에 추가했다.
- 닫힌 괄호가 있다면 경우를 두 가지로 나누어 주었는데, 만약 빈 리스트인데 닫는 괄호가 들어온다면 VPS가 아니므로 NO를 리턴해주고, pop을 했을 때 닫힌 괄호, 즉 이전 인덱스도 닫힌 괄호라면 NO를 리턴해주었다.
- 구글링을 하면서 알게된 것인데 리스트의 pop의 경우 비교문에만 써도 실행됨을 알게되었다.
- 검사를 마치고 최종적으로 리스트가 비어있다면 괄호의 짝이 다 맞는 것이기 때문에 YES를 리턴해주었다. 반대의 경우 NO를 리턴해주었다.
