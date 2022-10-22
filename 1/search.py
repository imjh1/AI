###### Write Your Library Here ###########
from queue import Queue
#########################################


def search(maze, func):
    return {
        "bfs": bfs,
        "astar": astar,
        "astar_four_circles": astar_four_circles,
        "astar_many_circles": astar_many_circles
    }.get(func)(maze)


# -------------------- Stage 01: One circle - BFS Algorithm ------------------------ #

def bfs(maze):
    """
    [문제 01] 제시된 stage1의 맵 세가지를 BFS Algorithm을 통해 최단 경로를 return하시오.(20점)
    """
    start_point=maze.startPoint()

    path=[]

    ####################### Write Your Code Here ################################
    goal = maze.circlePoints()[0]
    
    openList = Queue()
    closedList = []
    openList.put(start_point)
    
    parent = []
    for row in range(maze.rows):
        line = []
        for col in range(maze.cols):
            line.append(None)
        parent.append(line)
    
    while (not openList.empty()):
        v = openList.get()
        closedList.append(v)
        if(goal in closedList):
            break
        a = maze.neighborPoints(v[0], v[1])
        for i in range(len(a)):
            if a[i] not in closedList:
                parent[a[i][0]][a[i][1]] = v
                openList.put(a[i])
    
    index = goal    
    while(1):
        path.append(index)
        if(parent[index[0]][index[1]] == None):
            break
        index = parent[index[0]][index[1]]
        
    return path

    ############################################################################



class Node:
    def __init__(self,parent,location):
        self.parent=parent
        self.location=location 
        
        self.obj=[]
        
     #   self.mst=[]
        # F = G+H
        self.f=0
        self.g=0
        self.h=0

    def __eq__(self, other):
        return self.location==other.location and str(self.obj)==str(other.obj)

    def __le__(self, other):
        return self.g+self.h<=other.g+other.h

    def __lt__(self, other):
        return self.g+self.h<other.g+other.h

    def __gt__(self, other):
        return self.g+self.h>other.g+other.h

    def __ge__(self, other):
        return self.g+self.h>=other.g+other.h


# -------------------- Stage 01: One circle - A* Algorithm ------------------------ #

