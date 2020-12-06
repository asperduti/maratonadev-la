"""
Welcome to the Python submission app.

The purpose of this app is to request an IAM token from IBM Cloud and finally send it to a validation end point,
together with your e-mail used in Maratona and your WML scoring endpoint URL.
The app has some bugs in it and will not function properly without some modifications.
Feel free to edit any parts of the app, except the while loop at the end, which is needed for the app to not stop running.
Good luck! 

The Maratona Behind the Code Organization
"""

import json
import logging
import os

import requests

from token_request import token_request
from submit import submit
# Use info logging to see the logs in OpenShift console
logging.getLogger().setLevel(logging.INFO)

if __name__ == '__main__':
    logging.info('App starting')
    token = token_request()
    submit(token)

    logging.info('OK')

    # WARNING: Do not remove the code below this line. The application must keep running after completing its job.
    while 1:
        pass
