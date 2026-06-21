# -*- coding: utf-8 -*-
"""
图的存储与遍历 作业

包含：
  1. 图的两种存储方式：邻接矩阵 + 邻接表
  2. 深度优先遍历（DFS）：递归版 + 栈版
  3. 广度优先遍历（BFS）：队列版
  4. 在课程示例图上演示

示例图（有向图，来自课程第四章最短路径）：
     A --2--> B --1--> C
     |        |        |
     2        5        3
     v        v        v
     D --1--> E --2--> C  (D->B:1, D->E:4, C->E:3)

边：A->B:2  A->D:2  B->C:1  B->E:5  C->E:3  D->B:1  D->E:4  E->C:2
"""

from collections import deque

# ============================================================
# 第一部分：图的存储
# ============================================================

class GraphAdjacencyMatrix:
    """邻接矩阵存储（适合稠密图，O(V^2) 空间）"""

    def __init__(self, vertices):
        self.vertices = vertices          # 顶点名列表
        self.n = len(vertices)            # 顶点数
        self.name_to_idx = {v: i for i, v in enumerate(vertices)}
        # 初始化矩阵，INF 表示无边
        INF = float('inf')
        self.matrix = [[INF] * self.n for _ in range(self.n)]
        for i in range(self.n):
            self.matrix[i][i] = 0         # 自己到自己距离为 0

    def add_edge(self, u, v, weight=1):
        """添加有向边 u -> v"""
        i, j = self.name_to_idx[u], self.name_to_idx[v]
        self.matrix[i][j] = weight

    def add_undirected_edge(self, u, v, weight=1):
        """添加无向边"""
        self.add_edge(u, v, weight)
        self.add_edge(v, u, weight)

    def get_neighbors(self, u):
        """获取顶点 u 的所有邻居（出边）"""
        i = self.name_to_idx[u]
        neighbors = []
        for j in range(self.n):
            if self.matrix[i][j] != float('inf') and self.matrix[i][j] != 0:
                neighbors.append((self.vertices[j], self.matrix[i][j]))
        return neighbors

    def display(self):
        """打印邻接矩阵"""
        print("  邻接矩阵：")
        header = "     " + "  ".join("{:>4}".format(v) for v in self.vertices)
        print(header)
        print("     " + "-" * (5 * self.n))
        for i, v in enumerate(self.vertices):
            row = "  ".join("{:>4}".format(
                "0" if self.matrix[i][j] == 0 else
                "inf" if self.matrix[i][j] == float('inf') else
                str(int(self.matrix[i][j]))
            ) for j in range(self.n))
            print("  {} | {}".format(v, row))


class GraphAdjacencyList:
    """邻接表存储（适合稀疏图，O(V+E) 空间）"""

    def __init__(self, vertices):
        self.vertices = vertices
        self.n = len(vertices)
        # 每个顶点对应一个列表，元素为 (邻居, 权值)
        self.adj = {v: [] for v in vertices}

    def add_edge(self, u, v, weight=1):
        """添加有向边 u -> v"""
        self.adj[u].append((v, weight))

    def add_undirected_edge(self, u, v, weight=1):
        """添加无向边"""
        self.add_edge(u, v, weight)
        self.add_edge(v, u, weight)

    def get_neighbors(self, u):
        """获取顶点 u 的所有邻居"""
        return self.adj[u]

    def display(self):
        """打印邻接表"""
        print("  邻接表：")
        for v in self.vertices:
            neighbors = ", ".join("{}->{}({})".format(v, n, w) for n, w in self.adj[v]) if self.adj[v] else "(无出边)"
            print("    {}: {}".format(v, neighbors))


# ============================================================
# 第二部分：图的遍历
# ============================================================

