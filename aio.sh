# All in One Script upto the String Generation for ease to newbies.

# DO NOT MAKE CHANGES HERE!

# Copyright (c) 2021, jaaat4u <devangsingh369@gmail.com>

which "apt"

RESULT=$?
if [ $RESULT -eq 0 ]; then

  echo " Debian System Detected."

sudo apt update && sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip
pip3 install requirements.txt
bash userbot/stringgen.py

else

  echo " Arch Distro. You seem to be so Pero Af!"

sudo pacman -Syyu
sudo pacman -S python3
sudo pacman -S python-pip
pip3 install requirements.txt
bash userbot/stringgen.py

fi
