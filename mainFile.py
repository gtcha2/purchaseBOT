from browserLinkPacker import *
import geckodriver_autoinstaller
import chromedriver_autoinstaller
import threading
from selenium import webdriver
chromedriver_autoinstaller.install()
geckodriver_autoinstaller.install()
DSNs=['DSI_1785|DSN_San%20Antonio%20West|DSZ_78250','DSI_2426|DSN_San%20Antonio%20Culebra|DSZ_78253','DSI_1523|DSN_Balcones%20Heights%20Crossroads|DSZ_78201','DSI_2187|DSN_La%20Cantera|DSZ_78257','DSI_2467|DSN_Park%20North|DSZ_78216','DSI_1979|DSN_San%20Antonio%20Westover|DSZ_78245','DSI_176|DSN_Bitters|DSZ_78232','DSI_1354|DSN_San%20Antonio%20North|DSZ_78258','DSI_2803|DSN_Alamo%20Heights|DSZ_78209','DSI_771|DSN_SW%20Military%20Drive|DSZ_78224','DSI_2239|DSN_Stone%20Oak|DSZ_78258','DSI_1852|DSN_San%20Antonio%20SE|DSZ_78223','DSI_1204|DSN_San%20Antonio%20NE|DSZ_78154','DSI_2429|DSN_New%20Braunfels|DSZ_78130','DSI_2438|DSN_San%20Marcos|DSZ_78666','DSI_3335|DSN_San%20Marcos%20Downtown|DSZ_78666']
driverListTarget=[]
def main(x):
    #for x in range(len(DSNs)):
    driver = webdriver.Chrome()
    driver.get('https://www.target.com/p/crash-bandicoot-4-it-39-s-about-time-playstation-4/-/A-80563446')#"https://www.target.com/p/playstation-5-console/-/A-81114595")
    targetSetup(DSNs[x],driver)
    driverListTarget.append(driver)
    imReadyToCheckOut(headToCheckOut(addToCartSequence(targetCartAdd(driver),driver),driver),driver)


if __name__ == '__main__':
    for t in range(len(DSNs)):
        t = threading.Thread(target=main,args=(t,))
        t.start()