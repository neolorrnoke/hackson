import json
import wechat_work_webhook
import requests
import time
import dingtalk

def lambda_handler(event, context):

    url='https://open.ys7.com/api/lapp/device/capture'
    data = {"POST" : "/api/lapp/token/get HTTP/1.1","Host":"open.ys7.com","Content-Type": "application/x-www-form-urlencoded","accessToken":"at.e11nangrdmtrflqu7tmr5jbmd2nw58rq-7avvfym9ff-1h66jmc-epvrs98yv","deviceSerial":"G05678073","channelNo":"1"}
    response = requests.request('POST', url, data=data)

    wechat = wechat_work_webhook.connect("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=e8fd8250-8d6f-4ce3-81d7-ef359e3ca712")
    access_token = 'e08b125f4f4b455a04c8d2b69e34c95e08baca469a9f504e10810301d43ab5e5'
    dt = dingtalk.DingTalk(access_token)

    localtime = time.asctime( time.localtime(time.time()) )
    picturedict = json.loads(response.text.encode('utf8'))
    picturelist = picturedict['data']
    videoURL = 'https://open.ys7.com/view/h5/9cc702d11236401ba594eefed6e7b8d8'

    wechat.news([{"title" : "告警视频","description" : localtime,"url" : videoURL,"picurl" : picturelist['picUrl']}])
    wechat.news([{"title" : "告警图片","description" : localtime,"url" : picturelist['picUrl'],"picurl" : picturelist['picUrl']}])
    dt.send_link(text=localtime,title='告警视频',picture_url=picturelist['picUrl'],message_url=videoURL)
    dt.send_link(text=localtime,title='告警图片',picture_url=picturelist['picUrl'],message_url=picturelist['picUrl'])
    
#    dic4=event['alertData']['triggerData'][0]['trigger']['type']

    dic1=event['alertData']
    dic2=dic1['triggerData']
    dic3=dic2[0]['trigger']
    dic4=dic3['type']

    ifdoor='door'
    ifwater_detection='water_detection'
    iftemperature='temperature'
    if (ifdoor==dic4):
        wechat.text('侦测到开门')
    else:
    	if(ifwater_detection==dic4):
    		wechat.text('侦测到漏水')
    	else:
    		if(iftemperature==dic4):
    		    wechat.text('侦测到高温')


