from flask import Flask
app = Flask(__name__)
#__name__ which links our module to flask object

@app.route("/")
def index():
    return 'Hello Chandanhs19mar1999'

#if __name__ == '__main__' :
    #app.run(port=5000,debug=True)

#git remote add origin https://github.com/Chandanhs19mar1999/Flaskapp.git
#git push -u origin master 