FROM python:3.9-slim

# 1. Aktualizacja systemu
RUN apt-get update
RUN apt-get install -y xvfb
RUN apt-get install -y x11-utils
RUN apt-get install -y python3-tk
RUN apt-get install -y imagemagick
RUN apt-get install -y gnome-screenshot
RUN apt-get install -y xserver-xephyr
RUN apt-get install -y gnumeric
RUN apt-get install -y tigervnc-standalone-server
RUN apt-get install -y x11-apps
RUN apt-get install -y xterm
RUN apt-get install -y lxterminal
RUN apt-get install -y xfce4-terminal

RUN apt-get install -y tilix
RUN apt-get install -y fonts-firacode
RUN apt-get install -y dconf-cli

RUN apt-get install -y dbus-x11
RUN apt-get install -y  rxvt-unicode
RUN apt-get install -y  kitty



RUN pip install pyautogui pillow pyvirtualdisplay
RUN pip install  tk easyprocess

# Skopiuj skrypt
COPY script.py /home/script.py

# Ustaw katalog roboczy
WORKDIR /home

RUN touch /root/.Xauthority

RUN mkdir -p /home/outcome && chmod 777 /home/outcome

