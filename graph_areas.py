import ice
import cv2
import matplotlib.pyplot as plt
#obtain areas, contours, and coordinates
ara,cont,coord = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-10",display=True,areaMethod="area_LL2",retCnt=True,areaThresh=7000,cutOff=8000)
ara2,cont2,coord2 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-11",display=True,retCnt=True,areaMethod="area_LL2")
ara3,cont3,coord3 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-12",display=True,retCnt=True,areaThresh=7000,cutOff=8000,areaMethod="area_LL2")
ara4,cont4,coord4 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-13",display=True,retCnt=True,areaThresh=7000,cutOff=8000,areaMethod="area_LL2")
ara5,cont5,coord5 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-14",display=True,setThresh=100,retCnt=True,areaMethod="area_LL2")
ara6,cont6,coord6 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT_TRUE_2020-12-15",display=True,retCnt=True,areaMethod="area_LL2")
ara7,cont7,coord7 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-16",display=True,setThresh=215,retCnt=True,areaThresh=7000,cutOff=8000,areaMethod="area_LL2")
ara8,cont8,coord8 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-17",display=True,retCnt=True,areaMethod="area_LL2")
ara9,cont9,coord9 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT_TRUE_2020-12-18",display=True,retCnt=True,areaMethod="area_LL2")
ara10,cont10,coord10 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT_TRUE_2020-12-19",display=True,setThresh=222,retCnt=True,areaMethod="area_LL2")
ara11,cont11,coord11 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-20",display=True,retCnt=True,areaMethod="area_LL2")
ara12,cont12,coord12 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-21",display=True,setThresh=180,retCnt=True,areaThresh=7000,cutOff=8000,areaMethod="area_LL2")
ara13,cont13,coord13 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-22",display=True,retCnt=True,areaMethod="area_LL2")
ara14,cont14,coord14 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-23",display=True,setThresh=180,retCnt=True,areaMethod="area_LL2")
ara15,cont15,coord15 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-24",display=True,retCnt=True,areaMethod="area_LL2")
ara16,cont16,coord16 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-25",display=True,retCnt=True,areaMethod="area_LL2")
ara17,cont17,coord17 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-26",display=True,retCnt=True,areaMethod="area_LL2")
ara18,cont18,coord18 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-27",display=True,retCnt=True,areaThresh=7000,cutOff=8000,areaMethod="area_LL2")
ara19,cont19,coord19 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_NOAA_TRUE_2020-12-28",display=True,retCnt=True,areaMethod="area_LL2")
ara20,cont20,coord20 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-29",display=True,retCnt=True,areaMethod="area_LL2")
#ara21,cont21,coord21 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-30",display=True,retCnt=True,areaMethod="area_LL2") #too cloudy
#ara28,cont28,coord28 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-31",display=True,retCnt=True,areaMethod="area_LL2") #too cloudy
ara22,cont22,coord22 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2021-01-01",display=True,retCnt=True,areaMethod="area_LL2")
ara23,cont23,coord23 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_NOAA_TRUE_2021-01-02",display=True,retCnt=True,areaThresh=4000,cutOff=6000,areaMethod="area_LL2")
ara24,cont24,coord24 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_NOAA_TRUE_2021-01-03",display=True,retCnt=True,areaMethod="area_LL2")
ara25,cont25,coord25 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2021-01-04",display=True,areaThresh=4000,cutOff=6000,retCnt=True,areaMethod="area_LL2")
ara26,cont26,coord26 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2021-01-05",display=True,retCnt=True,areaMethod="area_LL2")
ara27,cont27,coord27 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2021-01-06",display=True,retCnt=True,areaMethod="area_LL2")


from xy2ll_area import ll_area
print(ll_area(coord))
print(ll_area(coord2))
print(ll_area(coord3))
print(ll_area(coord4))
print(ll_area(coord5))
print(ll_area(coord6))
print(ll_area(coord7))
print(ll_area(coord8))
print(ll_area(coord9))
print(ll_area(coord10))
print(ll_area(coord11))
print(ll_area(coord12))
print(ll_area(coord13))
print(ll_area(coord14))
print(ll_area(coord15))
print(ll_area(coord16))
print(ll_area(coord17))
print(ll_area(coord18))
print(ll_area(coord19))
print(ll_area(coord20))
#print(ll_area(coord21))
#print(ll_area(coord28))
print(ll_area(coord22))
print(ll_area(coord23))
print(ll_area(coord24))
print(ll_area(coord25))
print(ll_area(coord26))
print(ll_area(coord27))

area1 = ll_area(coord)
area2 = ll_area(coord2)
area3 = ll_area(coord3)
area4 = ll_area(coord4)
area5 = ll_area(coord5)
area6 = ll_area(coord6)
area7 = ll_area(coord7)
area8 = ll_area(coord8)
area9 = ll_area(coord9)
area10 = ll_area(coord10)
area11 = ll_area(coord11)
area12 = ll_area(coord12)
area13 = ll_area(coord13)
area14 = ll_area(coord14)
area15 = ll_area(coord15)
area16 = ll_area(coord16)
area17 = ll_area(coord17)
area18 = ll_area(coord18)
area19 = ll_area(coord19)
area20 = ll_area(coord20)
#area21 = ll_area(coord21)
#area22 = ll_area(coord28)
area23 = ll_area(coord22)
area24 = ll_area(coord23)
area25 = ll_area(coord24)
area26 = ll_area(coord25)
area27 = ll_area(coord26)
area28 = ll_area(coord27)

# importing the required module
import matplotlib.pyplot as plt
import pandas as pd
 
# x axis values
date = ['2020-12-10','2020-12-11','2020-12-12','2020-12-13','2020-12-14','2020-12-15','2020-12-16','2020-12-17','2020-12-18','2020-12-19','2020-12-20','2020-12-21','2020-12-22','2020-12-23','2020-12-24','2020-12-25','2020-12-26','2020-12-27','2020-12-28','2020-12-29','2021-01-01','2021-01-02','2021-01-03','2021-01-04','2021-01-05','2021-01-06']
date = pd.to_datetime(date)

# corresponding y axis values
data = [area1,area2,area3,area4,area5,area6,area7,area8,area9,area10,area11,area12,area13,area14,area15,area16,area17,area18,area19,area20,area23,area24,area25,area26,area27,area28]

DF = pd.DataFrame()
DF['value'] = data
DF = DF.set_index(date)
plt.plot(DF,marker='o', markerfacecolor='red', markersize=4)
plt.gcf().autofmt_xdate()
# plotting the points 
#plt.plot(x, y, marker='o', markerfacecolor='red', markersize=6000)
 
# naming the x axis
plt.xlabel('Date')
# naming the y axis
plt.ylabel('Area km2')
 
# giving a title to my graph
plt.title('Area')
 
# function to show the plot
plt.show()

#jump happened on 24th to 3019.5866808101655 km2 when bottom part of iceberg broke off
#some are overestimating area due to cloud coverage
