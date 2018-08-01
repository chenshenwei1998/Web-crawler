import requests
import re
import time

def get_one_page(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.text
    return None

def write_to_file(item):
    with open('maoyan_top100.txt', 'a', encoding='utf-8') as f:
        f.write("No."+item[0]+"   "+item[2] + '\n')
        f.write(item[3].strip() + '\n')
        f.write(item[4].strip() + '\n')
        f.write("评分："+item[5]+item[6]+'\n\n')

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        print("No."+item[0]+"   "+item[2])
        print(item[3].strip())
        print(item[4].strip())
        print("评分："+item[5]+item[6]+'\n')
        write_to_file(item)

def write_time():
    f = open("maoyan_top100.txt", "w",encoding='utf-8' )
    f.write("猫眼电影Top100榜单\n")
    f.write('更新时间：'+time.strftime('%Y-%m-%d %H:%M:%S')+'\n\n')
    f.close()
        
def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    #print(html)
    parse_one_page(html)

if __name__=="__main__":
    write_time()
    for i in range(10):
        main(i*10)
        time.sleep(1)
        
