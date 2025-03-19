class Queue:

    def __init__(self):
        self.queue = []
        self.rear = -1

    def is_empty(self):
        if self.rear == -1:
            return 1
        else:
            return 0

    def front_enqueue(self,element):
        self.queue.insert(0,element)
        self.rear = self.rear + 1


    def rear_enqueue(self,element):
        self.queue.append(element)
        self.rear = self.rear + 1

        print(f"{element} is added to END of the Queue..")

    def front_dequeue(self):
        if self.is_empty() == 1:
            print("Queue Under flow Error")
        else:

            self.rear = self.rear - 1
            print(f"{self.queue.pop(0)} is Removed from the Queue..")


    def rear_dequeue(self):
        if self.is_empty() == 1:
            print("Queue Under flow Error")
        else:

            self.rear = self.rear - 1
            print(f"{self.queue.pop(-1)} is Removed from the Queue..")


    def display(self):
        print(self.queue)


q = Queue()
q.front_enqueue("lossu")
q.front_enqueue("Minato")
q.rear_enqueue(23)
q.rear_enqueue('Mukesh')
q.rear_enqueue(20)
q.rear_enqueue(29)
q.rear_enqueue(26)
q.rear_enqueue(27)



q.display()

q.rear_dequeue()
q.display()
q.rear_dequeue()
q.display()




