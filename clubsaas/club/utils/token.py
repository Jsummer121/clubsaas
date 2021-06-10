
def getToken(username):
    """
    根据用户名和时间戳生成用户登陆成功的随机字符串
    :param username: 字符串格式的用户名
    :return: 字符串格式的Token
    """
    import time
    import hashlib
    timestamp = str(time.time()) # 当前时间戳
    m = hashlib.md5(bytes(username, encoding='utf8'))
    m.update(bytes(timestamp, encoding='utf8')) # update必须接收一个bytes
    return m.hexdigest()