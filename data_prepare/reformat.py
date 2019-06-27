import os
import argparse
import xml.dom.minidom as MD

parser = argparse.ArgumentParser(description='Json Convert')
parser.add_argument("--txt_file", type=str, help="path to text file to convert")
args = parser.parse_args()

source = args.txt_file
name = source.split('.')[0]

def parseXML(xmlfile):
    relevant = {}
    tree = MD.parse(xmlfile)
    width = float(tree.getElementsByTagName('width')[0].firstChild.data)
    height = float(tree.getElementsByTagName('height')[0].firstChild.data)
    xmin = tree.getElementsByTagName('xmin')
    if xmin:
        xmin = float(xmin[0].firstChild.data)
    ymin = tree.getElementsByTagName('ymin')
    if ymin:
        ymin = float(ymin[0].firstChild.data)
    xmax = tree.getElementsByTagName('xmax')
    if xmax:
        xmax = float(xmax[0].firstChild.data)
    ymax = tree.getElementsByTagName('ymax')
    if ymax:
        ymax = float(ymax[0].firstChild.data)

    assert xmin < xmax
    assert ymin < ymax
    
    return int(xmin), int(ymin), int(xmax), int(ymax)


with open('/home/jg925/CornerNet-Lite-for-DAC2019-Yang/data_prepare/for_jinny/class.txt') as f:
    classes = f.read().strip().split()
print("Successful parse of classes")
print(len(classes))

def getClassID(name):
    return classes.index(name)+1

##Format: category/image_file category_id (max 95) bounding box?
##^format of labels.txt and train_dataset/val_dataset

with open(source,'r') as f:
    for line in f:
        img = line.strip()[12:]
        xmin, ymin, xmax, ymax = parseXML(line.split('.')[0][5:]+'.xml')
        cls_id = getClassID(line.split('/')[2])
        with open(name+'_ref.txt','a') as fin:
            fin.write('%s %s %.6f %.6f %.6f %.6f\n' % (img,cls_id,xmin,ymin,xmax,ymax))
        
