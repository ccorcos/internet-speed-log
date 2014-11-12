from pylab import *

# need to update this for the new format

f = open("speedLog.txt", 'r')
a = f.read()
a = a.replace(',','')
a = a.split('\n')[0:-1]
a = [b.split(' ') for b in a]

# date ranges. include leading zeros.
# maxDate is a day after you want plotted
minDate = '09/19/2013'
maxDate = '10/20/2013'

date = [b[0] for b in a]

begin = date.index(minDate)
end = date.index(maxDate)

speed = [float(b[2])*8.0/1000000.0 for b in a]
speed = speed[begin:end]
date = date[begin:end]

# figure()
# plot(speed)
# ylabel('MB/s')
# xlabel('Dates')
# grid()
# show()

speed = array(speed)
percent = str(mean(speed<15)*100)[0:4]


fig = figure()
title('Internet Speeds Tested Every Hour\n'+percent+'% < 15 MB/s')
ax = fig.add_subplot(111)
ax.plot(speed)


tick = [0,]
label = [date[0],]
for i in range(1,len(date)):
	if date[i] != label[-1]:
		label.append(date[i])
		tick.append(i)

ax.set_xticks(tick)
ax.set_xticklabels(label)
xticks(rotation='vertical')
subplots_adjust(bottom=.2)
ylabel('MB/s')
xlabel('Dates')
show()
