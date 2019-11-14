import sys

# 项目的根路径
BASE_DIR = sys.path[0]

# 阿里云支付的，应用私钥文件
APP_PRIVATE_KEY_FILE = BASE_DIR + "/keys/app_private_key.pem"
# 阿里云支付的，阿里云公钥文件
ALIPAY_PUBLIC_KEY_FILE = BASE_DIR + "/keys/alipay_public_key.pem"

# 七牛的域名
QINIU_URL_DOMAIN = "http://q0w7mhayl.bkt.clouddn.com/"
# fastDFS存储服务器地址
FAST_DFS_TRACKER_URL = "http://192.168.205.148:8888/"

# fdfs配置文件的路径
FDFS_CLIENT_CONFIG_PATH = BASE_DIR + "/project_name/utils/fdfs/client.conf"

# 短信验证码的有效期, 单位：秒
SMS_CODE_EXPIRES = 300