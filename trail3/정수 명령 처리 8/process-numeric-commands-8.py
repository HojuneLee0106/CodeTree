N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

class Node:
    def __init__(self, data): # 매개변수를 하나로 통일
        self.data = data
        self.prev = None
        self.next = None

class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0
        
    def push_front(self, new_data): # n 대신 self
        new_node = Node(new_data)
        if self.head != None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.node_num += 1

    def push_back(self, new_data): # n 대신 self
        new_node = Node(new_data)
        if self.tail != None: # tail 대신 None으로 수정
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.node_num += 1
        
    def pop_front(self): # self 추가
        if self.node_num == 0: return -1 # 예외 처리
        if self.head.next == None:
            temp = self.head
            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            self.node_num -= 1
            return temp.data
            
    def pop_back(self): # self 추가
        if self.node_num == 0: return -1 # 예외 처리
        if self.tail.prev == None:
            temp = self.tail
            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            self.node_num -= 1
            return temp.data # tamp.data -> temp.data 오타 수정

    def size(self): # self 추가
        return self.node_num
        
    def empty(self): # self 추가
        return 1 if self.node_num == 0 else 0
        
    def front(self): # self 추가
        if self.node_num == 0: return -1
        return self.head.data
        
    def back(self): # self 추가
        if self.node_num == 0: return -1
        return self.tail.data

l = DLList()

for i in range(N):
    if command[i] == "push_back":
        l.push_back(A[i])
    elif command[i] == "push_front":
        l.push_front(A[i])
    elif command[i] == "front":
        print(l.front())
    elif command[i] == "size":
        print(l.size())
    elif command[i] == "back":
        print(l.back())
    elif command[i] == "pop_front":
        print(l.pop_front()) # pop_front된 값을 출력하도록 print 추가
    elif command[i] == "pop_back":
        print(l.pop_back())  # pop_back된 값을 출력하도록 print 추가
    elif command[i] == "empty":
        print(l.empty())

# Please write your code here.
