import json
import os

class Database:

    @staticmethod
    def load_data(filename):

        if not os.path.exists(filename):
            return []
        
        try:
            with open(filename ,'r') as file:
                return json.load(file)
            
        except:
            return [] 

    @staticmethod
    def savedata(filename,data):  

        with open(filename , 'w') as file:
            json.dump(data , file , indent=4)     
        