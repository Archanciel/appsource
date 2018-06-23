class SayHello:
    def __init__(self, fullName):
        self.firstName, self.lastName = fullName.split(' ')

    def greet(self):
        return 'Hello ' + self.firstName + ' ' + self.lastName + ', how are you doing ?'

s = SayHello('Philippe Brolly')
print(s.greet())