'''

Step 1 − Put the starting vertex into the stack.
        Mark it as visited.
        Display it.

Step 2 −   if( STACK[top]  has adjacent unvisited vertex )
 {
        Visit the adjacent unvisited vertex and  Mark it as visited.
        push it  into the STACK.
        Display  it.
 }
 else
                  {
        pop top element of stack.
 }
 (repeat rule 2 until stack is empty)

'''

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

# This using stack

def dfs(graph,node):
    visited=[]
    if node not in graph:
        return
    stack=[]
    stack.append(node)                    #3,7

    while stack:                          # 3
        current=stack.pop()               # current = 5 , 7 ,8,3,4,8,2
        if current not in visited:        # 5 , 7 ,8,3,4,2
            print(current,end=" ")        # 5 , 7,8,3,4,2
            visited.append(current)       # 5  , 7 ,8,3,4,2
            for i in graph[current]:      # graph[5] = ['3','7'] , graph[7] = ['8'],graph[8]=[],graph[3]=[2,4],graph[4]=[8],graph[2]=[]
                stack.append(i)           # stack[]



# Using recursion_math
'''
visited=[]

def dfs(visited,graph,node):
  if node not in visited:               #   5,3,2,4,8,7
    print(node,end=' ')                 #   5,3,2,4,8,7

    visited.append(node)                # visited=[5,3,2,4,8,7]
    for neighbour in graph[node]:       # graph[5] = ['3','7'], graph[3] = [2,4],graph[2] =[],graph[4]=[8],graph[8]=[],graph[7]=[8]
      dfs(visited,graph,neighbour)      # dfs(visited,graph,3) , dfs(visited,graph,2) ,dfs(visited,graph,4),dfs(visited,graph,8),dfs(visited,graph,7)

dfs( visited,graph, '5')

'''

dfs(graph, '5')


# o/p: 5 7 8 3 4 2




