nas_cifs_rpi
============

Raspberry Pi CIFS mount script, plus transmission daemon restart and DMS check in

Simple little script to ensure that a remote CIFS NAS drive is mounted
 - If it is then we check in with a remote monitoring service
 - If it's not, then we perform the required mounting, and restart a daemon

Useful for a Raspberry Pi running a torrent server with remote storage

How To:

1) Copy the script to some where and input your information 
	nano /nas_cifs_mount_and_check.sh

2) Make it executable
	chmod +x /nas_cifs_mount_and_check.sh
	
3) Add to your crontab
	crontab -e
	*/15 * * * *    python /nas_cifs_mount_and_check.sh &> /dev/null