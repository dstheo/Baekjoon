H, M = map(int, input().split())

T = int(input())

if M + T >= 60:
    H += (M + T) // 60
    M = (M + T) % 60
    if H > 23:
        H %= 24
    print(H, M)
else:
    M += T
    print(H, M)