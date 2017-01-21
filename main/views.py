from django.http import HttpResponse, JsonResponse
import time

# Use lights
use_light = False
use_music = True

if use_light:
    def lights(state):
        import RPi.GPIO as GPIO
        if state:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.output(7, not GPIO.LOW)
        else:
            GPIO.output(7, GPIO.HIGH)

if use_music:
    def music(state):
        import pygame
        if state:
            pygame.mixer.init()
            pygame.mixer.music.load("licorne.wav")
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.stop()


# Create your views here.
def index(request):

    if use_light:
        lights(True)
    if use_music:
        music(True)

    # Wait
    time.sleep(20)

    if use_light:
        lights(False)
    if use_music:
        music(False)

    return JsonResponse({'status':'launched'})
