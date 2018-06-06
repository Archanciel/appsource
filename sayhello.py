class SayHello:
    def __init__(self, fullName):
        self.fullName = fullName

    def greet(self):
        return 'Hello ' + self.fullName

s = SayHello('Philippe Brolly')
print(s.greet())