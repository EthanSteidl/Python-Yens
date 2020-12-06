import Graph
import tests


#entry point for program.
#runs test functions for Yens and Dijkstras
def main():
    tests.test()
    #presentation()



def presentation():
    print("Presentation Yen")
    edges = [
        ('Me', 'High School', 4),
        ('Me', 'Park', 5),
        ('Me', 'Ice Rink', 1),
        ('High School','Ice Rink', 3),
        ('Park', 'Ice Rink', 3),
        ('Park', 'Thrift Store', 16),
        ('Ice Rink', 'Park', 3),
        ('Ice Rink', 'Thrift Store', 20),
        ('Ice Rink', 'High School', 3),
        ('Thrift Store', "McDonald's", 10),


    ]
    g = Graph.Graph()
    for edge in edges:
        g.add_edge_directed(*edge)

    paths = g.yen('Me', "McDonald's",2)
    print(paths)

main()