# def count_connected_groups(adj):
#     n = len(adj)
#     nodes_to_check = set([i for i in range(n)]) # [] not needed in python 3
#     count = 0
#     while nodes_to_check:
#         count += 1
#         node = nodes_to_check.pop()
#         adjacent = adj[node]
#         other_group_members = set()
#         for i in nodes_to_check:
#             if adjacent[i]:
#                 other_group_members.add(i)
#         nodes_to_check -= other_group_members
#     return count

# def findCircleNum(isConnected):
#     visited = set()
#     res = 0
#
#     for idx, row in enumerate(isConnected):
#         print(idx, row)
#
#         if idx not in visited:
#
#             res += 1
#
#             current = [idx]
#             frontier = []
#
#             while current:
#                 node = current.pop()
#                 if node not in visited:
#                     visited.add(node)
#                     neighbours = [i for i, val in enumerate(isConnected[node]) if val]
#                     print(neighbours)
#                     for nei in neighbours:
#                         if nei not in visited:
#                             frontier.append(nei)
#
#                 if not current:
#                     current, frontier = frontier, current
#
#     return res


def findCircleNum(isConnected):
    N = len(isConnected)
    visited = set()

    def dfs(cityI):
        # cityIConnections is a row in isConnected, which contains the city i's connections
        cityIConnections = isConnected[cityI]
        visited.add(cityI)  # add cityI to seen, so we won't dfs it again (because we called it just now!)
        # we want to take all 1's in cityIConnections to put together into a province
        for cityJ in range(N):
            # check cityJ's connections first before finishing cityI's connections
            if (cityJ not in visited) and (int(cityIConnections[cityJ]) == 1) and (cityI != cityJ):
                dfs(cityJ)
        # we're done searching cityI's direct connections
        return

    numProvinces = 0
    for cityI in range(N):
        # each entire dfs recursion set is going to be one province
        if cityI not in visited:
            dfs(cityI)
            numProvinces += 1
    return numProvinces

# your example:
adj_0 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# same with tuples and booleans:
adj_1 = ((True, True, False), (True, True, False), (False, False, True))
# another connectivity matrix:
adj_2 = ((1, 1, 1, 0, 0),
         (1, 1, 1, 0, 0),
         (1, 1, 1, 0, 0),
         (0, 0, 0, 1, 1),
         (0, 0, 0, 1, 1))
# and yet another:
adj_3 = ((1, 0, 1, 0, 0),
         (0, 1, 0, 1, 0),
         (1, 0, 1, 0, 0),
         (0, 1, 0, 1, 0),
         (0, 0, 0, 0, 1))
# for a in adj_0, adj_1, adj_2, adj_3:
#     print(a)
#     print(count_connected_groups(a))

# A = [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]

# A = ['1100', '1110', '0110', '0001']

A = ['1000001000',
'0100010001',
'0010100000',
'0001000000',
'0010100000',
'0100010000',
'1000001000',
'0000000100',
'0000000010',
'0100000001']
print(A)

# print(count_connected_groups(A))

print(findCircleNum(A))