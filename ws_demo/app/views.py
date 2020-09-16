# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render

# Create your views here.
import json
import time


from django.shortcuts import render
from dwebsocket.decorators import accept_websocket


@accept_websocket
def test(request):

    if request.is_websocket():
        print "ws flag"
        print('websocket connection....')
        # msg = request.websocket.wait()  # 接收前端发来的消息
        # print help(request.websocket)
        # msg = request.websocket
        # print(msg, type(msg), json.loads(msg))  # b'["1","2","3"]' <class 'bytes'> ['1', '2', '3']
        i = 0
        while 1:
            msg = request.websocket.wait()  # 接收前端发来的消息
            if msg:
                # 你要返回的结果
                # for i in range(10):
                # request.websocket.send('service message: {}'.format(i).encode())  # 向客户端发送数据
                request.websocket.send(raw_input("Please Enter Informaiton :").encode())
                time.sleep(0.5)  # 每0.5秒发一次
                i += 1
            else:
                request.websocket.close()
    else:  # 如果是普通的请求返回页面
        print "http flag"
        return render(request, 'test.html')