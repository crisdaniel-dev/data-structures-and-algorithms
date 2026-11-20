class Node:
    
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
        
    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, prev):
        self.__prev = prev
        
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next):
        self.__next = next