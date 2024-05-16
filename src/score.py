import json
class score:
    def __init__(self):
        self.filename = "assets/score.json"
        self.getscores() 
    def getscores(self):
        try: 
            with open(self.filename,"r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {"win": 0, "loss": 0, "tie": 0}
        return self.data
    def setscores(self):
        with open(self.filename,"w") as file:
            json.dump(self.data, file)
    def win(self):
        self.data["win"] +=1
    def loss(self):
        self.data["loss"] +=1
    def tie(self):
        self.data["tie"] +=1
