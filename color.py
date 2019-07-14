import json
import numpy as np
from PIL import Image, ImageDraw
IMG_PATH = "./zaihou.jpg"
im01 = Image.open(IMG_PATH)
width, height = im01.size
newIm= Image.new('RGB', (width, height), 'red')
def fillcolor(label):
    if label=='0':
        temp=(255, 0, 0)
    elif label=='1':
        temp=(0,0,255)
    elif label=='2':
        temp=(0,255,0)
    elif label=='3':
        temp=(255,255,0)
    return temp
def covtuple(points):
    list1=[]
    for items in points:
        itemstuple=tuple(items)
        list1.append(itemstuple)
    return list1
def drawpoints(points,label):
    draw = ImageDraw.Draw(newIm)
    pointslist=covtuple(points)
    #print(pointslist)
    draw.polygon(pointslist, fill = fillcolor(label))
def getdis(point1,point2):
    dis=0
    length=4
    #print(point2)
    for i in range(length):
        dis+=(point1[i]-point2[i])*(point1[i]-point2[i])
    return dis
def returnlabel(point):
    dis0=getdis(point,(255, 0, 0,255))
    dis1=getdis(point,(0,0,255,255))
    dis2=getdis(point,(0,255,0,255))
    dis3=getdis(point,(255,255,0,255))
    mindis= min(dis0,dis1,dis2,dis3)
    if mindis==dis0:
        return 0
    elif mindis==dis1:
        return 1
    elif mindis==dis2:
        return 2
    elif mindis==dis3:
        return 3
def convmask(IM):
    mask=[]
    
    width1, height1 = IM.size
    img_src = IM.convert('RGBA')
    str_strlist = img_src.load()
    for x in range(width1):
        maskrow=[]
        for y in range(height1):
            point=str_strlist[x,y]
            pointlabel=returnlabel(point)
            maskrow.append(pointlabel)
        mask.append(maskrow) 
    return mask   
with open('./road.json', 'r') as f:
    dict1 = json.load(f)
f.close()
for items in dict1['shapes']:
    drawpoints(items['points'],items['label'])
newIm.show()
IMG_PATH2 = "./test.jpg"
im03 = Image.open(IMG_PATH2)
mask=convmask(im03)
data=open("./mask.txt","w")
print(mask,file=data)
data.close()
with open("./mask1.txt","w") as wt:
    for items in mask:
        for item in items:
            wt.write(str(item))
            wt.write(' ')
wt.close()
#print(mask)
newIm.save(r'./dye.jpg')