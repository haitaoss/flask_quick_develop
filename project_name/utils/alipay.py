from alipay import AliPay
from project_name import constants


class My_Alipay(object):
    """阿里云支付的类"""

    # 初始化            应用id   私钥文件的二进制数据     公钥文件的二进制数据
    def __init__(self, appid, private_key_data=None, public_key_data=None, app_notify_url=None, sign_type="RSA2",
                 debug=False):
        if not private_key_data:
            private_key_data = open(constants.APP_PRIVATE_KEY_FILE).read()
        if not public_key_data:
            public_key_data = open(constants.ALIPAY_PUBLIC_KEY_FILE).read()
        self.alipay = AliPay(
            appid=appid,  # 应用id
            app_notify_url=app_notify_url,  # 默认回调url
            # 绑定应用公钥对应的私钥信息
            app_private_key_string=private_key_data,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=public_key_data,
            sign_type=sign_type,  # RSA 或者 RSA2
            debug=debug,  # 默认False是访问真实的地址。True就是访问沙箱的地址
        )
        self.api_alipay_trade_page_pay_url = "https://openapi.alipay.com/gateway.do?"
        self.api_alipaydev_trade_page_pay_url = "https://openapi.alipaydev.com/gateway.do?"

    # 拉去支付宝的交易界面                  交易订单流水号   交易金额（必须是字符串）        主体   是否获取沙箱的支付地址
    def api_alipay_trade_page_pay(self, out_trade_no, total_amount, subject, dev=False, return_url=None,
                                  notify_url=None):
        order_string = self.alipay.api_alipay_trade_page_pay(
            out_trade_no=out_trade_no,  # 订单id
            total_amount=total_amount,  # 支付总金额,因为我们的是Decimal类型无法被json序列化，所以变成字符串
            subject=subject,
            return_url=return_url,
            notify_url=notify_url  # 可选, 不填则使用默认notify url,支付宝服务器主动通知商户服务器里指定的页面
        )
        # 返回支付宝交易的url地址
        if dev:
            return self.api_alipaydev_trade_page_pay_url + order_string

        return self.api_alipay_trade_page_pay_url + order_string

    # 根据流水号，查询用户是否支付成功
    def api_alipay_trade_query(self, out_trade_no):

        response = self.alipay.api_alipay_trade_query(out_trade_no)
        code = response.get('code')
        if code == '10000' and response.get('trade_status') == 'TRADE_SUCCESS':
            return True
        else:
            # 支付出错
            return False
