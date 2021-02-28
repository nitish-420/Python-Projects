import time
from pygame import mixer

class Play:
    def __init__(self, file, t, msg):
        self.file = file
        self.time = t
        self.message = msg

    def play(self):
        time.sleep(self.time)
        mixer.init()
        mixer.music.load(self.file)
        mixer.music.play()
        print(f"Enter {self.message} to stop this {self.file} sound")
        while True:
            i = input()
            if i == self.message:
                mixer.music.stop()
                mixer.quit()
                break


if __name__ == "__main__":
    water = Play("water.ogg", 40*60, "drank")
    eyes = Play("eyes.ogg", 45*60, "eydone")
    exercise = Play("exercise.ogg", 30*60, "exdone")
    itwater = 40*60
    iteyes = 45*60
    itexercise = 30*60

    while True:
        tm = time.time()
        mm = min([water.time, eyes.time, exercise.time])
        if mm == water.time:
            if water.time < 0:
                negtime = water.time
                water.time = 0
                water.play()
                water.time = negtime+itwater+tm-time.time()
            else :
                water.play()
                water.time=water.time+tm-time.time()
            eyes.time = eyes.time+tm-time.time()
            exercise.time = exercise.time+tm-time.time()
        elif mm == exercise.time:
            if exercise.time < 0:
                negtime = exercise.time
                exercise.time = 0
                exercise.play()
                exercise.time = negtime+itexercise+tm-time.time()
            else :
                exercise.play()
                exercise.time=exercise.time+tm-time.time()
            water.time=water.time+tm-time.time()
            eyes.time=eyes.time+tm-time.time()
        elif mm==eyes.time:
            if eyes.time < 0:
                negtime = eyes.time
                eyes.time = 0
                eyes.play()
                eyes.time = negtime+iteyes+tm-time.time()
            else :
                eyes.play()
                eyes.time=eyes.time+tm-time.time()
            exercise.time=exercise.time+tm-time.time()
            water.time=water.time+tm-time.time()
        
        if water.time<0 :
            water.time+=itwater
        elif exercise.time<0 :
            exercise.time+=itexercise
        elif eyes.time<0 :
            eyes.time+=iteyes
