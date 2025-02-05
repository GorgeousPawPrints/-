import time

from selenium.webdriver.common.by import By


def login(driver):
    driver.get("https://course.qqhru.edu.cn/meol/index.do")
    # loginbtn
    login_button = driver.find_element(By.ID, "loginbtn")
    login_button.click()
    # 找到用户名和密码输入框
    username = driver.find_element(By.ID, "userName")
    password = driver.find_element(By.ID, "passWord")
    # 输入用户名和密码
    username.send_keys("2021023014")
    password.send_keys("qd_123456")
    # 找到登录按钮并点击
    login_button = driver.find_element(By.CLASS_NAME, "submit")
    login_button.click()

def openPage(driver,url):
    driver.get(url)
    findLearn = driver.find_element(By.XPATH,'//*[@id="tmenu"]/li[5]/a/span')
    time.sleep(2)
    # //*[@id="tmenu"]/li[5]/a/span
    findLearn.click()
    # //*[@id="menu"]/ul[2]/li[4]/a/span
    time.sleep(2)
    findLearn = driver.find_element(By.XPATH, '//*[@id="menu"]/ul[2]/li[4]/a/span')
    # //*[@id="tmenu"]/li[5]/a/span
    findLearn.click()

def checkTest(driver,num,name):
    # 点进查看试卷
    driver.switch_to.frame("mainFrame")

    # /html/body/div/table/tbody/tr[5]/td[8]/a/img
    # /html/body/div/table/tbody/tr[4]/td[8]/a/img
    # /html/body/div/table/tbody/tr[3]/td[8]/a/img
    # /html/body/div/table/tbody/tr[2]/td[8]/a/img
    ans = driver.find_element(By.XPATH,f'/html/body/div/table/tbody/tr[{num}]/td[8]/a/img')
    ans.click()
    # driver.switch_to.default_content()
    # 切换到新的标签页或窗口
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    for j in range(1,25):
        # /html/body/div/table/tbody/tr[2]/td[5]/a
        ans =driver.find_element(By.XPATH,f'/html/body/div/table/tbody/tr[{j+1}]/td[5]/a')
        ans.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        pageData=driver.page_source
        with open(f'{name}\\{name}{j}.txt',encoding='gbk',mode='a+') as f:
            f.write(pageData)
        f.close()
        driver.close()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    print("First is finish!")
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    openPage(driver,"https://course.qqhru.edu.cn/meol/jpk/course/layout/newpage/index.jsp?courseId=60865")
    driver.switch_to.window(driver.window_handles[-1])
def openFirst(driver,num):
    # 进入课程答题页面
    # //*[@id="startbox252468701"]
    # findLearn = driver.find_element(By.XPATH,'//*[@id="699530"]/span')
    # findLearn.click()
    # findLearn = driver.find_element(By.XPATH,'//*[@id="700718"]/span')
    # findLearn.click()

    # 自动答题提交
    for i in range(1,25):
        if i!=1:
            time.sleep(62)
        driver.switch_to.frame("mainFrame")
        # driver.switch_to.frame("main-content-two")
        # //*[@id="startbox252468701"]
        start = driver.find_elements(By.XPATH,'//*[starts-with(@id, "startbox")]')
        start = start[num]
        start.click()
        time.sleep(2)
        # 进入确定层
        # 获取所有的iframe
        try:
            iframes = driver.find_elements(By.TAG_NAME,"iframe")

            # 遍历所有的iframe
            for iframe in iframes:
                driver.switch_to.frame(iframe)
            start_ready=driver.find_element(By.XPATH,'//*[@id="sureButton"]')
            start_ready.click()
            driver.switch_to.parent_frame()
        except:
            driver.switch_to.default_content()
            driver.switch_to.frame("mainFrame")
            driver.switch_to.frame("main-content-two")
        time.sleep(2)
        iframe_info = driver.execute_script(
            "return window.frameElement ? window.frameElement.outerHTML : 'you are in the main context';"
        )
        print(iframe_info)
        # 进入答题区
        submit = driver.find_element(By.XPATH,'/html/body/div/div[4]/div/input')
        submit.click()
        time.sleep(2)
        alert = driver.switch_to.alert  # 切换到警告弹框
        print(alert.text)  # 打印警告信息
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert  # 切换到警告弹框
        print(alert.text)  # 打印警告信息
        alert.accept()
        time.sleep(2)

        driver.switch_to.default_content()

    #
    # # 点进查看试卷
    # driver.switch_to.frame("mainFrame")
    # driver.switch_to.frame("main-content-two")
    # ans = driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[8]/td/a/img')
    # ans.click()
    # # driver.switch_to.default_content()
    # # 切换到新的标签页或窗口
    # driver.switch_to.window(driver.window_handles[-1])
    # time.sleep(2)
    # for j in range(1,101):
    #     # /html/body/div/table/tbody/tr[2]/td[5]/a
    #     ans =driver.find_element(By.XPATH,f'/html/body/div/table/tbody/tr[{j+1}]/td[5]/a')
    #     ans.click()
    #     time.sleep(2)
    #     driver.switch_to.window(driver.window_handles[-1])
    #     pageData=driver.page_source
    #     with open(f'First\\First{j}.txt',encoding='gbk',mode='a+') as f:
    #         f.write(pageData)
    #     f.close()
    #     driver.close()
    #     time.sleep(2)
    #     driver.switch_to.window(driver.window_handles[-1])
    # driver.close()
    # print("First is finish!")
    # time.sleep(3)
    # driver.switch_to.window(driver.window_handles[-1])
    # openPage(driver)
    # driver.switch_to.window(driver.window_handles[-1])

