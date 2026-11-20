class Node:
    
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
        self.next = None
        
    @property
    def priority(self):
        return self.__priority
    
    @priority.setter
    def priority(self, priority):
        self.__priority = priority
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
        
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next):
        self.__next = next