from flask import Flask, render_template, request, jsonify, make_response
import json
import sys
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3200
HOST = '0.0.0.0'

with open('{}/databases/movies.json'.format("."), 'r') as jsf:
   movies = json.load(jsf)["movies"]

# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>",200)

@app.route("/template", methods=['GET'])
def template():
    return make_response(render_template('index.html', body_text='This is my HTML template for Movie service'),200)

@app.route("/json", methods=['GET'])
def get_json():
    res = make_response(jsonify(movies), 200)
    return res

@app.route("/movies/<movieid>", methods=['GET'])
def get_movie_byid(movieid):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            res = make_response(jsonify(movie),200)
            return res
    return make_response(jsonify({"error":"Movie ID not found"}),400)

@app.route("/moviesbytitle", methods=['GET'])
def get_movie_bytitle():
    json = ""
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie["title"]) == str(req["title"]):
                json = movie

    if not json:
        res = make_response(jsonify({"error":"movie title not found"}),400)
    else:
        res = make_response(jsonify(json),200)
    return res

@app.route("/movies/<movieid>", methods=['DELETE'])
def del_movie(movieid):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movies.remove(movie)
            write(movies)
            return make_response(jsonify(movie),200)

    res = make_response(jsonify({"error":"movie ID not found"}),400)
    return res

@app.route("/movies/rate/<movieid>/<rate>", methods=['PUT'])
def update_movie_rating(movieid, rate):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movie["rating"] = rate
            write(movies)
            return make_response(jsonify(movie),200)

    res = make_response(jsonify({"error":"movie ID not found"}),201)
    return res

@app.route("/addmovie", methods=['POST'])
def add_movie():
    req = request.get_json()
    print(req)
    for movie in movies:
        if str(movie["id"]) == str(req["id"]):
            return make_response(jsonify({"error":"movie ID already exists"}),409)
    movies.append(req)
    write(movies)
    res = make_response(jsonify({"message":"movie added"}),200)
    return res

def write(movies):
    with open('{}/databases/movies.json'.format("."), 'w') as f:
        json.dump(movies, f)

@app.route("/movies/<movieid>/rating", methods=['GET'])
def get_movie_rating(movieid):
    rating = ""
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            rating = movie["rating"]

    if not rating:
        res = make_response(jsonify({"error": "movie id not found"}), 400)
    else:
        res = make_response(jsonify(rating), 200)
    return res

@app.route("/help", methods=['GET'])
def get_help():
    endpoints = {
        "/": "Root - Welcome message.",
        "/json": "GET - Returns the list of all movies in JSON format.",
        "/addmovie/<movieid>": "POST - Add a new movie with a unique movie ID.",
        "/movies/<movieid>": "GET - Get movie details by its ID.",
        "/movies/<movieid>/<rate>": "PUT - Update movie rating.",
        "/moviesbytitle" : "GET - GET - movies by title.",
        "/movies/<movieid>/rating" : "GET - movie rating.",
        "/deletemovie/<movieid>": "DELETE - Delete a movie by its ID.",
        "/help": "GET - List of available endpoints and their usage."

    }
    return make_response(jsonify(endpoints), 200)

if __name__ == "__main__":
    #p = sys.argv[1]
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)
