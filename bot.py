import os
from io import open
from selenium.common.exceptions import TimeoutException
from selenium import webdriver 
#from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement 
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
from selenium.webdriver.common.keys import Keys
import time
#from urllib import urlopen,urlretrieve
#from bs4 import BeautifulSoup ,re
#from urllib import urlopen
#from bs4 import BeautifulSoup ,re


def toolBot(dataInput):

    outputFile = open("input.txt", "w",encoding="utf-8")
    outputFile.write(dataInput.decode('utf-8'))
    outputFile.close()
    
    # file1 = open("input.txt","w") 

    # file1.write(dataInput) 
    # file1.close()
    directory = "ref"
    os.system("rm -rf "+directory)
    os.system("mkdir "+directory)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-plugins-discovery");
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(r"/var/www/html/rnd/aditya/Aditya/chromedriver",chrome_options=chrome_options)
    driver.delete_all_cookies()
    driver.set_window_size(800,800)
    driver.set_window_position(0,0)
    print('arguments done')
    driver.get("https://quillbot.com/")

    inputFile = open('input.txt', 'r')
    outputFile = open("output.txt", "a")
    data= inputFile.read().strip() 
    array= []
    splat = data.split("\n\n")
    # splat = data.split("\n\n")
    #len(splat)
    for string_i in range(len(splat)):
        multiOutputCount=1
        firstParaphrase="-1"
        laterParaphrase="+1"
        while firstParaphrase!=laterParaphrase and multiOutputCount!=5:
            try:
                if (firstParaphrase == "-1"):
                    fname="input.txt"
                    inputBox= WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#inputText")))
                    inputBox.clear()                                   
                    inputBox.send_keys(splat[string_i])
                    submit= WebDriverWait(driver,10 ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#inOutContainer div.Pane.vertical.Pane1 > div > div > div:nth-child(2) > div > div > div > div > div:nth-child(2) > div > div > div > button[type='button']")))
        #            print(submit.text)               
                    submit.click()
        #            print(submit.value_of_css_property('opacity'))
                    time.sleep(0.6)
                    while(submit.value_of_css_property('opacity')!='1'):
            #            print(submit.text)   #            print(submit.value_of_css_property('opacity'))
                        time.sleep(0.2)
                    outputBox=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#outputText > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-true")))
                    firstParaphrase=outputBox.text
                    print("\n\nInput No. "+str(string_i + 1))
                    print("\n\n\nParaphrase #1:\n\n" + firstParaphrase)
                    
                    fileName="ref/r"+str(string_i + 1)+"_"+str(multiOutputCount)+".txt"
                    output="output/o"+str(string_i + 1)+".txt"
                    hypo="h.txt"
                    fname = fileName
                    displayFile="output.txt"
                    outputFile = open(fileName, "w",encoding="utf-8")
                    display = open(displayFile, "a",encoding="utf-8")
                    # fn = open(fname, "a",encoding="utf-8")

                    outputFile.write(firstParaphrase)
                    # fn.write(fileName.decode('utf-8')+" ")
                    # ss = decode('utf-8')
                    ss = "\n\n#####################################################################"
                    display.write(ss.decode('utf-8'))
                    ss = "\n\n\nParaphrase #1:\n\n " + firstParaphrase+"\n"
                            
                    display.write(ss.decode('utf-8'))

                    outputFile.close()
                    display.close()
                  
                    
                    # outputFile1 = '/'+outputFile
                    # print outputFile1

                    # os.system("perl blu.pl %s < %s" % (fileName,hypo))
                    # time.sleep(1)
        #            break
                else:
                    while(True):
                        if multiOutputCount==5:
                            break
                        submit.click()
                        time.sleep(0.6)
                        while(submit.value_of_css_property('opacity')!='1'):
                            time.sleep(0.2)
                        laterParaphrase=outputBox.text
                        if(laterParaphrase == firstParaphrase):
                            break
                        else:
                            multiOutputCount+=1
                            
                            print("####################################################")

                            print("\n\n\n\nParaphrase #"+ str(multiOutputCount)+":\n\n"+laterParaphrase+"\n")

                            fileName="ref/r"+str(string_i+1)+"_"+str(multiOutputCount)+".txt"
                            # fname = "/home/aditya/Desktop/frnd/filenames.txt"
                            fname += " "+fileName
                            outputFile = open(fileName, "w",encoding="utf-8")
                            # fn = open(fname, "a",encoding="utf-8")
                            
                            # fn.write(fileName.decode('utf-8')+" ")
                            outputFile.write(laterParaphrase)
                            ss = "\n\n#####################################################################"

                            displayFile="output.txt"
                            display = open(displayFile, "a",encoding="utf-8")
                            display.write(ss.decode('utf-8'))
                            ss = "\n\n\n\nParaphrase #"+ str(multiOutputCount)+":\n\n"+laterParaphrase +"\n"        
                            display.write(ss.decode('utf-8'))
                            
                            # display.write("\n\n\n\nParaphrase #"+ str(multiOutputCount)+":\n\n "+laterParaphrase)
                            #display.write(firstParaphrase)

                            outputFile.close()
                            display.close()
                            hypo = "h.txt"

                            # os.system("perl blu.pl %s < %s" % (fileName,hypo))
                            # time.sleep(1)

            except Exception as e:
                print("exception occured",e)
                popupBox=driver.find_elements_by_css_selector("div.MuiPaper-root.MuiDialog-paper.jss396.MuiDialog-paperScrollPaper.MuiDialog-paperWidthMd.MuiPaper-elevation24.MuiPaper-rounded")
                if len(popupBox)!=0 :
                    closeButton=popupBox[0].find_element_by_tag_name("button")
                    closeButton.click()
                    print("Popup box was there and is removed")
                
                else :
    #                html = driver.page_source
    #                b= BeautifulSoup(html,'html.parser')
                    feedBox=driver.find_elements_by_xpath("//*[contains(text(), 'Feedback')]")
                    
    #                feedBox=driver.find_elements_by_class_name("MuiButtonBase-root.MuiIconButton-root")
    #                FeedBox=b.find("button",{"class":re.compile("\.*MuiButtonBase-root MuiIconButton-root jss\.*")})
                    
    #                search_box = driver.find_element(by='name', value=" ".join(FeedBox.attrs['class']))
    #                button.MuiButtonBase-root.MuiIconButton-root.jss570
                    if len(feedBox)!=0 :
                        closeButton=feedBox[0].find_element_by_xpath("..").find_element_by_css_selector("button")
                        closeButton.click()
                        print("Feedback box was there and is removed");
                    else :
                        loginBox=driver.find_elements_by_css_selector("button.MuiButtonBase-root.MuiIconButton-root.auth-close-btn")
                        if(len(loginBox)!=0):
                            loginBox[0].click()
                        else:
                            print("Unhandled stopping")
                            break
    #inputFile.close()
    print(fname)
    os.system("perl blu.pl %s < %s" % (fname,hypo))
    time.sleep(1)
    # os.system("perl blu1.pl %s < %s" % (inputFile,hypo))
    # time.sleep(1)
    # os.system("rm -rf "+directory)

    with open("output.txt") as f:
        with open(output, "w") as f1:
            for line in f:
                f1.write(line)
    

    driver.close()



# def writeIp(data)
#     # Python program to illustrate 
#     # Append vs write mode 
#     file1 = open("input.txt","w") 

#     file1.write(data) 
#     file1.close() 
