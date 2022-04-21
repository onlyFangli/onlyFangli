import hashlib
import datetime
import json

from data import selenium_logs
timestamp_header=round(datetime.datetime.now().timestamp()*1000)
# govtoken = selenium_logs.get_token()

'''---------------拼接sign md5加密前---------------'''
# def sign_join_before(json,params,method,timeStamp,govtoken):
#     if method =='post':
#         if json == {}:
#             sign_join =str(timeStamp) + govtoken
#         else:
#             sign_join_before = json.dumps(json, separators=(',', ':'))+str(timeStamp) + govtoken
#     elif method == 'get':
#         sign_join_before = json.dumps(json, separators=(',', ':')) + str(timeStamp) + govtoken
#     else:
#         print('暂时不支持该种接口请求！！')
#     return sign_join_before


def sign_join_before(json_data,params,timeStamp,govtoken):
    # print(type(json_data))
    if json_data == None:
        sign_join_bef =str(timeStamp) + govtoken
    else:
        sign_join_bef = json.dumps(json_data, separators=(',', ':'))+str(timeStamp) + govtoken
    # print(sign_join_bef)
    return sign_join_bef

'''-----------md5:生成sign----------------'''
def sign_md5(value):
    hl = hashlib.md5()
    hl.update(value.encode(encoding='utf-8'))
    sign = hl.hexdigest()
    return sign

