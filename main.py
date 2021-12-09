import requests
import json
url="https://wxzx.cqyti.com/wxProjectNew/Login"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "content-type":"application/json",
    "Referer":"https://servicewechat.com/wxfc560ae5ffd61c28/250/page-frame.html",
    "Accept-Encoding":"gzip, deflate, br"
}
data={
    "xh":"",
    "password":"",
    "userName":"",
    "code":"",
    "avatarUrl":"",
    "loginType":"100"
}
response=requests.post(url=url,headers=header,data=json.dumps(data))
print(response.text)
# file=open("login.json","a+")
# file.write(response.text)
# data=json.load(file)
# for str in data['data']['classTable']:
#     print(str['courseName'])
# print(data['data']['classTable'][0]['courseName'])
