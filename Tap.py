class Tap:
    def __init__(self, i):
        self.id = i
        self.isAvailable = False

    def __str__(self):
        string = 'id:\n\t' + str(self.id) + '\n'
        string += 'isAvailable:\n\t' + str(self.isAvailable) + '\n'
        string += 'visitors (' + str(len(self.visitors)) + '):\n\t' + str(self.visitors) + '\n'
        string += 'utilityVisitors (' + str(len(self.utilityVisitors)) + '):\n\t' + str(self.utilityVisitors)
        return string