def manhatten_dist(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def astar(maze):

    """
    [문제 02] 제시된 stage1의 맵 세가지를 A* Algorithm을 통해 최단경로를 return하시오.(20점)
    (Heuristic Function은 위에서 정의한 manhatten_dist function을 사용할 것.)
    """

    start_point=maze.startPoint()

    end_point=maze.circlePoints()[0]

    path=[]

    ####################### Write Your Code Here ################################
    startNode = Node(None, start_point)
    
    openList = []
    closedList = []    
    openList.append(startNode)
    
    while openList:
        current = openList[0]           
        for node in openList: ## openList안에서 f값이 가장 작은 위치를 찾아내어 openList에서 뺀 후 closedList에 추가
            if node.f < current.f:
                current = node
        openList.remove(current)
                            
        closedList.append([current.location, current.obj])
        
        if(current.location == end_point): ## end_point에 도달시 end_point에서부터 부모 노드를 따라가며 path에 길 입력 후 path return
            current_node = current
            while current_node is not None:
                path.append(current_node.location)
                current_node = current_node.parent
            break
            
        children = []
        a = maze.neighborPoints(current.location[0], current.location[1])               
        for i in range(len(a)):## closedlist 안에 있는 위치는 제외하고 current에서 움직일 수 있는 위치의 Node 생성
            if [a[i], current.obj] in closedList:
                continue
            children.append(Node(current, a[i]))
        
        for child in children:                   ## child: 현재 위치에서 움직일 수 있는 좌표
            child.g = current.g + 1
            child.h = manhatten_dist(child.location, end_point)
            child.f = child.g + child.h 
                
            append = 1                   
            for node in openList:
                if child == node and child.g >= node.g: ##child가 이미 openList에 있을 경우, g값(이동한 거리)을 비교하여 g값이 더 작을 경우 openList에 추가
                    append = 0
                    break                    
            if append:
                openList.append(child)
        
    return path

    ############################################################################


# -------------------- Stage 02: Four circles - A* Algorithm  ------------------------ #
def push_MinHeap(openList, node):            # Min Heap push
    count = len(openList) - 1
    openList.append(node)
    count += 1
    i = count                
    while(i>1):
        if(openList[i].f < openList[int(i/2)].f):
            openList[i],openList[int(i/2)] = openList[int(i/2)],openList[i]
            i = int(i/2)
        else:
            break        
    
def pop_MinHeap(openList):                   #Min Heap pop    
    count = len(openList) - 1
    a = openList[1]
    if(count > 1):               
        openList[1] = openList.pop()
    else:
        openList.pop()
    count -= 1
    i = 1
    while (i <= count):
        j = 2 * i
        if(j > count):
            break
        if(j+1 <= count):
            if(openList[i].f <= openList[j].f and openList[i].f <= openList[j+1].f):
                break
            if(openList[j].f > openList[j + 1].f):
                j = j + 1              
        else:
            if(openList[i] <= openList[j]):
                break                    
        openList[i],openList[j] = openList[j],openList[i]
        i = j    
    return a

def stage2_heuristic(p1, end_points, objectives):
    h = 0
    width = end_points[1][1] - end_points[0][1]
    height = end_points[2][0] - end_points[0][0]
    
    arr = []     
    for i in range(len(objectives)):
            arr.append(abs(p1[0] - objectives[i][0]) + abs(p1[1] - objectives[i][1])) 
    if(len(objectives) > 0):
        close_dist = min(arr)
    
    if(len(objectives) == 4):
        h = close_dist + width + height
        if(width > height):
            h += height
        else:
            h += width
    elif(len(objectives) == 3):
        h = close_dist + width + height
    elif(len(objectives) == 2):
        h = close_dist + abs(objectives[0][0] - objectives[1][0]) + abs(objectives[0][1] - objectives[1][1])
    elif(len(objectives) == 1):
        h = close_dist

    return h


def astar_four_circles(maze):
    """
    [문제 03] 제시된 stage2의 맵 세가지를 A* Algorithm을 통해 최단 경로를 return하시오.(30점)
    (단 Heurstic Function은 위의 stage2_heuristic function을 직접 정의하여 사용해야 한다.)
    """

    end_points=maze.circlePoints()
    end_points.sort()

    path=[]

    ####################### Write Your Code Here ################################
    startNode = Node(None, maze.startPoint())
    startNode.obj = end_points
    
    openList = []
    push_MinHeap(openList, Node(None, (0,0)))
    push_MinHeap(openList, startNode)
    closedList = []

    while openList:
        current = pop_MinHeap(openList)   #f값이 가장 작은 노드 추출
               
        closedList.append([current.location, current.obj]) #cloesdList에 추출한 노드 정보 추가
        
        if(len(current.obj) == 0): #4개의 목표좌표 모두 지났을 경우 path에 경로 저장후 탐색 종료
            current_node = current
            while current_node is not None:
                path.append(current_node.location)
                current_node = current_node.parent
            break
           
        
        children = []
        a = maze.neighborPoints(current.location[0], current.location[1]) 
        for i in range(len(a)): #현재 위치에서 이동할 수 있는 좌표들 중 closedList에 있는 노드는 저장하지 않음
            if [a[i], current.obj] in closedList:
                continue
            children.append(Node(current, a[i]))
       
        for child in children: #closedList에 없는 자식 노드들의 정보
            child.obj = current.obj.copy()     
            if(child.location in child.obj):
                child.obj.remove(child.location)                  
            child.g = current.g + 1
            child.h = stage2_heuristic(child.location, end_points, child.obj)
            child.f = child.g + child.h
            
            append = 1            
            for node in openList:#자식노드가 closedList에는 없더라도 openList에 있을 경우 g값을 비교하여 저장 여부 결정                                
                if(child == node and child.g >= node.g):
                    append = 0
                    break

            if append:
                push_MinHeap(openList, child)   
    return path

    ############################################################################



# -------------------- Stage 03: Many circles - A* Algorithm -------------------- #
def find(v, root): 
    if root[v] != v:
        root[v] = find(root[v], root)
    return root[v]

def mst(vertexs, edges): ##Kruskal

    cost_sum=0
    ####################### Write Your Code Here ################################
    root = [i for i in range(len(vertexs))]  #정점의 root      
    check = [0 for i in range(len(vertexs))] #정점에 연결된 간선의 수
    edge_count = len(vertexs) - 1  #정점의 개수 - 1개만큼 간선 연결
        
    while edge_count > 0:
        weight, v, w = edges.pop(0) # 가중치가 가장 작은 edge 추출
        if check[v] > 1 or check[w] > 1: #정점에 연결된 간선이 2이상이면 연결하지 않음
            continue
        root_v = find(v, root)
        root_w = find(w, root)
        if root_v is root_w: # 두 정점의 root가 같으면 연결하지 않음 (연결시 cycle 생성됨)
            continue
        else:            
            root[root_w] = root_v
            edge_count -= 1
            check[v] += 1
            check[w] += 1
            cost_sum += weight   
    return cost_sum

def new_mst(objectives, mst_idx, mst_values, vertexs, idx, i, num_vertexs):
    
    cost_sum = 0
    ####################### Write Your Code Here ################################
    root = [i for i in range(len(vertexs))]  #정점의 root      
    check = [0 for i in range(len(vertexs))] #정점에 연결된 간선의 수
    edges = []
    edge_count = len(vertexs) - 1  #정점의 개수 - 1개만큼 간선 연결
    
    for j in range(len(vertexs)):      
        for k in range(j+1, len(vertexs)): ##모든 목표 좌표들을 연결하여 edge에 추가
            weight = abs(vertexs[j][0] - vertexs[k][0]) + abs(vertexs[j][1] - vertexs[k][1])
            edges.append([weight, j, k])    
    edges.sort()        # 가중치가 작은 순서대로 정렬
        
    while edge_count > 0:
        weight, v, w = edges.pop(0) # 가중치가 가장 작은 edge 추출
        if check[v] > 1 or check[w] > 1: #정점에 연결된 간선이 2이상이면 연결하지 않음
            continue
        root_v = find(v, root)
        root_w = find(w, root)
        if root_v is root_w: # 두 정점의 root가 같으면 연결하지 않음 (연결시 cycle 생성됨)
            continue
        else:            
            root[root_w] = root_v
            edge_count -= 1
            check[v] += 1
            check[w] += 1
            cost_sum += weight   
    mst_idx[tuple(vertexs)] = idx
    mst_values[idx] = cost_sum
    
    if(idx >= (1 << num_vertexs) - 1):
        print(idx, vertexs, cost_sum)

    for j in range(i+1, num_vertexs):
        vertexs.append(objectives[j])
        tmp = 1 << j
        new_mst(objectives, mst_idx, mst_values, vertexs, idx+tmp, j, num_vertexs)
        vertexs.pop()
    ############################################################################
def new_stage3_heuristic(p1, objectives, end_points, mst_idx, mst_values):    
    if len(objectives) == 0:
        return 0
    idx = mst_idx[tuple(objectives)]
    """
    j = 0
    tmp = 1
    for i in range(len(end_points)):
        if(j == len(objectives)):
            break
        if end_points[i] == objectives[j]:
            idx += tmp
            j = j+1
        tmp *= 2
    """
        
    closest_dist = -1
    for i in range(len(objectives)):
        if closest_dist < 0 or closest_dist > abs(p1[0] - objectives[i][0]) + abs(p1[1] - objectives[i][1]):
            closest_dist = abs(p1[0] - objectives[i][0]) + abs(p1[1] - objectives[i][1])
    
    return mst_values[idx] + closest_dist
    
    
def stage3_heuristic(p1, objectives):   
    h = 0
    vertexs = []
    edges = []
    if len(objectives) > 0:
        close_dist = -1
        index = 0
        for i in range(len(objectives)): 
            vertexs.append(objectives[i])
            if close_dist < 0 or close_dist > abs(p1[0] - objectives[i][0]) + abs(p1[1] - objectives[i][1]):#현재 좌표와 가장 가까운 좌표 
                close_dist = abs(p1[0] - objectives[i][0]) + abs(p1[1] - objectives[i][1])
                index = i
            for j in range(i+1,len(objectives)): ##모든 목표 좌표들을 연결하여 edge에 추가
                weight = abs(objectives[i][0] - objectives[j][0]) + abs(objectives[i][1] - objectives[j][1])
                edges.append([weight, i, j])    
        edges.sort()        # 가중치가 작은 순서대로 정렬
        vertexs.append(p1)
        edges.insert(0, [close_dist, index, len(vertexs) - 1]) #현재 좌표와 가장 가까운 좌표 사이의 연결만 edge에 추가
        h += mst(vertexs, edges) 
    return h

def astar_many_circles(maze):
    """
    [문제 04] 제시된 stage3의 맵 세가지를 A* Algorithm을 통해 최단 경로를 return하시오.(30점)
    (단 Heurstic Function은 위의 stage3_heuristic function을 직접 정의하여 사용해야 하고, minimum spanning tree
    알고리즘을 활용한 heuristic function이어야 한다.)
    """

    end_points= maze.circlePoints()
    end_points.sort()

    path=[]
    ####################### Write Your Code Here ###############################
    startNode = Node(None, maze.startPoint())
    startNode.obj = end_points.copy()
    openList = []
    push_MinHeap(openList, Node(None, (0,0)))
    push_MinHeap(openList, startNode)
    closedList = {} #closedList에 노드가 있는지 확인하기 위헤 dictionary형태 사용
    check_in_openList = {} #openList에 노드가 있는지 확인하기 위해 dictionary형태 사용
    check_in_openList[(startNode.location, tuple(startNode.obj))] = [startNode.g]    
    mst_value = {}
    mst_idx = {}
    
    vertexs = []
    tmp = 1
    for i in range(len(end_points)):
        vertexs.append(end_points[i])
        new_mst(end_points, mst_idx, mst_value, vertexs, tmp, i, len(end_points))
        tmp *= 2
        vertexs.pop()

    print("mst evaluation finish")

    k = len(end_points)
    search_cnt = 0
    while openList:
        search_cnt += 1
        if(search_cnt % 1000000 == 0):
            print(search_cnt)

        current = pop_MinHeap(openList) #f값이 가장 작은 노드 추출
        check_in_openList[(current.location, tuple(current.obj))].remove(current.g) 
        
        if closedList.get((current.location, tuple(current.obj))):
            continue
        closedList[(current.location, tuple(current.obj))] = True   #closedList에 해당 노드 정보 추가

        if(len(current.obj) == k):
            print(k)
            k-=1

        if(len(current.obj) == 0): # 모든 목표좌표 지났을 경우 path에 경로 추가 후 탐색 종료
            current_node = current
            while current_node is not None:
                path.append(current_node.location)
                current_node = current_node.parent
            break
                   
        children = []
        a = maze.neighborPoints(current.location[0], current.location[1])
        for i in range(len(a)): #현재 위치에서 이동할 수 있는 좌표들 중 closedList에 있는 노드는 저장하지 않음
            if not closedList.get((a[i], tuple(current.obj))):
                children.append(Node(current, a[i]))

        for child in children: #closedList에 없는 자식 노드들의 정보
            child.obj = current.obj.copy() 
            if(child.location in child.obj):
                child.obj.remove(child.location)              
            child.g = current.g + 1
            child.h = new_stage3_heuristic(child.location, child.obj, end_points, mst_idx, mst_value)
            child.f = child.g + child.h
            
            append = 1
            #자식노드가 closedList에는 없더라도 openList에 있을 경우 g값을 비교하여 저장 여부 결정
            if (child.location, tuple(child.obj)) in check_in_openList:
                for i in range(len(check_in_openList[(child.location, tuple(child.obj))])):
                    if check_in_openList[(child.location, tuple(child.obj))][i] <= child.g:
                        append = 0
                        break
                if append == 1:
                    check_in_openList[(child.location, tuple(child.obj))].append(child.g)
                    push_MinHeap(openList, child)
            else:
                push_MinHeap(openList, child)
                check_in_openList[(child.location, tuple(child.obj))] = [child.g]
    
    return path
    
    ############################################################################
