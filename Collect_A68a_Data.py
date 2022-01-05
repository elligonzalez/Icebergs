import ice
import pickle
import matplotlib.pyplot as plt

#~~~~~~~~~~~~~~~~~~~~~~~~~PIXEL COUNT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pix367 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT367_2020-*",layerName="red") #process
pix721 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT721_2020-*",layerName="blue")
pixA = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-*")
pixT = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT_TRUE_2020-*")
pixM = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_NOAA_M11I2I1_2020-*",layerName="blue")
pixN = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_NOAA_TRUE_2020-*")
pixS = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_SNPP_TRUE_2020-*")
print('done')

a68a_pixel_areas2020 = [] #pickle dump
a68a_pixel_areas2020.extend([pix367,pix721,pixA,pixT,pixM,pixN,pixS])
with open('a68a_pixel_areas2020.pkl', 'wb') as outfile:
    pickle.dump(a68a_pixel_areas2020, outfile, pickle.HIGHEST_PROTOCOL)
            
print('367\n') #stats
ice.iceStats(pix367.values())
print('721\n')
ice.iceStats(pix721.values())
print('AQU\n')
ice.iceStats(pixA.values())
print('TER\n')
ice.iceStats(pixT.values())
print('M11\n')
ice.iceStats(pixM.values())
print('NOAA\n')
ice.iceStats(pixN.values())
print('SNPP\n')
ice.iceStats(pixS.values())

#~~~~~~~~~~~~~~~~~~~~~~~~~PS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
p_1 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT367_2020-*",layerName="red",areaMethod="area_PS")
p_2 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT721_2020-*",layerName="blue",areaMethod="area_PS")
p_3 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-*",areaMethod="area_PS")
p_4 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT_TRUE_2020-*",areaMethod="area_PS")
p_5 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_NOAA_M11I2I1_2020-*",layerName="blue",areaMethod="area_PS")
p_6 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_NOAA_TRUE_2020-*",areaMethod="area_PS")
p_7 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_SNPP_TRUE_2020-*",areaMethod="area_PS")

print('MOD367_2020\n')
ice.iceStats(p_1.values())
print('MODT721_2020\n')
ice.iceStats(p_2.values())
print('MODA_2020\n')
ice.iceStats(p_3.values())
print('MODT_2020\n')
ice.iceStats(p_4.values())
print('VIR_NOAA_M11I2I1_2020\n')
ice.iceStats(p_5.values())
print('VIR_NOAA_2020\n')
ice.iceStats(p_6.values())
print('VIR_SNPP_2020\n')
ice.iceStats(p_7.values())

rp_1 = ice.findtooLarge(p_1) #reprocess
rdp_1 = ice.ice_olate(rp_1,layerName="red",areaMethod="area_PS",areaThresh=7000,cutOff=8000)
p_1.update(rdp_1)
print('MOD367_2020\n')
ice.iceStats(p_1.values())

rp_2 = ice.findtooLarge(p_2)
rdp_2 = ice.ice_olate(rp_2,layerName="blue",areaMethod="area_PS",areaThresh=7000,cutOff=8000)
p_2.update(rdp_2)
print('MODT721_2020\n')
ice.iceStats(p_2.values())

rp_3 = ice.findtooLarge(p_3)
rdp_3 = ice.ice_olate(rp_3,areaMethod="area_PS",areaThresh=7000,cutOff=8000)
p_3.update(rdp_3)
print('MODA_2020\n')
ice.iceStats(p_3.values())

rp_4 = ice.findtooLarge(p_4)
rdp_4 = ice.ice_olate(rp_4,areaMethod="area_PS",areaThresh=7000,cutOff=8000)
p_4.update(rdp_4)
print('MODT_2020\n')
ice.iceStats(p_4.values())

rp_5 = ice.findtooLarge(p_5)
rdp_5 = ice.ice_olate(rp_5,layerName="blue",areaMethod="area_PS",areaThresh=7000,cutOff=8000)
p_5.update(rdp_5)
print('VIR_NOAA_M11I2I1_2020\n')
ice.iceStats(p_5.values())

