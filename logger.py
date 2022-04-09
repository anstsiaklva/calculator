class Logger:
    def __init__(self, addr="history.txt"):
        self.history = open(addr, "w+")

    def log(self, string):
        self.history.write(string) 
    
    def clear(self):
        self.history.close()