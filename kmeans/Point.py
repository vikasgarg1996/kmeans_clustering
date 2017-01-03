import math

class Point:
    dimension = 0

    def __init__(self, all_coordinates):
        self.dimension = len(all_coordinates)
        self.coordinates = all_coordinates

    def add(self, p):
        assert (p.dimension == self.dimension), "Dimensions Not Matching"
        for i in range(self.dimension):
            self.coordinates[i] = self.coordinates[i] + p.coordinates[i]

    def divide(self,div):
        assert (div != 0), "Can not divide with Zero"
        for i in range(self.dimension):
            self.coordinates[i] = self.coordinates[i]/div

    def distance(self, p):
        assert (p.dimension == self.dimension), "Dimensions Not Matching"
        sqr_dist = 0
        for i in range(self.dimension):
            sqr_dist += pow(self.coordinates[i] - p.coordinates[i],2)
        return math.sqrt(sqr_dist)

    def print_point(self):
        print self.coordinates[0],
        for i in range(self.dimension-1):
            print ", ",self.coordinates[i+1],
        print ""

    def equals(self,p):
        for i in range(self.dimension):
            if(self.coordinates[i]!=p.coordinates[i]):
                return False
        return True





