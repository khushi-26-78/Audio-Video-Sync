import threading
import time

#import excel
#import pandas as pd
from testScripts import testVideo
#from reuseable import serverAppium
from audio import listen


if __name__ == '__main__':
    #try:
       #serverAppium.start_server()
    try:
        testVideo.launch_appium_driver()
    except: pass
    # testVideo.action_click()

    thread2 = threading.Thread(target=testVideo.three())
    thread2.start()
    thread2.join()


    for i in range(1,6):
        thread1 = threading.Thread(target=testVideo.playing)
        thread3 = threading.Thread(target=listen.listen)
       # time.sleep(4)


        thread1.start()
        thread3.start()

        testVideo.timeSleep()

        thread5 = threading.Thread(target=testVideo.pauseVideo)
        #
        thread5.start()
        #
        #thread1.join()
        thread5.join()
        thread1.join()
        thread3.join()

            # testVideo.pauseVideo()
        print(testVideo.dct)
        #excel.writedata(testVideo.dct)
        #rint(listen.lst1)
        print("....//iteration completed//....", i)
    testVideo.close_app()
    # except:
    #     print("There is an error in code!!")
    # finally:
    # serverAppium.stop_server()
