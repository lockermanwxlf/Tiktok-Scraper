import csv
import os
import json

class Profiles:
    def __init__(self, use_state = True) -> None:
        os.makedirs(".state", exist_ok=True)
        if not os.path.exists(".state/state.json"):
            with open(".state/state.json", "w") as file:
                json.dump(
                    obj={ "last": 0 },
                    fp=file
                )
        with open(".state/state.json", "r+") as file:
            state = json.load(file)
        self.__profiles = list(csv.reader(open("profiles.csv", "r")))[1:]
        self.__place = 0 if not use_state or state["last"] >= len(self.__profiles) else state["last"]
        
    def __iter__(self):
        if self.__place >= len(self.__profiles):
            self.__profiles = list(csv.reader(open("profiles.csv", "r")))[1:]
            self.__place = 0
        return self
    
    def __next__(self):
        with open(".state/state.json", "w") as file:
            json.dump(
                obj={ "last": 0 if self.__place >= len(self.__profiles) else self.__place },
                fp=file
            )
        place = self.__place
        self.__place += 1
        if place >= len(self.__profiles):
            raise StopIteration
        return self.__profiles[place]
