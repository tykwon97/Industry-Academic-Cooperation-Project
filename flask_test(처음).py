# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 15:24:25 2020

@author: yoon2
"""

from flask import Flask

#flask 인스턴스 생성
app = Flask(__name__)

#웹 표현 : route() 메소드 사용
@app.route("/")
#맨 앞에 @가 붙는 것은 장식자를 나타낸다.
#flask에서는 이러한 장식자가 URL연결에 활용된다.
#장식자들 사용하면 다음 행의 함수부터 장식자가 적용된다.

def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run() # 웹앱 실행 요