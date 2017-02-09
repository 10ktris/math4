import csv
import matplotlib.pyplot as plot

def timecode_to_seconds(timecode):
	hours, minutes, seconds = timecode.split(":")
	seconds, ms = seconds.split(".")

	total_ms = (int(ms) / 1000 + 
			   	int(seconds) + 
			   	int(minutes) * 60 + 
			   	int(hours)   * 60 * 60)
	return total_ms

time_changes = []
speed_changes = []

with open("data.csv", "r") as f:
	data = csv.reader(f)
	for timecode, speed in data:
		time = timecode_to_seconds(timecode)
		time_changes.append(time)
		speed_changes.append(float(speed) / 100)



plot.plot(time_changes, speed_changes)
plot.xlabel("time in seconds")
plot.ylabel("speed")
plot.show()