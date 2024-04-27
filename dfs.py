def dfs(graph,source_node,destination_node):
  stack = [source_node]
  visited_nodes = []
  while len(stack) > 0 and destination_node not in visited_nodes:
     element = stack.pop()
     if element not in visited_nodes:    
      visited_nodes.append(element)
      for adj in sorted(graph[element],reverse=True):
        if adj not in visited_nodes:
          stack.append(adj)
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
print(dfs(G1,'S','C'))