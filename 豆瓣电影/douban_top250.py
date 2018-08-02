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
    with open('douban_top250.txt', 'a', encoding='utf-8') as f:
        f.write("No."+item[0]+"   "+item[1] + '\n')
        f.write(item[2].strip() + '\n')
        f.write("评分："+item[3].strip() + '\n\n')

def parse_one_page(html):
    pattern = re.compile('<div class="item">.*?<em.*?>(.*?)</em>.*?title.*?>(.*?)</span>.*?bd.*?"">(.*?)</p>.*?average">(.*?)</span>.*?</li>', re.S)   
    items = re.findall(pattern, html)
    for item in items:
        item_tmp = (list)(item)
        print("No."+item_tmp[0]+"   "+item_tmp[1])
        item_tmp[2] = item_tmp[2].replace("&nbsp"," ")
        item_tmp[2] = item_tmp[2].replace(";"," ")
        item_tmp[2] = item_tmp[2].replace("<br>"," ")
        print(item_tmp[2].strip())
        print("评分："+item_tmp[3].strip())
        write_to_file(item_tmp)

def write_time():
    f = open("douban_top250.txt", "w",encoding='utf-8' )
    f.write("豆瓣电影Top250榜单\n")
    f.write('更新时间：'+time.strftime('%Y-%m-%d %H:%M:%S')+'\n\n')
    f.close()
        
def main(offset):
    url = 'https://movie.douban.com/top250?start='+str(offset)+'&filter='
    html = get_one_page(url)
    #print(html)
    parse_one_page(html)

if __name__=="__main__":
    write_time()
    for i in range(10):
        main(25*i)
        time.sleep(1)
        
