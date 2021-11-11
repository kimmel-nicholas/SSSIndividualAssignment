from flask import Flask, render_template           # import flask framework

app = Flask(__name__)             # create an app instance

@app.route("/")                
def homepage():                    
    return render_template('index.html') 

@app.route("/grid")                
def grid():                    
    return render_template("grid.html")  

@app.route("/wizard")                
def wizard():                    
    return render_template("wizard.html")  

if __name__ == "__main__":        # when running python app.py
    app.run(debug=True)           # run the flask app





# @app.route("/<name>")              # route with URL variable /<name>
# def hello_name(name):              # call method hello_name
#     return "Hello " + name         # which returns "hello + name 
