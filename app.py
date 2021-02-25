from flask import Flask, jsonify


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate Analysis API<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/climate_analysis/data<br/>")
        # f"/api/v1.0/stations<br/>"
        # f"/api/v1.0/tobs/<br/>"

@app.route("/precipitation")
def climate_analysis():
    """Return the justice league data as json"""

    return "hello"       

@app.route("/stations")
def climate_analysis():
#     """Return the justice league data as json"""

    return "hello again"  

# @app.route("/tobs")
# def climate_analysis():
#     """Return the justice league data as json"""

#     return "hello again again"

# @app.route("/api/v1.0/justice-league/<real_name>")
# def justice_league_character(real_name):
#     """Fetch the Justice League character whose real_name matches
#        the path variable supplied by the user, or a 404 if not."""

#     canonicalized = real_name.replace(" ", "").lower()
#     for character in justice_league_members:
#         search_term = character["real_name"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return jsonify(character)

#     return jsonify({"error": f"Character with real_name {real_name} not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)
