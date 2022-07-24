class Customer:
    if __name__ == '__main__':
     def __init__(self):
        self.rentalTime = 0
        self.gameName = ""
        self.bill = 0

    def requestRental(self):
        self.gameName = input("which game would you like to rent?")
        return self.gameName

    def returnGame(self):
        if self.gameName and self.rentalTime:
            return self.rentalTime, self.gameName
        else:
            return 0,0
