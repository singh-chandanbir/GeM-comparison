from flask import Flask,render_template as rt,session, redirect, url_for, request
from api.gemProducts import gem_products
from api.gemPages import getPages
app = Flask(__name__)

app.secret_key = 'BCQWR#$@@WE@12332423@121'

#Routes Will be here
@app.route('/',methods = ["GET","POST"])
def landing():
    return rt('index.html')

@app.route('/categories', methods = ["POST"])
def result():
    query = request.form.get("searchquery")
    categorylist = getPages(query)
    return rt('category_page.html', searchquery = query, categories = categorylist)

@app.route('/Products', methods = ["POST"])
def showProducts():
    product_link = request.form.get("selected_product")
    print("product link is: ", product_link)
    return rt('products.html')

if __name__ == '__main__':
    app.run(debug=True)