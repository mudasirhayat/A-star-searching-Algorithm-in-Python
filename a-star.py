from queue import PriorityQueue


class Graph:

  def __init__(self, vertices):
    self.vertices = vertices
    self.container = [[] for i in range(vertices)]

  def add_edge(self, node_1, node_2, cost, cost2):
    self.container[node_1].append([node_2, cost+cost2])
    self.container[node_2].append([node_1, cost+cost2])

  def a_star(self, start, goal):
    p = PriorityQueue()
    visited = [False for i in range(self.vertices)]
    visited[start] = True
    p.put((0, start))

    while not p.empty():
      item = p.get()
      node = item[1]

      print(f'-> {node}', end=' ')

      if node == goal:
        return True

      for link in self.container[node]:
        if visited[link[0]]:
          continue

        visited[link[0]] = True
        p.put((link[1], link[0]))


g = Graph(14)
g.add_edge(0, 1, 3, 33)
g.add_edge(0, 2, 6, 23)
g.add_edge(0, 3, 5, 42)
g.add_edge(1, 4, 9, 3)
g.add_edge(1, 5, 8, 42)
g.add_edge(2, 6, 12, 12)
g.add_edge(2, 7, 14, 34)
g.add_edge(3, 8, 7, 12)
g.add_edge(8, 9, 5, 43)
g.add_edge(8, 10, 6, 2)
g.add_edge(9, 11, 1, 0)
g.add_edge(9, 12, 10, 0)
g.add_edge(9, 13, 2, 0)

if g.a_star(0, 9):
  print('Successfully Found!')
