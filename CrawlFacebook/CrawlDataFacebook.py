from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import schedule
import time
from time import sleep
from datetime import datetime
import mysql.connector

def job():
    cnx = mysql.connector.connect(user='root', password='',
                                    host='127.0.0.1',
                                    database='ttcs')
    cursor = cnx.cursor()  

    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/HocvienPTIT/?locale=vi_VN')
    close_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div > div > div:nth-child(5) > div > div > div > div > div:nth-child(2) > div > div > div > div > div')
    close_button.click()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    for i in range(5):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.x9f619.x1n2onr6.x1ja2u2z.xeuugli.x1iyjqo2.xs83m0k.x1xmf6yo.x1emribx.x1e56ztr.x1i64zmx.xjl7jj.x19h7ccj.x65f84u > div:first-child')
            )
        )
    for i in range(10):
        try:
            z = i+1 
            post = driver.find_element(
                By.CSS_SELECTOR, f'.x9f619.x1n2onr6.x1ja2u2z.xeuugli.x1iyjqo2.xs83m0k.x1xmf6yo.x1emribx.x1e56ztr.x1i64zmx.xjl7jj.x19h7ccj.x65f84u > div:first-child >div:nth-child({z})'
                )
            
            target= post.find_element(
                By.CSS_SELECTOR, '.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs.x126k92a > div:first-child'
                )
            
            emotion = post.find_element(
                By.CSS_SELECTOR, '.xrbpyxo.x6ikm8r.x10wlt62.xlyipyv.x1exxlbk .x1e558r4'
                )
            
            comments_and_shares = post.find_elements(
                By.CSS_SELECTOR, '.x9f619.x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.x1qughib.x1qjc9v5.xozqiw3.x1q0g3np.xykv574.xbmpl8g.x4cne27.xifccgj .x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x3x7a5m.x6prxxf.xvq8zen.xo1l8bm.xi81zsa'
            ) 
            
            title = target.text
            emotion = emotion.text
            comment = comments_and_shares[0].text
            share = comments_and_shares[1].text
            
            print(f"Div {z} text: {title}")
            print(f"Div {z} emotion: {emotion}")
            print(f"Div {z} comment: {comment}")
            print(f"Div {z} share: {share}")
            print("----------------------------------------------------")
            
            add_data = ("INSERT INTO datacrawl "
                        "(title, react, comment, share, time ) "
                        "VALUES (%s, %s, %s, %s, %s)")
            
            data = (title, emotion, comment, share, current_time)
            cursor.execute(add_data, data)
            cnx.commit() 
                    
        except NoSuchElementException:
            print(f"Div {z} không có phần tử target.")
            continue
            
    sleep(5)
    driver.close()
    cursor.close()
    cnx.close()
    
schedule.every(1).minutes.do(job) 

while True:
    schedule.run_pending()
    time.sleep(1)    