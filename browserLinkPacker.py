#this will be packing up links and autofilling 
##need to import webdrivers
## things to do, have links
## add to cart based on link, practice via selenium
## finally when added auto entyr purchase and pickup.
## Target stores, 
# Best buy
# walmart
#best buy
# gamestop
#amazon
# organize sites
# 
import time
import geckodriver_autoinstaller
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
##
def setup():
    chromedriver_autoinstaller.install()
    geckodriver_autoinstaller.install()
setup()
def driverSpawn():
    return webdriver.Chrome()
# driver.get( 'https://www.target.com/p/crash-bandicoot-4-it-39-s-about-time-playstation-4/-/A-80563446')
    #'https://www.target.com/p/watch-dogs-legion-playstation-4/-/A-76620904')
    #"https://www.target.com/p/playstation-5-console/-/A-81114595")
# 

#[“https://www.target.com/p/playstation-5-console/-/A-81114595”,”https://www.walmart.com/ip/PlayStation5-Console/363472942”,”https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149”,”https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html?condition=New”]
listOfLinks=[""]
listOfXPaths=[""]






def targetSetup(cookie,driver):
    ##get the cookie, then delete the cookie change the value
    deleteCookies=driver.get_cookie("fiatsCookie")
    driver.delete_cookie("fiatsCookie")
    deleteCookies["value"]=cookie
    driver.add_cookie(deleteCookies)
    driver.refresh()
    return
def targetCartAdd(driver):
    y=1
    while y==1:
        driver.refresh()
        time.sleep(2.5)
        
        #TODO: add in try statements for the clicks also run the next
        try:
            xpath=driver.find_element_by_xpath('//*[@id="viewport"]/div[5]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[1]/div[2]/button')
            print("success on first try")
            xpath.click()
            y=0
            return True
        except NoSuchElementException:
            try:
                buttonList=driver.find_elements_by_tag_name('button')
                if (len(buttonList)!=0):
                    for x in buttonList:
                        if(x.text=="Pick it up"):
                            x.click()
                            y=0
                            return True
                        # i dont know if this works?
            except NoSuchElementException:
                #need to add in the notification popup for window. 
                ## also add in the refresh every .3 seconds. 
                return print("did not work..")
def addToCartSequence(bool,driver):
    y=1
    if bool:
        while(y==1):
            time.sleep(.5)
            try:
                declineCoverage=driver.find_element_by_xpath('/html/body/div[15]/div/div/div/div/div/div/div/div[2]/div[2]/button')
                declineCoverage.click()
                print("found try1")
                y=0
                return True
            except NoSuchElementException:
                try:
                    buttons=driver.find_elements_by_tag_name('button')
                    for x in buttons:
                        
                        if (x.text=="Decline coverage"):
                            x.click()
                            y=0
                            return True
                except NoSuchElementException:
                    return print("nothgin to find")
def headToCheckOut(boolean,driver):
    y=1
    if boolean:
        while y==1:
            try:
                checkout=driver.find_element_by_xpath('/html/body/div[16]/div/div/div/div/div/div/div[2]/div[3]/button')
                checkout.click()
                y==0
                return True
            except NoSuchElementException:
                try:
                    buttons=driver.find_elements_by_tag_name('button')
                    for x in buttons:
                        if (x.text == 'View cart & checkout'):
                            x.click()
                            y=0
                            return True
                except NoSuchElementException:
                    return False
def imReadyToCheckOut(truth,driver):
    # might need more time to wait for page to reload via the injected JS
    y=1
    while y==1:
        time.sleep(2)
        if truth:
            try:
                checkoutfinally=driver.find_element_by_xpath('//*[@id="viewport"]/div[5]/div[2]/div[1]/div[3]/div/div[2]/div/button')
                checkoutfinally.click()
                print('first seq')
                y=0
                return True
            except NoSuchElementException:
                try:
                    buttonsOnPage=driver.find_elements_by_tag_name('button')
                    print(len(buttonsOnPage))
                    for x in buttonsOnPage:
                        if x.text=="I'm ready to check out":
                            x.click()
                            y=0
                            return True
                except NoSuchElementException:
                    print('nothing')
                    return False
