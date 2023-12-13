from flask import Flask,render_template as rt 
app = Flask(__name__)



#Routes Will be here
@app.route('/')
def landing():
    return rt('landing.html')

if __name__ == '__main__':
    app.run(debug=True)