# BEGIN CODE HERE
from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT

import numpy as np


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# END CODE HERE

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pspi"
CORS(app)
mongo = PyMongo(app)


# flask - -app main run - -debugger --> terminal --> Activating a connection via Flask with interactive


mongo.db.products.create_index([("name", TEXT)])


@app.route("/search", methods=["GET"])
def search():
    # BEGIN CODE HERE
    name = request.args.get("name")
    json=mongo.db.products.find({"$text":{"$search": name}}).sort("price",-1)
    
    if json is None:
        json=[]
        return json
    
    
    finale=[]
    
    for j in json:
        finale.append({'name':j['name'],
                       'production_year':j['production_year'],
                       'price':j['price'],
                       'color':j['color'],
                       'size':j['size']  
                       })


        
        
    
    return jsonify(finale)
    
    # END CODE HERE


@app.route("/add-product", methods=["POST"])
def add_product():
    # BEGIN CODE HERE
  
    new=request.json
   # name=new["name"]
    #year=int(new["production_year"])
    #price=int(new["price"])
    #color=int(new["color"])
    #size=int(new["size"])

    #elegxos eisodou
    if (new["color"]>3 or new["color"]<1) or(new["size"]<1 or new['size']>4):
        return "mistakes were made"

    
    name=new["name"]
    old=mongo.db.products.find_one({"$text":{"$search": f"\"{name}\""} })
    

    if old is None:
     #   new["name"]=name
      #  new["production_year"]=year
       # new["price"]=price
       # new["color"]=color
        #new["size"]=size

        mongo.db.products.insert_one(new)
    elif old is not None:
       mongo.db.products.update_one({"name":new["name"]},{"$set":{"price":new["price"],"production_year":new["production_year"],"color":new["color"],"size":new["size"]}})
        
    return "addition is done"
   
    # END CODE HERE


@app.route("/content-based-filtering", methods=["POST"])
def content_based_filtering():
    # BEGIN CODE HERE
     input=request.json

     allMyProducts=mongo.db.products.find()
     inputArray= [input["production_year"],  input['price'],input['color'], input['size']]
     inputArray=np.array(inputArray)#1 by 4 array
                      
   


     theListOfAllMyProducts=[]
     paralerArray=[]


     for j in allMyProducts:
           paralerArray.append(j["name"])
           theListOfAllMyProducts.append([
                       j["production_year"],
                       j['price'],
                       j['color'],
                       j['size']  
                       ]
                       )

     NameArray=np.array(paralerArray)#n by 1
     ProductsArray=np.array(theListOfAllMyProducts) #n by 4


         
     

         


     #max=np.max(ProductsArray[:,0])
     #if (max<inputArray[0]):
         #max=inputArray[0]

     #ProductsArray[:,0] = (ProductsArray[:,0] /max)
     #inputArray[0]/=max 



     above=np.dot(ProductsArray,inputArray.T)





     magnitudeOfA=np.sqrt(np.sum(np.square(ProductsArray),axis=1))
     magnitudeOfB=np.sqrt(np.sum(np.square(inputArray)))
     below=magnitudeOfA*magnitudeOfB


     resultArray=above/below



    
     #resultArray=np.concatenate((resultArray, NameArray), axis=0)
     listOfReturnedNames=[]
     resultArray = np.column_stack((resultArray, NameArray))
     for i in resultArray:
         if float(i[0])>0.70:
             listOfReturnedNames.append(i[1])






     resultArray=list(resultArray)

    



     return listOfReturnedNames
    # END CODE HERE


@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE

     try:
        semester=request.args.get("semester")
        url="https://qa.auth.gr/el/x/studyguide/600000438/current"
        options=Options()
        options.headless=False

        driver = webdriver.Chrome(options=options)

        driver.get(url)
        courses = driver.find_element(By.ID,"exam"+semester)
        result=[]
        for i in courses:
            result.append(i)
        return jsonify(result)

     except Exception as e:
         return "BAD REQUEST", 400
    # END CODE HERE
