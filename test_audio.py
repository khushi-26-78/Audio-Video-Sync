import base64
import os
import threading
import time
from telnetlib import EC

from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import datetime
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from datetime import datetime


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from reuseable.configs import MobileConfig
from locators import videoLocators

global dt
global time_now
dct={}

def launch_appium_driver():
    global driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", MobileConfig.desired_caps)
    driver.implicitly_wait(10)
    driver.start_activity("org.videolan.vlc", "org.videolan.vlc.StartActivity")

def action_click():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(166, 176)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

def click_audio():
    driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Audio"]').click()

def click_audio_f():
    driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Audio track: 1_to_20.wav, Duration: 20 seconds, Album: , Artist: "]').click()

def click():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(528, 1571)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()


def pause_audio():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(542, 1699)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()



    driver.back()
    driver.back()

