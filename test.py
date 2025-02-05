import re
from lxml import etree
import html as HTML


def check(page):
    d=""
    for i in range(1, 25):
        print(f"当前为第{i}页")
        data = ""
        with open(f'{page}\\{page}{i}.txt', encoding='gbk', mode='r') as f:
            data = f.read()
        f.close()
    d=d+data
    return d

def chuli(page):
        data = ""
        with open(f'题目.txt', encoding='gbk', mode='r') as f:
            data = f.read()
        f.close()
        html = etree.parse(f'题目.txt', etree.HTMLParser())
        # 使用XPath获取元素
        result_select = html.xpath('/html/body/div/div/div[3]/div[1]/div')[0]
        #   /html/body/div/div/div[3]/div[1]/div/div[3]/div[2]/div[4]
        #   /html/body/div/div/div[3]/div[1]/div/div[2]/div[2]/div[2]/div
        # /html/body/div/div/div[3]/div[1]/div
        # result_panduan = html.xpath('/html/body/div/div/div[3]/div[2]/div')[0]
        # result_tiankong = html.xpath('/html/body/div/div/div[3]/div[3]/div')[0]
        # result_wenda = html.xpath('/html/body/div/div/div[3]/div[4]/div')[0]
        # itemWrapper
        for j in range(2, 206):
            try:
                now_result = result_select.xpath(f'.//div[{j}]')[0]
                now_data_timu = \
                now_result.xpath("//*[@id[substring(., string-length(.) - string-length('content') + 1) = 'content']]")[
                    j - 2]
                # now_data_anser = now_result.xpath(f'./div[2]/div')[0]
                now_data_anser = now_result.xpath('//*[@class="itemWrapper"]')[j - 2]
                now_data_timu = etree.tostring(now_data_timu).decode('gbk')
                now_data_anser = etree.tostring(now_data_anser).decode('gbk')
                now_data_timu = HTML.unescape(now_data_timu).replace('（我的答案）', '').replace('\n', '').replace(" ",
                                                                                                                 '')
                now_data_anser = HTML.unescape(now_data_anser).replace('（我的答案）', '').replace("\n", '').replace(" ", '')

                if now_data_anser in select:
                    continue
                else:
                    select.append(now_data_anser)
                print(select.__len__())
                with open(f'{nowpage}选择.txt', mode='a+', encoding='gbk') as f:
                    f.write(f"第{len(select)}题")
                    f.write(now_data_timu)
                    f.write(now_data_anser)
                f.close()
            except:
                break
    # 打开并读取txt文件
    with open(f'{nowpage}选择.txt', 'r') as f:
        content = f.read()
    f.close()
    # 删除所有空格和换行符
    content = content.replace('&nbsp;', '').replace(' ', '').replace('\n', '').replace('</div>', '').replace('<div>',
                                                                                                             '').replace(
        '</span><span>（答案）', '（答案）').replace('<span>', '\n').replace('</span>', '').replace(
        '"/><divclass="itemWrapper">', '')
    content = re.sub(r'<inputtype="hidden".*?value="', '\n', content)
    content = content.replace('\n\n','\n')
    # 使用正则表达式替换字符串
    content = re.sub(r'第.*?题', add_space, content)
    # 写入文件
    print(content)
    with open(f'{nowpage}选择.txt', 'w') as f:
        f.write(content)
    f.close()

if __name__ == '__main__':
    data=""

    data=data+check('First')+check('Second')+check('Th')+check('For')
    with open(f'选择.txt', mode='a+', encoding='gbk') as f:
        f.write(data)
    f.close()