import Graph

#performs test cases
def test():
    test_Dijkstra()
    test_single_Dijkstra()
    test_yen_1()
    test_yen_2()
    test_yen_3()
    test_presentation()




#test case for example used in presentation
def test_presentation():
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

    answer = [['Me', 'Ice Rink', 'Park', 'Thrift Store', "McDonald's"], ['Me', 'Ice Rink', 'Thrift Store', "McDonald's"]]
    if(paths != answer):
        print('Paths were\n', paths)
        print('It should have been\n', answer)

#test for k=3 yens
def test_yen_3():
    print("test Yen 3")
    edges = [
        ('C', 'D', 3),
        ('C', 'E', 2),
        ('D', 'F', 4),
        ('E', 'D', 1),
        ('E', 'F', 2),
        ('E', 'G', 3),
        ('F', 'G', 2),
        ('F', 'H', 1),
        ('G', 'H', 2),

    ]
    g2 = Graph.Graph()
    for edge in edges:
        g2.add_edge_directed(*edge)

    paths = g2.yen('C','H',3)

    answer = [['C', 'E', 'F', 'H'], ['C', 'E', 'G', 'H'], ['C', 'D', 'F', 'H']]
    if(paths != answer):
        print('Paths were\n', paths)
        print('It should have been\n', answer)


#test for k=2 yens
def test_yen_2():
    print("test Yen 2")
    edges = [
        ('C', 'D', 3),
        ('C', 'E', 2),
        ('D', 'F', 4),
        ('E', 'D', 1),
        ('E', 'F', 2),
        ('E', 'G', 3),
        ('F', 'G', 2),
        ('F', 'H', 1),
        ('G', 'H', 2),

    ]
    g2 = Graph.Graph()
    for edge in edges:
        g2.add_edge_directed(*edge)

    paths = g2.yen('C','H',2)

    answer = [['C', 'E', 'F', 'H'], ['C', 'E', 'G', 'H']]
    if(paths != answer):
        print('Paths were\n', paths)
        print('It should have been\n', answer)

#test for k=1 yens
def test_yen_1():
    print("test Yen 1")
    edges = [
        ('C', 'D', 3),
        ('C', 'E', 2),
        ('D', 'F', 4),
        ('E', 'D', 1),
        ('E', 'F', 2),
        ('E', 'G', 3),
        ('F', 'G', 2),
        ('F', 'H', 1),
        ('G', 'H', 2),

    ]
    g2 = Graph.Graph()
    for edge in edges:
        g2.add_edge_directed(*edge)

    paths = g2.yen('C','H',1)

    answer = [['C', 'E', 'F', 'H']]
    if(paths != answer):
        print('Paths were\n', paths)
        print('It should have been\n', answer)

#test Dijkstras pathfind
def test_Dijkstra():
    print('test Dijkstra')
    edges = [
        ('X', 'A', 7),
        ('X', 'B', 2),
        ('X', 'C', 3),
        ('X', 'E', 4),
        ('A', 'B', 3),
        ('A', 'D', 4),
        ('B', 'D', 4),
        ('B', 'H', 5),
        ('C', 'L', 2),
        ('D', 'F', 1),
        ('F', 'H', 3),
        ('G', 'H', 2),
        ('G', 'Y', 2),
        ('I', 'J', 6),
        ('I', 'K', 4),
        ('I', 'L', 4),
        ('J', 'L', 1),
        ('K', 'Y', 5),
        ('L', 'Y', 2),
    ]
    g2 = Graph.Graph()
    for edge in edges:
        g2.add_edge(*edge)

    path = g2.dijkstra('X','Y')
    answer = ['X', 'C', 'L', 'Y']
    if(path != answer):
        print('Dijkstras found\n', answer)
        print('It should have been\n', answer)

#tests when Dijkstras has a direct path to the end
def test_single_Dijkstra():
    print('test Dijkstra single')
    edges = [
        ('X', 'A', 7),
        ('X', 'B', 2),
        ('X', 'C', 3),
        ('X', 'E', 4),
        ('A', 'B', 3),
        ('A', 'D', 4),
        ('B', 'D', 4),
        ('B', 'H', 5),
        ('C', 'L', 2),
        ('D', 'F', 1),
        ('F', 'H', 3),
        ('G', 'H', 2),
        ('G', 'Y', 2),
        ('I', 'J', 6),
        ('I', 'K', 4),
        ('I', 'L', 4),
        ('J', 'L', 1),
        ('K', 'Y', 5),
        ('L', 'Y', 2),
        ('X', 'Y', 5),
    ]
    g2 = Graph.Graph()
    for edge in edges:
        g2.add_edge(*edge)

    path = g2.dijkstra('X','Y')
    answer = ['X', 'Y']
    if(path != answer):
        print('Dijkstras found\n', answer)
        print('It should have been\n', answer)