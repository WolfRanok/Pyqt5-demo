import json

"""
百度用来充当服务器，用于爬虫
"""


def handler(event, context):
    # event 参数类型为 dict，event 中包含了触发函数执行的基本信息，可以是平台定义的格式，也可以自定义格式。函数被触发开始执行后，可以在代码内部对 event 进行处理。
    # context 为 SCF 平台提供的入参，将 context 入参传递给执行方法，代码可通过解析 context 入参对象，获取到运行环境及当前请求的相关信息。
    # 封装为特定的数据给百度云一个出口
    # 在客户端所提交的文本会以字符串的格式写入
    json_params = json.loads(event["body"])  # 从这里提取到用户的表单

    user_name = json_params["user_name"]

    password = json_params["password"]

    val = {"error": "用户名或密码错误"}

    if user_name == "ranok" and password == "ranok666":
        val = {"return": "登录成功"}

    # 发送的格式不会发生改变
    # 但是浏览器只会显示body的内容,py爬虫则是全部返回
    res = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": val
    }

    return res


'''
以下为一个完整的被接接收到的请求参数，其中event的内容如下
{
         'resource': '/ranok',
         'path': '/ranok',
         'httpMethod': 'POST',
         'headers': {
             'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'close',
             'Content-Length': '46',
             'Content-Type': 'application/json', 'User-Agent': 'python-requests/2.28.1',
             'X-Bce-Request-Id': '092ba9bd-7236-45c1-ae7e-ac515d772f1f'
         },
         'queryStringParameters': {},
         'pathParameters': {},
         'requestContext': {
             'stage': 'cfc', 'requestId': '092ba9bd-7236-45c1-ae7e-ac515d772f1f',
             'resourcePath': '/ranok',
             'httpMethod': 'POST', 'apiId': '1hew6hzryk65t', 'sourceIp': '219.140.59.35'
         },
         'body': '{"user_name": "ranok", "password": "ranok666"}', ## 这里是上传上去的信息
          'isBase64Encoded': False
}
'''
