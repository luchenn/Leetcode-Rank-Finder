from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


target_username = "xxx"
url = "https://leetcode.com/contest/weekly-contest-69/ranking/"
driver = webdriver.Firefox(executable_path="./geckodriver")
timeout_sec = 5
ans = "Username" + target_username + " found at page {page}, row {row}, rank {rank}!"

for page in range(1, 100):
    print "Now visiting page:", page
    driver.get(url + str(page))

    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'ranking-username'))
        WebDriverWait(driver, timeout_sec).until(element_present)
    except TimeoutException:
        print "Page Timeout!"

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    users = [x.get("title") for x in soup.find_all("a", attrs={"class": "ranking-username"})]
    if target_username in users:
        row = users.index(target_username) + 1
        result = {"page": page, "row": row, "rank": 25*(page-1)+row}
        print ans.format(**result)
        # driver.close()
        break