rp_6 = ice.findtooLarge(p_6)
rdp_6 = ice.ice_olate(rp_6,areaMethod="area_PS",areaThresh=7000,cutOff=8000)
p_6.update(rdp_6)
print('VIR_NOAA_2020\n')
ice.iceStats(p_6.values())

rp_7 = ice.findtooLarge(p_7)
rdp_7 = ice.ice_olate(rp_7,areaMethod="area_PS",areaThresh=7000,cutOff=8000)
p_7.update(rdp_7)
print('VIR_SNPP_2020\n')
ice.iceStats(p_7.values())

a68a_PS_areas2020= []
a68a_PS_areas2020.extend([p_1,p_2,p_3,p_4,p_5,p_6,p_7])
with open('a68a_PS_areas2020.pkl', 'wb') as outfile:
    pickle.dump(a68a_PS_areas2020, outfile, pickle.HIGHEST_PROTOCOL)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~LL~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
l_1 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT367_2020-*",layerName="red",areaMethod="area_LL")
l_2 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT721_2020-*",layerName="blue",areaMethod="area_LL")
l_3 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-*",areaMethod="area_LL")
l_4 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT_TRUE_2020-*",areaMethod="area_LL")
l_5 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_NOAA_M11I2I1_2020-*",layerName="blue",areaMethod="area_LL")
l_6 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_NOAA_TRUE_2020-*",areaMethod="area_LL")
l_7 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_SNPP_TRUE_2020-*",areaMethod="area_LL")

print('MOD367_2020\n')
ice.iceStats(l_1.values())
print('MODT721_2020\n')
ice.iceStats(l_2.values())
print('MODA_2020\n')
ice.iceStats(l_3.values())
print('MODT_2020\n')
ice.iceStats(l_4.values())
print('VIR_NOAA_M11I2I1_2020\n')
ice.iceStats(l_5.values())
print('VIR_NOAA_2020\n')
ice.iceStats(l_6.values())
print('VIR_SNPP_2020\n')
ice.iceStats(l_7.values())

rl_1 = ice.findtooLarge(l_1)
rdl_1 = ice.ice_olate(rl_1,layerName="red",areaMethod="area_LL",areaThresh=7000,cutOff=8000)
l_1.update(rdl_1)
print('MOD367_2020\n')
ice.iceStats(l_1.values())

rl_2 = ice.findtooLarge(l_2)
rdl_2 = ice.ice_olate(rl_2,layerName="blue",areaMethod="area_LL",areaThresh=7000,cutOff=8000)
l_2.update(rdl_2)
print('MODT721_2020\n')
ice.iceStats(l_2.values())


rl_3 = ice.findtooLarge(l_3)
rdl_3 = ice.ice_olate(rl_3,areaMethod="area_LL",areaThresh=7000,cutOff=8000)
l_3.update(rdl_3)
print('MODA_2020\n')
ice.iceStats(l_3.values())


rl_4 = ice.findtooLarge(l_4)
rdl_4 = ice.ice_olate(rl_4,areaMethod="area_LL",areaThresh=7000,cutOff=8000)
l_4.update(rdl_4)
print('MODT_2020\n')
ice.iceStats(l_4.values())


rl_5 = ice.findtooLarge(l_5)
rdl_5 = ice.ice_olate(rl_5,layerName="blue",areaMethod="area_LL",areaThresh=7000,cutOff=8000)
l_5.update(rdl_5)
print('VIR_NOAA_M11I2I1_2020\n')
ice.iceStats(l_5.values())


rl_6 = ice.findtooLarge(l_6)
rdl_6 = ice.ice_olate(rl_6,areaMethod="area_LL",areaThresh=7000,cutOff=8000)
l_6.update(rdl_6)
print('VIR_NOAA_2020\n')
ice.iceStats(l_6.values())

rl_7 = ice.findtooLarge(l_7)
rdl_7 = ice.ice_olate(rl_7,areaMethod="area_LL",areaThresh=7000,cutOff=8000)
l_7.update(rdl_7)
print('VIR_SNPP_2020\n')
ice.iceStats(l_7.values())

