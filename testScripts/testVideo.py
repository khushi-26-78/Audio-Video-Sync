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
# Launching appium driver here
def launch_appium_driver():
    global driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", MobileConfig.desired_caps)
    driver.implicitly_wait(10)
    driver.start_activity("org.videolan.vlc", "org.videolan.vlc.StartActivity")

# Starting screen recording
def start_record():
    driver.start_recording_screen()
    #time_now = datetime.now()
    # a_current_time = time.time()
    # print('Timestamp of Record.....:', a_current_time)

# Opening the VLC player from menu list
def action_click():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(173, 156)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(542, 1598)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(549, 763)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    # driver.find_element(AppiumBy.XPATH, videoLocators.vlc_app()).click()
    # # driver.start_activity("org.videolan.vlc", "org.videolan.vlc.gui.video.VideoPlayerActivity")

def video():
    driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Video']/android.view.ViewGroup/android.widget.TextView").click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Audio"]').click()
    #time.sleep(1)


def three():
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Facebook video 3692218894175394"]').click()
    #video playing started


    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(542, 1719)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(1)
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(542, 1723)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    #normal click on screen
    time.sleep(2)
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(1053, 1733)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(2)

    #playback speed
    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Playback speed"]').click()

    #set speed

    #actions = TouchAction(driver)
    # speed_input = input("enter your suitable speed: ")
    # element = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Increase speed"]')
    # #actions.press(element).wait(300).release().perform()
    # # actions.release().perform()
    # el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.videolan.vlc:id/playback_speed_value"]').is_displayed()
    # text = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.videolan.vlc:id/playback_speed_value"]').text
    # print("Element text: ", text)

    actions = TouchAction(driver)
    speed_input = input("Enter desired playback speed (e.g. 2.00x): ")
    target_speed = speed_input.strip() + " "
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Increase speed"]')
    while True:
        actions.long_press(element).perform()
        playback_speed_element = driver.find_element(AppiumBy.XPATH,
                                                     '//android.widget.TextView[@resource-id="org.videolan.vlc:id/playback_speed_value"]')
        playback_speed = playback_speed_element.text.strip()
        if playback_speed == target_speed:
            print(f"Playback speed set to {playback_speed}")
            actions.release().perform()
            break
        actions.wait(1000).release().perform()
        print(f"Current playback speed: {playback_speed}. Increasing speed...")

    driver.back()
    driver.back()

    time.sleep(4)

def playing():
    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Facebook video 3692218894175394"]').click()
    b_current_time = time.time()
    dct["play"] = b_current_time
    print('Timestamp of play...:', b_current_time)
def timeSleep():
    time.sleep(10)



def pauseVideo():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(542, 1719)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(1)
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(542, 1723)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    #time_now = datetime.now()
    c_curretn_time = time.time()
    dct["pause"]=c_curretn_time
    print('Timestamp of Pause:', c_curretn_time)
    # time.sleep(5)
    driver.back()
    # driver.back()

def stop_record():
    recording_raw = driver.stop_recording_screen()

    time_now = datetime.now()
    d_current_time = time_now.time()
    #lst.append(d_current_time)
    #print('Timestamp of Stop_record:', d_current_time)
    video_name = "Recording" + driver.current_activity
    filepath = os.path.join("C:/Users/Anuj/PycharmProjects/Project(video-audio)/Recording/", video_name + ".mp4")

    with open(filepath, "wb+") as videoRecorder:
        videoRecorder.write(base64.b64decode(recording_raw))



def close_app():
    driver.quit()

