class SayHello:
    GREETING_MESSAGE = "Hello {} !"

    def __init__(self, fullName):
        self.fullName = fullName

    def greet(self):
        return self.GREETING_MESSAGE.format(self.fullName)

s = SayHello('Philippe Brolly')
print(s.greet())