#!/bin/bash
#Setup system to run Metar Map Application 
#Change mode before using - chmod +x installscript.sh
#For initial setup - ./installscript.sh
#initial setup will restart the system
#To setup crontab job - ./installscript.sh cron
#written by Herb Spenner
#rev. 05/10/2018
cronString="cron"
if [ "$1" == "$cronString" ]
then
	echo "Establishing cron job"
	( crontab -l ; echo "*/10 * * * * /home/pi/MetarMap/runmetarscript.sh /home/pi/MetarMap/MetarMapMain.py" ) | crontab -
	echo "cron job created for Metar"
else
	echo "Initializing Metar application"
	read -p "This will reboot the system. Are you ready? (y) or (n): "  userinput
	if [ "$userinput" == "y" ] || [ "$userinput" = "Y" ]
	then
		sudo echo "blacklist snd_bcm2835" >>  /etc/modprobe.d/snd-blacklist.conf
		sudo sed -i '/dtparam=audio/ s/dtparam/#dtparam/' /boot/config.txt
		sudo apt-get update
		sudo apt-get install build-essential python-dev git scons swig
		sudo apt-get install python-urllib3
		sudo apt-get install python-lxml
		chmod +x /home/pi/MetarMap/runmetarscript.sh
		echo "Rebooting"
		sudo shutdown -r now
	else
		echo "System not initialized"
		echo "Run \"installscript.sh\" to initialize system"
		echo "Run \"installscript.sh cron\" to create cron job"
	fi
fi


