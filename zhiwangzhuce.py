from selenium import webdriver
from model.chaojiying import Chaojiying
from io import BytesIO
from PIL import Image
import time



CHAOJIYING_USERNAME = 'zengxing'
CHAOJIYING_PASSWORD = 'zx520522'
CHAOJIYING_SOFT_ID = '721e4b062ac79ffdc834d35a08b6e591'
CHAOJIYING_KIND = 1004
c_j_y = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)
# 代理IP
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=http://61.135.217.7:80')
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()
url = 'http://my.cnki.net/elibregister/commonRegister.aspx'
driver.get(url)
time.sleep(3)
html = driver.page_source
print(html)
user = driver.find_element_by_id('username')
password = driver.find_element_by_id('txtPassword')
Email = driver.find_element_by_id('txtEmail')
CheckCode = driver.find_element_by_id('txtOldCheckCode')
btnReg = driver.find_element_by_id('ButtonRegister')
user.send_keys('liu0007')
time.sleep(2)
password.send_keys('hui123456')
time.sleep(2)
Email.send_keys('270709083@qq.com')
time.sleep(2)

driver.save_screenshot('./images/zhiwang.png')
img = driver.find_element_by_id('checkcode')
left = img.location['x']#验证码图片左上角横坐标
top = img.location['y']#验证码图片左上角纵坐标
right = left + img.size['width']#验证码图片右下角横坐标
bottom = top + img.size['height']#验证码图片右下角纵坐标
im = Image.open('./images/zhiwang.png')
im_crop = im.crop((left, top, right, bottom))#这个im_crop就是从整个页面截图中再截出来的验证码的图片
im_crop.save('./images/zrecaptchar.png')
bytes_array = BytesIO()
im_crop.save(bytes_array, format='PNG')
result = c_j_y.post_pic(bytes_array.getvalue(), CHAOJIYING_KIND).get('pic_str')
print(result)




CheckCode.send_keys(result)
#模拟点击按钮
btnReg.click()