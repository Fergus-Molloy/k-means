import sys
class Point:
    def __init__(self, X, Y):
        self.x=X
        self.y=Y

def distance(p1, p2):
    sqaure1 = (p1.x-p2.x)**2
    sqaure2 = (p1.y-p2.y)**2
    return (sqaure1+sqaure2)**0.5

def equal_points(p1, p2):
    if(p1.x==p2.x and p1.y==p2.y):
        return True
    return False

def average_point(arr):
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
    a0 = Point(1.0,1.0)
    a1 = Point(1.0,0.0)
    a2 = Point(0.0,2.0)
    a3 = Point(2.0,4.0)
    a4 = Point(3.0,5.0)
    arr = [a0, a1, a2, a3, a4]

    #k==2
    cluster_means = [a0, a2]
    prev_cluster_means = [a1, a3]
    cl1 = []
    cl2 = []
    for i in range(iterations):
        if(equal_points(cluster_means[0],prev_cluster_means[0]) and equal_points(cluster_means[1], prev_cluster_means[1])):
            print("iterations: {}".format(i))
            break;
        for j in arr:
            distance1 = distance(j, cluster_means[0])
            distance2 = distance(j, cluster_means[1])
            if(distance1<distance2):
                if(not j in cl1 and not j in cl2):
                    cl1.append(j)
                if(j in cl1 and j in cl2):
                    cl2.remove(j)
                if(j in cl2):
                    cl2.remove(j)
                    cl1.append(j)
            else:
                if(not (j in cl1 or j in cl2)):
                    cl2.append(j)
                if(j in cl1 and j in cl2):
                    cl1.remove(j)
                if(j in cl1):
                    cl2.remove(j)
                    cl1.append(j)
        #calculate new means
        prev_cluster_means[0] = cluster_means[0]
        prev_cluster_means[1] = cluster_means[1]
        cluster_means[0] = average_point(cl1)
        cluster_means[1] = average_point(cl2)
    else:
        print("iterations: {}".format(iterations))

    print("Cluster 1:")
    for x in cl1:
        print("X: {0}, Y: {1}".format(x.x,x.y))
    print("final mean:\nX: {}, Y: {}\n".format(cluster_means[0].x, cluster_means[0].y))
    print("Cluster 2:")
    for x in cl2:
        print("X: {0}, Y: {1}".format(x.x,x.y))
    print("final mean:\nX: {}, Y: {}".format(cluster_means[1].x, cluster_means[1].y))


if __name__ == "__main__":
    try:
        main(iterations=int(sys.argv[1]))
    except IndexError:
        main()
    except KeyboardInterrupt:
        exit()
