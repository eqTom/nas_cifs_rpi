#!/usr/bin/python
import os

# Don't forget to check out the ReadMe :)
# eqTom - 12/04/14

#
# Config Start
#

# Put where in your OS we should mount the CIFS drive
mount_point = "/mnt/nas"

# CIFS auth and remote folder information 
nas_user = "nas-user"
nas_pass = "nas-pass"
nas_path = "//nas/Volume_1/Downloads"

# Restart a daemon after the NAS is mounted?
daemon_restart = True
daemon_name = "transmission-daemon"

# deadmanssnitch.com intergration (It's free!)
# Get eMail alerts if the mount fails to work!

dms_url = "https://nosnch.in/abcd1234"

#
# Config End
#

# The Core code start's here

mnt = os.system("mount -l | grep " + mount_point)

if mnt:
  print ("not mounted")
  os.system("sudo mount -t cifs -o user=" + nas_user + ",password=" + nas_pass + " " + nas_path + " " + mount_point)
  if daemon_restart:
    os.system("service " + daemon_name + " restart")
else:
  print ("mounted")
  os.system("curl " + dms_url + " &> /dev/null")