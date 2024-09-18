from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_edge(self, edge: "Node"):
        self.edges.append(edge)

    def get_edges(self):
        return self.edges

    def has_child(self):
        if self.edges:
            return True
        return False


class Graph:
    def __init__(self):
        self.nodes: set = set()
        self.root: Optional[Node] = None

    def add_node(self, value):
        self.nodes.add(Node(value))

    def add_edge(self, value1, value2):
        node1 = self.get_node(value1)
        node2 = self.get_node(value2)
        node1.add_edge(node2)

    def show(self):
        for node in self.nodes:
            print(node.value, ' ', end='')

    def nodes_count(self):
        return len(self.nodes)

    def get_node(self, value) -> Optional[Node]:
        for node in self.nodes:
            if node.value == value:
                return node
        return None
