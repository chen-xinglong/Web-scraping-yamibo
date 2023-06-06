# 百合会 小说  橡树之庭 提取
# https://www.yamibo.com
# 只需要修改book_name以及target两项即可
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

def get_content(target):
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', class_="panel-body") #修改
    # 提取所有<p>标签的内容作为段落
    paragraphs = [p.get_text() for p in texts.find_all('p')] #以<p>标签分段
    paragraphs = [p for p in paragraphs if p.strip()] #删除空行
    return paragraphs

if __name__ == '__main__':
    server = 'https://www.yamibo.com'
    ### 修改以下两项即可
    book_name = '橡树之庭.txt'
    target = 'https://www.yamibo.com/novel/265605' #目录页
    ###
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', class_='list-view')# class属性使用‘class_’
    chapters = chapters.find_all('a',class_='margin-r-5')
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))##
            f.write('\n')

# f.write('\n'.join(content)) 是将列表content中的字符串元素连接起来，
# 并用换行符('\n')分隔它们，然后将整个结果写入文件中。
# 这样可以确保每个段落写入文件时都占据一行，并且段落之间通过换行符分隔。
#具体来说，'\n'.join(content)使用换行符('\n')将
# 列表content中的所有字符串元素连接成一个大的字符串。
# 例如，如果content是['段落1', '段落2', '段落3']，
# 那么'\n'.join(content)将返回'段落1\n段落2\n段落3'。
#然后，f.write('\n'.join(content))将连接后的字符串写入文件，每个段落占据一行。


# 参考：https://mp.weixin.qq.com/s/5e2_r0QXUISVp9GdDsqbzg

