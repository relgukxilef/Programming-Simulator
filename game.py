
class Guy:
    def __init__(self, name):
        self.name = name
        self.said = set()

    def say(self, text):
        if text in self.said:
            return
        self.said.add(text)
        print(self.name + ": " + text + "\n")

def write(text):
    print("\t" + text.replace("\n", "\t"))

def narrate(text):
    print(text + "\n")
