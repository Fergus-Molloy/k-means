import sys
class Point:
    #class for holding x and y co-ordinates
    def __init__(self, X, Y):
        self.x=X
        self.y=Y

def distance(p1, p2):
    #return the euclidian distance between two points
    sqaure1 = (p1.x-p2.x)**2
    sqaure2 = (p2.y-p2.y)**2
    return (sqaure1+sqaure2)**0.5

def equal_points(p1, p2):
    #check if two points are equall
    if(p1.x==p2.x and p1.y==p2.y):
        return True
    return False

def average_point(arr):
    #return the mean point from an array of points
    p=Point(0.0,0.0)
    total_x=0
    total_y=0
    for x in arr:
        total_x+=x.x
        total_y+=x.y
    p.x=total_x/len(arr)
    p.y=total_y/len(arr)
    return p

def main(iterations=1):
    #create points and add to arr
    a0 = Point(1.0,1.0)
    a1 = Point(2.0,1.0)
    a2 = Point(4.0,3.0)
    a3 = Point(5.0,4.0)
    arr = [a0, a1, a2, a3]
    #k==2
    cluster_means = [a0, a1]
    prev_cluster_means = [a1, a3]
    cl1 = []
    cl2 = []
    for i in range(iterations):
        #check if previous means are the same
        #if they are then break
        if(equal_points(cluster_means[0],prev_cluster_means[0])
           and equal_points(cluster_means[1], prev_cluster_means[1])):
            print("iterations: {}".format(i)) #print nuber of iterations if prev is the same
            break;

        for j in arr:
            #get euclidian distances between point and each of the cluster means
            distance1 = distance(j, cluster_means[0])
            distance2 = distance(j, cluster_means[1])
            #check which cluster point is closest to
            if(distance1<distance2):
                #closest to cluster1
                if(not j in cl1 and not j in cl2): #not in either cluster
                    cl1.append(j)
                if(j in cl1 and j in cl2): #in both clusters
                    cl2.remove(j)
                if(j in cl2): #swap clusters
                    cl2.remove(j)
                    cl1.append(j)
            else:
                #closest to cluster 2
                if(not (j in cl1 or j in cl2)): #not in either cluster
                    cl2.append(j)
                if(j in cl1 and j in cl2): #in both clusters
                    cl1.remove(j)
                if(j in cl1): #swap clusters
                    cl2.remove(j)
                    cl1.append(j)

        prev_cluster_means[0] = cluster_means[0]
        prev_cluster_means[1] = cluster_means[1]
        #calculate new means
        cluster_means[0] = average_point(cl1)
        cluster_means[1] = average_point(cl2)
    else:
        print("iterations: {}".format(iterations)) #print number of iterations if no break

    print("~~~~~~~~~~~~~~~~~~~~")
    #Print output
    print("Cluster 1:")
    print("final mean -> X: {:.5f}, Y: {:.5f}".format(cluster_means[0].x, cluster_means[0].y))
    for x in cl1:
        print("X: {0}, Y: {1}".format(x.x,x.y))
    print("\nCluster 2:")
    print("final mean -> X: {:.5f}, Y: {:.5f}".format(cluster_means[1].x, cluster_means[1].y))
    for x in cl2:
        print("X: {0}, Y: {1}".format(x.x,x.y))


if __name__ == "__main__":
    try:
        i=int(sys.argv[1])
        if(i<1):
            raise ValueError("number of iterations cannot be less than 1")
        main(iterations=i)
    except ValueError as e:
        print(e)
    except IndexError:
        main()
    except KeyboardInterrupt:
        exit()
