from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time
 
flag = 0
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=option)
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
                         })
 
def autoFillSpace(username, sid, phone, dept):
    browser.get(url)  # 获取问卷星 url
    time.sleep(0.1)
    answers = browser.find_elements(By.CSS_SELECTOR, ".ui-field-contain")
    i = 0
    for answer in answers:
        try:
            i+=1
            browser.execute_script("arguments[0].scrollIntoView();", answer)
            title = answer.find_element(By.CSS_SELECTOR, ".field-label")
            print(title.text)
            ### 有选项
            if ("姓名" in title.text or "名字" in title.text):
                idfind="q%d"%i
                a = browser.find_element(By.ID,idfind)
                a.send_keys(username)
            elif ("院" in title.text):
                idfind="q%d"%i
                a = browser.find_element(By.ID,idfind)
                a.send_keys(dept)
            elif ("学号" in title.text ):
                idfind = "q%d" % i
                browser.find_element(By.ID,idfind).send_keys(sid)
            elif ("手机" in title.text or "电话" in title.text):
                idfind = "q%d" % i
                browser.find_element(By.ID,idfind).send_keys(phone)

        except Exception as e:
            print(e)
 
    # # 提交
    try:
        am = browser.find_element(By.XPATH,"//*[@id='ctlNext']")
        am.click()
    except:
        return 0

    time.sleep(0.1)
    #
    # # 模拟点击智能验证按钮
    # 先点确认
    try:
        browser.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]').click()
        time.sleep(1)
    except:
        pass
    # 再点智能验证提示框，进行智能验证
    try:
        browser.find_element(By.XPATH, '//*[@id="SM_BTN_WRAPPER_1"]').click()
        time.sleep(3)
    except:
        pass
    print("finish!")
    return 1
 
if __name__ == '__main__':
    url = 'https://xxxxxxxx.aspx'  # 问卷星的链接
    username = u'阳光开朗大男孩'  # 您的姓名
    sid = '20000000'  # 学号
    phone = '13311111111'  # 电话号码
    dept = u'某院'  # 所在学院
    cnt = 0
    while True:
        flag = autoFillSpace(username, sid, phone, dept)
        if flag == 1:
            time.sleep(10)
            break
        else:
            cnt += 1
            print(f'时间未到{cnt + 1}')
