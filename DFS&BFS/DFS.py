# DFS 메서드 정의
def dfs(graph, v, visited):

    visited[v] = True # 현재 노드를 방문 처리
    print(v, end=' ') #방문한 노드 출력

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: # 현재 노드의 인접 노드를 모두 방문
        if not visited[i]: # i가 방문 처리되지 않았다면
            dfs(graph, i, visited) # 재귀적 방문
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * (len(graph) + 1) # 각 노드의 방문 여부를 나타내는 리스트

dfs(graph, 1, visited) # 1번 노드부터 DFS 탐색 시작