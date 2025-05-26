# -*- coding: utf-8 -*-
"""本益比.ipynb """

from requests import get as rqstGET
from pandas import read_csv, to_numeric
from io import StringIO
from datetime import datetime, timedelta

今日=datetime.today().date()
前週=今日-timedelta(days=7)
#日期=前週.date#()
datestr=str(前週).replace('-', '')
URL=f'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date={datestr}&selectType=ALL'
回應=rqstGET(URL)
資框=read_csv(StringIO(回應.text), header=1)
#資框=資框.iloc[1:]
#print(資框.columns)

print(資框.columns)
資框['本益比'] = to_numeric(資框['本益比'], errors='coerce')

資框.nlargest(10, ['本益比'])[['證券代號', '證券名稱', '本益比']]
import pandas_profiling
資框.profile_report()

from google.colab import drive
drive.mount('/content/drive')

!pip install --upgrade pandas_profiling
