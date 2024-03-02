''' 
Author: Deralive
Data: 2/17/2024
Description: I'm Very Vegetable.
Tips:
在While循环中定义 i = -1 的原因: 在浏览器中选中对象, 右击 -> 复制 -> 复制Selector
内容为 "span:nth-child(奇数)" 时, 是文本"第n张"
内容为 "img:nth-child(偶数)"时, 是图片的src地址
本网页是child(奇数)+child(偶数)作为一个元组, 但每一话的张数不同.
因为在读取完所有图片及文本后, 还有一条span:nth-child 不是我们想要的内容
故使用try / except语句, 调换i+1先执行, 可以省去多加一个条件判断的麻烦.
'''

#读取元素前置
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

#文件命名、Base64编码处理前置
import os
import base64

#在桌面创建空文件夹
path = 'C:\\Users\\26421\\Desktop'
if not os.path.exists(os.path.join(path, 'ImagesOutput')):
    os.makedirs(os.path.join(path, 'ImagesOutput'))

#初始化模块
url = 'https://www.didamh.com/chapter/9972-1-2.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}

#切入li列表，获取章节名并建立文件夹
RoomText = requests.get(url=url,headers=headers).text
Soup = BeautifulSoup(RoomText,'lxml')
li_list = Soup.select('div.playlist.mod.clearfix[style*="display:block"] > ul > li')
#注意事项：playlist mod clearfix 分为 display:block 与 display:none，后者不能用，有部分章节乱码


'''
以上，前置工作准备完毕
以下，开始爬取漫画图片
'''


#根据li列表，进入每一话的页面，为爬取图片做准备。
for li in li_list:
    
    #进入当前话页面
    RoomUrl = 'https://www.didamh.com/' + li.a['href']
    Edge = webdriver.Edge()
    Edge.get(RoomUrl)
    
    #创建当前话的文件夹
    RoomTitle = li.a.string
    path = 'C:\\Users\\26421\\Desktop\\ImagesOutput'
    if not os.path.exists(os.path.join(path, RoomTitle)): #使用os.path.join(path, Name) 连接指定路径
        os.makedirs(os.path.join(path, RoomTitle))
        print("成功创建本话文件夹。")

    #CSS定位iframe，并进入
    Location = Edge.find_element(By.CSS_SELECTOR, value= "#playleft > iframe") #目标iframe里没有ID，无法直接定位，需要从上层定位爬取，进入Location = iframe
    Edge.switch_to.frame(Location) #新版本Selenium中，find_element_by_class_name("value")有所修改
    
    i = -1
    while True:
        #载入图片信息
        i = i+2
        try: #寻找是否存在span:nth-child(偶数)的元素
            Page_Name = Edge.find_element(By.CSS_SELECTOR, value = "body > span:nth-child(" + str(i+1) + ") > em.em2"  ).get_attribute("textContent")
            
            #若有，继续执行以下代码：
            Img_Url = Edge.find_element(By.CSS_SELECTOR, value =  "body > img:nth-child(" + str(i) + ")"  ).get_attribute("src")
            print(Page_Name, "\t", Img_Url, "\t", "Downloading")
            
            # 指定保存路径
            Save_Path = "C:\\Users\\26421\\Desktop\ImagesOutput\\" + str(RoomTitle)

            #判断是否以Base64的方式编码，并解码
            if Img_Url.startswith("data:image"):
                base64_str = Img_Url.split("base64,")[1]
                ImageData = base64.b64decode(base64_str)
                
            else:      # 获取图片二进制数据，并进行文件写入
                ImageData = requests.get(url=Img_Url, headers=headers).content
                
            File_Path = os.path.join(Save_Path, str(Page_Name) + '.jpg')
            with open(File_Path, 'wb') as f:
                f.write(ImageData)
                print(str(RoomTitle) + " " + str(Page_Name) + " 下载成功！")
                
        except NoSuchElementException:
            print("本话图片已下载完毕")
            #退出本网页的iframe界面，准备进入下一话读取
            Edge.switch_to.default_content()
            break


#程序运行结束
print("下载已结束！请检查是否下载正确无误。")
Edge.quit()