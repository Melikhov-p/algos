from DataStructures import LinkedList
from DataStructures import Graph, Node


def main():
    # stack = Stack()
    # print(stack.is_empty())
    #
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    #
    # print(stack.is_empty())

    # queue = Queue()
    # print(queue.is_empty())
    #
    # queue.enqueue(1)
    # queue.enqueue(2)
    # queue.enqueue(3)
    # print(queue.is_empty())
    #
    # print(queue.dequeue())

    # linkedlist = LinkedList()
    # linkedlist.show()
    # linkedlist.insert(1)
    # linkedlist.insert(2)
    # linkedlist.insert(3)
    # print(linkedlist[1].next)
    # linkedlist.show()

    graph = Graph()
    graph.nodes.add(Node(1))
    graph.nodes.add(Node(2))
    graph.nodes.add(Node(3))
    graph.show()
    print("\n")

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)

    graph.add_node(4)
    graph.add_edge(3, 4)

    graph.add_node(5)
    graph.add_edge(1, 5)

    graph.add_node(6)
    graph.add_edge(2, 6)

    graph.show()


if __name__ == "__main__":
    main()
