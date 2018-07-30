#!/usr/bin/env python
# coding: utf-8
import traceback, json, datetime
import urllib.request

from flask import Flask, render_template, request

app = Flask(__name__)
title="Compassサンプルアプリ"

@app.route('/')
def get_index():
    return render_template('top.html',title=title, result={})

@app.route('/', methods=['POST'])
def post_index():
    # リクエストURLの組み立て
    url = "https://connpass.com/api/v1/event/?"
    search_type = "keyword"

    ## キーワードの組み立て(AND/ORも)
    keyword_list = request.form["keyword"].split(",")
    if len(keyword_list) != 0:
        if request.form["search"] == "or":
            search_type = "keyword_or"
        for i in range(len(keyword_list)):
            if keyword_list[i] != "":
                if i == 0:
                    url += search_type + "=" + keyword_list[i]
                else:
                    url += "&" + search_type + "=" + keyword_list[i]

    ## 検索結果の表示順
    url += "&order=" + request.form["view"]
    
    ## 表示件数
    if request.form["number"] != "":
        url += "&count=" + request.form["number"]

    # Jsonのパース
    data = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))["events"]
    e_id = 1
    result_dict = {}
    for dd in data:
        result_dict[e_id] = [dd["title"], dd["event_url"], dd["catch"] ,dd["address"], dd["hash_tag"] ,dd["started_at"][:16].replace("T", " "), dd["ended_at"][:16].replace("T", " ")]
        e_id += 1
        
    return render_template('top.html',title=title, result=result_dict)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
