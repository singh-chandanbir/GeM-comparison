from flask import Flask,render_template as rt,session, redirect, url_for, request
from api.category import getCategory
app = Flask(__name__)

app.secret_key = 'BCQWR#$@@WE@12332423@121'

#Routes Will be here
@app.route('/',methods = ["GET","POST"])
def landing():
    if request.method == "POST":
        session["query"] = request.form.get("searchquery")
        return redirect(url_for('result'))
    return rt('landing.html')


@app.route('/result')
def result():
    (category,subcategory) = getCategory(session["query"])
    return rt('results.html', searchquery = session["query"], category = category, subcategory = subcategory)
if __name__ == '__main__':
    app.run(debug=True)