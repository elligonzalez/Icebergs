import ice
import pickle
import matplotlib.pyplot as plt

#~~~~~~~~~~~~~~~~~~~~~~~~~PIXEL COUNT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
results = []
with (open("a68a_pixel_areas2020.pkl", "rb")) as openfile: #open file
    while True:
        try:
            results.append(pickle.load(openfile))
        except EOFError:
            break

final = {k: v for k, v in results[0][0].items() if v >= 40000 and v <= 100000} #constrain data
print(len(list(final)))
final2 = {k: v for k, v in results[0][1].items() if v >= 76000 and v <= 100000}
print(len(list(final2)))
final3 = {k: v for k, v in results[0][2].items() if v >= 25000 and v <= 100000}
print(len(list(final3))
final4 = {k: v for k, v in results[0][3].items() if v >= 50000 and v <= 100000}
print(len(list(final4)))
final5 = {k: v for k, v in results[0][4].items() if v >= 50000 and v <= 100000}
print(len(list(final5)))
final6 = {k: v for k, v in results[0][5].items() if v <= 100000}
print(len(list(final4)))
final7 = {k: v for k, v in results[0][6].items() if v >= 25000 and v <= 100000}
print(len(list(final7)))

check = ice.getdates(final) #convert dates to date time objects
y = [j for i,j in check] #y values
x = [i for i,j in check] #x values
check2 = ice.getdates(final2)
y2 = [j for i,j in check2]
x2 = [i for i,j in check2]
check3 = ice.getdates(final3)
y3 = [j for i,j in check3]
x3 = [i for i,j in check3]
check4 = ice.getdates(final4)
y4 = [j for i,j in check4]
x4 = [i for i,j in check4]
check5 = ice.getdates(final5)
y5 = [j for i,j in check5]
x5 = [i for i,j in check5]
check6 = ice.getdates(final6)
y6 = [j for i,j in check6]
x6 = [i for i,j in check6]
check7 = ice.getdates(final7)
y7 = [j for i,j in check7]
x7 = [i for i,j in check7]

plt.style.use("seaborn") #plot
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x,y,color="red")
plt.title("Pixel Areas of A68a in 2020\n MODIS 367",pad=10)
plt.xlabel("Date (YYYY-MM)",labelpad=10)
plt.ylabel("Area (Pixels)",labelpad=10)
plt.xticks(rotation=45)
plt.subplots_adjust(left=0.1)
plt.show()

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x2,y2,c="#0000ff")
plt.title("Pixel Areas of A68a in 2020\n MODIS 721")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (Pixels)")
plt.xticks(rotation=45)
plt.show()

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x3,y3)
plt.title("Pixel Areas of A68a in 2020\n Aqua MODIS")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (Pixels)")
plt.xticks(rotation=45)
plt.show()

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x4,y4,c="#29995f")
plt.title("Pixel Areas of A68a in 2020\n Terra MODIS")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (Pixels)")
plt.xticks(rotation=45)
plt.show()

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x5,y5,c="#00a9bd")
plt.title("Pixel Areas of A68a in 2020\n VIIRS NOAA M11-I2-I1")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (Pixels)")
plt.xticks(rotation=45)
plt.show()

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x6,y6,c="#bd0075")
plt.title("Pixel Areas of A68a in 2020\n VIIRS NOAA")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (Pixels)")
plt.xticks(rotation=45)
plt.show()

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x7,y7,c="#bdb700")
plt.title("Pixel Areas of A68a in 2020\n VIIRS SNPP")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (Pixels)")
plt.xticks(rotation=45)
plt.show()

#~~~~~~~~~~~~~~~~~~~~~~~~~PS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
results1 = []
with (open("a68a_PS_areas2020.pkl", "rb")) as openfile:
    while True:
        try:
            results1.append(pickle.load(openfile))
        except EOFError:
            break 
final = {k: v for k, v in results1[0][0].items() if v >= 3500 and v <= 7500}
print(len(list(final)))
final2 = {k: v for k, v in results1[0][1].items() if v >= 3500 and v <= 7500}
print(len(list(final2)))
final3 = {k: v for k, v in results1[0][2].items() if v >= 3500 and v <= 7500}
print(len(list(final3)))
final4 = {k: v for k, v in results1[0][3].items() if v >= 3500 and v <= 7500}
print(len(list(final4)))
final5 = {k: v for k, v in results1[0][4].items() if v >= 3500 and v <= 7500}
print(len(list(final5)))
final6 = {k: v for k, v in results1[0][5].items() if v >= 3500 and v <= 7500}
print(len(list(final4)))
final7 = {k: v for k, v in results1[0][6].items() if v >= 3500 and v <= 7500}
print(len(list(final7)))
      
