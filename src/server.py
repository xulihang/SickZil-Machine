#!/usr/bin/env python3

import os
import time
import datetime
from bottle import route, run, template, request, static_file
import json

import utils.fp as fp
import imgio as io
import core
from pathlib import Path


@route('/getmask', method='POST')
def getmask():
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    print(ext.lower())
    if ext.lower() not in ('.png','.jpg','.jpeg'):
        return "File extension not allowed."
        
    timestamp=str(int(time.time()*1000))
    savedName=timestamp+ext
    save_path = "./uploaded/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = "{path}/{file}".format(path=save_path, file=savedName)
    mask_path = "{path}/{file}".format(path=save_path, file=savedName+"-mask.png")
    if os.path.exists(file_path)==True:
        os.remove(file_path)
    upload.save(file_path)        
    
    genmask(file_path,mask_path)
    return static_file(savedName+"-mask.png", root='uploaded')  
    
@route('/gettxtremoved', method='POST')
def get_txtremoved():
    origin = request.files.get('origin')
    mask = request.files.get('mask')
    
    name, ext = os.path.splitext(origin.filename)
    mask_name, mask_ext = os.path.splitext(mask.filename)
    if ext.lower() not in ('.png','.jpg','.jpeg'):
        return "File extension not allowed."
    if mask_ext.lower() not in ('.png','.jpg','.jpeg'):
        return "File extension not allowed."        
        
    timestamp=str(int(time.time()*1000))
    origin_savedName=timestamp+ext
    mask_savedName=timestamp+"-mask"+mask_ext
    ouputName=timestamp+"-text-removed.jpg"
    
    save_path = "./uploaded/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    origin_path = "{path}/{file}".format(path=save_path, file=origin_savedName)
    mask_path = "{path}/{file}".format(path=save_path, file=mask_savedName)
    output_path = "{path}/{file}".format(path=save_path, file=ouputName)
    origin.save(origin_path)        
    mask.save(mask_path)    
    
    rm_txt(origin_path,mask_path,output_path)
    return static_file(ouputName, root='uploaded')      


@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='www')

def imgpath2mask(imgpath):
    return fp.go(
        imgpath,
        lambda path: io.load(path, io.NDARR),
        core.segmap,
        io.segmap2mask
    )
    
def genmask(imgpath, outputpath):
    mask = imgpath2mask(imgpath)
    io.save(outputpath, mask)    
    
def rm_txt(imgpath, maskpath, outputpath):
    if imgpath is None: return None
    image = io.load(imgpath, io.IMAGE)
    mask  = io.load(maskpath, io.MASK) 
    inpainted = core.inpainted(image, mask)
    io.save(outputpath, inpainted) 

    
if __name__ == '__main__':
    run(host='127.0.0.1', port=8080)     