def scrapy():
  import time
  import chromedriver_binary
  from selenium import webdriver
  from settings import STUDENT_ID, PASSWORD

  driver = webdriver.Chrome()
  driver.get('https://portal.kansai-u.ac.jp/Portal/index.jsp')
  time.sleep(5)

  # 大学マイアカウントにログイン
  student_id = driver.find_element_by_name("IDToken1")
  password = driver.find_element_by_name("IDToken2")
  login = driver.find_element_by_name("Login.Submit")
  student_id.send_keys(STUDENT_ID)
  password.send_keys(PASSWORD)
  login.submit()

  time.sleep(5)

  iframe = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/iframe')
  driver.switch_to.frame(iframe)
  time.sleep(5)

  class_information_list = []
  for i in range(5):
    i += 1
    try:
      period = driver.find_element_by_xpath(f'//tr[@class="timetable"]/td[@class="near"][1]/dl{[i]}/dt').text
      subject = driver.find_element_by_xpath(f'//tr[@class="timetable"]/td[@class="near"][1]/dl{[i]}//a').text
      classroom = driver.find_element_by_xpath(f'//tr[@class="timetable"]/td[@class="near"][1]/dl{[i]}/dd[2]').text
      try:
        information = driver.find_element_by_xpath(f'//tr[@class="timetable"]/td[@class="near"]/dl{[i]}//img').get_attribute('alt')
        information = infomation_check(information)
      except:
        information = "連絡事項はありません"
      class_dict = dict(period=period, subject=subject, classroom=classroom, information=information)
      class_information_list.append(class_dict)
    except:
      pass
  time.sleep(5)
  driver.quit()
  return class_information_list

def infomation_check(info):
  if info == "連絡":
    return "連絡事項があります"
  elif info == "休校":
    return "本日は休校です"
  else:
    return "エラー"
