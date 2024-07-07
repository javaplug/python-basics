
class Parent:
    def __init__(self, value):
        self.value = value

    def spam(self):
        print('from Parent.spam value :', self.value)

    def grok(self):
        print('from parent.grok')
        self.spam()
