from flask import Blueprint
from control.SeriesController import consultarSeries

series_routes = Blueprint('series_routes', __name__)

series_routes.route('/series', methods=['GET', 'POST'])(consultarSeries)