def openSecond(driver):
    # 进入课程答题页面
    findLearn = driver.find_element(By.XPATH,'//*[@id="699531"]/span')
    findLearn.click()
    findLearn = driver.find_element(By.XPATH,'//*[@id="700719"]/span')
    findLearn.click()

    # 自动答题提交
    for i in range(1,101):
        driver.execute_script("window.scrollTo(0, 0);")
        if i != 1:
            time.sleep(62)
        driver.switch_to.frame("mainFrame")
        driver.switch_to.frame("main-content-two")
        start = driver.find_elements(By.XPATH,'//*[starts-with(@id, "startbox")]')
        start = start[-1]
        start.click()
        time.sleep(2)
        # 进入确定层
        # 获取所有的iframe
        try:
            iframes = driver.find_elements(By.TAG_NAME,"iframe")

            # 遍历所有的iframe
            for iframe in iframes:
                driver.switch_to.frame(iframe)
            start_ready=driver.find_element(By.XPATH,'//*[@id="sureButton"]')
            start_ready.click()
            driver.switch_to.parent_frame()
        except:
            driver.switch_to.default_content()
            driver.switch_to.frame("mainFrame")
            driver.switch_to.frame("main-content-two")
        time.sleep(2)
        iframe_info = driver.execute_script(
            "return window.frameElement ? window.frameElement.outerHTML : 'you are in the main context';"
        )
        print(iframe_info)
        try:
            # 进入答题区/html/body/div/div[4]/div/input
            submit = driver.find_element(By.XPATH,'/html/body/div/div[4]/div/input')

            submit.click()
            time.sleep(2)
        except:
            pageData=driver.page_source
            with open(f'Second.txt',encoding='gbk',mode='w') as f:
                f.write(pageData)
            f.close()
            submit = driver.find_element(By.NAME,"Submit3")
            driver.execute_script("arguments[0].click();", submit)
            time.sleep(2)

        alert = driver.switch_to.alert  # 切换到警告弹框
        print(alert.text)  # 打印警告信息
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert  # 切换到警告弹框
        print(alert.text)  # 打印警告信息
        alert.accept()
        time.sleep(2)
        driver.switch_to.default_content()


    # 点进查看试卷
    driver.switch_to.frame("mainFrame")
    driver.switch_to.frame("main-content-two")
    ans = driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[8]/td/a/img')
    ans.click()
    # driver.switch_to.default_content()
    # 切换到新的标签页或窗口
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    for j in range(1,101):
        # /html/body/div/table/tbody/tr[2]/td[5]/a
        ans =driver.find_element(By.XPATH,f'/html/body/div/table/tbody/tr[{j+1}]/td[5]/a')
        ans.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        pageData=driver.page_source
        with open(f'Second\\Second{j}.txt',encoding='gbk',mode='a+') as f:
            f.write(pageData)
        f.close()
        driver.close()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    print("Second is finish!")
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    openPage(driver)
    driver.switch_to.window(driver.window_handles[-1])

