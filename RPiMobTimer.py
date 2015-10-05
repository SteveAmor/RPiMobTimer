#!/usr/bin/python

#Mob programming screen blanking timer by Steve Amor
#For the Raspberry Pi - add to /etc/xdg/lxsession/LXDE-pi/autostart

import pygame, sys, time
from pygame.locals import *

# constants
TIMEOUT = 600 # Timer in seconds between changing Driver
WAITTIME = 20 # seconds to leave New Driver message on screen

# set up the colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def message(msgText, backgroundColour):
	windowSurface.fill(backgroundColour)
	basicFont = pygame.font.SysFont(None, 180)
	text = basicFont.render(msgText, True, WHITE, backgroundColour)
	textRect = text.get_rect()
	textRect.centerx = windowSurface.get_rect().centerx
	textRect.centery = windowSurface.get_rect().centery
	windowSurface.blit(text, textRect)
	pygame.display.update()

def smallMessage(smallText, backgroundColour):
	basicFont = pygame.font.SysFont(None, 30)
	text = basicFont.render(smallText, True, WHITE, backgroundColour)
	textRect = text.get_rect()
	textRect.centerx = windowSurface.get_rect().centerx
	textRect.centery = windowSurface.get_rect().centery+100
	windowSurface.blit(text, textRect)
	pygame.display.update()

def countdown(counter):
	while counter != 0:
		smallMessage('  %s  '%counter, BLACK)
		counter=counter-1
		time.sleep(1)

def waitForSpaceKey():
	pygame.event.clear()
	spacePressed = False
	while not spacePressed:
		time.sleep(0.1)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				spacePressed = True

#main starts here

while True:
	time.sleep(TIMEOUT)
	pygame.init()

#	windowSurface = pygame.display.set_mode((1360, 768), 0,32)
	windowSurface = pygame.display.set_mode((1360, 768), pygame.FULLSCREEN)
	message('Change Driver', BLACK)

	countdown(WAITTIME)
	smallMessage("Press space to continue with new driver",BLACK)
	waitForSpaceKey()
	pygame.display.quit()
