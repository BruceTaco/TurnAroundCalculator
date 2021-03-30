# -----------------------------------------------------------------------------
# Author: Michael Williamson
# Date: 03/30/2021

# The purpose of this program is to take some information from a user about
# their next scheduled run under the Garmin coaching program and return to
# them the necessary turn around times in order to complete an out-and-back
# style run.
# -----------------------------------------------------------------------------


racePace = input("Enter your desired race pace in the following format [mm:ss] ")
racePaceList = racePace.split(":")
racePaceMinutes = int(racePaceList[0])
racePaceSeconds = int(racePaceList[1])
totalRacePaceSeconds = ((racePaceMinutes*60) + racePaceSeconds)

warmupTime = int(input("How long, in minutes, is your warmup going to be? "))
mainRunTime = int(input("How long, in minutes, will your main run last? "))
extraRunTime = int(input("How many minutes will you run during the extra time? "))

runPace = input("Enter your pace for today's main run in the following format [mm:ss] ")
runPaceList = racePace.split(":")
runPaceMinutes = int(runPaceList[0])
runPaceSeconds = int(runPaceList[1])
totalRunPaceSeconds = ((runPaceMinutes*60) + runPaceSeconds)

distanceWarmCool = ((warmupTime * 2) * 60) / (totalRacePaceSeconds + 120)       # distance run during warmup and cool down periods
distanceMain = (mainRunTime * 60) / totalRunPaceSeconds
distanceExtra = (extraRunTime * 60) / totalRunPaceSeconds
turnAroundDistance = round(float((distanceExtra + distanceMain + distanceWarmCool)/2), 2)
turnAroundTime = int(((warmupTime * 2) + mainRunTime + extraRunTime)/2)         # because this is an int it's rounding the time to the lower value
print('Turn around distance: ', turnAroundDistance)
print("You should turn around at ", turnAroundTime, "minutes, after running ", turnAroundDistance, "miles.")
print("Your run should cover ", (turnAroundDistance * 2), "miles.")
