# ダイクストラ法 サンプル

import math

route_list = [
    [0, 50, 80, 0, 0],
    [0, 0, 20, 15, 0],
    [0, 0, 0, 10, 15],
    [0, 0, 0, 0, 30],
    [0, 0, 0, 0, 0]
]  # 初期のノード間の距離のリスト

node_num = len(route_list)  # ノードの数 5

unsearched_nodes = list(range(node_num))  # 未探索ノード 0 ~ 4
node_index = list(range(node_num))
distance = [math.inf] * node_num  # ノードごとの距離のリスト distance = [INF, INF, ...]
pre_nodes = [-1] * node_num  # 最短経路でそのノードのひとつ前に到達するノードのリスト
distance[0] = 0  # 初期のノードの距離は0とする

while unsearched_nodes:
  cost = math.inf
  for i in unsearched_nodes:
    if cost > distance[i]:
      cost = distance[i]
  
  index = distance.index(cost) # 最小のノードが探索済みかどうか
  if index in unsearched_nodes:
    target_node = index
  
  unsearched_nodes.remove(target_node)

  target_edge = route_list[target_node] # 0 → [0, 50, 80, 0, 0]
  for i, v in enumerate(target_edge):
    if v != 0 and distance[i] > (distance[target_node] + v):
      distance[i] = distance[target_node]+v
      pre_nodes[i] = target_node
  print(distance)