#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


class Feladatok():
    def __init__(self):
        self.ev3 = EV3Brick()# tégla
        self.jm =Motor(Port.B)#motorok
        self.bm =Motor(Port.C)
        self.km =Motor(Port.A)
        self.cs =ColorSensor(Port.S3)#szenzorok
        self.cs =TouchSensor(Port.S1)
        self.cs =GyroSensor(Port.S2)
        self.cs =UltrasonicSensor(Port.S4)
        self.robot = DriveBase(self.jm, self.bm, 55, 115)#a motorok egyut mozogjanak , 3. paraméter a a kerékátmároje, 4. paraméter a a kerekek kőzőtti távolság(lemér5t keerék távolság gumival minusz ketszer a sugar)


    def elsoFeladat(self):
        #robot elöre 30 cm
        self.robot.straight(200)

    def masodikFeladat(self):
        #fordul jobra
        self.robot.turn(90)

    def harmadikFeladat(self):
        ut = 100
        fordul = 90

        #robot elöre 30 cm
        self.robot.straight(ut)
        #fordul jobra
        self.robot.turn(fordul)
        #fordul balra
        self.robot.turn(-1*fordul)
        #hatra
        self.robot.straight(ut*(-1))
    
    def beszelAngolulFenyek(self):
        self.ev3.light.on(Color.YELLOW)#felkapcsolja a fényt kéken
        self.ev3.speaker.set_volume(100)  #hangerö
        self.ev3.speaker.set_speech_options('en','f2', 400,400)#beszélőbeállitásai ,nyelv,nem,sebeséd,mélység
        self.ev3.speaker.say("Hi! Have a nice day!")#koszon
        self.ev3.light.off()
        self.ev3.light.on(Color.GREEN)
        self.ev3.speaker.play_file(SoundFile.ELEPHANT_CALL)#külsö fajl lejatszása .wav
        self.ev3.speaker.play_file("elefant_call.wav")
        self.ev3.speaker.play_file(SoundFile.CAT_PURR)
        self.ev3.speaker.play_file(SoundFile.DOG_BARK_1)
        self.ev3.speaker.play_file(SoundFile.DOG_BARK_2)
        self.ev3.speaker.play_file(SoundFile.DOG_GROWL)
        self.ev3.speaker.play_file(SoundFile.DOG_SNIFF)
        self.ev3.speaker.play_file(SoundFile.INSECT_BUZZ_1)
        self.ev3.speaker.play_file(SoundFile.SNAKE_HISS)
        #beépitett hangfájl lejátszása
        self.ev3.speaker.play_file(SoundFile.BOING)





    def egyeniFeladat(self):
        self.robot.straight(200)
        self.robot.turn(90)
        self.ev3.speaker.beep()
        self.robot.straight(200)
        self.robot.turn(-90)
        self.ev3.speaker.beep()
        self.robot.straight(20)
        self.robot.turn(-360)
        self.ev3.speaker.beep()
        self.robot.straight(-100)
        self.robot.straight(150)
        self.robot.turn(-90)
        self.ev3.speaker.beep()
        self.robot.straight(100)




    def csipog(self):
        self.ev3.speaker.beep()

    def korbefordulas1(self):
        self.robot.turn(360)#elentéts irányu kerekek

    def korbefordulas2(self):#egyik kereék nem mozdul
        self.jm.run_target(200, 1630)
        


    def korbefordulas2a(self):#egyik kereék nem mozdul
        for i in range(1,360,1):
            self.robot.straight(1)
            self.robot.turn(1)

    def korbefordulas3(self):
        for i in range(1,37,1):
            self.robot.straight(10)
            self.robot.turn(-10)
            



    




