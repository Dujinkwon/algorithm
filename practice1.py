# N M K를 공백으로 구분하여 입력 받기.
n,m,k=map(int, input().split()) 
data=list(map(int,input().split()))

data.sort() # 입력받은수를 정렬
first =data[n-1] # 가장 큰수
second=data[n-2] # 두번 째로 큰수

result=0

while True:
  for i in range(k): # 가장 큰수를 k번 더하기,  range=길이를 뜻한다
    if m==0:
      break
    result += first
    m -= 1
  if m == 0: #m이 0이라면 반복문 탈출
    break
  result += second
  m -= 1

print(result)
