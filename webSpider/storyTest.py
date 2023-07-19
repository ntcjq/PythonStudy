from bs4 import BeautifulSoup
import requests



###
if __name__ == "__main__":
     target = 'http://www.biqukan.com/1_1094/5403177.html'
     req = requests.get(url = target)
     html = req.text
     bf = BeautifulSoup(html,features="html.parser")
     #爬取正文
     texts = bf.find_all('div', class_ = 'showtxt')
     #去除符号
     print(texts[0].text.replace('\xa0'*8,'\n\n'))
###


if __name__ == "__main__":
     server = 'http://www.biqukan.com/'
     target = 'http://www.biqukan.com/1_1094/'
     req = requests.get(url = target)
     req.encoding = 'gb2312'
     html = req.text
     div_bf = BeautifulSoup(html,features="html.parser")
     div = div_bf.find_all('div', class_ = 'listmain')
     #print(div[0])
     a_bf = BeautifulSoup(str(div[0]))
     a = a_bf.find_all('a')
     for each in a:
          print(each.string, server + each.get('href'))