from flask import Flask,render_template
app = Flask(__name__)
#__name__ which links our module to flask object

@app.route("/")
def index():
    return  render_template('about.html')

#if __name__ == '__main__' :
    #app.run()

#git remote add origin https://github.com/Chandanhs19mar1999/Flaskapp.git
#git push -u origin master 