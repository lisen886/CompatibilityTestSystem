# -*- coding: utf-8 -*-
from flask import Flask,request
from browserCompatibility import runCom
import subprocess
app = Flask(__name__)


#  http://localhost:1122/?platform=mac&browser=chrome&action=test&pushChannelName=lisenwindows7&browserVersion=(10,11,12)
@app.route('/',methods=['GET','POST'])
def doGet():
    platform = request.args['platform']
    action = request.args['action']
    browser = request.args['browser']
    pushChannelName = request.args['pushChannelName']
    browserVersion = request.args['browserVersion']
    try:
        if platform == "windows":
            if action == "runWindowsLiveStream":
                sub = subprocess.Popen("ffmpeg -f gdigrab -framerate 30 -offset_x 0 -offset_y 0 -video_size 1920x1080 -i desktop -f flv rtmp://10.80.0.221/live/"+pushChannelName,shell=True,stdout=subprocess.PIPE,close_fds=True)
                sub.wait()
            elif action == "runCompatibility":
                jsonStr =""
                if browser == "chrome":
                    jsonStr = "{\"winchrome\" :" + browserVersion + "}"
                elif browser == "firefox":
                    jsonStr = "{\"winfirefox\":" + browserVersion + "}"
                runCom(jsonStr)
            elif action == "stopWindowsLiveStream":
                sub = subprocess.Popen("taskkill /f /im ffmpeg.exe",shell=True, stdout=subprocess.PIPE,close_fds=True)
                sub.wait()
        elif platform == "mac":
            if action == "runMacLiveStream":
                sub = subprocess.Popen("ffmpeg -f avfoundation -pixel_format uyvy422 -i '1' -f flv rtmp://10.80.0.221/live/"+pushChannelName,shell=True,stdout=subprocess.PIPE,close_fds=True)
                sub.wait()
            elif action == "runCompatibility":
                jsonStr = ""
                if browser == "chrome":
                    jsonStr = "{\"macchrome\" :" + browserVersion + "}"
                elif browser == "firefox":
                    jsonStr = "{\"macfirefox\":" + browserVersion + "}"
                runCom(jsonStr)
            elif action == "stopMacLiveStream":
                sub = subprocess.Popen("ps -ef | grep ffmpeg | grep -v grep | awk '{print $2}' | xargs kill -9", shell=True, stdout=subprocess.PIPE,close_fds=True)
                sub.wait()
        return "pass"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1122,debug=True)



