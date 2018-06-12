#!/usr/bin/env python
# coding: utf-8
import traceback, re, unicodedata

import urllib.request
import urllib.parse

from bs4 import BeautifulSoup
import MeCab as mecab

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def get_index():
    return render_template('top.html',title="top", result=[])

@app.route('/', methods=['POST'])
def post_index():
    url = request.form['url']
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        contents = soup.find("div", { "class" : "main_text" }).text
        temp_list = mecab.Tagger().parse(unicodedata.normalize("NFKC", "\n".join([x for x in re.sub(r'（.*）', "", contents).replace("　","").replace("\r", "").split("\n") if x]))).split("\n")
        result_dict = {}
        for item in temp_list:
            if 5 < len((str(temp_list.count(item)) + "," + item).replace("\t",",").split(",")):
                result_dict[item.replace("\t",",")] = temp_list.count(item)
       
        result_list = sorted(result_dict.items(), key=lambda x:x[1], reverse=True)
        return render_template('top.html',title="top", result=result_list)

    except Exception as e:
        return render_template('top.html',title="top", result=[])

if __name__ == "__main__":
    app.run(debug=True, port=8000)
