import time

from selenium import webdriver
url_baidu = "https:baidu.com"

url_jd = "https://jd.com"

driver = webdriver.Chrome()
# driver.set_window_size(480, 800)
# driver.get(url_baidu)
driver.get(url_jd)

# driver.back()
# driver.forward()
# driver.refresh() #刷新

# 点击的方式
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("wahaha")
# driver.find_element_by_id("su").click()
# 点击的方式

#  表单提交方式

# search_text = driver.find_element_by_id("kw")
# search_text.send_keys("wahaha")
# search_text.submit()

# 表单提交的方式

#切换界面

# search_windows = driver.current_window_handle
# driver.find_element_by_link_text('登录').click()
# time.sleep(2)
# driver.find_element_by_link_text('立即注册').click()
#
# all_handles = driver.window_handles
#
# for handle in all_handles:
#     if handle != search_windows:
#         driver.switch_to.window(handle)
#         print("now register window!")
#         driver.find_element_by_name("userName").send_keys("username")
#         driver.find_element_by_name("password").send_keys("password")
#         time.sleep(2)
# <div class="login-tab login-tab-r">
# <a href="javascript:void(0)" clstag="pageclick|keycount|login_pc_201804112|10">账户登录</a>
# </div>
# time.sleep(1)
# driver.find_element_by_link_text('账户登录').click()
#
#
# time.sleep(1)
# driver.find_element_by_id("loginname").clear()
# driver.find_element_by_id("loginname").send_keys("13192265868")
# time.sleep(5)
# driver.find_element_by_id("nloginpwd").clear()
# driver.find_element_by_id("nloginpwd").send_keys("Lkb@JD2018")
# time.sleep(5)
# driver.find_element_by_id("loginsubmit").click()
# time.sleep(1)
driver.add_cookie("[{'domain': 'passport.jd.com', 'httpOnly': True, 'name': 'alc', 'path': '/', 'secure': False, 'value': 'ORXZKWGwno4aLg9WhB6hOA=='}, {'domain': '.jd.com', 'expiry': 1559282987.301558, 'httpOnly': False, 'name': '__jdu', 'path': '/', 'secure': False, 'value': '1543730974334635704996'}, {'domain': 'passport.jd.com', 'httpOnly': False, 'name': '_t', 'path': '/', 'secure': False, 'value': 'W2e5+M3zjb4fiTYD+Dnx5AW4XFnQVovnF+nIY17udfo='}, {'domain': '.jd.com', 'expiry': 1924905600, 'httpOnly': False, 'name': '3AB9D23F7A4B3C9B', 'path': '/', 'secure': False, 'value': 'JP7V37WDMRDWJQW2D4UH3VCLDPP2ZOZBB22SK3D4D2L5YGLSY557J4AOIVFYLF6JUL467CB7PB3JU6EDOZSVRYWJSA'}, {'domain': '.jd.com', 'expiry': 1559282974, 'httpOnly': False, 'name': '__jda', 'path': '/', 'secure': False, 'value': '122270672.1543730974334635704996.1543730974.1543730974.1543730974.1'}, {'domain': '.jd.com', 'httpOnly': False, 'name': '__jdc', 'path': '/', 'secure': False, 'value': '122270672'}, {'domain': '.jd.com', 'httpOnly': False, 'name': 'wlfstk_smdl', 'path': '/', 'secure': False, 'value': 'd9np2yws9je18pwxfza6nd8ag8ofxvrb'}, {'domain': '.jd.com', 'expiry': 1545026974, 'httpOnly': False, 'name': '__jdv', 'path': '/', 'secure': False, 'value': '122270672|direct|-|none|-|1543730974334'}, {'domain': '.jd.com', 'expiry': 1543732774, 'httpOnly': False, 'name': '__jdb', 'path': '/', 'secure': False, 'value': '122270672.2.1543730974334635704996|1.1543730974'}]")
# print(cookie)

# [{'domain': 'passport.jd.com', 'httpOnly': True, 'name': 'alc', 'path': '/', 'secure': False, 'value': 'ORXZKWGwno4aLg9WhB6hOA=='}, {'domain': '.jd.com', 'expiry': 1559282987.301558, 'httpOnly': False, 'name': '__jdu', 'path': '/', 'secure': False, 'value': '1543730974334635704996'}, {'domain': 'passport.jd.com', 'httpOnly': False, 'name': '_t', 'path': '/', 'secure': False, 'value': 'W2e5+M3zjb4fiTYD+Dnx5AW4XFnQVovnF+nIY17udfo='}, {'domain': '.jd.com', 'expiry': 1924905600, 'httpOnly': False, 'name': '3AB9D23F7A4B3C9B', 'path': '/', 'secure': False, 'value': 'JP7V37WDMRDWJQW2D4UH3VCLDPP2ZOZBB22SK3D4D2L5YGLSY557J4AOIVFYLF6JUL467CB7PB3JU6EDOZSVRYWJSA'}, {'domain': '.jd.com', 'expiry': 1559282974, 'httpOnly': False, 'name': '__jda', 'path': '/', 'secure': False, 'value': '122270672.1543730974334635704996.1543730974.1543730974.1543730974.1'}, {'domain': '.jd.com', 'httpOnly': False, 'name': '__jdc', 'path': '/', 'secure': False, 'value': '122270672'}, {'domain': '.jd.com', 'httpOnly': False, 'name': 'wlfstk_smdl', 'path': '/', 'secure': False, 'value': 'd9np2yws9je18pwxfza6nd8ag8ofxvrb'}, {'domain': '.jd.com', 'expiry': 1545026974, 'httpOnly': False, 'name': '__jdv', 'path': '/', 'secure': False, 'value': '122270672|direct|-|none|-|1543730974334'}, {'domain': '.jd.com', 'expiry': 1543732774, 'httpOnly': False, 'name': '__jdb', 'path': '/', 'secure': False, 'value': '122270672.2.1543730974334635704996|1.1543730974'}]
# [{'domain': 'www.jd.com', 'expiry': 1575267075, 'httpOnly': False, 'name': 'o2Control', 'path': '/', 'secure': False, 'value': 'webp'}, {'domain': '.jd.com', 'expiry': 1559283075, 'httpOnly': False, 'name': '__jda', 'path': '/', 'secure': False, 'value': '122270672.1543731075402917024622.1543731075.1543731075.1543731075.1'}, {'domain': '.jd.com', 'expiry': 1543732875, 'httpOnly': False, 'name': '__jdb', 'path': '/', 'secure': False, 'value': '122270672.1.1543731075402917024622|1.1543731075'}, {'domain': '.jd.com', 'httpOnly': False, 'name': '__jdc', 'path': '/', 'secure': False, 'value': '122270672'}, {'domain': '.jd.com', 'expiry': 1545027075, 'httpOnly': False, 'name': '__jdv', 'path': '/', 'secure': False, 'value': '122270672|direct|-|none|-|1543731075402'}, {'domain': '.jd.com', 'expiry': 1559283075.589585, 'httpOnly': False, 'name': '__jdu', 'path': '/', 'secure': False, 'value': '1543731075402917024622'}]




