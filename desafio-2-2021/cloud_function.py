#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
from math import inf

allowed_values_by_room = {
    'activity-room': {
        'co2': {
            'min': -inf,
            'max': 500
        },
        'temperature': {
            'min': 19,
            'max': 22
        },
        'humidity': {
            'min': 50,
            'max': 60
        },
        'sound': {
            'min': 0,
            'max': 40
        },
        'illumination': {
            'min': 300,
            'max': 750
        },
    },
    'refectory': {
        'co2': {
            'min': -inf,
            'max': 400
        },
        'temperature': {
            'min': 20,
            'max': 23
        },
        'humidity': {
            'min': 50,
            'max': 70
        },
        'sound': {
            'min': 20,
            'max': 35
        },
        'illumination': {
            'min': 200,
            'max': 500
        },
    },
    'room-1': {
        'co2': {
            'min': -inf,
            'max': 300
        },
        'temperature': {
            'min': 21,
            'max': 23
        },
        'humidity': {
            'min': 50,
            'max': 60
        },
        'sound': {
            'min': 10,
            'max': 30
        },
        'illumination': {
            'min': 100,
            'max': 200
        },
    },
    'bathroom-main': {
        'co2': {
            'min': -inf,
            'max': 500
        },
        'temperature': {
            'min': 22,
            'max': 25
        },
        'humidity': {
            'min': 60,
            'max': 75
        },
        'sound': {
            'min': 20,
            'max': 35
        },
        'illumination': {
            'min': 100,
            'max': 200
        },
    },
    'garden': {
        'co2': {
            'min': -inf,
            'max': 500
        },
        'temperature': {
            'min': 15,
            'max': 22
        },
        'humidity': {
            'min': 50,
            'max': 80
        },
        'sound': {
            'min': 10,
            'max': 35
        },
        'illumination': {
            'min': -inf,
            'max': inf
        },
    },
}


def get_alerts_for_room(room, values):
    alerts = []
    for var, value in values.items():
        min_value = allowed_values_by_room[room][var]["min"]
        max_value = allowed_values_by_room[room][var]["max"]
        
        if value < min_value or value > max_value:
            alerts.append(var)
    
    return alerts


def main(dict):
    try:
        alerts = get_alerts_for_room(room=dict["room"], values=dict["values"])
    except:
        alerts = []
    
    return {'alerts': alerts}
