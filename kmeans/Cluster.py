from Point import *

class Cluster:
    dimension = 0
    points = []
    def __init__(self, all_points):
        self.points = all_points
        self.check_dimension()
        self.find_centroid()

    def check_dimension(self):
        assert (len(self.points) > 0), "Empty Set Of Points"
        self.dimension = self.points[0].dimension
        for single_point in self.points:
            assert (single_point.dimension == self.dimension), "Dimensions not matching"
        return

    def find_centroid(self):
        self.centroid = Point([0 for i in range(self.dimension)])
        for i in range(len(self.points)):
            self.centroid.add(self.points[i])

        self.centroid.divide(len(self.points))

    def update_centroid(self, new_points):
        last_centroid = self.centroid
        self.points = new_points
        self.check_dimension()
        #print  "updating Centroid"
        #for p in new_points:
        #    p.print_point()

        self.find_centroid()
        #print "After updating"
        #self.centroid.print_point()
        #print "Done"
        #print ""
        #print ""
        return last_centroid.distance(self.centroid)

    def print_cluster(self):
        print "Centroid is", self.centroid.print_point()
        for i in range(0,len(self.points)):
            print i," (",self.points[i].print_point(),")"