from flask import Flask,render_template as rt,session, redirect, url_for, request
from api.gemProducts import gem_products
app = Flask(__name__)

app.secret_key = 'BCQWR#$@@WE@12332423@121'

#Routes Will be here
@app.route('/',methods = ["GET","POST"])
def landing():
    return rt('index.html')


@app.route('/result', methods = ["POST"])
def result():
    query = request.form.get("searchquery")
    gemproductlist = gem_products(query)
    table_headers = ['Title', 'Brand', 'Min Quantity', 'List Price', 'Final Price', 'Image Link', 'Product Link']
    return rt('results.html', searchquery = query, gemproductlist = gemproductlist, table_headers = table_headers)

if __name__ == '__main__':
    app.run(debug=True)