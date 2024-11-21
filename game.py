
class Guy:
    def __init__(self, name):
        self.name = name
        self.said = set()

    def say(self, text):
        if text in self.said:
            return
        self.said.add(text)
        print(self.name + ": " + text + "\n")

def write(text="", end="\n"):
    print("\t" + text.replace("\n", "\t"), end=end)

def narrate(text):
    print(text + "\n")
