
import nose.tools as nt  # contains testing tools like ok_, eq_, etc.
import kmeans.Kmeans
import kmeans.Point
import random
import math

'''def test_distancePointFromCentroid():
    num_points = 100
    dimensions = 10
    lower = 0
    upper = 30
    num_clusters = 50
    opt_cutoff = 0.00001


    points = [kmeans.Point.Point([random.uniform(lower,upper) for i in range(dimensions)]) for j in range(num_points)]

    clusters = kmeans.Kmeans.algorithm(points)

    for c in clusters:
        if(len(c.points) > 0):
            for p in c.points:
                for oc in clusters:
                    if oc.centroid.equals(c.centroid):
                        assert(p.distance(c.centroid) <= p.distance(oc.centroid))'''


def test_internalClusterDistance():

    num_points = 10
    dimensions = 2
    lower = 0
    upper = 9
    num_clusters = 2
    opt_cutoff = 0.00001

    points =[]
    x = 0
    for i in xrange(0, num_points/2):
        points += [kmeans.Point.Point([x, x])]
    x = x+0.5

    x = 7
    for i in xrange(0, num_points/2):
        points += [kmeans.Point.Point([x, x])]
    x = x+0.5

    clusters = kmeans.Kmeans.algorithm(points)
    print "Hello"

    for c in clusters:
        c.print_cluster()

    for c in clusters:
        if(len(c.points) > 0):
            for p in c.points:
                assert(p.distance(c.centroid) <= math.sqrt(2))


def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

