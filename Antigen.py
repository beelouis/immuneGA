class Antigen:
    def __init__(self, label):
        self.string = []
        self.label = label
        self.generateString()

    def generateString(self):
        pass

    def infect(self, host):
        self.host = host
        self.host.getInfected(self)
