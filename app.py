# BEGIN CODE HERE
from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT
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


@app.route("/add-product", methods=["POST","GET"])
def add_product():
    # BEGIN CODE HERE
    new={}
    name=request.args.get("name")
    year=int(request.args.get("production_year"))
    price=int(request.args.get("price"))
    color=int(request.args.get("color"))
    size=int(request.args.get("size"))
    

    #elegxos eisodou
    flag=True

    if (color>3 or color<1) or(size<1 or size>4):
        return "mistakes were made"

    

    old=mongo.db.products.find_one({"$text":{"$search": f"\"{name}\""} })
    
    



    if old is None:
        new["name"]=name
        new["production_year"]=year
        new["price"]=price
        new["color"]=color
        new["size"]=size

        mongo.db.products.insert_one(new)
    elif old is not None:
       mongo.db.products.update_one({"name":name},{"$set":{"price":size,"production_year":year,"color":color,"size":size}})
        
    return old["name"]
   
    # END CODE HERE


@app.route("/content-based-filtering", methods=["POST"])
def content_based_filtering():
    # BEGIN CODE HERE
    return ""
    # END CODE HERE


@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE
    return ""
    # END CODE HERE
