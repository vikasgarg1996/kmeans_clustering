import random
from Cluster import *

num_points = 10
dimensions = 2
lower = 0
upper = 9
num_clusters = 2
cutoff_distance = 0.00001

def initialize_data():
    random_points = [Point([random.uniform(lower,upper) for i in range(dimensions)]) for j in range(num_points)]
    #for p in random_points:
        #p.print_point()
    return random_points

def create_random_clusters(points):
    minarray = points[0].coordinates[:]
    maxarray = points[0].coordinates[:]
    for i in range(1,len(points)):
        for j in range(0,dimensions):
            minarray[j] = min(minarray[j], points[i].coordinates[j])
            maxarray[j] = max(maxarray[j], points[i].coordinates[j])

    random_clusters = []
    for i in range(num_clusters):
        point_coords = []
        for j in range(dimensions):
            point_coords.append(random.uniform(minarray[j],maxarray[j]))
        point_obj = Point(point_coords)
        random_clusters.append(Cluster([point_obj]))
    #for c in random_clusters:
        #c.print_cluster()

    return  random_clusters


def assign_clusters(points,clusters):
    assigned = [ [] for c in clusters]
    for p in points:
        min_distance = p.distance(clusters[0].centroid)
        good_cluster = 0
        for i in range(1,len(clusters)):
            distance = p.distance(clusters[i].centroid)
            if distance<min_distance:
                min_distance = distance
                good_cluster = i
        assigned[good_cluster].append(p)
        #print "Assigning to", good_cluster

    return assigned

def algorithm(points):
    clusters = create_random_clusters(points)
    iteration_count = 0
    while True:
        iteration_count += 1
        assigned = assign_clusters(points,clusters)
        max_update = 0
        for i in range(len(clusters)):
            if(len(assigned[i]) > 0):
                here_update = clusters[i].update_centroid(assigned[i])
                max_update= max(max_update,here_update)

        #print ""
        #print ""

        #print iteration_count
        cluster_count = 0
        for c in clusters:
            cluster_count += 1
            #print "Cluster is",cluster_count,"\n"
            #c.print_cluster()

        if max_update < cutoff_distance:
            print "Finished Iterations",iteration_count
            break
    return clusters

def kmeans():
    points = initialize_data()
    clusters = algorithm(points)
    '''for i,c in enumerate(clusters):
        for p in c.points:
            print " Cluster: ", i, "\t Point :", p
    return'''

if __name__ == "__main__":
    kmeans()