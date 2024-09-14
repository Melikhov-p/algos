from Stack import Stack
from Queue import Queue


def main():
    # stack = Stack()
    # print(stack.is_empty())
    #
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    #
    # print(stack.is_empty())

    queue = Queue()
    print(queue.is_empty())

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.is_empty())

    print(queue.dequeue())


if __name__ == "__main__":
    main()
