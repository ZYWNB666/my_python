import json

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.dnspod.v20210323 import dnspod_client, models

try:
    cred = credential.Credential("AKIDToqpiW9e086sW2TnvuhPxJT5cu8E9rPn", "Vs31kFe1NZjtDPaf3RhtFOL6e2Ldonie")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "dnspod.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = dnspod_client.DnspodClient(cred, "", clientProfile)

except TencentCloudSDKException as err:
    print(err)
Domain_name = input("请输入域名：")
def select_all(Domain_name):
    # 列出域名下所有记录的详细值
    # 实例化一个请求对象,每个接口都会对应一个request对象
    # Domain_name = input("请输入域名：")
    req = models.DescribeRecordListRequest()
    params = {
        "Domain": Domain_name
    }
    req.from_json_string(json.dumps(params))

    # 返回的resp是一个DescribeRecordListResponse的实例，与请求对象对应
    resp_select_all = client.DescribeRecordList(req)
    return resp_select_all

def select_only ():
    # 只查询一条记录的详细内容
    req = models.DescribeRecordRequest()
    params = {
        "Domain": "osip.cc",
        "RecordId": 1652663743
    }
    req.from_json_string(json.dumps(params))
    resp_select_only = client.DescribeRecordList(req)
    return resp_select_only

def insert_dns ():
    # 添加一条域名解析记录
    req = models.CreateRecordRequest()
    params = {
        "Domain": "osip.cc",
        "SubDomain": "test",
        "RecordType": "A",
        "RecordLine": "默认",
        "Value": "8.8.8.8"
    }
    req.from_json_string(json.dumps(params))
    resp_insert_dns = client.DescribeRecordList(req)
    return resp_insert_dns

def delete_dns ():
    req = models.DeleteRecordRequest()
    params = {
        "Domain": "osip.cc",
        "RecordId": 123456
    }
    req.from_json_string(json.dumps(params))
    resp_delete_dns = client.DescribeRecordList(req)
    return resp_delete_dns






# Domain_name = input("请输入域名：")
print("1. 列出域名下所有记录的详细值")
print("2. 只查询一条记录的详细内容")
print("3. 添加一条域名解析记录")
print("4. 删除一条域名解析记录")
option = input("请输入选项中的数字：")
if option == "1":
    resp_select_all = select_all(Domain_name)
    # print(resp_select_all.to_json_string())
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
######################################################################
elif option == "2":
    qianzhui = input("请输入域名前缀：")
    resp_select_all = select_all(Domain_name)
    json_data = resp_select_all.to_json_string()
    parsed_data_list = json.loads(json_data)
    test_records = []
    for record in parsed_data_list.get("RecordList", []):
        # 只存储包含域名前缀test的RecordId值
        if qianzhui in record['Name']:
            test_records.append(record['RecordId'])

    record_id_str = ",".join(map(str, test_records))

    req = models.DescribeRecordRequest()
    params = {
        "Domain": Domain_name,
        "RecordId": record_id_str
    }
    req.from_json_string(json.dumps(params))
    resp_select_only = client.DescribeRecordList(req)
    json_data = resp_select_only.to_json_string()
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

elif option == "3":
    resp_insert_dns = insert_dns()
    print(resp_insert_dns.to_json_string())
elif option == "4":
    resp_delete_dns = delete_dns()
    print(resp_delete_dns.to_json_string())
else:
    print("输入错误，请重新输入")



# print(resp.to_json_string())
# except TencentCloudSDKException as err:
#     print(err)
