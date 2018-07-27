#! /usr/bin/python3

import time
from time import gmtime, strftime
import os
import cv2
import pyautogui
import pygame as pg

#Globals
password = "swordfish"

def take_pic(name):
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    del(camera)
    cv2.imwrite(name, image)

savedir= os.path.dirname(os.path.realpath(__file__))
def get_name():
    return savedir+'/images/delfino'+strftime("%m_%d_%H_%M_%S", gmtime())+'.png'
    
def main():
    pg.init()
    clock = pg.time.Clock()
    font = pg.font.Font(None, 32)
    
    pyautogui.screenshot(savedir+"/sfondo.png")
    
    picture = pg.image.load(savedir+"/sfondo.png")
    pg.display.set_mode((1366,768), pg.FULLSCREEN)
    main_surface = pg.display.get_surface()
    main_surface.blit(picture, (0,0))
    pg.display.update()
    exit = False
    active = False
    pwd_box = pg.Rect(600, 300, 32, 96)
    input_box = pg.Rect(600, 364, 32, 32)
    main_surface.blit(picture, (0,0))
    pg.display.flip()
    
    writing = "Inserire password" 
    photoname = ""
    
    while not exit:
        for event in pg.event.get():
            timer = 300
            if (event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN) and not active:
                active = True
                photoname = get_name()
                take_pic(photoname)
                pwd = ''
            if event.type == pg.KEYDOWN and active:
                if event.key == pg.K_RETURN:
                    if pwd == password:
                        os.system("rm "+photoname)
                        exit = True
                    else:
                        pwd = ''
                        writing = "Password errata!"
                elif event.key == pg.K_BACKSPACE:
                    pwd = pwd[:-1]
                elif event.key == pg.K_ESCAPE:
                    active = False
                else:
                    pwd += event.unicode
            main_surface.blit(picture, (0,0))
            if active:
                cheese_surface = font.render("Say cheese!", True, pg.Color('black'))
                inp_surface = font.render(writing, True, pg.Color('black'))
                txt_surface = font.render('*'*len(pwd), True, pg.Color('black'))
                width = max(200, txt_surface.get_width()+10)
                input_box.w = width
                pwd_box.w = width
                pg.draw.rect(main_surface, pg.Color('white'), pwd_box, 0)
                pg.draw.rect(main_surface, pg.Color('grey'), input_box, 2)
                main_surface.blit(cheese_surface, (pwd_box.x+5, pwd_box.y+5))
                main_surface.blit(inp_surface, (pwd_box.x+5, pwd_box.y+37))
                main_surface.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pg.display.flip()
        clock.tick(30)
        timer -= 1
        if timer == 0:
            active = False
            main_surface.blit(picture, (0,0))
            pg.display.flip()

if __name__ == "__main__":
    main()