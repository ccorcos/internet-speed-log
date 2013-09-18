InternetSpeedLog
================

Using this repo, https://github.com/teeks99/speed_check, I modified it to write out to test internet speeds every hour and write it out to a text file. I'm hoping to get my internet bill prorated for not getting the internet speeds they promised ;)

I'm doing this on my rasperberry pi so I dont have to use a computer. I am plugging my raspi straight into the ethernet -- usb wifi can be slower than your real internet speed.

Here's how I set it up.

Once you have your raspberry pi set up and logged in:

> `sudo aptitude update`
> `sudo apt-get install git`
? `sudo apt-get install tmux`
> `git clone https://github.com/ccorcos/InternetSpeedLog.git`
> `tmux`
> `cd InternetSpeedLog`
> `python SpeedCheck.py`
> control-b
> d

Tmux is a program that allows you to quit terminal while leaving the program running. This is particularly useful is you ssh into the computer to do all of this as I did. 

from terminal to get back to tmux to stop the program from running, 
tmux attach

Also, note that if you are ssh'd into your raspi, to get out of tmux you need to hold the function key, 
fn+control+b

The log of internet speed is written to a file, speedLog.txt. Rather than go into tmux to view the print statements, you can just navigate to this file and open it:

if you using ssh and kind of a noob:
> `cd InternetSpeedLog`
> `vi speedLog.txt`
> esc
> `:`
> `q`

good luck!



