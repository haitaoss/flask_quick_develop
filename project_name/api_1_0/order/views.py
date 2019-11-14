from . import api_order
from flask import request, jsonify, current_app
from project_name.utils.response_code import RET
from project_name.utils.alipay import My_Alipay
import random

# 订单号，这只是测试，而已
ORDER_ID = None


# http://localhost/api/v1.0/order/pay
@api_order.route("/pay", methods=["POST"])
def pay():
    """
    给用户返回支付宝的链接地址
    参数
    {
        "price":""
    }
    :return:
    """
    req_dict = request.get_json()
    price = req_dict.get("price")

    try:
        price = int(price)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="参数格式不正确")

    # 调用支付宝SDK

    # 创建My_Alipay的实例对象
    appid = "2016101300673201"

    alipay = My_Alipay(appid, debug=True)

    # 获取支付宝交易的url
    global ORDER_ID
    ORDER_ID = "06%d" % random.randint(0, 999999)

    try:
        pay_url = alipay.api_alipay_trade_page_pay(ORDER_ID, price, "测试支付宝交易", dev=True)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="获取支付宝交易地址错误")

    return jsonify(errno=RET.OK, errmsg="OK", data={"pay_url": pay_url})


# http://localhost/api/v1.0/order/check
@api_order.route("/check")
def check_order_status():
    # 创建My_Alipay的实例对象
    appid = "2016101300673201"

    alipay = My_Alipay(appid, debug=True)

    try:
        code = alipay.api_alipay_trade_query(ORDER_ID)
    except Exception as e:
        current_app.logger.error(e)
        # 实际过程，修改订单状态为为支付状态
        return jsonify(errno=RET.THIRDERR, errmsg="支付失败，请重新支付订单")
    if code:
        # 实际过程，修改订单状态为已支付状态
        return jsonify(errno=RET.OK, errmsg="支付成功")
    return jsonify(errno=RET.THIRDERR, errmsg="支付失败")
