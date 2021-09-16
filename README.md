Meraki-MT-work-with-3-party-Camera

Motivation
Cisco Meraki MV camera and Webex teams cannot be sold in mainland China.The Meraki iot solution cannot be used well in mainland China.
So I replaced the Meraki MV with a camera from a 3-party, which can be sold  in mainland China
At the same time, WeChat and Dingtalk are also integrated together. Used for immediate alerts .They are commonly used instant messaging software in mainland China.

Features
Can be integrated with 3-party camera, and real-time image capture (this time using Hikvision)
You can push alarm information, images, and videos to corporate WeChat and DingTalk 


Technologies & Frameworks Used
Use AWS's API Gateway to monitor webhooks alarms from Meraki Dashboard, and control Yingshi Cloud to capture images and videos through the pre-set Python code on AWS's Lambda.Finally, it is sent to these two instant messaging software through Enterprise wechat api and dingtalk api. (Idea referenced from MV&Webex Teams image alert by yiren wang) 

Cisco Products & Services
  Cisco Meraki Cloud Managed Network
  Cisco Meraki API

Tools & Frameworks
  Meraki API
  Yingshi Cloud API
  AWS API Gateway & Lambda
  Dingtalk & Wechat Webhook API

Python library:
  dingtalk(Already integrated)
  wechat_work_webhook(Already integrated)
  requests(Need to download or use zip file "code-0809-1.zip")

Pre-requisites
-This application needs to be hosted AWS's lambda or somewhere where is has access to the internet. 
-You need a Meraki Network and a Meraki API Key (that you get from the Meraki Dashboard).
-You need a Yingshi Cloud account and get 3-party camera's Serial & token,And connect the  camera to Yingshi Cloud.(this time using Hikvision)
-You need a Enterprise WeChat & Dingtalk Account and get webook address


Installation:

The first step:
download the entire "Meraki-MT-work-with-3-party-Camera" code 

The second step:
Replace Key  in lambda_function.py: 

-Replace Yingshi Cloud的Serial & token to your own:
  "accessToken"
  "deviceSerial"
  
-Replace Enterprise WeChat webook address to your own:
  "wechat_work_webhook.connect"

-Replace Dingtalk token to your own:
  "access_token"

Next thing
download Python's requests library or use zip file "code-0809-1.zip"
Compressed together with "dingtalk.py", "lambda_function.py", "wechat_work_webhook.py" and upload to lambda 


Finally
To apply for an AWS account, you can use the service for free for one year,
Configure the api gateway to be associated with Lambda to listen to the alarm information uploaded from the Meraki dashboard. 
Fill in your AWS api gateway address into the Meraki dashboard alert webhook. 


Authors & Maintainers 
Yanchen Pan 
yancpan@cisco.com

License
This project is licensed to you under the terms of the Cisco Sample Code License.




