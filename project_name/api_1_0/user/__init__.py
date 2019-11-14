from flask import Blueprint

# 创建蓝图对象
api_user = Blueprint('user', __name__)

from . import views, models
