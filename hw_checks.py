#Run with python3!

import subprocess as sub
import os,datetime

def getrevision():
    # From https://www.raspberrypi-spy.co.uk/2012/09/getting-your-raspberry-pi-revision-number-using-python/
    # Extract board revision from cpuinfo file
    revision = "undefined"
    try:
        f = open('/proc/device-tree/model','r')
        for line in f:
            length=len(line)
            revision = line[0:length-1]
        f.close()
    except:
        revision = input("PI version not detected, enter manually:\n")
    return revision

def getmac():
    # Extract Wlan mac address from sys file
    mac = "00:00:00:00:00:00"
    try:
        f = open('/sys/class/net/wlan0/address','r')
        for line in f:
            length=len(line)
            mac = line[0:length-1]
        f.close()
    except:
        mac = input("MAC address not detected, enter manually:\n")
    return mac

def gethat():
    # Extract HAT id from device-tree
    hat = "undefined"
    try:
        f = open('/proc/device-tree/hat/product','r')
        for line in f:
            length=len(line)
            hat = line[0:length-1]
        f.close()
    except:
        hat = input("HAT not detected, enter manually:\n")
    return hat

def getusb():
    try:
        command = "lsblk -o NAME,SIZE | grep -w sda"
        usb = str(sub.check_output(command, shell=True))
        size=int(len(usb))
        usb=float(usb[size-9:size-4])
        if usb > 128:
            output = "256GB"
        elif usb > 64:
            output = "128GB"
        elif usb > 32:
            output = "64GB"
        elif usb > 16:
            output = "32GB"
        elif usb > 8:
            output = "16GB"
        else:
            output = "USB Memory to small!"
    except:
        output = "No USB memory detected!"
    return output

def getsd():
    try:
        command = "lsblk -o NAME,SIZE | grep -w mmcblk0"
        sd = str(sub.check_output(command, shell=True))
        size=int(len(sd))
        sd=float(sd[size-9:size-4])
        if sd > 128:
            output = "256GB"
        elif sd > 64:
            output = "128GB"
        elif sd > 32:
            output = "64GB"
        elif sd > 16:
            output = "32GB"
        elif sd > 8:
            output = "16GB"
        else:
            output = "SD Memory to small!"
    except:
        output = "Error detecting the SD storage!"
    return output

hw_request = input("Did all HW checks pass? [y/n]\n")
if hw_request=='y':
    verdict = "True"
else:
    verdict = "False"

hostname = os.uname()[1]

date = str(datetime.date.today())

mac = str(getmac())

platform = str(getrevision())

hat_version = str(gethat())

usb_memory = str(getusb())
sd_memory = str(getsd())

bat_request = input("Is the duckiebot using a standard white battery? [y/n]\n")
if bat_request=='y':
    battery = "RAVPOWER RP-PB07"
else:
    battery = input("Enter the battery description:\n")

act_request = input("Is the duckiebot using a standard actuation? [y/n]\n")
if act_request=='y':
    actuation = "DG01D dual-axis drive gear (48:1)"
else:
    actuation = input("Enter the actuation description:\n")

tester_name = input("Enter your name:\n")

filename = "/data/config/"+date+"_hardware-compliance.yaml"

f= open(filename,"w+")
f.write("verdict: "+verdict+"\n")
f.write("hostname: "+hostname+"\n")
f.write("date: "+date+"\n")
f.write("mac-adress: "+mac+"\n")
f.write("platform: "+platform+"\n")
f.write("hat_version: "+hat_version+"\n")
f.write("usb-memory: "+usb_memory+"\n")
f.write("sd-memory: "+sd_memory+"\n")
f.write("battery: "+battery+"\n")
f.write("actuation: "+actuation+"\n")
f.write("tester_name: "+tester_name)
f.close()
