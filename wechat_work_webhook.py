import json
import wechat_work_webhook
import requests
import time
import dingtalk

def lambda_handler(event, context):

    wechat = wechat_work_webhook.connect("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxxxxx")#您的（企业）微信机器人地址
    access_token = 'xxxxxx'#您的（企业）钉钉机器人token
    dt = dingtalk.DingTalk(access_token)

    url='https://open.ys7.com/api/lapp/device/capture'
    data = {"POST" : "/api/lapp/token/get HTTP/1.1","Host":"open.ys7.com","Content-Type": "application/x-www-form-urlencoded","accessToken":"!!!填您的萤石云token!!!","deviceSerial":"G05678073","channelNo":"1"}#您的萤石云token
    response = requests.request('POST', url, data=data)

    localtime = time.asctime( time.localtime(time.time()) )
    picturedict = json.loads(response.text.encode('utf8'))
    picturelist=picturedict['data']
    videoURL='https://open.ys7.com/view/h5/您的萤石云直播地址' #您的萤石云直播地址

    dic1=event['alertData']#整理收meraki平台到的告警数据
    dic2=dic1['triggerData']
    dic3=dic2[0]['trigger']
    dic4=dic3['type']

    ifdoor='door'
    ifwater_detection='water_detection'
    iftemperature='temperature'
    if (ifdoor==dic4):
        dt.send_link(text=localtime,title='侦测到开门告警视频',picture_url=picturelist['picUrl'],message_url=videoURL)
        dt.send_link(text=localtime,title='侦测到开门告警图片',picture_url=picturelist['picUrl'],message_url=picturelist['picUrl'])
        wechat.news([{"title" : "侦测到开门告警视频","description" : localtime,"url" : videoURL,"picurl" : picturelist['picUrl']}])
        wechat.news([{"title" : "侦测到开门告警图片","description" : localtime,"url" : picturelist['picUrl'],"picurl" : picturelist['picUrl']}])
#    	wechat.text('侦测到开门')
    else:
    	if(ifwater_detection==dic4):
    	    dt.send_link(text=localtime,title='侦测到漏水告警视频',picture_url=picturelist['picUrl'],message_url=videoURL)
    	    dt.send_link(text=localtime,title='侦测到漏水告警图片',picture_url=picturelist['picUrl'],message_url=picturelist['picUrl'])
    	    wechat.news([{"title" : "侦测到漏水告警视频","description" : localtime,"url" : videoURL,"picurl" : picturelist['picUrl']}])
    	    wechat.news([{"title" : "侦测到漏水告警图片","description" : localtime,"url" : picturelist['picUrl'],"picurl" : picturelist['picUrl']}])
#    		wechat.text('侦测到漏水')
    	else:
    		if(iftemperature==dic4):
    		    dt.send_link(text=localtime,title='侦测到高温告警视频',picture_url=picturelist['picUrl'],message_url=videoURL)
    		    dt.send_link(text=localtime,title='侦测到高温告警图片',picture_url=picturelist['picUrl'],message_url=picturelist['picUrl'])
    		    wechat.news([{"title" : "侦测到高温告警视频","description" : localtime,"url" : videoURL,"picurl" : picturelist['picUrl']}])
    		    wechat.news([{"title" : "侦测到高温告警图片","description" : localtime,"url" : picturelist['picUrl'],"picurl" : picturelist['picUrl']}])
#    			wechat.text('侦测到高温')
