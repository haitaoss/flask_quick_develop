# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from .CCPRestSDK import REST
import random

# �����λ������֤��
six_code = "%06d" % random.randint(0, 999999)

# ���ʺ�
accountSid = '8a216da86e011fa3016e4fe587fe2be9'

# ���ʺ�Token
accountToken = '7ad3f01719c445a0a32184a6afb4b47a'

# Ӧ��Id
appId = '8a216da86e011fa3016e4fe5885f2bf0'

# �����ַ����ʽ���£�����Ҫдhttp://
serverIP = 'app.cloopen.com'

# ����˿�
serverPort = '8883'

# REST�汾��
softVersion = '2013-12-26'


# ����ģ�����
# @param to �ֻ�����
# @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
# @param $tempId ģ��Id

class CCP(object):
    """���Ͷ�����֤�룬����ģʽ"""

    def __new__(cls):
        # �ж���û��������instance
        if not hasattr(cls, "instance"):
            # ���û�У��򴴽������Ķ��󣬲����浽������instance��
            obj = super(CCP, cls).__new__(cls)

            # ��ʼ��REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            # ���������
            cls.instance = obj

        # ����У���ֱ�ӷ��ض���
        return cls.instance

    # sendTemplateSMS(�ֻ�����,��������,ģ��Id)
    def send_template_sms(self, to, datas, temp_id=1):

        # ������ͨѶ�Ĺ���rest���Ͷ���
        result = self.rest.sendTemplateSMS(to, datas, temp_id)  # �ֻ�����,��������[��֤��,ʱ��],ģ��Id

        status_code = result.get("statusCode")
        if status_code == "000000":
            # ��ʾ���ͳɹ�
            return 0
        else:
            # ����ʧ��
            return -1


if __name__ == '__main__':
    pass
    # ccp = CCP()
    # ret = ytx.send_template_sms('18389356431', ['1234', "5"], 1)
    # ret = ccp.send_template_sms('18389356431', ['1234', "5"], 1)
    # print(ret)
