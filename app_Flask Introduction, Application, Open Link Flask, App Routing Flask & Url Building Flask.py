from flask import Flask # bascially import flask flask is pythomic library used to crete or expose api/function.  to outer world.this code written in python but we want this same code/function  accesiable through website.
from flask import request

app = Flask(__name__) #__name__ is tunder. app variabel is a object.

@app.route("/") #decorator
def hello_world():
    return "<h1>Hello, World!</h1>"# h1 is basicaally is   heading html tag
# basic moto to run this programm is to crete client and server architecture. with the help of rest protocol becasue it follows http protocol.server is python programm /code is creted by flask. client is used to access all serves method/programm.app.route provide a route to client see function.
@app.route("/Hello_World1") #it used to binding  url binding
def hello_world1():
    return "<h1>Hello, World1!</h1>"

@app.route("/Hello_World2") #decorator #if we to access only this hello world throgh client ,then simply copy url and paste it another browser and do /:5000 "/hello world," it hit this server function and return hello world2 in client interface.hit using get method
def hello_world2():
    return "<h1>Hello, World2!</h1>" #we want to access this 3 function but not using python.

@app.route("/test") #this is app routing
def test():
    print("this is my function to run app") #print throgh none ,return is not here.

@app.route("/test1")
def test1():
    a=5+6
    return("this is my function to run app {}".format(a)) # we does not want cosole output we want client server based hitting.

#we want to make that functiom who take input. means we does not want url base hitting. we want client should take input and then hit server

@app.route("/test2/test2") #test2 is path. simply server function begg for argument if we gave from client interface then its excute.
def test2():
    data =request.args.get('x')#x is basically is  input. key is used to request server function to give input (x).
    return "this is my function to return app {}".format(data)  #how does sombody came to this functon x then we to defined route

#gives none because none enter the data.  how we give data similar to in search engine we gAVE data as q= data.







if __name__=="__main__":
    app.run(host="0.0.0.0")#ip address.
#this is a development server. this is not run in production grade.to access this programm go to machine  ,use lab url copy and paste in another tab then it show python code outcome ,that we write in html tag,that is hello world.in browser,then client is basically this browser interface hello world,and we can access server, from here interface , and server is python code. basicaalliy client hit the server function that is html tag hello world .we use here rest (http )protocal.
#200 means sucessful and 400 means error.#this made global url it can access using phone also, but if we do/create client server archictecture it does not work, it is done in lab that why.