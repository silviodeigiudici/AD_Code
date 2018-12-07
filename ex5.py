class MySet:
    def __init__(self):
        self.set = set()
    #in order to do side effect on the set
    def union(self, new_set): #new_set is a MySet instance, not a set standard instance
        self.set = self.set.union(new_set.set)
    def add(self, elem):
        self.set.add(elem)
    def __str__(self):
        return str(self.set)

class Edge:
    def __init__(self, w, u, v):
        self.weight = w
        self.u = u
        self.v = v
        u.edges.append(self)
        v.edges.append(self)
    def __str__(self):
        return str(self.weight)

class Node:
    def __init__(self):
        self.set = None
        self.visit = False
        self.edges = []

def add_order(l, e):
    for i in range(0, len(l)):
        if l[i].weight == e.weight:
            break
    return l[:i] + [e] + l[i:]

def print_list(l):
    print("[ ", end="")
    for e in l:
        print(e, end=", ")
    print(" ]")

def order_fun(e):
    return e.weight

def kruscal(list_edge, e):
    list_edge.sort(key=order_fun)
    list_edge = add_order(list_edge, e)
    minimum_spanning_tree = []
    for edge in list_edge:
        u = edge.u
        v = edge.v
        set_u = u.set
        set_v = v.set
        if set_v == None and set_u == None:
            s = MySet()
            s.add(u)
            s.add(v)
            u.set = s
            v.set = s
            minimum_spanning_tree.append(edge)
        elif set_v == None and set_u != None:
            u.set.add(v)
            v.set = u.set
            minimum_spanning_tree.append(edge)
        elif set_v != None and set_u == None:
            v.set.add(u)
            u.set = v.set
            minimum_spanning_tree.append(edge)
        else:
            if set_u != set_v:
                u.set.union(set_v)
                v.set.union(set_u)
                minimum_spanning_tree.append(edge)
            else:
                if edge == e:
                    print("No MST found contained e")
                    return []
    return minimum_spanning_tree

list_edges = []
n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()
e1 = Edge(3, n2, n3)
e2 = Edge(1, n1, n2)
e3 = Edge(2, n1, n4)
e4 = Edge(3, n3, n4)
e5 = Edge(4, n1, n3)
list_edges += [e1, e2, e3, e5]

mst = kruscal(list_edges, e4) #note that list_edge doesn't have e, it will add in the algorithm

print("MST with e:")
print_list(mst)
