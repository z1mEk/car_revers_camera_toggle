#!/usr/bin/python3  
# script for qu4q

# importy bibliotek
import RPi.GPIO as GPIO  # obsługo gpio
import os, sys # wykorzystana do uruchamiania komend powłoki
import time # wykorzystana do funkcji sleep()

relay_gpio = 23 # ustawiamy gpio na 23

# ustawienie GPIO
GPIO.setmode(GPIO.BCM)  
GPIO.setup(relay_gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # gpio ustawiony jako pulldown

  
# to jest funkcja, która zostanie wywołana przez przerwanie
# gdy włączymy lub wyłączymy wsteczny
def camera_toggle(channel):
    if GPIO.input(relay_gpio): 
        # tu wpisujemy komendę jaka ma się wykonać gdy pin dostenie HIGH
        print("Wsteczny włączony")
        os.system("/usr/local/bin/camera_on")   
    else:
        # tu wpisujemy komendę jaka ma się wykonać gdy pin dostenie LOW
        print("Wsteczny wyłączony")
        os.system("/usr/local/bin/camera_off")

  
# włączamy obsługę przerwania dla kanału 23 (pin 16)
# jeśli na pinie 16 zostanie zmieniony stan to zostanie wywołana 
# funkcja o nazwie camera_toggle
GPIO.add_event_detect(relay_gpio, GPIO.BOTH, callback=camera_toggle)  

print("Grzecznie czekamy na włączenie lub wyłączenie wstecznego ;)")

i = 0

while True:
    try:  
        # tutaj nakurwiamy pętlą żeby się skrypt nie skończył
        # jak wciśniemy Ctrl+c to wskoczy w except i zakończy skrypt
        # polecam skrypt uruchomić jako daemon albo w screenie
        i += 1
        print("czekam"+"".join("." * i), end="\r")
        time.sleep(1)
        if i == 10:
            i = 0   
            print(" " * 20, end="\r")

    
    except KeyboardInterrupt:
        print("Umieram!")
        GPIO.cleanup() # czyścimy GPIO w razie ubicia skryptu
        sys.exit()
