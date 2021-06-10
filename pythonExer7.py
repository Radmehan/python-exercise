from pygame import mixer
from datetime import datetime
from time import time

def mususic_on_loop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break


def file_log(msg):
    with open("myLog","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # mususic_on_loop("water.mp3","stopper")
    init_water=time()
    init_eyes = time()
    init_exercise = time()

    water_secs=5
    eyes_secs=20
    exercise_secs=10

    while True:
        if time()-init_water>water_secs:
            print("Water drinking time. Enter 'drank' to stop the alarm")
            mususic_on_loop("water.mp3","drank")
            init_water=time
            file_log("Drank water at")

        if time()-init_eyes>eyes_secs:
            print("Water drinking time. Enter 'eyes' to stop the alarm")
            mususic_on_loop("water.mp3","drank")
            init_eyes = time()
            file_log("Eyes Relaxed at")

        if time()-init_exercise>exercise_secs:
            print("Water drinking time. Enter 'exercise' to stop the alarm")
            mususic_on_loop("water.mp3","drank")
            init_exercise = time()
            file_log("Physical Activity done at")