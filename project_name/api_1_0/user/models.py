from project_name import db
from project_name.api_1_0 import BaseModel


class User(BaseModel, db.Model):
    """用户"""

    __tablename__ = "ih_user_profile"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    name = db.Column(db.String(32), unique=True, nullable=False)  # 用户名称
    password = db.Column(db.String(128), nullable=False)  # 密码
