#!/usr/bin/env python
# coding: utf-8

import os, urllib.request
import pandas as pd

from operator import itemgetter
from flask import Flask, render_template, request

app = Flask(__name__)
title="Pandasサンプルアプリ"

@app.route('/', methods=['GET'])
def get_top():
    data = "./data/all2.csv"
    if os.path.isfile(data) is False: urllib.request.urlretrieve("http://www.toshiseibi.metro.tokyo.jp/bosai/chousa_6/download/all2.csv", data)
    df= pd.read_csv("./data/all2.csv",encoding="SHIFT-JIS")
    label = list(itemgetter(0,1,4,5,7,8,10,11,13,14)(df.columns.values.tolist()))
    select_list = df.groupby(df.columns.values.tolist()[0]).sum().reset_index()[df.columns.values.tolist()[0]].values.tolist()
    result = df.loc[:,list(itemgetter(0,1,4,5,7,8,10,11,13,14)(df.columns.values.tolist()))].values.tolist()

    return render_template('top.html',title=title, label=label, result=result, select_list=select_list)

@app.route('/', methods=['POST'])
def post_index():
    # ImmutableMultiDict([('search_word', ''), ('order', '建物倒壊危険度順位'), ('sort', 'Desc'), ('action', '')])
    df= pd.read_csv("./data/all2.csv",encoding="SHIFT-JIS")

    label = list(itemgetter(0,1,4,5,7,8,10,11,13,14)(df.columns.values.tolist()))
    select_list = df.groupby(df.columns.values.tolist()[0]).sum().reset_index()[df.columns.values.tolist()[0]].values.tolist()
    print(request.form)
    if request.form["sort"] == "Desc":
        df_result = df[(df[df.columns.values.tolist()[1]].str.contains(request.form["search_word"])) & (df[df.columns.values.tolist()[0]].str.contains(request.form["city"]))].sort_values(by=[request.form["order"]], ascending=False)

    else:
        df_result = df[(df[df.columns.values.tolist()[1]].str.contains(request.form["search_word"])) & (df[df.columns.values.tolist()[0]].str.contains(request.form["city"]))].sort_values(by=[request.form["order"]], ascending=True)

    result = list(itemgetter(0,1,4,5,7,8,10,11,13,14)(df_result.values.tolist()))
    print(result)

    return render_template('top.html',title=title, label=label, result=result, select_list=select_list)
    
@app.errorhandler(404)
def error_handler(error):
    return "Error"

if __name__ == "__main__":
    app.run(debug=True, port=8000)
