class SayHello:
    GREETING_MESSAGE = "Hello {} {}, how are you doing ?"

    def __init__(self, fullName):
        self.firstName, self.lastName = fullName.split(' ')

    def greet(self):
        return self.GREETING_MESSAGE.format(self.firstName, self.lastName)

s = SayHello('Philippe Brolly')
print(s.greet())