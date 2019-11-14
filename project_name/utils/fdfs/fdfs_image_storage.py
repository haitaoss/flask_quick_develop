from fdfs_client.client import Fdfs_client
from project_name import constants
import sys


def upload_image(image_data):
    """
    上传图片
    :param image_data: 图片的二进制数据
    :return: 返回图片的访问路径
    """

    # 创建Fdfs_client对象

    client = Fdfs_client(constants.FDFS_CLIENT_CONFIG_PATH)
    # 上传文件的流
    res = client.upload_by_buffer(image_data)
    if res.get('Status') != 'Upload successed.':
        # 上传失败
        raise Exception('上传文件到fast dfs失败')
    # 获取返回文件的ID
    filename = res.get("Remote file_id")

    return filename


