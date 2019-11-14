from . import api_order


@api_order.route("/")
def index():
    return "order"
