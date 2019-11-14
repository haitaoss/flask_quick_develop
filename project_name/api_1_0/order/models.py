from project_name import db
from project_name.api_1_0 import BaseModel


class User(BaseModel, db.Model):
    """用户"""

    __tablename__ = "ih_order_info"

    id = db.Column(db.Integer, primary_key=True)  # 订单编号
    comment = db.Column(db.String(32), unique=True, nullable=False)  # 备注
    amount = db.Column(db.Float(2), nullable=False)  # 合计
