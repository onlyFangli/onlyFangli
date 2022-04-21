import os

import yaml


path_2=os.getcwd()


#读yaml文件1,加载请求参数
def load_yaml(filename,apiname):
    path_2= 'F:\\pycharm\\project\\projectTest\\yaml\\'+filename
    # path_2 = '../yaml/' + filename
    with open(path_2,encoding='utf-8') as f:
        datas = yaml.full_load(f)
    data = datas[apiname]
    # print(data)
    # url = 'http://192.168.40.97'+data[1]['url']
    # headers = data[2]['headers']
    # json_data = data[3]['json']
    # method = data[0]['method']
    # ass_code=data[4]['expect']['code']
    # ass_success=data[4]['expect']['success']
    return data

#读yaml文件2,读取中间变量
def read_yaml(key):
    with open('../extract.yml',encoding="utf-8") as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value[key]


#写yaml文件，写入中间变量
def write_yaml(data):
    with open('../extract.yml' ,encoding="utf-8",mode="a") as f:
        value = yaml.dump(data,stream=f,allow_unicode=True)
        return value

#清空yaml文件
def clear_yaml():
    with open('../extract.yml',encoding="utf-8",mode="w") as f:
        f.truncate()
