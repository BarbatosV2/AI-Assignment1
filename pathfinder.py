import sys

from astar import AStar #link with astar.py
from bfs import BFS     #link with bfs.py
from ucs import UCS     #link with ucs.py

class PathFinder:
    def __init__(self, startpoint, endpoint, pointM, pointN, pathmap, algo, heuristic=None):
        self.startpoint = startpoint
        self.endpoint = endpoint
        self.pointM = pointM
        self.pointN = pointN
        self.map = pathmap
        self.algo = algo
        self.heuristic = heuristic

    def run(self):
        if self.algo == "bfs":  #if bfs 
            model = BFS(self.startpoint, self.endpoint, self.pointM, self.pointN, self.map)
            route = model.run()
            return route
        
        if self.algo == "ucs":  #if ucs 
            model = UCS(self.startpoint, self.endpoint, self.pointM, self.pointN, self.map)
            route = model.run()
            return route
        
        if self.algo == "astar":    #if astar
            model = AStar(self.startpoint, self.endpoint, self.pointM, self.pointN, self.map, self.heuristic)
            route = model.run()
            return route


if __name__ == "__main__":
    mapfile = sys.argv[1]
    algo = sys.argv[2]

    if len(sys.argv) > 3:
        heuristic = sys.argv[3]
    else:
        heuristic = None
    
    mfile = open(mapfile)

    listy = mfile.readline()
    listy = listy.strip().split(" ")
    pointM, pointN = int(listy[0]), int(listy[1])
    startpoint = mfile.readline().split()
    startpoint = (int(startpoint[0])-1, int(startpoint[1])-1)
    endpoint = mfile.readline().split()
    endpoint = (int(endpoint[0])-1, int(endpoint[1])-1)

    pathmap = []
    for listy in mfile.readlines():
        listy = listy.strip().split()
        pathmap.append(listy)
    
    pf = PathFinder(startpoint, endpoint, pointM, pointN, pathmap, algo, heuristic)
    
    route = pf.run()

    output = open("./final.txt", "w+")  #write in final txt and open output

    for x, y in route:
        pathmap[x][y] = "*"   #to change * in the move location
    
    if not route:
        print("null")
        output.write("null\n")
    else:
        for listy in pathmap:
            s = " ".join(listy)
            print(s)
            output.write(s + "\n")
    output.close()
    mfile.close()