check = ice.getdates(final)
y = [j for i,j in check]
x = [i for i,j in check]
check2 = ice.getdates(final2)
y2 = [j for i,j in check2]
x2 = [i for i,j in check2]
check3 = ice.getdates(final3)
y3 = [j for i,j in check3]
x3 = [i for i,j in check3]
check4 = ice.getdates(final4)
y4 = [j for i,j in check4]
x4 = [i for i,j in check4]
check5 = ice.getdates(final5)
y5 = [j for i,j in check5]
x5 = [i for i,j in check5]
check6 = ice.getdates(final6)
y6 = [j for i,j in check6]
x6 = [i for i,j in check6]
check7 = ice.getdates(final7)
y7 = [j for i,j in check7]
x7 = [i for i,j in check7]

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x,y,label="MODIS 367",color="red")
plt.legend()
plt.title("Area Estimates of A68a in 2020 Using Polar Stereographic Coordinates\n (Red)")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (km^2)")
plt.xticks(rotation=45)
plt.ylim(3000, 8000)

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x2,y2,label="MODIS 721",c="#0000ff")
plt.scatter(x5,y5,label="VIIRS NOAA M11-I2-I1",c="#00a9bd")
plt.legend()
plt.title("Area Estimates of A68a in 2020 Using Polar Stereographic Coordinates\n (Blue)")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (km^2)")
plt.xticks(rotation=45)
plt.ylim(3000, 8000)

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x3,y3,label="Aqua MODIS")
plt.scatter(x4,y4,label="Terra MODIS",c="#29995f")
plt.legend()
plt.title("Area Estimates of A68a in 2020 Using Polar Stereographic Coordinates\n (True Color)")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (km^2)")
plt.xticks(rotation=45)
plt.ylim(3000, 8000)

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x6,y6,label="VIIRS NOAA",c="#bd0075")
plt.scatter(x7,y7,label="VIIRS SNPP",c="#bdb700")
plt.legend()
plt.title("Area Estimates of A68a in 2020 Using Polar Stereographic Coordinates\n (True Color)")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (km^2)")
plt.xticks(rotation=45)
plt.ylim(3000, 8000)
      
#~~~~~~~~~~~~~~~~~~~~~~~~~LL~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       
results2 = []
with (open("a68a_LL_areas2020.pkl", "rb")) as openfile:
    while True:
        try:
            results2.append(pickle.load(openfile))
        except EOFError:
            break      
final = {k: v for k, v in results2[0][0].items() if v >= 3500 and v <= 7500}
print(len(list(final)))
final2 = {k: v for k, v in results2[0][1].items() if v >= 3500 and v <= 7500}
print(len(list(final2)))
final3 = {k: v for k, v in results2[0][2].items() if v >= 3500 and v <= 7500}
print(len(list(final3)))
final4 = {k: v for k, v in results2[0][3].items() if v >= 3500 and v <= 7500}
print(len(list(final4)))
final5 = {k: v for k, v in results2[0][4].items() if v >= 3500 and v <= 7500}
print(len(list(final5)))
final6 = {k: v for k, v in results2[0][5].items() if v >= 3500 and v <= 7500}
print(len(list(final4)))
final7 = {k: v for k, v in results2[0][6].items() if v >= 3500 and v <= 7500}
print(len(list(final7)))      
      