a68a_LL_areas2020= []
a68a_LL_areas2020.extend([l_1,l_2,l_3,l_4,l_5,l_6,l_7])
with open('a68a_LL_areas2020.pkl', 'wb') as outfile:
    pickle.dump(a68a_LL_areas2020, outfile, pickle.HIGHEST_PROTOCOL)

#~~~~~~~~~~~~~~~~~~~~~~~~~LL2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ll_1 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT367_2020-*",layerName="red",areaMethod="area_LL2")
ll_2 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT721_2020-*",layerName="blue",areaMethod="area_LL2")
ll_3 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODA_TRUE_2020-*",areaMethod="area_LL2")
ll_4 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/MODT_TRUE_2020-*",areaMethod="area_LL2")
ll_5 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_NOAA_M11I2I1_2020-*",layerName="blue",areaMethod="area_LL2")
ll_6 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_NOAA_TRUE_2020-*",areaMethod="area_LL2")
ll_7 = ice.ice_olate(r"/nbhome/Nuzhat.Khan/a68/a68a/VIR_SNPP_TRUE_2020-*",areaMethod="area_LL2")

print('MOD367_2020\n')
ice.iceStats(ll_1.values())
print('MODT721_2020\n')
ice.iceStats(ll_2.values())
print('MODA_2020\n')
ice.iceStats(ll_3.values())
print('MODT_2020\n')
ice.iceStats(ll_4.values())
print('VIR_NOAA_M11I2I1_2020\n')
ice.iceStats(ll_5.values())
print('VIR_NOAA_2020\n')
ice.iceStats(ll_6.values())
print('VIR_SNPP_2020\n')
ice.iceStats(ll_7.values())

rll_1 = ice.findtooLarge(ll_1)
rdll_1 = ice.ice_olate(rll_1,layerName="red",areaMethod="area_LL2",areaThresh=7000,cutOff=8000)
ll_1.update(rdll_1)
print('MOD367_2020\n')
ice.iceStats(ll_1.values())

rll_2 = ice.findtooLarge(ll_2)
rdll_2 = ice.ice_olate(rll_2,layerName="blue",areaMethod="area_LL2",areaThresh=7000,cutOff=8000)
ll_2.update(rdll_2)
print('MODT721_2020\n')
ice.iceStats(ll_2.values())


rll_3 = ice.findtooLarge(ll_3)
rdll_3 = ice.ice_olate(rll_3,areaMethod="area_LL2",areaThresh=7000,cutOff=8000)
ll_3.update(rdll_3)
print('MODA_2020\n')
ice.iceStats(ll_3.values())


rll_4 = ice.findtooLarge(ll_4)
rdll_4 = ice.ice_olate(rll_4,areaMethod="area_LL2",areaThresh=7000,cutOff=8000)
ll_4.update(rdll_4)
print('MODT_2020\n')
ice.iceStats(ll_4.values())


rll_5 = ice.findtooLarge(ll_5)
rdll_5 = ice.ice_olate(rll_5,layerName="blue",areaMethod="area_LL2",areaThresh=7000,cutOff=8000)
ll_5.update(rdll_5)
print('VIR_NOAA_M11I2I1_2020\n')
ice.iceStats(ll_5.values())


rll_6 = ice.findtooLarge(ll_6)
rdll_6 = ice.ice_olate(rll_6,areaMethod="area_LL2",areaThresh=7000,cutOff=8000)
ll_6.update(rdll_6)
print('VIR_NOAA_2020\n')
ice.iceStats(ll_6.values())

rll_7 = ice.findtooLarge(ll_7)
rdll_7 = ice.ice_olate(rll_7,areaMethod="area_LL2",areaThresh=7000,cutOff=8000)
ll_7.update(rdll_7)
print('VIR_SNPP_2020\n')
ice.iceStats(ll_7.values())

a68a_LL2_areas2020= []
a68a_LL2_areas2020.extend([ll_1,ll_2,ll_3,ll_4,ll_5,ll_6,ll_7])
with open('a68a_LL2_areas2020.pkl', 'wb') as outfile:
    pickle.dump(a68a_LL2_areas2020, outfile, pickle.HIGHEST_PROTOCOL)
