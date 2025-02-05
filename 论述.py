import re
from lxml import etree
import html as HTML


def add_space(match):
    return '\n' + match.group()


lunshu = []
def analys(page,nowpage):
    for i in range(1,26):
        print(f"当前为第{i}页")
        data=""
        with open(f'{page}\\{page}{i}.txt',encoding='gbk',mode='r') as f:
            data=f.read()
        f.close()
        html = etree.parse(f'{page}\\{page}{i}.txt', etree.HTMLParser())
        # 使用XPath获取元素
        # result_select = html.xpath('/html/body/div/div/div[3]/div[1]/div')[0]
        # result_lunshu = html.xpath('/html/body/div/div/div[3]/div[2]/div')[0]
        # /html/body/div/div/div[3]/div[5]/div/div[2]/div[1]
        result_lunshu = html.xpath('/html/body/div/div/div[3]/div[5]/div')[0]
        # result_wenda = html.xpath('/html/body/div/div/div[3]/div[4]/div')[0]
        # itemWrapper
        for j in range(2,100):
            try:
                now_result = result_lunshu.xpath(f'.//div[{j}]')[0]
                # /html/body/div/div/div[3]/div[5]/div/div[2]/div[2]/div[2]/div[5]
                #print(HTML.unescape(etree.tostring(now_result).decode('gbk')))
                now_data_timu = now_result.xpath(".//*[@id[substring(., string-length(.) - string-length('content') + 1) = 'content']]")[j - 2]
                print(HTML.unescape(etree.tostring(now_data_timu).decode('gbk')))
                # now_data_anser = now_result.xpath(f'./div[2]/div')[0]
                # /html/body/div/div/div[3]/div[3]/div/div[2]/div[2]/div[2]/div[5]
                now_data_anser = now_result.xpath('./div[2]/div[2]/div[5]')[0]
                # /html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[5]
                # /html/body/div/div/div[3]/div[2]/div/div[3]/div[2]/div[2]/div[5]
                now_data_timu = etree.tostring(now_data_timu).decode('gbk')
                now_data_anser = etree.tostring(now_data_anser).decode('gbk')
                now_data_timu=HTML.unescape(now_data_timu).replace('\n', '').replace(" ", '')
                now_data_timu = re.sub(r'<input.*?value',"",now_data_timu)
                now_data_anser=HTML.unescape(now_data_anser).replace("\n", '').replace(" ", '')
                print(now_data_timu)
                if now_data_timu in lunshu:
                    print(lunshu)
                    continue
                else:
                    lunshu.append(now_data_timu)
                with open(f'{nowpage}论述.txt', mode='a+', encoding='gbk') as f:
                    f.write(f"第{len(lunshu)}题")
                    f.write(now_data_timu)
                    f.write(now_data_anser)
                f.close()
            except:
                break
    # 打开并读取txt文件
    with open(f'{nowpage}论述.txt', 'r') as f:
        content = f.read()
    f.close()
    # 删除所有空格和换行符
    content = content.replace(' ', '').replace('\n', '').replace('</div>','').replace('<div>','').replace('</span><span>（答案）','（答案）').replace('<span>','\n').replace('</span>','').replace('"/><divclass="itemWrapper">','')
    content = re.sub(r'<inputtype="hidden".*?value="','\n',content)
    # 使用正则表达式替换字符串
    content = re.sub(r'第.*?题', add_space, content)
    content = content.replace('"/><divclass="rightAnswer_body">'," ")
    content = content.replace('="', "\n")
    # 写入文件
    with open(f'{nowpage}论述.txt', 'w') as f:
        f.write(content)
    f.close()

if __name__ == '__main__':
    analys('First','第一章')