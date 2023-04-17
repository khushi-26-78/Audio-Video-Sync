import threading
import time

import pandas as pd
from testScripts import testVideo
from reuseable import serverAppium
from audio import listen


if __name__ == '__main__':
    # try:
    serverAppium.start_server()
    try:
        testVideo.launch_appium_driver()
    except:
        pass
    dict_excel={'Listen_start':[],'Video_play':[],'Video_pause':[],'Listen_stop':[]}
    for i in range(0, 10):
        thread1 = threading.Thread(target=testVideo.play_video)
        thread1.start()

        thread3 = threading.Thread(target=listen.listen)
        thread3.start()

        testVideo.timeSleep()

        thread5 = threading.Thread(target=testVideo.pauseVideo)

        thread5.start()
        thread5.join()
        thread1.join()
        thread3.join()

        print(testVideo.dict)
        for i in dict_excel.keys():
            dict_excel[i].extend([testVideo.dict[i]])

        print("....//iteration completed//....", i)
    testVideo.close_app()
    df=pd.DataFrame(dict_excel)
    df.to_excel("output_final.xlsx",index=False)
# except:
#     print("There is an error in code!!")
# finally:
# serverAppium.stop_server()
