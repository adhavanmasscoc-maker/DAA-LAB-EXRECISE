from itertools import permutations
INF = float('inf')

def tsp_brute_force(cost, n):
    cities = list(range(1, n))
    best_cost = INF
    best_path = None
    for perm in permutations(cities):
        path = [0] + list(perm) + [0]
        c = sum(cost[path[i]][path[i+1]] for i in range(n))
        if c < best_cost:
            best_cost = c
            best_path = path
    return best_path, best_cost

if __name__ == '__main__':
    cost = [
        [INF, 10, 8, 9, 7],
        [ 10, INF, 10, 5, 6],
        [ 8, 10, INF, 8, 9],
        [ 9, 5, 8, INF, 6],
        [ 7, 6, 9, 6, INF]
    ]
    n = 5
    cities = ['A', 'B', 'C', 'D', 'E']
    best_path, best_cost = tsp_brute_force(cost, n)
    print('5-City TSP - Cost Matrix:')
    print(f'{"":>4}', ' '.join(f'{c:>5}' for c in cities))
    for i, row in enumerate(cost):
        r = ['INF' if x == INF else str(x) for x in row]
        print(f'{cities[i]:>4}', ' '.join(f'{v:>5}' for v in r))

    print(f'\nOptimal Tour: {" -> ".join(cities[i] for i in best_path)}')
    print(f'Minimum Cost: {best_cost}')
    print('\nPath verification:')
    for i in range(n):
        u, v = best_path[i], best_path[i+1]
        print(f' {cities[u]} -> {cities[v]}: cost = {cost[u][v]}')
