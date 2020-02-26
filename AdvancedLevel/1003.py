def main():
    x = input().split(' ')
    n = int(x[0])
    m = int(x[1])
    c1 = int(x[2])
    c2 = int(x[3])
    x = input().split(' ')
    point = list(map(int,x))
    route = [[0 for j in range(n)] for i in range(n)]
    for j in range(m):
        x = input().split(' ')
        a = int(x[0])
        b = int(x[1])
        c = int(x[2])
        route[a][b] = c
        route[b][a] = c
    visited = [0 for i in range(n)]
    weight = [float('inf') for i in range(n)]
    power = [0 for i in range(n)]
    weight[c1] = 0
    power[c1] = point[c1]
    visited[c1] = 1
    y = c1
    num = [0 for j in range(n)]
    num[c1] = 1
    while visited[c2] == 0:
        for i in range(n):
            if route[y][i] != 0 and visited[i] != 1:
                if weight[i] >= weight[y] + route[y][i]:
                    if weight[i] == weight[y] + route[y][i]:
                        num[i] = num[i] + num[y]
                        if power[i] < power[y] + point[i]:
                            power[i] = power[y] + point[i]
                    else:
                        if weight[i] > weight[y] + route[y][i]:
                            power[i] = power[y] + point[i]
                            num[i] = num[y]
                    weight[i] = weight[y] + route[y][i]
        small = sorted([weight[y] for y in range(n) if visited[y] !=  1])[0]
        index = [y for y in range(n) if weight[y] == small and visited[y] != 1][0]
        visited[index] = 1
        y = index
    print(num[c2],power[c2])

if __name__ == '__main__':
    main()