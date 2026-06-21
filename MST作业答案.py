# -*- coding: utf-8 -*-
"""
第五章 最小生成树（MST）作业答案

图结构（6个顶点，无向带权）:
    A ---2--- B ---4--- C
    |         |         |
    3         1         5
    |         |         |
    D ---6--- E ---2--- F

边列表：A-B:2  B-C:4  A-D:3  B-E:1  C-F:5  D-E:6  E-F:2
"""

# ============================================================
# 1. Prim 算法（从顶点 A 出发）
# ============================================================
print("=" * 60)
print("Prim 算法求解 MST（从 A 出发）")
print("=" * 60)

V = 6
INF = float('inf')

# 邻接表（无向图）
graph = {
    0: [(1, 2), (3, 3)],               # A
    1: [(0, 2), (2, 4), (4, 1)],       # B
    2: [(1, 4), (5, 5)],               # C
    3: [(0, 3), (4, 6)],               # D
    4: [(1, 1), (3, 6), (5, 2)],       # E
    5: [(2, 5), (4, 2)],               # F
}
idx_to_name = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

import heapq

dist = [INF] * V
used = [False] * V
parent = [-1] * V          # 记录每个顶点通过哪条边连入 MST
dist[0] = 0
pq = [(0, 0)]
mst_edges = []
step = 0

print("\n初始：dist = [A:0, B:inf, C:inf, D:inf, E:inf, F:inf]")
print("优先队列 pq = [(0, A)]\n")

while pq:
    d, u = heapq.heappop(pq)
    if used[u]:
        continue
    used[u] = True
    step += 1

    if parent[u] != -1:
        mst_edges.append((idx_to_name[parent[u]], idx_to_name[u], d))

    print("第{}步：选中 {}（到 MST 的最小边权 = {}），将其加入 MST".format(step, idx_to_name[u], d))
    if parent[u] != -1:
        print("  -> 加入边 {}-{}({})".format(idx_to_name[parent[u]], idx_to_name[u], d))

    updates = []
    for v, w in graph[u]:
        if not used[v] and w < dist[v]:
            dist[v] = w
            parent[v] = u
            heapq.heappush(pq, (w, v))
            updates.append("{}={}".format(idx_to_name[v], w))

    if updates:
        print("  更新邻居距离：{}".format(', '.join(updates)))
    print("  当前 dist = [A:{}, B:{}, C:{}, D:{}, E:{}, F:{}]".format(
        dist[0], dist[1], dist[2], dist[3], dist[4], dist[5]))
    print("  used  = {}".format([idx_to_name[i] for i, v in enumerate(used) if v]))
    print()

total_prim = sum(w for _, _, w in mst_edges)
print("MST 边集合：{}".format(mst_edges))
print("MST 总权值：{}".format(total_prim))
print()

# ============================================================
# 2. Kruskal 算法
# ============================================================
print("=" * 60)
print("Kruskal 算法求解 MST")
print("=" * 60)

# 边列表 (权值, u, v)
edges = [
    (2, 0, 1),   # A-B
    (4, 1, 2),   # B-C
    (3, 0, 3),   # A-D
    (1, 1, 4),   # B-E
    (5, 2, 5),   # C-F
    (6, 3, 4),   # D-E
    (2, 4, 5),   # E-F
]
edges.sort()
print("\n边按权值升序排列：")
for w, u, v in edges:
    print("  {}-{}: {}".format(idx_to_name[u], idx_to_name[v], w))

# 并查集
fa = list(range(V))

def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

def unite(x, y):
    rx, ry = find(x), find(y)
    if rx != ry:
        fa[rx] = ry
        return True
    return False

print("\n初始并查集：{}  (每个顶点自成一集合)\n".format(fa))

mst_kruskal = []
ans = 0
cnt = 0

for w, u, v in edges:
    uname, vname = idx_to_name[u], idx_to_name[v]
    if find(u) != find(v):
        unite(u, v)
        mst_kruskal.append((uname, vname, w))
        ans += w
        cnt += 1
        print("[OK] 选中 {}-{}({})，累计权值={}，边数={}".format(uname, vname, w, ans, cnt))
    else:
        print("[SKIP] 跳过 {}-{}({})，会形成环".format(uname, vname, w))
    if cnt == V - 1:
        print("\n已选满 V-1 = {} 条边，算法结束".format(V - 1))
        break

print("\nMST 边集合：{}".format(mst_kruskal))
print("MST 总权值：{}".format(ans))

# ============================================================
# 3. 验证与比较
# ============================================================
print("\n" + "=" * 60)
print("验证与比较")
print("=" * 60)
print("Prim 总权值：   {}".format(total_prim))
print("Kruskal 总权值：{}".format(ans))
print("结果一致：{}".format(total_prim == ans))
print("边数 = V-1 = 5：{}".format(len(mst_edges) == 5 and cnt == 5))

# 画图
print("\n" + "=" * 60)
print("MST 示意图（文本）")
print("=" * 60)
print("""
    A ---2--- B ---4--- C
    |         |
    3         1
    |         |
    D         E ---2--- F

MST 包含的边：
  A-B(2)  <- Prim第1步 / Kruskal第2步
  B-E(1)  <- Prim第2步 / Kruskal第1步
  E-F(2)  <- Prim第3步 / Kruskal第3步
  A-D(3)  <- Prim第4步 / Kruskal第4步
  B-C(4)  <- Prim第5步 / Kruskal第5步

排除的边：
  D-E(6) <- 代价太高，A-D(3)+A-B(2)+B-E(1)=6 已经连通 D 和 E
  C-F(5) <- 代价太高，B-C(4)+B-E(1)+E-F(2)=7 已经连通 C 和 F
""")
