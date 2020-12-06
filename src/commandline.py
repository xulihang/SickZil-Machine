import utils.fp as fp
import imgio as io
import core
from pathlib import Path

def imgpath2mask(imgpath):
    return fp.go(
        imgpath,
        lambda path: io.load(path, io.NDARR),
        core.segmap,
        io.segmap2mask
    )
    
def genmask(imgpath):
    mask = imgpath2mask(imgpath)
    io.save("./mask.png", mask)    
    
def rm_txt(imgpath, maskpath, outputpath):
    if imgpath is None: return None
    image = io.load(imgpath, io.IMAGE)
    mask  = io.load(maskpath, io.MASK) 
    inpainted = core.inpainted(image, mask)
    io.save(outputpath, inpainted) 

    
if __name__ == '__main__':
    print("processing...")
    genmask("./1.jpg")
    rm_txt("./1.jpg","./mask.png","removed.jpg")