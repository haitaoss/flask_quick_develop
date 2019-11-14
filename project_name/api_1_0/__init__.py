from project_name import db
from datetime import datetime


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""
    # 因为我们的order模块和user模块都导入了db导致一些问题，加上这个就没问题
    # sqlalchemy.exc.InvalidRequestError: Table 'ih_user_profile' is already defined for this MetaData instance.
    # Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
    __table_args__ = {"useexisting": True}
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间
