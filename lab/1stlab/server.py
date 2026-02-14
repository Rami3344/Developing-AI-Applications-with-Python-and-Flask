from flask import Flask,jsonify,make_response,request
app = Flask(__name__)
@app.route("/")
def home():
    msg=jsonify({"message":"Hello World"})
    return msg.message
@app.route("/no_content")
def no_content():
    msg="No content Found"
    return jsonify(msg)
@app.route("/exp")
def index_explicit():
    res = make_response({"message":"Hello, World from exp!"})
    res.status_code = 200
    return res


data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]
@app.route("/data")
def get_data():
    try:
        if data and len(data)>0:
            return {"message":f"Data of length {len(data)} found"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404
@app.route("/name_search")
def name_search():
    fName = request.args.get("q")
    if fName.strip() == "" or fName.isdigit():
        return {"message": "Invalid input parameter"}, 422
    if not fName:
        return jsonify({"error": "Missing query parameter 'q'"}), 400

    for d in data:
        if d["first_name"] == fName:
            return jsonify(d), 200

    return jsonify({"error": "Person not found"}), 404

@app.route("/count")
def count():
    return {"data_count":len(data)}
@app.route("/person/<uuid:id>")
def find_by_uuid(id):
    for person in data:
        if(person["id"]==str(id)):
            return person,200
    return {"message":"person not found"}
@app.route("/person/<uuid:id>",methods=["DELETE"])
def delete_by_uuid(id):
    for person in data:
        if(person["id"]==str(id)):
            data.remove(person)
            return {"message": "person deleted"}
    return {"message": "person not found"},404
@app.route("/person",methods=["POST"])
def add_by_uuid():
    new_person = request.get_json()
    if not new_person:
        return {"message": "Invalid input parameter"}
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500
    return {"message":new_person["id"]}
@app.errorhandler(404)
def api_not_found(error):
    # This function is a custom error handler for 404 Not Found errors
    # It is triggered whenever a 404 error occurs within the Flask application
    return {"message": "API not found"}, 404
@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500
@app.route("/test500")
def test500():
    raise Exception("Forced exception for testing")