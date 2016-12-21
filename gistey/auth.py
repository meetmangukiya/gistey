import requests
import datetime
import time
import getpass
from functools import partial

end = "https://api.github.com/"


def authorize(func):
    """
    Authorize application

    :param func:
        function to decorate for required authorization.
    """

    username = input('Enter GitHub Username: ')
    password = getpass.getpass()
    return partial(func, auth=(username, password))


@authorize
def create_token(end, auth):
    """
    Get the Personal access token or create one if not exists already.

    :param end:
        End point of the API.
    :param auth:
        A tuple consisting of username and password
    """

    params = {
        "scope": ["gist"],
        "note": "gistey"
    }

    rq = requests.post(end + "authorizations/", params=params, auth=auth)

    if "X-GitHub-OTP" in rq.headers:
        otp = input("Enter 2FA code: ")
        rq = requests.put(end + "authorizations/", params=params, auth=auth,
                          headers={"X-GitHub-OTP": otp})

        return rq
    # TODO Returns 404 =/ Confusing
