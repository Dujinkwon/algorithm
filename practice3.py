# n,k=map(int,input().split())
# result=0
# while n > k:
#   # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기.
#   while n%k !=0:
#     n-=1
#     result +=1
#     #K로 나누기
#     n//=k
#     result+=1

# #마지막으로 남은 수에 대하여 1씩 빼기
# while n>1:
#   n-=1
#   result += 1

# print(result)


n,k=map(int,input().split())
result = 0

while True :
  #N==K가 될때까지 1씩 한번에 빼기
  target=(n//k)*k
  result += (n-target)
  n=target

  if(n<k):
    break
  result +=1
  n//=k

  #마지막으로 남은 수에 대하여 1씩 빼기
  result +=(n-1)

  print(result)