class GraphTraversal:
    """图遍历（DFS 和 BFS），基于邻接表"""

    def __init__(self, graph):
        self.graph = graph      # GraphAdjacencyList 实例
        self.visited = set()
        self.order = []         # 记录遍历顺序

    def reset(self):
        self.visited = set()
        self.order = []

    # ---------- DFS：递归版 ----------
    def dfs_recursive(self, start):
        """深度优先遍历 -- 递归实现（系统栈）"""
        self.reset()
        print("  DFS 递归版（从 {} 开始）：".format(start))
        self._dfs_recurse(start)
        print("    遍历顺序：{}".format(" -> ".join(self.order)))

    def _dfs_recurse(self, u):
        self.visited.add(u)
        self.order.append(u)
        for v, _ in self.graph.get_neighbors(u):
            if v not in self.visited:
                self._dfs_recurse(v)

    # ---------- DFS：显式栈版 ----------
    def dfs_stack(self, start):
        """深度优先遍历 -- 显式栈实现"""
        self.reset()
        stack = [start]
        print("  DFS 栈版（从 {} 开始）：".format(start))

        while stack:
            u = stack.pop()
            if u not in self.visited:
                self.visited.add(u)
                self.order.append(u)
                # 邻居按反序入栈，保证与递归版顺序一致
                neighbors = self.graph.get_neighbors(u)
                for v, _ in reversed(neighbors):
                    if v not in self.visited:
                        stack.append(v)

        print("    遍历顺序：{}".format(" -> ".join(self.order)))

    # ---------- BFS：队列版 ----------
    def bfs(self, start):
        """广度优先遍历 -- 队列实现"""
        self.reset()
        queue = deque([start])
        self.visited.add(start)
        print("  BFS 队列版（从 {} 开始）：".format(start))

        while queue:
            u = queue.popleft()
            self.order.append(u)
            for v, _ in self.graph.get_neighbors(u):
                if v not in self.visited:
                    self.visited.add(v)
                    queue.append(v)

        print("    遍历顺序：{}".format(" -> ".join(self.order)))

    # ---------- BFS 求最短路径（无权图 / 边权为 1） ----------
    def bfs_shortest_path(self, start, target):
        """BFS 求无权图最短路径（边数最少），返回路径和距离"""
        self.reset()
        queue = deque([(start, [start])])
        self.visited.add(start)

        while queue:
            u, path = queue.popleft()
            if u == target:
                return path, len(path) - 1
            for v, _ in self.graph.get_neighbors(u):
                if v not in self.visited:
                    self.visited.add(v)
                    queue.append((v, path + [v]))
        return None, -1


# ============================================================
# 第三部分：在课程示例图上演示
# ============================================================

if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']

    print("=" * 60)
    print("图的存储")
    print("=" * 60)
    print("课程示例图（有向图）：")
    print("  A->B:2  A->D:2  B->C:1  B->E:5  C->E:3  D->B:1  D->E:4  E->C:2")
    print()

    # --- 邻接矩阵 ---
    g_matrix = GraphAdjacencyMatrix(vertices)
    g_matrix.add_edge('A', 'B', 2)
    g_matrix.add_edge('A', 'D', 2)
    g_matrix.add_edge('B', 'C', 1)
    g_matrix.add_edge('B', 'E', 5)
    g_matrix.add_edge('C', 'E', 3)
    g_matrix.add_edge('D', 'B', 1)
    g_matrix.add_edge('D', 'E', 4)
    g_matrix.add_edge('E', 'C', 2)
    g_matrix.display()

    print("\n  特点：查询边 O(1)，空间 O(V^2)={}，适合稠密图".format(len(vertices)**2))

    # --- 邻接表 ---
    print()
    g_list = GraphAdjacencyList(vertices)
    g_list.add_edge('A', 'B', 2)
    g_list.add_edge('A', 'D', 2)
    g_list.add_edge('B', 'C', 1)
    g_list.add_edge('B', 'E', 5)
    g_list.add_edge('C', 'E', 3)
    g_list.add_edge('D', 'B', 1)
    g_list.add_edge('D', 'E', 4)
    g_list.add_edge('E', 'C', 2)
    g_list.display()

    n, e = len(vertices), 8
    print("\n  特点：遍历邻居快，空间 O(V+E)={}+{}={}，适合稀疏图".format(n, e, n+e))

    # ============================================================
    print()
    print("=" * 60)
    print("图的遍历")
    print("=" * 60)
    print("核心：visited 数组防止重复访问，时间复杂度 O(V+E)")
    print()

    traversal = GraphTraversal(g_list)

    # DFS 递归
    traversal.dfs_recursive('A')

    # DFS 栈
    print()
    traversal.dfs_stack('A')

    # BFS
    print()
    traversal.bfs('A')

    # BFS 最短路径（无权）
    print()
    path, dist = traversal.bfs_shortest_path('A', 'E')
    print("  BFS 求 A 到 E 的最短路径（按边数）：")
    print("    路径：{} (共 {} 条边)".format(" -> ".join(path), dist))

    # ============================================================
    print()
    print("=" * 60)
    print("DFS vs BFS 对比")
    print("=" * 60)
    print("""
            DFS（深度优先）              BFS（广度优先）
  数据结构   栈（递归/显式栈）            队列
  遍历方式   沿一条路走到底，再回溯        逐层向外扩展
  实现      递归简洁，栈版不需递归深度限制  队列实现，天然非递归
  适用      拓扑排序、连通分量、回溯      无权最短路径、层级遍历
  时间       O(V+E)                       O(V+E)
  空间       递归 O(V) / 栈 O(V)         队列 O(V)
""")