def openTh(driver):
    # 进入课程答题页面
    # //*[@id="700721"]/span
    findLearn = driver.find_element(By.XPATH,'//*[@id="699532"]/span')
    findLearn.click()
    submit = driver.find_element(By.XPATH,'//*[@id="700721"]/span')
    driver.execute_script("arguments[0].click();", submit)
    # 自动答题提交
    for i in range(1,2):
        driver.switch_to.window(driver.window_handles[-1])
        if i!=1:
            time.sleep(62)
        driver.switch_to.frame("mainFrame")
        driver.switch_to.frame("main-content-two")
        time.sleep(2)
        start = driver.find_elements(By.XPATH,'//*[starts-with(@id, "startbox")]')
        start = start[-1]
        start.click()
        time.sleep(2)
        # 进入确定层
        # 获取所有的iframe
        try:
            iframes = driver.find_elements(By.TAG_NAME,"iframe")

            # 遍历所有的iframe
            for iframe in iframes:
                driver.switch_to.frame(iframe)
            start_ready=driver.find_element(By.XPATH,'//*[@id="sureButton"]')
            start_ready.click()
            driver.switch_to.parent_frame()
        except:
            driver.switch_to.default_content()
            driver.switch_to.frame("mainFrame")
            driver.switch_to.frame("main-content-two")
        time.sleep(2)
        iframe_info = driver.execute_script(
            "return window.frameElement ? window.frameElement.outerHTML : 'you are in the main context';"
        )
        print(iframe_info)
        # 进入答题区
        driver.execute_script("window.scrollTo(0, 0);")
        try:
            # 进入答题区/html/body/div/div[4]/div/input
            submit = driver.find_element(By.XPATH,'/html/body/div/div[4]/div/input')
            submit.click()
            time.sleep(2)
        except:
            pageData=driver.page_source
            with open(f'Th.txt',encoding='gbk',mode='w') as f:
                f.write(pageData)
            f.close()
            submit = driver.find_element(By.NAME,"Submit3")
            driver.execute_script("arguments[0].click();", submit)
            time.sleep(2)
        alert = driver.switch_to.alert  # 切换到警告弹框
        print(alert.text)  # 打印警告信息
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert  # 切换到警告弹框
        print(alert.text)  # 打印警告信息
        alert.accept()
        time.sleep(2)

        driver.switch_to.default_content()


    # 点进查看试卷
    driver.switch_to.frame("mainFrame")
    driver.switch_to.frame("main-content-two")
    ans = driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[8]/td/a/img')
    ans.click()
    # driver.switch_to.default_content()
    # 切换到新的标签页或窗口
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    for j in range(1,101):
        driver.switch_to.window(driver.window_handles[-1])
        # /html/body/div/table/tbody/tr[2]/td[5]/a
        ans =driver.find_element(By.XPATH,f'/html/body/div/table/tbody/tr[{j+1}]/td[5]/a')
        ans.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        pageData=driver.page_source
        with open(f'Th\\Th{j}.txt',encoding='gbk',mode='a+') as f:
            f.write(pageData)
        f.close()
        driver.close()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    print("Th is finish!")
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    openPage(driver)
    driver.switch_to.window(driver.window_handles[-1])

def openFor(driver):
    # 进入课程答题页面
    # //*[@id="700721"]/span
    findLearn = driver.find_element(By.XPATH,'//*[@id="699533"]/span')
    findLearn.click()
    submit = driver.find_element(By.XPATH,'//*[@id="700723"]/span')
    driver.execute_script("arguments[0].click();", submit)
    # 自动答题提交
    for i in range(1,26):
        driver.switch_to.window(driver.window_handles[-1])
        if i!=1:
            time.sleep(62)
        driver.switch_to.frame("mainFrame")
        driver.switch_to.frame("main-content-two")
        time.sleep(2)
        start = driver.find_elements(By.XPATH,'//*[starts-with(@id, "startbox")]')
        start = start[-1]
        start.click()
        time.sleep(2)
        # 进入确定层
        # 获取所有的iframe
        try:
            iframes = driver.find_elements(By.TAG_NAME,"iframe")

            # 遍历所有的iframe
            for iframe in iframes:
                driver.switch_to.frame(iframe)
            start_ready=driver.find_element(By.XPATH,'//*[@id="sureButton"]')
            start_ready.click()
            driver.switch_to.parent_frame()
        except:
            driver.switch_to.default_content()
            driver.switch_to.frame("mainFrame")
            driver.switch_to.frame("main-content-two")
        time.sleep(2)
        iframe_info = driver.execute_script(
            "return window.frameElement ? window.frameElement.outerHTML : 'you are in the main context';"
        )
        print(iframe_info)
        # 进入答题区
        driver.execute_script("window.scrollTo(0, 0);")
        try:
            # 进入答题区/html/body/div/div[4]/div/input
            submit = driver.find_element(By.XPATH,'/html/body/div/div[4]/div/input')
            submit.click()
            time.sleep(2)
        except:
            pageData=driver.page_source
            with open(f'Th.txt',encoding='gbk',mode='w') as f:
                f.write(pageData)
            f.close()
            submit = driver.find_element(By.NAME,"Submit3")
            driver.execute_script("arguments[0].click();", submit)
            time.sleep(2)
        alert = driver.switch_to.alert  # 切换到警告弹框
        print(alert.text)  # 打印警告信息
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert  # 切换到警告弹框
        print(alert.text)  # 打印警告信息
        alert.accept()
        time.sleep(2)

        driver.switch_to.default_content()


    # 点进查看试卷
    driver.switch_to.frame("mainFrame")
    driver.switch_to.frame("main-content-two")
    ans = driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[8]/td/a/img')
    ans.click()
    # driver.switch_to.default_content()
    # 切换到新的标签页或窗口
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    for j in range(1,26):
        driver.switch_to.window(driver.window_handles[-1])
        # /html/body/div/table/tbody/tr[2]/td[5]/a
        ans =driver.find_element(By.XPATH,f'/html/body/div/table/tbody/tr[{j+1}]/td[5]/a')
        ans.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        pageData=driver.page_source
        with open(f'For\\For{j}.txt',encoding='gbk',mode='a+') as f:
            f.write(pageData)
        f.close()
        driver.close()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    print("Th is finish!")
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    openPage(driver)
    driver.switch_to.window(driver.window_handles[-1])

