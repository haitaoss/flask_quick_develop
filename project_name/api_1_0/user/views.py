from . import api_user
from flask import request, jsonify, current_app, make_response
from project_name.utils.commons import RET
# from project_name.utils.fdfs.fdfs_image_storage import upload_image
from project_name.utils.qiniu.qiniu_image_storage import upload_image
from project_name.utils.captcha.captcha import captcha
from project_name import constants


@api_user.route("/")
def index():
    return "user"


@api_user.route("/avatar", methods=["POST"])
def upload_avatar():
    """保存图片"""
    # 提取参数
    req_data = request.files.get("image")
    # 校验参数
    if not req_data:
        return jsonify(errno=RET.PARAMERR, errmsg="请选择图片文件")

    # 保存图片
    file_data = req_data.read()
    try:
        filename = upload_image(file_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="上传图片失败")

    # image_url = constants.FAST_DFS_TRACKER_URL+filename
    image_url = constants.QINIU_URL_DOMAIN + filename
    # 响应
    return jsonify(errno=RET.OK, errmsg="上传成功", data={"image_url": image_url})


# GET 127.0.0.1/api/v1.0/user/image_codes/
@api_user.route("/image_codes/")
def get_image_code():
    """
    获取图片验证码
    """
    # 生成验证码图片
    name, text, image_data = captcha.generate_captcha()  # 名字，真实文本，图片数据
    resp = make_response(image_data)
    resp.headers['Content-Type'] = 'image/jpg'
    return resp
