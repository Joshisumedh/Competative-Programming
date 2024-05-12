from collections import deque

# TEMPLATES
def fs():
    return map(int, input().split())

def sat(n, pos):
    return n | (1 << pos)

def reset(N, pos):
    return N & ~(1 << pos)

def cak(n, pos):
    return bool(n & (1 << pos))

def binPow(a, q, mud):
    a %= mud
    if q == 0:
        return 1
    return ((a if q % 2 == 1 else 1) * binPow(a * a, q // 2, mud)) % mud


# Main code
def bfs(start):
    q = deque([start])
    d[start] = 0
    mark[start] = True

    while q:
        u = q.popleft()

        for v in nod[u]:
            if not mark[v]:
                mark[v] = True
                d[v] = d[u] + 1
                q.append(v)


if __name__ == "__main__":
    T = int(input())

    for k in range(1, T + 1):
        n, m = map(int, input().split())

        nod = {}
        d = {}
        mark = {}

        for i in range(n):
            str_ = input().strip()
            cnt = 0

            while str_[-1] != ':':
                str_ = str_[:-1]
            str_ = str_[:-1]

            str_ = str_.replace(',', ' ')
            str_ = str_.split()

            nam = []
            for j in range(0, len(str_), 2):
                nam.append(str_[j] + ' ' + str_[j + 1])

            for j in range(len(nam)):
                for k in range(j + 1, len(nam)):
                    if nam[j] not in nod:
                        nod[nam[j]] = []
                    if nam[k] not in nod:
                        nod[nam[k]] = []
                    nod[nam[j]].append(nam[k])
                    nod[nam[k]].append(nam[j])

        bfs("Erdos, P.")

        print(f"Scenario {k}")
        for i in range(m):
            str_ = input().strip()
            if str_ in d:
                print(f"{str_} {d[str_]}")
            else:
                print(f"{str_} infinity")


#Sample Input
#1
#4 3
#Smith, M.N., Martin, G., Erdos, P.: Newtonian forms of prime factor matrices
#Erdos, P., Reisig, W.: Stuttering in petri nets
#Smith, M.N., Chen, X.: First oder derivates in structured programming3
#Jablonski, T., Hsueh, Z.: Selfstabilizing data structures
#Smith, M.N.
#Hsueh, Z.
#Chen, X.


#Sample Output
#Scenario 1
#Smith, M.N. 1
#Hsueh, Z. infinity
#Chen, X. 2