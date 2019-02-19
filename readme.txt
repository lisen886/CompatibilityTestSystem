使用说明：
1、Lisen'MBP docker启动一个rtmp服务器，：docker run -d -p 1935:1935 --name nginx-rtmp tiangolo/nginx-rtmp
2、运行兼容测试网站脚本CompatibilitySystem.py(记下机器A的IP)
3、各个兼容执行机器上启动client.py脚本
4、http://机器A的IP:8090 进入登录界面，账户密码为：lisen、123456
5、兼容测试界面输入执行机IP，点击开始推流，可以实时查看执行机推流结果(网站需要允许Flash权限)
6、点击兼容测试按钮，可以自行选择浏览器，多选版本进行兼容测试