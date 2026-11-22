class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int) or isinstance(data, bool):
            raise TypeError("Data must be an integer")
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next
