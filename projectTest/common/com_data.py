# /usr/local/bin/python
# encoding:utf-8

import time
import random


# 公共配置信息
config = {
    "ip": "127.0.0.1",
}

# tenant_info = {
#     "tenantid": "0a80a23a-70f0-46f4-8d2a-75d781f07d7a",
#     "orderid": "1ab4b295-cadc-4827-88f2-bd21db24b008",
#     "productid": "58fd4d48-cbe5-430c-8cca-8b5b39469bd5",
#     "communityid": "76efffde-1720-4e5d-934a-44803170cc7b",
#     "regionid": "f8d8957c-73a0-48c2-a95f-2b81d84a6a7f",
#     "regionid_china": "babb5342-6ade-4158-b070-baf1d18dae1c",
# }

# 平台登录用信息
platform_info_dict = {
    "host": "http://192.168.40.97",
    "username": "testapi",
    "password": "7df28a7b548bdf41cd26a656df96f835",
}

# mysql数据库相关信息,暂不使用
# mysql_info_dict = {
#     "host": "192.168.10.248",
#     "port": 3306,
#     "user": "root",
#     "password": "zjly@2015",
#     "database": "test_gbase",
#     "charset": "utf8"}

# 服务器redis相关信息
service_redis_info_dict = {
    "host-port": [{"192.168.10.248": 7001}, {"192.168.10.248": 7002}, {"192.168.10.248": 7003}, {"192.168.10.248": 7004}, {"192.168.10.248": 7005}, {"192.168.10.248": 7006}],
    "db": "0"}


def random_name():
    ''''随机生成一个姓名'''
    first_name_list = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王',
                       '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许']
    boy = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
    name = '中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝'
    first_name = random.choice(first_name_list)
    second_name = name[random.randint(1, len(name) - 1)]
    third_name = boy[random.randint(1, len(boy) - 1)]
    final_name = first_name + second_name + third_name
    return final_name


def random_community_name():
    '''随机生成一个场景名称'''
    first_name_l = '对酒当歌人生几何'
    second_name_l = '譬如朝露去日苦多'
    third_name_l = '月明星稀乌鹊南飞'
    forth_name_l = '何以解忧唯有杜康'
    first_name = first_name_l[random.randint(1, len(first_name_l) - 1)]
    second_name = second_name_l[random.randint(1, len(second_name_l) - 1)]
    third_name = third_name_l[random.randint(1, len(third_name_l) - 1)]
    forth_name = third_name_l[random.randint(1, len(forth_name_l) - 1)]
    final_name = first_name + second_name + third_name + forth_name
    return final_name


def random_phonenum():
    '''随机生成手机号码'''
    phone_num = "1" + \
        random.choice(["3", "5", "7", "8", "9"]) + \
        str(random.randint(100000000, 999999999))
    return phone_num


def random_plate_num():
    '''随机生成车牌号'''
    char0 = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
    char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    plate_num = char0[random.randint(1, len(char0) - 1)] + char1[random.randint(
        1, len(char1) - 1)] + str(random.randint(10000, 99999))
    return plate_num

def get_value_from_list(keys, li):
    '''从字典列表中找到对应key的值,返回字典形式，方便提取'''
    result = {}
    for i in li:
        for key in keys:
            if key in i.keys():
                result[key] = i[key]
    return result


# if __name__ == "__main__":
#     l = random_plate_num()
#     print(l)
