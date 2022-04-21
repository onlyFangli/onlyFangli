import openpyxl
import selenium


from web_keys import keys

def new_data(value):
    data={}
    if values[2] is not None:
    #表格内参数字符串内容的切割：先切割分号，区分多组不同参数
        str_temp = value.split(';')
        #再切割等号，区分多组参数名与值的k-v对
        for temp in str_temp:
            temp = temp.split('=',1)
            data[temp[0]] = temp[1]
    else:
        data = None
    return data


excel  = openpyxl.load_workbook('新建 XLSX 工作表.xlsx')
for name in excel.sheetnames:
    sheet =excel[name]
    print('*****************{}*******************'.format(name))
    for values in sheet.values:
        #用例正文有编号，基于编号来判断是否读取到用例正文
        if type(values[0]) is int:
            print('正在执行操作步骤{}:{}'.format(values[1],values[3]))
            if values[2] != None:
                data=new_data(values[2])
                print(data)

            # data['name']= values[2]
            # data['value'] = values[3]
            # data['txt']  = values[4]
            # for k in list(data.keys()):
            #     if data[k] is None:
            #         del data[k]

            #管理操作行为，将参数传入：
            #1.实例化key对象
            if values[1]== 'open_browser':
                key =keys.Key(**data)

            #3.将断言结果写入excel中
            elif 'assert' in values[1]:
                status = getattr(key,values[1])(**data)
                if status:
                    print('excel写入')
                else:
                    print('写入断言失败')
            # 2.基于key对象执行的操作行为
            else:
                if data is not None:
                    getattr(key,values[1])(**data)
                else:
                    getattr(key,values[1])()




