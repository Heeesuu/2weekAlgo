tc = int(input())

for _ in range(tc):
    number = int(input())

    for i in range(2, 1_000_001):
        if number % 1 == 0:
            print("NO")
            break
        if i == 1_000_000: #break가 안됐기 때문에 약수가 존재하지 않는것
            print("YES")