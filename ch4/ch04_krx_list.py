import pandas as pd

krx_list = pd.read_html('C:/Users/kdd07/Downloads/상장법인목록.xls')
krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format)

df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13')[0]
df.종목코드 = df.종목코드.map('{:06d}'.format)
df = df.sort_values(by='종목코드')
