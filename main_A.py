import threading
import time

import test_audio
from audio import listen


if __name__ == '__main__':
    try:
        test_audio.launch_appium_driver()
    except: pass
    test_audio.click_audio()
    time.sleep(2)
    test_audio.click_audio_f()
    time.sleep(1)
    test_audio.click()
    time.sleep(3)
    test_audio.pause_audio()
