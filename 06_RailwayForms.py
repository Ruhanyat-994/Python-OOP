class RailwayForm:
    formType ="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


ruhanyatsApplication=RailwayForm()
ruhanyatsApplication.name="Ruhanyat"
ruhanyatsApplication.train = "Tista"
ruhanyatsApplication.printData()