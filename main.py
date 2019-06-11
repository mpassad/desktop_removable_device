import os
from time import sleep

REMOVABLE_DEVICES_PATH = '/run/media/michael/'
DESKTOP_PATH = '/home/michael/Desktop/'
removable_icon = 'drive-removable-media-usb-pendrive'


def get_initial_state():
    all_desktop_files = [name for name in os.listdir(
        DESKTOP_PATH) if os.path.isfile(
            os.path.join(DESKTOP_PATH, name))]
    return all_desktop_files


def get_devices():
    """
    list all the removable devices
    """
    return [name for name in os.listdir(REMOVABLE_DEVICES_PATH)
            if os.path.isdir(os.path.join(REMOVABLE_DEVICES_PATH, name))]


def get_dot_desktop():
    """
    get all the files the the extension .desktop in the directory Desktop
    """
    all_desktop_files = [name for name in os.listdir(
        DESKTOP_PATH) if os.path.isfile(
            os.path.join(DESKTOP_PATH, name))]

    dot_desktop_list = []
    for item in all_desktop_files:
        suffix = '.desktop'
        if item.endswith(suffix):
            dot_desktop_list.append(item)
    return dot_desktop_list


def init_desktop(protected):
    for item in get_devices():
        if item not in protected:
            if item+'.desktop' not in get_dot_desktop():
                create_dot_desktop_file(item, item)
            else:
                if item not in get_devices():
                    os.remove(DESKTOP_PATH+item+'.desktop')
                    print('deleted: ', item+'.desktop')

    for item in get_dot_desktop():
        if item not in protected:
            new_item = item.replace('.desktop', '')
            if new_item not in get_devices():
                if item != 'Vault.dekstop' and item != 'Home.desktop':
                    os.remove(DESKTOP_PATH+item)
            sleep(1)


def create_dot_desktop_file(filename, name):
    """
    create a .desktop file with the link to the removable device
    """
    desktop_file = '[Desktop Entry]' +\
        '\nEncoding = UTF-8' +\
        '\nExec = dolphin ' + "'" + REMOVABLE_DEVICES_PATH + filename + "'" +\
        '\nIcon = '+removable_icon + \
        '\nName = '+name +\
        '\nStartupNotify = true' +\
        '\nTerminal = false' +\
        '\nType = Application' +\
        '\nVersion = 1.0'

    f = open(DESKTOP_PATH + filename+'.desktop', 'w')
    f.write(desktop_file)
    f.close()


if __name__ == "__main__":
    protected_state = get_initial_state()
    while True:
        init_desktop(protected_state)
