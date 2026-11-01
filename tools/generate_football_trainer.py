#!/usr/bin/env python3
"""Generate 56x56 four-shade Game Boy football trainer portraits (stdlib only)."""
import struct
import sys
import zlib
from football_redesign import football_portrait
from neymar_reference import neymar_portrait
from messi_reference import messi_portrait

PALETTE = (255, 170, 85, 0)

def portrait(name):
    if name == "neymar":
        return neymar_portrait()
    if name == "messi":
        return messi_portrait()
    if name == "cr7":
        return football_portrait(name)
    pixels = [[0] * 56 for _ in range(56)]
    def rect(x1,y1,x2,y2,c):
        for y in range(max(0,y1),min(56,y2+1)):
            for x in range(max(0,x1),min(56,x2+1)):
                pixels[y][x]=c
    def ellipse(cx,cy,rx,ry,c):
        for y in range(56):
            for x in range(56):
                if ((x-cx)/rx)**2+((y-cy)/ry)**2<=1:
                    pixels[y][x]=c
    def line(x1,y1,x2,y2,c,width=1):
        steps=max(abs(x2-x1),abs(y2-y1),1)
        for i in range(steps+1):
            x=round(x1+(x2-x1)*i/steps)
            y=round(y1+(y2-y1)*i/steps)
            rect(x-width//2,y-width//2,x+width//2,y+width//2,c)
    ellipse(28,18,13,15,3)
    ellipse(28,19,11,12,1)
    if name in ('maduro','che_guevara','putin'):
        rect(15,5,40,11,3)
        if name=='che_guevara':
            rect(12,3,43,7,3)
            rect(20,27,36,31,3)
        elif name=='putin':
            rect(20,7,36,9,1)
        else:
            rect(18,26,38,29,3)
    elif name=='kim_jong_un':
        rect(14,4,41,12,3)
        rect(18,12,38,14,2)
        rect(21,27,35,29,2)
    elif name=='xi_jinping':
        rect(15,5,40,10,3)
        rect(17,10,39,12,2)
        rect(21,27,35,28,2)
    elif name=='steve_jobs':
        rect(16,5,39,9,3)
        rect(17,14,25,20,2)
        rect(31,14,39,20,2)
        line(25,17,31,17,3)
        rect(22,27,34,29,3)
    elif name=='bill_gates':
        rect(17,5,38,10,3)
        rect(16,16,39,17,3)
        rect(17,14,24,20,2)
        rect(32,14,39,20,2)
        line(24,17,32,17,3)
    elif name=='jeff_bezos':
        rect(18,7,37,9,1)
        rect(19,12,36,13,2)
    elif name=='elon_musk':
        rect(16,5,39,9,3)
        rect(18,9,37,12,2)
    elif name=='trump':
        rect(14,5,40,11,1)
        rect(15,4,38,7,2)
        line(16,9,40,5,1,3)
    elif name=='messi':
        rect(17,5,37,10,3)
        rect(19,26,36,30,3)
    elif name=='cr7':
        rect(17,5,38,9,3)
        line(19,10,35,6,3,3)
    else:
        rect(17,4,38,10,3)
        rect(21,26,35,29,3)
    rect(22,17,24,18,3)
    rect(32,17,34,18,3)
    line(26,24,31,24,3)
    ellipse(28,51,20,21,3)
    ellipse(28,52,17,18,2)
    rect(25,32,31,55,1)
    if name in ('maduro','che_guevara','putin'):
        rect(18,35,38,55,2)
        line(27,35,28,53,3,2)
    elif name=='kim_jong_un':
        rect(16,35,40,55,3)
        rect(21,35,35,54,1)
    elif name=='xi_jinping':
        rect(19,35,37,55,1)
        line(27,35,28,53,3,3)
    elif name=='steve_jobs':
        rect(17,35,39,55,3)
        rect(22,36,34,54,2)
    elif name=='bill_gates':
        rect(18,35,38,55,1)
        line(27,35,28,50,3,2)
    elif name=='jeff_bezos':
        rect(18,35,38,55,1)
        line(18,40,38,40,3,2)
    elif name=='elon_musk':
        rect(20,35,36,55,1)
        line(20,39,36,39,3,2)
    elif name=='trump':
        rect(23,35,33,55,0)
        line(27,35,28,51,3,3)
    elif name=='messi':
        rect(17,34,20,55,1)
        rect(36,34,39,55,1)
    elif name=='cr7':
        line(15,35,40,54,1,4)
    else:
        rect(18,34,38,39,1)
    line(13,37,5,49,3,5)
    line(43,37,51,49,3,5)
    ellipse(7,49,6,6,3)
    ellipse(7,49,4,4,0)
    # Shirt number in a simple 3x5 bitmap.
    glyphs={'1':['010','110','010','010','111'],
            '0':['111','101','101','101','111'],
            '7':['111','001','010','010','010']}
    label='' if name in ('trump','elon_musk','jeff_bezos','bill_gates','steve_jobs','xi_jinping','kim_jong_un','maduro','che_guevara','putin') else ('7' if name=='cr7' else '10')
    for n,ch in enumerate(label):
        for y,row in enumerate(glyphs[ch]):
            for x,v in enumerate(row):
                if v=='1': rect(23+n*5+x,43+y,23+n*5+x,43+y,3)
    return pixels

def chunk(kind,data):
    return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data)&0xffffffff)

def main():
    name,path=sys.argv[1:]
    pixels=portrait(name)
    raw=b''.join(b'\0'+bytes(PALETTE[p] for p in row) for row in pixels)
    png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',56,56,8,0,0,0,0))+chunk(b'IDAT',zlib.compress(raw,9))+chunk(b'IEND',b'')
    with open(path,'wb') as f:f.write(png)

if __name__=='__main__':main()
