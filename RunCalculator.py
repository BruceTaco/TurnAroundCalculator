racePace = int(input(print("What is your desired race pace in whole minutes?")))
warmup = int(input(print("How long, in minutes, is your warmup going to be?")))
mainRun = int(input(print("How long, in whole minutes, will your long run last?")))
runPace = int(input(print("At what pace will you be running?")))
extraRun = bool(input(print("Will you complete the extra run: Y or N?")))
if extraRun:
    extraRunTime = int(input(print("How long will you run during the extra time?")))

distanceWarmCool = (warmup * 2)/(racePace + 2)
distanceMain = mainRun/runPace
if extraRun:
    distanceExtra = extraRunTime/runPace
turnAroundDistance = float((distanceExtra + distanceMain + distanceWarmCool)/2)
turnAroundTime = int((mainRun + extraRunTime + (warmup*2))/2)

print("You should turn around after ", turnAroundTime, "minutes, after running ", turnAroundDistance, "miles.")
print("Your run should cover ", turnAroundDistance*2, "miles.")

