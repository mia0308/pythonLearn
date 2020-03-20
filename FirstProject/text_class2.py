class Animal(object):
    def __init__(self, kind, voice):
        self.kind = kind
        self.voice = voice

    def speak(self):
        print(self.voice)


cat = Animal('cat', 'miaomiao')
dog = Animal('dog', 'wangwang')
cat.speak()
dog.speak()
