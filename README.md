# Internet Speed Log

This program will test your internet speed and append it to the file `speedLog.txt`.
You can schedule it to run however often you want using `crontab`. Also if you have
a laptop like me, it may be more suitable to run this on a Raspberry Pi or something
that is always connected to the internet.

## Getting Started

This program uses the fabulous `speedtest-cli` tool:

    sudo pip install speedtest-cli

Then download this repo and setup a cron job:

    git clone https://github.com/ccorcos/internet-speed-log.git

### Crontab

Setting up a cron job on a unix system (I use my Raspberry Pi) is pretty easy. There is simple [documentation](http://www.raspberrypi.org/documentation/linux/usage/cron.md) for
how to do it as well.

Run `crontab -e` to open up the cron job list. Append the following line:

```
# Speedtest
0 * * * * cd /home/pi/programs/internet-speed-log/ && python speedtest.py
```

This will run `speedtest.py` every hour on the hour.

### Plotting

I've including a `plot-data.py` script that is incomplete right now will plot your
download and upload speed as a function of a time span. This is coming soon.
