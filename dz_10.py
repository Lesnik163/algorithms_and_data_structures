def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                if take > dp[i][w]:
                    dp[i][w] = take

    return dp[n][capacity]


def lcs(first, second):
    n = len(first)
    m = len(second)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


def count_partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for part in range(1, n + 1):
        for total in range(part, n + 1):
            dp[total] += dp[total - part]

    return dp[n]


def floyd_warshall(matrix):
    n = len(matrix)
    dist = [row[:] for row in matrix]

    for middle in range(n):
        for start in range(n):
            for end in range(n):
                through = dist[start][middle] + dist[middle][end]
                if through < dist[start][end]:
                    dist[start][end] = through

    return dist


print("Задание 1. Рюкзак")
print("веса [2, 3, 4], цены [3, 4, 5], вместимость 5")
print("максимальная стоимость:", knapsack([2, 3, 4], [3, 4, 5], 5))

print("\nЗадание 2. Наибольшая общая подпоследовательность")
print("ABCD и ACD, длина:", lcs("ABCD", "ACD"))
print("AGGTAB и GXTXAYB, длина:", lcs("AGGTAB", "GXTXAYB"))

print("\nЗадание 3. Разбиение числа на сумму")
print("способов для 5:", count_partitions(5))
print("способов для 4:", count_partitions(4))

print("\nЗадание 4. Флойд-Уоршелл")
INF = float("inf")
graph = [
    [0, 1, 10],
    [INF, 0, 1],
    [INF, INF, 0],
]
print("было:")
for row in graph:
    print(row)
print("кратчайшие пути:")
for row in floyd_warshall(graph):
    print(row)
