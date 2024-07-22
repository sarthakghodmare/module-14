from flask import Flask, render_template,request,jsonify #basically we create here html page which has 1 submit button 2 input button and 1 dropdown as arithmatc operation,two input submit with the help of post mehod  to py file if avilable it return and show ouptput in html page. page creted in index.html and result capture in result.html

app = Flask(__name__)

@app.route("/", methods=['get','post'])
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_operation():#by using post method we can share data to py file by body/htmlpage and by using get we can share data by url
    if(request.method =='POST'):
        ops=request.form['operation'] #whichever  arithmatic data come from  form/body store in varible ops.
        num1 =int(request.form['num1']) #whicever data comes in text format this is data comes from field or 2 input button
        num2 =int(request.form['num2']) #above 3 data comes from form capture here , whichever comes from client side capture in server side
        if(ops=='add'):
            r=num1+num2
            result='the sum of '+str(num1)+'and'+str(num2)+'is'+str(r) 
        #render the results.html ,this capture in body /client side means shows output in body side
        #we want to call this fun whenever any click on submit button on client side we defined its path in html page /'math'(route) ,whenever any submit in client side response goes to route '/math' then it goes to py function math_operation and try to excute in py .if execute then it show result in client side
        if(ops=='subtract'):
            r=num1-num2
            result='the subtract of '+str(num1)+'and'+str(num2)+'is'+str(r) 
        
        if(ops=='multiply'):
            r=num1*num2
            result='the multiply of '+str(num1)+'and'+str(num2)+'is'+str(r) 
     
        if(ops=='divide'):
            r=num1/num2
            result='the divide of '+str(num1)+'and'+str(num2)+'is'+str(r) 
      
        
        return render_template('results.html',result=result)
        #we want to pass data in py file using other tools(postman) by using post method without using body.postman is  atool to test api
@app.route('/postman_data',methods=['POST'])
def math_operation1():
    if(request.method =='POST'):
        ops=request.json['operation'] #in dict key is operation and num 1 and num2 and value we have to gave in postman software/tool
        num1 =int(request.json['num1']) 
        num2 =int(request.json['num2']) 
        if(ops=='add'):
            r=num1+num2
            result='the sum of '+str(num1)+'and'+str(num2)+'is'+str(r) 
       
        if(ops=='subtract'):
            r=num1-num2
            result='the subtract of '+str(num1)+'and'+str(num2)+'is'+str(r) 
        
        if(ops=='multiply'):
            r=num1*num2
            result='the multiply of '+str(num1)+'and'+str(num2)+'is'+str(r) 
     
        if(ops=='divide'):
            r=num1/num2
            result='the divide of '+str(num1)+'and'+str(num2)+'is'+str(r) 
      
        
        return jsonify(result)#we want to render in json file because tool is not body/form it is postman json means dict form data,
#therfore post method is secular than get becasue in post method data does not seen in get method it seen in url
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0")