check = ice.getdates(final)
y = [j for i,j in check]
x = [i for i,j in check]
check2 = ice.getdates(final2)
y2 = [j for i,j in check2]
x2 = [i for i,j in check2]
check3 = ice.getdates(final3)
y3 = [j for i,j in check3]
x3 = [i for i,j in check3]
check4 = ice.getdates(final4)
y4 = [j for i,j in check4]
x4 = [i for i,j in check4]
check5 = ice.getdates(final5)
y5 = [j for i,j in check5]
x5 = [i for i,j in check5]
check6 = ice.getdates(final6)
y6 = [j for i,j in check6]
x6 = [i for i,j in check6]
check7 = ice.getdates(final7)
y7 = [j for i,j in check7]
x7 = [i for i,j in check7]

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x,y,label="MODIS 367",color="red")
plt.legend()
plt.title("Area Estimates of A68a in 2020 Using Lat Lon Coordinates\n (Red)")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (km^2)")
plt.xticks(rotation=45)
plt.ylim(3000, 8000)

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x2,y2,label="MODIS 721",c="#0000ff")
plt.scatter(x5,y5,label="VIIRS NOAA M11-I2-I1",c="#00a9bd")
plt.legend()
plt.title("Area Estimates of A68a in 2020 Using Lat Lon Coordinates\n (Blue)")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (km^2)")
plt.xticks(rotation=45)
plt.ylim(3000, 8000)

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x3,y3,label="Aqua MODIS")
plt.scatter(x4,y4,label="Terra MODIS",c="#29995f")
plt.legend()
plt.title("Area Estimates of A68a in 2020 Using Lat Lon Coordinates\n (True Color)")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (km^2)")
plt.xticks(rotation=45)
plt.ylim(3000, 8000)

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x6,y6,label="VIIRS NOAA",c="#bd0075")
plt.scatter(x7,y7,label="VIIRS SNPP",c="#bdb700")
plt.legend()
plt.title("Area Estimates of A68a in 2020 Using Lat Lon Coordinates\n (True Color)")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (km^2)")
plt.xticks(rotation=45)
plt.ylim(3000, 8000)
      
#~~~~~~~~~~~~~~~~~~~~~~~~~LL2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~               
results3 = []
with (open("a68a_LL2_areas2020.pkl", "rb")) as openfile:
    while True:
        try:
            results3.append(pickle.load(openfile))
        except EOFError:
            break
      
final = {k: v for k, v in results3[0][0].items() if v >= 3500 and v <= 7500}
print(len(list(final)))
final2 = {k: v for k, v in results3[0][1].items() if v >= 3500 and v <= 7500}
print(len(list(final2)))
final3 = {k: v for k, v in results3[0][2].items() if v >= 3500 and v <= 7500}
print(len(list(final3)))
final4 = {k: v for k, v in results3[0][3].items() if v >= 3500 and v <= 7500}
print(len(list(final4)))
final5 = {k: v for k, v in results3[0][4].items() if v >= 3500 and v <= 7500}
print(len(list(final5)))
final6 = {k: v for k, v in results3[0][5].items() if v >= 3500 and v <= 7500}
print(len(list(final4)))
final7 = {k: v for k, v in results3[0][6].items() if v >= 3500 and v <= 7500}
print(len(list(final7)))

check = ice.getdates(final)
y = [j for i,j in check]
x = [i for i,j in check]
check2 = ice.getdates(final2)
y2 = [j for i,j in check2]
x2 = [i for i,j in check2]
check3 = ice.getdates(final3)
y3 = [j for i,j in check3]
x3 = [i for i,j in check3]
check4 = ice.getdates(final4)
y4 = [j for i,j in check4]
x4 = [i for i,j in check4]
check5 = ice.getdates(final5)
y5 = [j for i,j in check5]
x5 = [i for i,j in check5]
check6 = ice.getdates(final6)
y6 = [j for i,j in check6]
x6 = [i for i,j in check6]
check7 = ice.getdates(final7)
y7 = [j for i,j in check7]
x7 = [i for i,j in check7]

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x,y,label="MODIS 367",color="red")
plt.legend()
plt.title("Area Estimates of A68a in 2020 Using Flipped Lat Lon Coordinates\n (Red)")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (km^2)")
plt.xticks(rotation=45)
plt.ylim(3000, 8000)

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x2,y2,label="MODIS 721",c="#0000ff")
plt.scatter(x5,y5,label="VIIRS NOAA M11-I2-I1",c="#00a9bd")
plt.legend()
plt.title("Area Estimates of A68a in 2020 Using Flipped Lat Lon Coordinates\n (Blue)")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (km^2)")
plt.xticks(rotation=45)
plt.ylim(3000, 8000)

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x3,y3,label="Aqua MODIS")
plt.scatter(x4,y4,label="Terra MODIS",c="#29995f")
plt.legend()
plt.title("Area Estimates of A68a in 2020 Using Flipped Lat Lon Coordinates\n (True Color)")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (km^2)")
plt.xticks(rotation=45)
plt.ylim(3000, 8000)

plt.style.use("seaborn")
plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(x6,y6,label="VIIRS NOAA",c="#bd0075")
plt.scatter(x7,y7,label="VIIRS SNPP",c="#bdb700")
plt.legend()
plt.title("Area Estimates of A68a in 2020 Using Flipped Lat Lon Coordinates\n (True Color)")
plt.xlabel("Date (YYYY-MM)")
plt.ylabel("Area (km^2)")
plt.xticks(rotation=45)
plt.ylim(3000, 8000)
