import time
from testScripts import testVideo
import pyfirmata
def arduino():

    port = pyfirmata.Arduino("COM5")
    pinA0=port.get_pin('a:0:i')
    it = pyfirmata.util.Iterator(port)
    it.start()
    output=[]
    for i in range(5):
        read_out=pinA0.read()
        output.append(read_out)
        # print(read_out)
        time.sleep(1)
    output_final=0
    for i in output:
        if i is not None:
            output_final+=float(i)*1000

    output_final=output_final/(len(output)-1)
    port.exit()
    print("Flash detection :",output_final)
    testVideo.dict["flash detection"]=output_final
# arduino()