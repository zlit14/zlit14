print(len(list(filter(lambda x: x % 3 == 0 and str(x)[-1] == '2', [int(input()) for _ in range(int(input()))]))))
