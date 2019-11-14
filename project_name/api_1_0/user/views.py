from . import api_user


@api_user.route("/")
def index():
    return "user"
