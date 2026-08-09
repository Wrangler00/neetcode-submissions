class Node:
    def __init__(self,key:int, val:int):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:
    hashMap : dict[int,Node] = {}

    def __init__(self, capacity: int):
        self.capacity:int = capacity
        # self.__cacheSize:int = 0
        self.__head: Node = Node(0,0)
        self.__tail: Node = Node(0,-1)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.hashMap = {}
        

    def __adjust(self, node: Node):
        # remove from current position
        node.prev.next = node.next
        node.next.prev = node.prev

        # insert after head
        node.prev = self.__head
        node.next = self.__head.next
        self.__head.next.prev = node
        self.__head.next = node

    def __add(self, node: Node):
        node.next = self.__head.next
        self.__head.next = node
        node.prev = self.__head
        node.next.prev = node

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        node = self.hashMap[key]
        self.__adjust(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        node : Node = None
        # print(value)
        if key not in self.hashMap:
            if len(self.hashMap) == self.capacity:
                #remove lfu cache
                # print(value)
                last = self.__tail.prev
                # print(last.val)
                # print(len(self.hashMap))
                # print(last.val)
                del self.hashMap[last.key]
                if last.prev:
                    last.prev.next = self.__tail
                self.__tail.prev = last.prev

            node = Node(key,value)
            self.hashMap[key] = node
            self.__add(node)
        else:
            self.hashMap[key].val = value
            self.__adjust(self.hashMap[key])

                
                

