import time
from selenium import webdriver



postUrl = "http://mail.sofia7.com";
driver=webdriver.Chrome();

driver.get(postUrl);
# time.sleep(3)
# driver.find_element_by_id("J_menu_login").click();
# time.sleep(1)
# driver.switch_to.frame("taobaoLoginIfr");
# driver.find_element_by_id("J_Quick2Static").click();
# time.sleep(3);
driver.find_element_by_id("user").send_keys("suxy3");
# time.sleep(3);
driver.find_element_by_id("password").send_keys("1qaz3edc");
# time.sleep(3);
driver.find_element_by_id("submitBtn").click();
time.sleep(3);
driver.find_element_by_id("gwt-uid-469").find_element("title","未读邮件").click();


# driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys("sxyw110");
# driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys("bd7236570");
# driver.find_element_by_id("TANGRAM__PSP_3__submit").click();
# driver.close();
