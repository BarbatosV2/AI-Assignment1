import heapq
import itertools
import math

class Move:
    def __init__(self, x, y, parent=None, val=0, odr=0):
        self.x = x
        self.y = y
        self.parent = parent
        self.val = val
        self.odr = odr
    
    def __lt__(self, otr):
        if self.val == otr.val:
            return self.odr < otr.odr
        return self.val < otr.val

    def get_direc(self, odr):
        map_dir = {'T': (self.x - 1, self.y),'B': (self.x + 1, self.y),'L': (self.x, self.y - 1),'R': (self.x, self.y + 1)}
        #defining the point direction to move
        sides = []
        
        for step in list(odr):
            sides.append(map_dir[step])
        
        return sides  #return the sides 
    
class AStar:
    
    #define eculidean
    def euclidean(self, startpoint, endpoint):
        return math.sqrt((endpoint[0] - startpoint[0])**2 + (endpoint[1] - startpoint[1])**2)   
 
    #define manhattan 
    def manhattan(self, startpoint, endpoint):
        return abs(startpoint[0] - endpoint[0]) + abs(startpoint[1] - endpoint[1])
    
    def __init__(self, startpoint, endpoint, pointM, pointN, pathmap, heuristic):
        self.x0, self.y0 = startpoint
        self.xt, self.yt = endpoint
        self.pointM = pointM
        self.pointN = pointN
        self.map = pathmap
        if heuristic == "manhattan":
            self.heuristic = self.manhattan
        elif heuristic == "euclidean":
            self.heuristic = self.euclidean
        else:
            print("Error")
    
    def run(self):
        h_root = self.heuristic((self.x0, self.y0), (self.xt, self.yt))
        s = Move(self.x0, self.y0)
        
        p_point = [(h_root, 0, s)]
        heapq.heapify(p_point)
        reached = set()
        reached.add((self.x0, self.y0))
        summ = itertools.count()
        
        while p_point:
            f, o, node = heapq.heappop(p_point)

            #to reach the end point
            if node.x == self.xt and node.y == self.yt:
                
                route = []
                
                while node is not None:
                    route.append((node.x, node.y))
                    node = node.parent
                return route[::-1]
            
            for nX, nY in node.get_direc("TBLR"):
                if (0 <= nX < self.pointM and 0 <= nY < self.pointN) and (self.map[nX][nY] != "X") and ((nX, nY) not in reached):
                    val = 1 + node.val + max(0, int(self.map[nX][nY]) - int(self.map[node.x][node.y]))
                    f_value = val + self.heuristic((nX, nY), (self.xt, self.yt))
                    odr = next(summ)
                    state_nbr = Move(nX, nY, node, val, odr)
                    heapq.heappush(p_point, (f_value, odr, state_nbr))
                    reached.add((nX, nY))
        
        return []