class Fila:
    def __init__(self, data = []):
        self.data = data
    
    def append(self, data):
        self.data.append(data)
    
    def pop(self):
        return(self.data.pop(0))
    
    def peek(self):
        return(self.data[0])

    def is_empty(self):
        return len(self.data) == 0
    
    def __str__(self):
        return str(self.data)
    
if __name__ == '__main__':
    s = Fila([1,2,3])
    print(s)
    s.append(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.is_empty())