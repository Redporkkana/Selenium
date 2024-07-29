import time
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    return chrome_driver


def test_jackets(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    women = driver.find_element(By.ID, 'ui-id-4')
    tops = driver.find_element(By.ID, 'ui-id-9')
    jackets = driver.find_element(By.ID, 'ui-id-11')
    actions = ActionChains(driver)
    actions.move_to_element(women)
    actions.move_to_element(tops)
    actions.click(jackets)
    actions.perform()


def test_drag_n_drop(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    draggable = driver.find_element(By.ID, 'rect-draggable')
    droppable = driver.find_element(By.ID, 'rect-droppable')
    ActionChains(driver).drag_and_drop(draggable, droppable).perform()
    actions = ActionChains(driver)


def test_open_tab(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    inputs = driver.find_elements(By.LINK_TEXT, 'Inputs')[0]
    ActionChains(driver).key_down(Keys.COMMAND).click(inputs).key_up(Keys.COMMAND).perform()
    time.sleep(1)
