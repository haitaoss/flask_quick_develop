from . import api_user
from flask import request, jsonify, current_app, make_response
from project_name.utils.commons import RET
# from project_name.utils.fdfs.fdfs_image_storage import upload_image
from project_name.utils.qiniu.qiniu_image_storage import upload_image
from project_name.utils.captcha.captcha import captcha
from project_name import constants
from project_name.libs.yuntongxun.sms import CCP
import random


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


@api_user.route('/sms_codes/<re(r"1[345678]\d{9}"):mobile>')
def get_sms_code(mobile):
    """获取短信验证"""

    # 手机号不存在，则生成短信验证码
    sms_code = "%06d" % random.randint(0, 999999)  # 最少是6位数，不够补0
    ccp = CCP()
    try:
        #                     要发送的手机号     发送的验证码      几分钟               使用云通讯的那个模板
        ccp.send_template_sms(mobile, [sms_code, int(constants.SMS_CODE_EXPIRES / 60)], 1)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR,errmsg="第三方错误")

    return jsonify(errno=RET.OK, errmsg="发送成功")
