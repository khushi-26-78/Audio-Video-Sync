import threading
import pandas as pd
from testScripts import testVideo
from reuseable import serverAppium
from audio import listen

if __name__ == '__main__':
    # try:
    # serverAppium.start_server()

    testVideo.launch_appium_driver()
    testVideo.action_click()

    thread1 = threading.Thread(target=testVideo.play_video)
    thread3 = threading.Thread(target=listen.listen)

    thread1.start()
    thread3.start()


    testVideo.timeSleep()


    thread5 = threading.Thread(target=testVideo.pauseVideo)
    #
    thread5.start()
    #
    thread5.join()
    thread1.join()
    thread3.join()

    testVideo.pauseVideo()
    testVideo.close_app()
    print(testVideo.lst)
    # except:
    #     print("There is an error in code!!")
    # finally:
    # serverAppium.stop_server()
