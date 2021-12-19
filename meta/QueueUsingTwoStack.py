# Enter your code here. Read input from STDIN. Print output to STDOUT

import os


class Queue:
    def __init__(self):
        self.stackpush = []
        self.stackdelete = []

    def enQueue(self, x):
        self.stackpush.append(x)

    # Dequeue an item from the queue
    def deQueue(self):
        if not self.stackdelete:
            while self.stackpush:
                self.stackdelete.append(self.stackpush.pop())
        self.stackdelete.pop()

    def peek(self):
        if not self.stackdelete:
            while self.stackpush:
                self.stackdelete.append(self.stackpush.pop())

        # print(len(self.stackdelete))
        return self.stackdelete[-1]

# https://www.youtube.com/watch?v=EUNGb8PMoCc
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queue = Queue()
    num_op = int(raw_input())
    for index_op in range(num_op):

        cur_op = list(raw_input().split(' '))
        # fptr.write(str(cur_op))
        if int(cur_op[0]) == 1:
            queue.enQueue(int(cur_op[1]))
        elif int(cur_op[0]) == 2:
            queue.deQueue()
        else:
            fptr.write(str(queue.peek()) + '\n')