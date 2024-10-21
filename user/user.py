from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3203
HOST = '0.0.0.0'

with open('{}/databases/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"

@app.route("/user-bookings/<userid>", methods=['GET'])
def bookings(userid):
   res = requests.get("http://127.0.0.1:3201/bookings/{userid}".format(userid=userid)).json()
   return jsonify(res)
@app.route("/movie-details/<userid>", methods=['GET'])
def movie_details(userid):
   user_bookings = requests.get("http://127.0.0.1:3201/bookings/{userid}".format(userid=userid)).json()
   movie_ids = []
   for user_booking in user_bookings:
       for date in  user_booking["dates"]:
          movie_ids += date["movies"]
   return jsonify(get_movie_details(movie_ids))

def get_movie_details(movie_ids):
   movies_with_details = []
   for id in movie_ids:
      movies_with_details.append(requests.get(f"http://127.0.0.1:3200/movies/{id}").json())
   return movies_with_details



if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
