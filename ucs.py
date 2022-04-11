import heapq
import itertools

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

class UCS:
    def __init__(self, startpoint, endpoint, pointM, pointN, pathmap):
        self.x0, self.y0 = startpoint
        self.xt, self.yt = endpoint
        self.pointM = pointM
        self.pointN = pointN
        self.map = pathmap

    def run(self):
        s = Move(self.x0, self.y0)
        
        p_point = [s]
        heapq.heapify(p_point)
        reached = set()
        reached.add((self.x0, self.y0))
        summ = itertools.count()

        while p_point:
            node = heapq.heappop(p_point)

            #to reach the end point 
            if node.x == self.xt and node.y == self.yt:
                route = []
                
                #if there is no node
                while node is not None:
                    route.append((node.x, node.y))
                    node = node.parent
                return route[::-1]
            
            for nX, nY in node.get_direc("TBLR"):
                if (0 <= nX < self.pointM and 0 <= nY < self.pointN) and (self.map[nX][nY] != "X") and ((nX, nY) not in reached):
                    val = 1 + node.val + max(0, int(self.map[nX][nY]) - int(self.map[node.x][node.y]))
                    state_nbr = Move(nX, nY, node, val, next(summ))
                    heapq.heappush(p_point, state_nbr)
                    reached.add((nX, nY))
        
        return []