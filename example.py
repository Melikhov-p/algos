from Stack import Stack


def main():
    stack = Stack()
    print(stack.is_empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.is_empty())
    print(stack.peek())
    print(stack.pop())
    print(stack.size())


if __name__ == "__main__":
    main()