# def logInButton(bool,driver):
#     ###CHANGE THIS ON THE SEND KEYS
#     y=1
#     if bool:
#         time.sleep(1.2)
#         driver.refresh()
#         time.sleep(1.5)
#         try:
#             el1=driver.find_element_by_id('username')
#             el1.send_keys('')
#             el2=driver.find_element_by_id('password')
#             el2.send_keys('')
#         except NoSuchElementException:
#                 try:
#                     xpath=driver.find_element_by_xpath('//*[@id="login"]')
#                     xpath.click()
#                     y=0
#                     return True
#                 except NoSuchElementException:
#                     try:
#                         buttonsOnPage=driver.find_elements_by_tag_name('button')
#                         print(len(buttonsOnPage))
#                         for x in buttonsOnPage:
#                             if x.text=="Sign in":
#                                 x.click()
#                                 y=0
#                                 return True
#                     except NoSuchElementException:
#                         print('nothing')
#                         return False
            
            

## after this is done then check if you hit check out. 
## move onto the next step. 
time.sleep(.8)
# imReadyToCheckOut(
#     headToCheckOut(
#         addToCartSequence(
#             targetCartAdd())))




##this is the start of the best buy specific code.
### too much sphaghetti code  create a recursive function

practiceLinkBestBuy="https://www.bestbuy.com/site/sony-playstation-5-hd-camera/6430166.p?skuId=6430166"

def searchFunction(driver,truthStuff=False,pageXpath='',tag_text='',timeout=0.5,repeat=False,tag_title=''):
    # need to add in the update function portion.
    time.sleep(timeout)
    try:
        xpathElement=driver.find_element_by_xpath(pageXpath)
        xpathElement.click()
    except NoSuchElementException:
        try: 
            buttons=driver.find_elements_by_tag_name('button')
            for x in buttons:
                print(x.text)
                if(x.text==tag_text):
                    x.click()
                    return True
        except NoSuchElementException:
            try: 
                shot_inTheDark=driver.find_elements_by_link_text(tag_text)
                for x in shot_inTheDark:
                    print(x.text)
            except NoSuchElementException:
                return False
    
## data  for best buy 
#xpath for add to cart
# def customCheckStorePattern(email,phone,driver):
#     try:
#         el1 = driver.find_element_by_id='user.emailAddress'
#         el1.send_keys(email)
#         el2=driver.find_element_by_id ='user.phone'
#         el2.send_keys(phone)
#         return
#     except NoSuchElementException:
#         time.sleep(3)
#         customCheckStorePattern(email,phone,driver)
#         try:
#             driver.find_elements_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button').click()
#             return True
#         except NoSuchElementException:
#                 try:
#                     buttonsOnPage=driver.find_elements_by_tag_name('button')
#                     for x in buttonsOnPage:
#                         if (x.text=="Continue to Payment Information"):
#                             x.click()
#                             return True
#                 except NoSuchElementException:
#                     return False
driver2 = webdriver.Chrome()
#driver2.get("https://www.bestbuy.com/site/sony-playstation-5-hd-camera/6430166.p?skuId=6430166")
def bestBUYbrowse(driver):
    firstResult=searchFunction(driver,True,'//*[@id="fulfillment-add-to-cart-button-d1a41139-6142-4a27-9a82-f73b2c22e818"]/div/div/div/button','Add to Cart',1.5)
    driver.get("https://www.bestbuy.com/cart")
    searchFunction(driver,True,'//*[@id="cartApp"]/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button','Checkout',1.3)
    searchFunction(driver,True,'/html/body/div[1]/div/section/main/div[4]/div/div[2]/button','Continue as Guest',3)
    #customCheckStorePattern('randoemail@gmail.com','8234719092',driver2)
##//*[@id="fulfillment-add-to-cart-button-d1a41139-6142-4a27-9a82-f73b2c22e818"]/div/div/div/button
## text:
## --
#bestBUYbrowse()
## proceed to checkout
##//*[@id="shop-attach-modal-60959053-modal"]/div/div[1]/div/div/div/div/div[1]/div[3]/a
##text:
##---

##next checkout 
##//*[@id="cartApp"]/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button
## text:
##Checkout?

##guest checkout
#/html/body/div[1]/div/section/main/div[4]/div/div[2]/button
#Continue as Guest?
#3 sec delay

#no clikcs
##email://*[@id="user.emailAddress"]
#id: user.emailAddress
##key entry:
##phone: //*[@id="user.phone"]
##id:user.phone
##key entry: unknown
##continue to payment information
#//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button
#

## auto fill or manual entry?
##HUGE TIME OUTS>>>> need to wait for full page. 





#driver.delete_cookie("fiatsCookie")
#deleteCookies["value"]="DSI_2187|DSN_La%20Cantera|DSZ_78257"
#driver.add_cookie(deleteCookies)
#driver.refresh()



