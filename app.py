
from flask import Flask,render_template
app = Flask(__name__,static_folder='static',static_url_path='')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/post')
def post():
    return render_template('post.html')
if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)

