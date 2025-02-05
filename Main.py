from selenium import webdriver
import click

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://course.qqhru.edu.cn/meol/")
    click.login(driver)
    url="https://course.qqhru.edu.cn/meol/jpk/course/layout/newpage/index.jsp?courseId=60865"
    click.openPage(driver,url)
    click.checkTest(driver, 4, 'Second')
    click.checkTest(driver, 3, 'Th')
    click.checkTest(driver, 2, 'For')
