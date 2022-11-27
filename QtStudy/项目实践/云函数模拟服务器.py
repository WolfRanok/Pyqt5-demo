import json

"""
百度用来充当服务器，用于爬虫
"""


# -*- coding: utf-8 -*-

def handler(event, context):
    # event 参数类型为 dict，event 中包含了触发函数执行的基本信息，可以是平台定义的格式，也可以自定义格式。函数被触发开始执行后，可以在代码内部对 event 进行处理。
    # context 为 SCF 平台提供的入参，将 context 入参传递给执行方法，代码可通过解析 context 入参对象，获取到运行环境及当前请求的相关信息。
    # 封装为特定的数据给百度云一个出口
    json_params = event.get("body")

    user_name = json_params.get("user_name")

    password = json_params.get("password")

    print("用户名：",user_name)
    print("密码：",password)
    val = {"error":"用户名或密码错误"}

    if user_name == "ranok" and password == "ranok666":
        val = {"return":"登录成功"}

    res = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"X-Custom-Header": "headerValue"},
        "body": json.dumps(val)
    }

    return res
