##!/bin/bash
#
# Start D-Bus
echo "Starting D-Bus..."
#dbus-daemon --system --fork

## Start Xvnc server
##echo "Starting Xvnc on display :99..."
##Xvnc :99 -geometry 1366x768 -depth 24 -nolisten tcp &
##export DISPLAY=:99
#
## Poczekaj na uruchomienie Xvnc
#sleep 2
#
## Zmień motyw GTK
#echo "Setting GTK theme to Greybird..."
#xfconf-query -c xsettings -p /Net/ThemeName -s "Greybird"
#
## Zmień motyw menedżera okien
#echo "Setting Window Manager theme to Greybird..."
#xfconf-query -c xfwm4 -p /general/theme -s "Greybird"
#
## Zmień tło pulpitu
#echo "Setting desktop wallpaper..."
#xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitorVirtual-1/workspace0/last-image -s "/usr/share/backgrounds/xfce/xfce-blue.png"
#
## Uruchom terminal (lub inną aplikację)
#xfce4-terminal --geometry=136x40 --hold
#
## Utrzymanie kontenera aktywnego
#tail -f /dev/null
