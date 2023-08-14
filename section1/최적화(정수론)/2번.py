#1978
n = int(input())
numbers = map(int, input().split())
answer = 0

for a in numbers:
    if a == 1:
        continue
    is_prime = True
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            is_prime = False
            break
    if is_prime:
        answer += 1

print(answer)



#11653
n = int(input())
primelist = []
if n == 1:
    exit()

#n이하의 소수 구하기
for i in range(2, n+1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1): #반복문의 범위가 맞지 않을땐 실행 안함 2,3일땐 반복문의 범위가 맞지 않고 isprime이 true상태이기 때문에 자동으로 append실행됨
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primelist.append(i)


#n을 소수로 나누기
idx = 0
while(idx+1 != len(primelist) or n != 0):
    if n % primelist[idx] == 0:
        print(primelist[idx])
        temp = n // primelist[idx]
        n = temp   
    else:
        idx += 1

    

    




        
