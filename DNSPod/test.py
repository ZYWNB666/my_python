import json

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.dnspod.v20210323 import dnspod_client, models

cred = credential.Credential("AKIDToqpiW9e086sW2TnvuhPxJT5cu8E9rPn", "Vs31kFe1NZjtDPaf3RhtFOL6e2Ldonie")
httpProfile = HttpProfile()
httpProfile.endpoint = "dnspod.tencentcloudapi.com"
clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile
client = dnspod_client.DnspodClient(cred, "", clientProfile)

# 变量
Domain_name = input("请输入域名：")


def select_all(Domain_name):
    if not Domain_name:
        Domain_name = "osip.cc"
    req = models.DescribeRecordListRequest()
    params = {
        "Domain": Domain_name
    }
    req.from_json_string(json.dumps(params))

    # 返回的resp是一个DescribeRecordListResponse的实例，与请求对象对应
    resp_select_all = client.DescribeRecordList(req)
    json_data = resp_select_all.to_json_string()
    parsed_data_list = json.loads(json_data)
    field_mapping = {
        "Name": "域名前缀",
        "RecordId": "记录ID",
        "Value": "记录值",
        "MX": "MX优先级",
        "TTL": "生存时间",
        "Status": "状态",
        "Weight": "权重",
        "Remark": "备注",
        "Line": "线路",
        "Type": "记录类型",
        "UpdatedOn": "更新时间",
        "RecordId": "域名ID",
        "DomainName": "域名",
    }
    print("-----------------------------")
    for record in parsed_data_list.get("RecordList", []):
        # 逐个提取字段值并输出
        print("域名：" + Domain_name)
        for field_name, description in field_mapping.items():
            field_value = record.get(field_name)
            if field_value is not None:
                print(f"{description}: {field_value}")
        print("------------------------------------")

Domain_names = input("请输入域名：")
qianzhui = input("请输入你要添加的子域名前缀：")
jiluleixing = input("请输入记录类型 A记录/CNAME记录/txt记录：")
jiluzhi = input("请输入记录值：")
def insert_one(Domain_names, qianzhui, jiluleixing, jiluzhi):
    if not Domain_names:
        exit("您没有输入域名")
    if not qianzhui:
        exit("您没有输入子域名前缀")
    if not jiluleixing:
        exit("您没有输入记录类型")
    if not jiluzhi:
        exit("您没有输入记录值")
    req = models.CreateRecordRequest()
    params = {
        "Domain": Domain_names,
        "SubDomain": qianzhui,
        "RecordType": jiluleixing,
        "RecordLine": "默认",
        "Value": jiluzhi
    }
    req.from_json_string(json.dumps(params))

if __name__ == '__main__':
    select_all(Domain_name)
    #insert_one(Domain_name, qianzhui, jiluleixing, jiluzhi)