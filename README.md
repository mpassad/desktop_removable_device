desktop_removable_device

When User Plugs in a removable device like a usb stick or an external hdd in KDE in the desktop created a *.desktop icon to open that device.

To use this utility:
1) download the file and store it in a directory.
2) Go to the /home/<YOUR_USERNAME>/.config/autostart
3) create a *.desktop file and copy the following to the file

[Desktop Entry]
Encoding=UTF-8
Exec=/usr/bin/python3 /path/to/file/main.py
Icon=drive-harddisk-system-symbolic
Name[en_US]=removable
Name=removable
StartupNotify=true
Terminal=false
Type=Application
Version=1.0
X-DBUS-StartupType=none
X-KDE-SubstituteUID=false

and save the file with any name you want.
