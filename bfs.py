import random

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
    
class BFS:
    def __init__(self, startpoint, endpoint, pointM, pointN, pathmap):
        self.x0, self.y0 = startpoint
        self.xt, self.yt = endpoint
        self.pointM = pointM
        self.pointN = pointN
        self.map = pathmap
    
    def run(self, randomized=False):
        s = Move(self.x0, self.y0)
        
        point = [s]
        reached = set()
        reached.add((self.x0, self.y0))

        while point:
            node = point.pop(0)

            #to reach the end point
            if node.x == self.xt and node.y == self.yt:

                route = []
                while node is not None:
                    route.append((node.x, node.y))
                    node = node.parent
                return route[::-1]
            
            
            if not randomized:
                sides = node.get_direc("TBLR")
            else:
                odr = "TBLR"
                random_order = ''.join(random.sample(odr, len(odr)))
                sides = node.get_direc(random_order)
            
            for nX, nY in sides:
                if (0 <= nX < self.pointM and 0 <= nY < self.pointN) and (self.map[nX][nY] != "X") and ((nX, nY) not in reached):
                    state_nbr = Move(nX, nY, node)
                    point.append(state_nbr)
                    reached.add((nX, nY))
        
        return []