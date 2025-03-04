from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# ROUTES
@app.route('/')
def homepage():
    return render_template("index.html")


# AJAX FUNCTIONS
if __name__ == '__main__':
   app.run(debug = True, port=5001)