import time
from bs4 import BeautifulSoup
import requests
import serial

dataOut = serial.Serial('COM4', 9600, timeout=0)

def sendData(temp, des):
    isThereLowerCase_curr = des.find("rain")
    isThereUpperCase_curr = des.find("Rain")
    
    if((isThereLowerCase_curr >= 0) or (isThereUpperCase_curr >= 0)):
        print("RJ")
        output = "RJ"
        dataOut.write(output.encode('utf-8'))
    elif(int(temp) <= -15):
        print('HWJ')
        output = "HWJ"
        dataOut.write(output.encode('utf-8'))
    elif(int(temp) > -15 and int(temp) <= 5):
        print('PJ')
        output = "PJ"
        dataOut.write(output.encode('utf-8'))
    elif(int(temp) > 5 and int(temp) <= 10):
        print('JJ')
        output = "JJ"
        dataOut.write(output.encode('utf-8'))
    elif(int(temp) > 10 and int(temp) <= 21):
        print('H')
        output = "Hoodie"
        dataOut.write(output.encode('utf-8'))
    else:
        print('S')
        output = "Shirt"
        dataOut.write(output.encode('utf-8'))

def main():
    update = 0
    tempIndex = 0

    url_current = 'https://weather.gc.ca/city/pages/ab-52_metric_e.html'
    url = 'https://weather.gc.ca/forecast/hourly/ab-52_metric_e.html'

    page_current = requests.get(url_current)
    print(page_current)
    soup_current = BeautifulSoup(page_current.text, 'html')

    page = requests.get(url)
    print(page)
    soup = BeautifulSoup(page.text, 'html')

    temp_current = soup_current.find('div', class_ = 'col-sm-2')
    tempcurr = temp_current.find('span')
    tempcurr_tempDataFormat = [data.text.strip() for data in tempcurr]
    
    if(tempcurr_tempDataFormat[0][1] == '°'):
        tempcurrNum = tempcurr_tempDataFormat[0][0]
    elif(tempcurr_tempDataFormat[0][2] == '°'):
        tempcurrNum = tempcurr_tempDataFormat[0][:2]
    elif(tempcurr_tempDataFormat[0][3] == '°'):
        tempcurrNum = tempcurr_tempDataFormat[0][:3]
    
    print(tempcurrNum)
    
    temp_current_des = soup_current.find('div', class_ = 'col-sm-4')
    tempcurr_des = temp_current_des.find('span')
    tempcurr_tempDataFormat_des = [data.text.strip() for data in tempcurr_des]
    print(tempcurr_tempDataFormat_des[0])

    sendData(tempcurrNum, tempcurr_tempDataFormat_des[0])

    table = soup.find('table')

    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    while(True):
        t = time.localtime()
        current_minute = time.strftime("%M", t)

        inp = dataOut.read(1)
        inp1 = str(inp)
        mainInp = inp1[2]

        if mainInp == 'w':
            print(mainInp)
            if(tempIndex < 5):
                tempIndex = tempIndex + 1
            if(tempIndex > 0):
                print("==================================")
                if len(rows[tempIndex]) < 2:
                    tempIndex = tempIndex + 1
                
                tempData = rows[tempIndex].find_all('td')
                tempDataFormat = [data.text.strip() for data in tempData]
                print(tempDataFormat)
                
                sendData(tempDataFormat[1], tempDataFormat[2])
            else:
                print("====================================")
                print(tempcurrNum)
                print(tempcurr_tempDataFormat_des[0])
                sendData(tempcurrNum, tempcurr_tempDataFormat_des[0])
        elif mainInp == 'q':
            print(mainInp)
            if(tempIndex > 0):
                tempIndex = tempIndex - 1
            if(tempIndex > 0):
                print("==================================")
                if len(rows[tempIndex]) < 2:
                    tempIndex = tempIndex - 1
                tempData = rows[tempIndex].find_all('td')
                tempDataFormat = [data.text.strip() for data in tempData]
                print(tempDataFormat)
				
                sendData(tempDataFormat[1], tempDataFormat[2])
            else:
                print("====================================")
                print(tempcurrNum)
                print(tempcurr_tempDataFormat_des[0])
                sendData(tempcurrNum, tempcurr_tempDataFormat_des[0])


        if(current_minute == "03"):
            update = 0

        if(current_minute == "02"): #new hour, get update
            tempIndex = 0
            if(update == 1):
                continue

            page_current = requests.get(url_current)
            print(page_current)
            soup_current = BeautifulSoup(page_current.text, 'html')

            page = requests.get(url)
            print(page)
            soup = BeautifulSoup(page.text, 'html')

            #get temperature
            temp_current = soup_current.find('div', class_ = 'col-sm-2')
            tempcurr = temp_current.find('span')
            tempcurr_tempDataFormat = [data.text.strip() for data in tempcurr]
            
            if(tempcurr_tempDataFormat[0][1] == '°'):
                tempcurrNum = tempcurr_tempDataFormat[0][0]
            elif(tempcurr_tempDataFormat[0][2] == '°'):
                tempcurrNum = tempcurr_tempDataFormat[0][:2]
            elif(tempcurr_tempDataFormat[0][3] == '°'):
                tempcurrNum = tempcurr_tempDataFormat[0][:3]

            print(tempcurrNum)

            #get description
            temp_current_des = soup_current.find('div', class_ = 'col-sm-4')
            tempcurr_des = temp_current_des.find('span')
            tempcurr_tempDataFormat_des = [data.text.strip() for data in tempcurr_des]
            print(tempcurr_tempDataFormat_des[0])

            sendData(tempcurrNum, tempcurr_tempDataFormat_des[0])
            
            table = soup.find('table')

            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
                
            update = 1

if __name__ == '__main__':
    main()
