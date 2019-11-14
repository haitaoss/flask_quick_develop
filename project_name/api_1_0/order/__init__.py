from flask import Blueprint

# 创建蓝图对象
api_order = Blueprint('order', __name__)

from . import views, models
