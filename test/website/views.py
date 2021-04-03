from flask import Blueprint, render_template, request, jsonify, make_response

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    return render_template("index.html")

@views.route('/getEntry', methods=['GET','POST'])
def getEntry():
    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message": "JSON recieved"}),200)
    return res