def openFif(driver):
    # 进入课程答题页面
    # //*[@id="700721"]/span
    findLearn = driver.find_element(By.XPATH,'//*[@id="706898"]/span')
    findLearn.click()
    submit = driver.find_element(By.XPATH,'//*[@id="701090"]/span')
    driver.execute_script("arguments[0].click();", submit)
    # 自动答题提交
    for i in range(1,26):
        driver.switch_to.window(driver.window_handles[-1])
        if i!=1:
            time.sleep(62)
        driver.switch_to.frame("mainFrame")
        driver.switch_to.frame("main-content-two")
        time.sleep(2)
        start = driver.find_elements(By.XPATH,'//*[starts-with(@id, "startbox")]')
        start = start[-1]
        start.click()
        time.sleep(2)
        # 进入确定层
        # 获取所有的iframe
        try:
            iframes = driver.find_elements(By.TAG_NAME,"iframe")

            # 遍历所有的iframe
            for iframe in iframes:
                driver.switch_to.frame(iframe)
            start_ready=driver.find_element(By.XPATH,'//*[@id="sureButton"]')
            start_ready.click()
            driver.switch_to.parent_frame()
        except:
            driver.switch_to.default_content()
            driver.switch_to.frame("mainFrame")
            driver.switch_to.frame("main-content-two")
        time.sleep(2)
        iframe_info = driver.execute_script(
            "return window.frameElement ? window.frameElement.outerHTML : 'you are in the main context';"
        )
        print(iframe_info)
        # 进入答题区
        driver.execute_script("window.scrollTo(0, 0);")
        try:
            # 进入答题区/html/body/div/div[4]/div/input
            submit = driver.find_element(By.XPATH,'/html/body/div/div[4]/div/input')
            submit.click()
            time.sleep(2)
        except:
            pageData=driver.page_source
            with open(f'Th.txt',encoding='gbk',mode='w') as f:
                f.write(pageData)
            f.close()
            submit = driver.find_element(By.NAME,"Submit3")
            driver.execute_script("arguments[0].click();", submit)
            time.sleep(2)
        alert = driver.switch_to.alert  # 切换到警告弹框
        print(alert.text)  # 打印警告信息
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert  # 切换到警告弹框
        print(alert.text)  # 打印警告信息
        alert.accept()
        time.sleep(2)

        driver.switch_to.default_content()


    # 点进查看试卷
    driver.switch_to.frame("mainFrame")
    driver.switch_to.frame("main-content-two")
    ans = driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[8]/td/a/img')
    ans.click()
    # driver.switch_to.default_content()
    # 切换到新的标签页或窗口
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    for j in range(1,26):
        driver.switch_to.window(driver.window_handles[-1])
        # /html/body/div/table/tbody/tr[2]/td[5]/a
        ans =driver.find_element(By.XPATH,f'/html/body/div/table/tbody/tr[{j+1}]/td[5]/a')
        ans.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        pageData=driver.page_source
        with open(f'Fif\\Fif{j}.txt',encoding='gbk',mode='a+') as f:
            f.write(pageData)
        f.close()
        driver.close()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    print("Th is finish!")
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    openPage(driver)
    driver.switch_to.window(driver.window_handles[-1])

