def bfs(graph,source_node,destination_node):
  queue = [source_node]
  visited_nodes = []
  while len(queue) > 0 and destination_node not in visited_nodes :
    element = queue.pop(0)
    if element not in visited_nodes:
      visited_nodes.append(element)
      for adj in sorted(graph[element]):
        if adj not in visited_nodes:
          queue.append(adj)
  return visited_nodes


G1 = {
  "S": ["A","H"],
  "A": ["B","C"],
  "B": ["D","E"],
  "C": ["G"],
  "D": ["I"],
  "E": [],
  "G": [],
  "H": [],
  "I": ["J","K"],
  "J": [],
  "K": [],
}
print(bfs(G1,'S','C'))