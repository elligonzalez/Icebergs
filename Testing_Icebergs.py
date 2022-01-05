import rasterio
import sys
from rasterio.plot import show
from rasterio.plot import show_hist
from rasterio.mask import mask
from pyproj import transformer
from pyproj import Transformer
import cv2
import numpy as np
np.set_printoptions(threshold=False)
import matplotlib.pyplot as plt
import glob
import ice

#from shapely.geometry import box
#np.set_printoptions(threshold=sys.maxsize)

#exploring rasterio
img = rasterio.open('/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-10')
show(img)
print(img.lnglat())
transformer = Transformer.from_crs("epsg:4326", "epsg:3031") 
x,y = transformer.transform(-67.95899999999989,-60.814) #convert lat/lon to polar stereographic
print(x,y)
print(img.transform * (img.width//2, img.height//2))
print(rasterio.transform.xy(img.transform, 100, 100, offset='center'))

#brightest pixel
img = cv2.imread('/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-12-10')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
print(maxLoc)
cv2.circle(img, maxLoc, 5, (255, 0, 0), 2)
plt.imshow(gray, cmap="gray")
plt.show()
plt.imshow(img)
plt.show()

#masking
white = np.array([255,255,255])
nonWhite = np.array([200,200,200])
img_mask = cv2.inRange(img,nonWhite,white)
masked_img = cv2.bitwise_and(img,img,mask=img_mask)
plt.imshow(masked_img)
plt.show()

#canny edge detector
edges2 = cv2.Canny(masked_img, threshold1=200, threshold2=500)
plt.imshow(edges2,cmap="gray")
plt.show()

#contour detector
contours, hierarchy = cv2.findContours(edges2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
imgcv = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
plt.imshow(img)
plt.show()

#effect of rotation
img = rasterio.open(r"/nbhome/Nuzhat.Khan/b15/b15aa/MODA_TRUE_2018-12-01")
show(img)
imgcv = cv2.imread(r"/nbhome/Nuzhat.Khan/b15/b15aa/MODA_TRUE_2018-12-01")
print(img.width//2, img.height//2) 

#setting rectangle points
cv2.circle(imgcv, (400,400), 5, (255, 0, 0), 2) #top left
cv2.circle(imgcv, (800,400), 5, (0, 0, 0), 2) #top right
cv2.circle(imgcv, (800,600), 5, (255, 0, 255), 2) #bottom right
cv2.circle(imgcv, (400,600), 5, (0, 255, 0), 2) #bottom left
plt.imshow(imgcv)
plt.show()
    
L=[[400,400],[800,400],[800,600],[400,600]] #transform to ps coordinates
temp = []
for i in L:
    temp.append(img.transform*(i[1],i[0]))
    #print(img.transform*(i[0],i[1]))
    print(temp)
ctr = np.array(L).reshape((-1,1,2)).astype(np.int32) #draw rectangle
cv2.drawContours(imgcv,[ctr],0,(255,0,0),5)
plt.imshow(imgcv)
plt.show()
# 400,400   (-1763870.3020877556, 2152395.3077464285)   latlon(-64.786432,129.334337) top left
# 800,400   (-1661481.2235894622, 2152395.3077464285)          -65.346801,127.665339 top right
# 800,600   (-1661481.2235894622, 2101200.7684972817)          -65.702043,128.334459 bottom right
# 400,600   (-1763870.3020877556, 2101200.7684972817)          -65.132695,130.012055 bottom left

# 400,400   (-1763870.3020877556, 2152395.3077464285)   latlon(-64.786432,129.334337) top left
# 800,400   (-1763870.3020877556, 2050006.2292481351)          -65.475925,130.709425 top right
# 800,600   (-1712675.762838609, 2050006.2292481351)           -65.767568,129.877037 bottom right
# 400,600   (-1712675.762838609, 2152395.3077464285)           -65.069035,128.509508 bottom left

wd = 2152395.3077464285-2050006.2292481351 #calculate area
print(wd)
ht = -1712675.762838609+1763870.3020877556
print(ht)
print((ht*wd)/1e+6)

def calca(cntr): #for transformation
    temp = []
    for i in cntr:
        temp.append(img.transform*(i[0][1],i[0][0]))
    print(temp)

#following functions taken from: https://medium.com/analytics-vidhya/tutorial-how-to-scale-and-rotate-contours-in-opencv-using-python-f48be59c35a2
def cart2pol(x, y):
    theta = np.arctan2(y, x)
    rho = np.hypot(x, y)
    return theta, rho

def pol2cart(theta, rho):
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    return x, y

def rotate_contour(cnt, angle):
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cnt_norm = cnt - [cx, cy]
    
    coordinates = cnt_norm[:, 0, :]
    xs, ys = coordinates[:, 0], coordinates[:, 1]
    thetas, rhos = cart2pol(xs, ys)
    
    thetas = np.rad2deg(thetas)
    thetas = (thetas + angle) % 360
    thetas = np.deg2rad(thetas)
    
    xs, ys = pol2cart(thetas, rhos)
    
    cnt_norm[:, 0, 0] = xs
    cnt_norm[:, 0, 1] = ys

    cnt_rotated = cnt_norm + [cx, cy]
    cnt_rotated = cnt_rotated.astype(np.int32)

    return cnt_rotated

ps_to_latlon = [] #transform to lat lon coordinates
transformer = Transformer.from_crs("epsg:3031","epsg:4326") 
for i in temp:
    (x,y) = transformer.transform(i[1],i[0])
    ps_to_latlon.append((x,y))
print(ps_to_latlon)

ara = ice.area_LL(ctr,"/nbhome/Nuzhat.Khan/b15/b15aa/MODA_TRUE_2018-12-01") #area calculated by functions
print(ara)
ps_ara = ice.area_PS(ctr,"/nbhome/Nuzhat.Khan/b15/b15aa/MODA_TRUE_2018-12-01")
print(ps_ara)

cnt_rotated = rotate_contour(ctr, 60) #rotate rectangle
cv2.drawContours(imgcv,[cnt_rotated],0,(255,0,0),5)
plt.imshow(imgcv)
plt.show()
print(cnt_rotated) #get rotated points

#confirm the points create the rotated rectangle
cv2.circle(imgcv, (587,277), 5, (0, 255, 0), 5) #top left
cv2.circle(imgcv, (786 ,623), 5, (0, 0, 0), 5) #top right
cv2.circle(imgcv, (613, 723), 5, (0,255, 255), 5) #bottom right
cv2.circle(imgcv, (414 ,377), 5, (255, 0, 255), 5) #bottom left
plt.imshow(imgcv)
plt.show()

calca(cnt_rotated) #tranform rotated points
ht = 102170.30809 #calculatorsoup
wd = 51149.083916
print((ht*wd)/1e+6)

ara2 = ice.area_LL(cnt_rotated,"/nbhome/Nuzhat.Khan/b15/b15aa/MODA_TRUE_2018-12-01")
print(ara2)
psara = ice.area_PS(cnt_rotated,"/nbhome/Nuzhat.Khan/b15/b15aa/MODA_TRUE_2018-12-01")
print(psara)

cnt_rotated2 = rotate_contour(ctr, 45)
cv2.drawContours(imgcv,[cnt_rotated2],0,(0,0,0),5)
print(cnt_rotated2)
cv2.circle(imgcv, (530 ,288), 5, (0, 255, 0), 5) #top left
cv2.circle(imgcv, (812 ,570), 5, (255, 255, 255), 5) #top right
cv2.circle(imgcv, (670 ,712), 5, (0,255, 255), 5) #bottom right
cv2.circle(imgcv, (388 ,430), 5, (255, 0, 255), 5) #bottom left
plt.imshow(imgcv)
plt.show()
calca(cnt_rotated2)
ht=102084.016533
wd=51404.008325
print((ht*wd)/1e+6)

ara3 = ice.area_LL(cnt_rotated2,"/nbhome/Nuzhat.Khan/b15/b15aa/MODA_TRUE_2018-12-01")
print(ara3)
psara3 = ice.area_PS(cnt_rotated2,"/nbhome/Nuzhat.Khan/b15/b15aa/MODA_TRUE_2018-12-01")
print(psara3)

cnt_rotated3 = rotate_contour(ctr, 90)
cv2.drawContours(imgcv,[cnt_rotated3],0,(0,255,255),5)
print(cnt_rotated3)
cv2.circle(imgcv, (699 ,300), 5, (0, 255, 0), 5) #top left
cv2.circle(imgcv, (700, 700), 5, (255, 25, 25), 5) #top right
cv2.circle(imgcv, (500 ,700), 5, (0,0, 0), 5) #bottom right
cv2.circle(imgcv, (500 ,301), 5, (255, 0, 255), 5) #bottom left
plt.imshow(imgcv)
plt.show()
calca(cnt_rotated3)
print((102389.398464*50939.209696)/1e+6)

ara4 = ice.area_LL(cnt_rotated3,"/nbhome/Nuzhat.Khan/b15/b15aa/MODA_TRUE_2018-12-01")
print(ara4)
psara4 = ice.area_PS(cnt_rotated3,"/nbhome/Nuzhat.Khan/b15/b15aa/MODA_TRUE_2018-12-01")
print(psara4)

print(cv2.contourArea(ctr)) #pixel count
print(cv2.contourArea(cnt_rotated))
print(cv2.contourArea(cnt_rotated))
print(cv2.contourArea(cnt_rotated))

#results
"""
Cnt     Rotated         True (km2)       Calculated latlon (km2)     Ratios(latlon/true)   Calculated ps (km2)    Ratio (ps/true)   Pixel Count
-------------------------------------------------------------------------------------------------------------------------------------------------------
0                  5241.761697864833       9237.79269338202             1.762                  5247.52763571177        1.001        80000

                   
1        60        5225.917662218984       9212.648151867477            1.763                  5225.905368728831       1.0          79758 
2        45        5247.52763571177        9251.707398128856            1.763                  5247.527635732518       1.0          79758
3        90        5215.6350390049965      9205.539031330292            1.765                  5222.137852508482       1.001        79758

"""

#triangle ∆
imgcv = cv2.imread(r"/nbhome/Nuzhat.Khan/b15/b15aa/MODT367_2018-02-11")
plt.imshow(imgcv)
plt.show()

cv2.circle(imgcv, (200,800), 5, (255, 0, 0), 2) #top left
cv2.circle(imgcv, (600,600), 5, (0, 255, 0), 2) #top right
cv2.circle(imgcv, (800,800), 5, (255, 0, 255), 2) #bottom right
plt.imshow(imgcv)
plt.show()

img = rasterio.open(r"/nbhome/Nuzhat.Khan/b15/b15aa/MODT367_2018-02-11")
L=[[200,800],[800,600],[800,800]]
temp = []
for i in L:
    temp.append(img.transform*(i[1],i[0]))
    #print(img.transform*(i[0],i[1]))
print(temp)
ctr = np.array(L).reshape((-1,1,2)).astype(np.int32)
cv2.drawContours(imgcv,[ctr],0,(255,0,0),5)
plt.imshow(imgcv)
plt.show()

base = 153583.617747
ht = 51194.539249
print(((base*ht)/2)/1e+6)

cnt_rotated = rotate_contour(ctr, 60)
cnt_rotated2 = rotate_contour(ctr, 45)
cnt_rotated3 = rotate_contour(ctr, 90)

cv2.drawContours(imgcv,[cnt_rotated],0,(0,255,0),5)
cv2.drawContours(imgcv,[cnt_rotated2],0,(255,0,255),5)
cv2.drawContours(imgcv,[cnt_rotated3],0,(255,255,0),5)
plt.imshow(imgcv)
plt.show()

calca(cnt_rotated)
calca(cnt_rotated2)
calca(cnt_rotated3)

print(((153097.567068*51370.856785)/2)/1e+6)
print(((153307.131677* 51042.008267)/2)/1e+6)
print(((153327.858718*50938.566553)/2)/1e+6)

ara = ice.area_LL(ctr,"/nbhome/Nuzhat.Khan/b15/b15aa/MODT367_2018-02-11")
print(ara)
ara2 = ice.area_LL(cnt_rotated,"/nbhome/Nuzhat.Khan/b15/b15aa/MODT367_2018-02-11")
print(ara2)
ara3 = ice.area_LL(cnt_rotated2,"/nbhome/Nuzhat.Khan/b15/b15aa/MODT367_2018-02-11")
print(ara3)
ara4 = ice.area_LL(cnt_rotated3,"/nbhome/Nuzhat.Khan/b15/b15aa/MODT367_2018-02-11")
print(ara4)
psara = ice.area_PS(ctr,"/nbhome/Nuzhat.Khan/b15/b15aa/MODT367_2018-02-11")
print(psara)
psara2 = ice.area_PS(cnt_rotated,"/nbhome/Nuzhat.Khan/b15/b15aa/MODT367_2018-02-11")
print(psara2)
psara3 = ice.area_PS(cnt_rotated2,"/nbhome/Nuzhat.Khan/b15/b15aa/MODT367_2018-02-11")
print(psara3)
psara4 = ice.area_PS(cnt_rotated3,"/nbhome/Nuzhat.Khan/b15/b15aa/MODT367_2018-02-11")
print(psara4)

print(round((12833.307310302918/3931.3212733761025),3))
print(round((12581.164840337127/3932.3765959910806),3))
print(round((12697.319683940934/3912.5519412237454),3))
print(round((12343.93797767099/3905.150667867912),3))

print(cv2.contourArea(ctr))
print(cv2.contourArea(cnt_rotated))
print(cv2.contourArea(cnt_rotated))
print(cv2.contourArea(cnt_rotated))

"""
Cnt     Rotated         True (km2)          Calculated latlon (km2)    Ratios (latlon/true)   Calculated ps (km2)     Ratios (ps/true)   Pixel Count
----------------------------------------------------------------------------------------------------------------------------------------------------
0                  3931.3212733761025       12833.307310302918          3.264                 3931.321273398637      1                   60000

                   
1        60        3932.3765959910806       12581.164840337127          3.199                 3932.369625738216      1                   60016
2        45        3912.5519412237454       12697.319683940934          3.245                 3912.549214318166      1                   60016
3        90        3905.150667867912        12343.93797767099           3.161                 3905.1452259199236     1                   60016

"""

#ellipse Ó
imgcv2 = cv2.imread(r"/nbhome/Nuzhat.Khan/b15/b15aa/MODT367_2018-02-11")
img2 = rasterio.open(r"/nbhome/Nuzhat.Khan/b15/b15aa/MODT367_2018-02-11")
cv2.ellipse(imgcv2,(256, 256),(100, 50), 0, 0,360, (0, 255, 0),5)
plt.imshow(imgcv2)
plt.show()

cv2.circle(imgcv2, (256,256), 5, (255, 0, 0), 8) #top left
cv2.circle(imgcv2, (256,306), 5, (255, 0, 255), 8) #top left
cv2.circle(imgcv2, (356,256), 5, (255, 255, 0), 8) #top left
plt.imshow(imgcv2)
plt.show()

temp=[]
for i in ((256,256),(256,306),(356,256)):
    temp.append(img2.transform*(i[1],i[0]))
print(temp)

a= 25597.269625
b= 12798.634812

cv2.ellipse(imgcv2,(256, 256),(100, 50), 45, 0,360, (0, 255, 0),5)
# cv2.ellipse(imgcv2,(256, 256),(100, 50), 60, 0,360, (255, 0, 0),5)
# cv2.ellipse(imgcv2,(256, 256),(100, 50), 90, 0,360, (255, 0, 255),5)
plt.imshow(imgcv2)
plt.show()
