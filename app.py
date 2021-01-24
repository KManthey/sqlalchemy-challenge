from flask import Flask, jsonify
import datetime as dt
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import numpy as np
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

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
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>")
        #f"/api/v1.0/<start>/<end><br/>")


@app.route("/api/v1.0/precipitation")
# convert query results to a dictionary using date as the key and prcp as the value
def climate_prcp():
    Lastyear = dt.date(2017, 8, 23)-dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= Lastyear).all()
    dict = {date:precipitation for date, prcp in precipitation}
    # return JSON representation of the dictionary
    return  jsonify(dict)



@app.route("/api/v1.0/stations")
def station():
#     """Return the justice league data as json"""
    station = session.query(Station.station).all()
    resultS = list(np.ravel(station))
    # return JSON list of stations from the dataset
    return jsonify(resultS)  

@app.route("/api/v1.0/tobs")
# query dates and temperature observations for most active station for the last year of data
def climate_tobs():
    Lastyear = dt.date(2017, 8, 23)-dt.timedelta(days=365)
    tobs = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= Lastyear).all()
    resultC = list(np.ravel(tobs))
    # return JSON list of temperature observations (TOBS) for the previous year
    return jsonify(resultC)

# return a JSON list of the minimum tem, avg temp, and max temp for a given start or end date range
#`/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
# when given the start only calculate TMIN, TAVG, TMax for all dates greater than and equal to the start date


# when given the start and the end date calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive
@app.route("/api/v1.0/<start>/<end>")
def calc_temps(start_date, end_date):
    result_temps = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >=start_date).filter(Measurement.date <= end_date).all()
    return jsonify(result_temps)
    #print(calc_temps('2017-02-28', '2017-03-05'))
   

if __name__ == "__main__":
    app.run(debug=True)
