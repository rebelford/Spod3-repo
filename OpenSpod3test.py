#!/usr/bin/python3
# 
# import datetime, time
# import gspread
# from google.auth.transport.requests import AuthorizedSession
# from google.oauth2 import service_account
# from time import sleep
# import math
# 
# #ESP stuff
import urllib.request
#TASK1
with urllib.request.urlopen('http://144.167.239.168') as response:
    data = response.read()
print(data)   
print(type(data))
print(10*'*')
    
    
# #webUrl = urllib.request.urlopen('http://144.167.212.266')
#TASK 2 convert data from class "bytes" to class "string"
#print(data)
data=data.rstrip()
# print(data)
# print(type(data))

# #TASK3  remove final quote 
data1=str(data)
# data1=data1.rstrip("'")
print(data1)
print(type(data1))
# #TASK4 function that converts string to a list
def Convert(string):
    li = list(string.split(","))
    return li
li = Convert(data1)
print(li)
print(type(li))



# #the angles will need to be variables in stacked pods that align with cardinal coordinates"
# #Task5 is a function that inputs three sensor signals and output x,y,r,angle in degrees, angle in radians and ave sensor value
# def config_vect(A_read,B_read,C_read):
#     '''this function inputs three sensor signals at the vertices of a triangle and returns values of the x axis,
# y axis, hypotenous and the angle in radians and degrees and average '''
#     ang_A=math.radians(90)
#     ang_B=math.radians(330)
#     ang_C=math.radians(210)
#     x=A_read*math.cos(ang_A)+B_read*math.cos(ang_B)+C_read*math.cos(ang_C)
#     y=A_read*math.sin(ang_A)+B_read*math.sin(ang_B)+C_read*math.sin(ang_C)
#     r=math.sqrt(x**2 +y**2)
#     rad=math.acos(x/r)
#     deg=math.degrees(rad)
#     ave=(A_read + B_read + C_read)/3
#     #print(f"x is {x}, y is {y}, r is {r}, the degrees in radians is {rad}, the degrees in degrees is {deg}")
#     #return(f"x is{x}, y is{y} and r is{r}")
#     return(x,y,r,rad,deg,ave)
# 
# data3 = Convert(data1)
# print(data3)
# # print(type(data3))
# #TASK 6 assign raw data from list to variables using list indexes
# #Pulling Data from SPOD 
# MAC_A = data3[0]
# ESP_ID = data3[1]
# T_A = data3[2]
# RH_A = data3[3]
# P_A = data3[4]
# VOC_A = data3[5]
# T_B = data3[6]
# RH_B = data3[7]
# P_B = data3[8]
# VOC_B = data3[9]
# T_C = data3[10]
# RH_C = data3[11]
# P_C = data3[12]
# VOC_C = data3[13]
#  #TASK7 - convert data to float and then input to configuration vector function
# #the data in the list are strings and we need to convert to float in order to do math 
# #print(type(VOC_A))
# n_VOC_A=float(VOC_A)
# n_VOC_B=float(VOC_B)
# n_VOC_C=float(VOC_C)
#  
#  #VOC calc
# output=config_vect(n_VOC_A,n_VOC_B,n_VOC_C)
# output=list(output)
# VOC_x=output[0]
# VOC_y=output[1]
# VOC_r=output[2]
# VOC_rad=output[3]
# VOC_deg=output[4]
# VOC_ave=output[5]
# print(f"VOC_x={VOC_x} of class{type(VOC_x)} and VOC_y={VOC_y} and VOC_r={VOC_r}")
# 
#  #temp calc
# n_T_A=float(T_A)
# n_T_B=float(T_B)
# n_T_C=float(T_C)
# 
# output=config_vect(n_T_A,n_T_B,n_T_C)
# output=list(output)
# T_x=output[0]
# T_y=output[1]
# T_r=output[2]
# T_rad=output[3]
# T_deg=output[4]
# T_ave=output[5]
# print(f"T_x={T_x} of class{type(T_x)} and T_y={T_y} and VOC_r={T_r}")
# 
#  #P calc
# n_P_A=float(P_A)
# n_P_B=float(P_B)
# n_P_C=float(P_C)
# 
# output=config_vect(n_P_A,n_P_B,n_P_C)
# output=list(output)
# P_x=output[0]
# P_y=output[1]
# P_r=output[2]
# P_rad=output[3]
# P_deg=output[4]
# P_ave=output[5]
# print(f"P_x={P_x} of class{type(P_x)} and P_y={P_y} and P_r={P_r}")
# 
#  #Relative Humidity Calc
# n_RH_A=float(RH_A)
# n_RH_B=float(RH_B)
# n_RH_C=float(RH_C)
# 
# output=config_vect(n_RH_A,n_RH_B,n_RH_C)
# output=list(output)
# RH_x=output[0]
# RH_y=output[1]
# RH_r=output[2]
# RH_rad=output[3]
# RH_deg=output[4]
# RH_ave=output[5]
# print(f"RH_x={RH_x} of class{type(RH_x)} and RH_y={RH_y} and RH_r={RH_r}")
#  
#  #TASK8 upload data to Google Sheet through API
# #Access Google API
# googleAPI = '/home/pi/Programs/0_crontab/API_proj_1_key.json'
# scope = ['https://www.googleapis.com/auth/drive']
# credentials = service_account.Credentials.from_service_account_file(googleAPI)
# scopedCreds = credentials.with_scopes(scope)
# gc = gspread.Client(auth=scopedCreds)
# gc.session = AuthorizedSession(scopedCreds)
# sheet = gc.open("Spod1")
# worksheet = sheet.worksheet("openSpod1")
# 
# time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# values =[time, MAC_A, ESP_ID, n_VOC_A, n_VOC_B, n_VOC_C, VOC_ave, VOC_x, VOC_y, VOC_r, VOC_deg, VOC_rad,
#          n_P_A, n_P_B, n_P_C, P_ave, P_x, P_y, P_r, P_deg, P_rad, n_T_A, n_T_B, n_T_C, T_ave, T_x, T_y, T_r,
#          T_deg, T_rad, n_RH_A, n_RH_B, n_RH_C, RH_ave, RH_x, RH_y, RH_r, RH_deg, RH_rad
# ]
# #worksheet.insert_row(values, 2, value_input_option='str')
# #worksheet.insert_row(values, 2, value_input_option='RAW')
# worksheet.insert_row(values, 2, value_input_option='USER_ENTERED')
# print("Google Sheet Updated")
# # the following code makes backup file
# #TASK 9 dump data to local back file (csv)
# #note how we removed brackets from the list when we converted to strings
Spod3Backup = open("newbackup.csv","a")
#Spod3Backup.write("\n")
Spod3Backup.write(str(li)[1:-1])
Spod3Backup.write("\n")
Spod3Backup.close()
# 