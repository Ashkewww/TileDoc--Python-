#this file is going to include all the necessary functions needed for the application
import json
import os



#this function will add an element to the JSON
def checkRecipe(category,sNumber,versionNo):
    flag = False
    with open("categoryPath.json","r") as new:
        data = json.load(new)
        for i in data:
            if i == category:
                flag = True
                break
            else:
                makeDirectory(category)

def makeDirectory(nameOftheDirectory):
    os.mkdir(nameOftheDirectory)
    
def addDictionary(categoryName):
    path = os.path.join(categoryName,categoryName+".json")
    with open(path,"w"):
        dict = {
            "000001":{
                
            }
        }  
               
    




#addRecipe("C0097V1",0,0)
