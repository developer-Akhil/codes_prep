"""
https://www.youtube.com/watch?v=TD6jcJ9iIZ4

BFS Algorithm:

START
Step 1 − Visit the starting vertex and mark it as visited.
         Display it.
        Set a pointer to the starting vertex.(Currently working Vertex.)

Step 2 −   if( Currently working Vertex  has adjacent unvisited vertex )
 {
       Visit the adjacent unvisited vertex and  Mark it as visited.
        Insert it in a queue. (enqueue)
        Display it.
 }
 else{
        Update the pointer to the first element of queue.
        Remove the first element from queue. (dequeue)
 }
 (repeat rule 2 until queue is empty)
END

"""
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.    [5,3,7,2,4,8]
queue = []     #Initialize a queue


def bfs(visited,graph,node):

  visited.append(node)            #
  queue.append(node)              #

  while queue:

    m = queue.pop(0)              # m=5
    print(m,end=" ")              #  5,3,7,2,4,8

    for neighbour in graph[m]:    #  graph[5]

      if neighbour not in visited:    # 8 not in visited
        visited.append(neighbour)     # 8
        queue.append(neighbour)       # 8

print("Following is the Breadth-First Search")

pr=bfs(visited,graph, '5')
