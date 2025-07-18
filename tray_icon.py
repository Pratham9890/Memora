import subprocess
import sys
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

# Create a simple tray icon
def create_image():
    img = Image.new('RGB', (64, 64), color='white')
    return img

# Launch main.py
def launch_menu(icon, item):
    launch_script('components/main')



def launch_script(script_name):
    if getattr(sys, 'frozen', False):
        return subprocess.Popen([script_name+'.exe'])  # When frozen
    else:
        return subprocess.Popen([sys.executable, script_name+'.py'])  # When running as script

# Exit tray
def exit_app(icon, item):
    alarm.terminate()
    icon.stop()

# Create and run tray icon
icon = Icon(
    'Memora',
    icon=Image.open('components/icon.png'),
    title='Simple Tray',
    menu=Menu(
        MenuItem('Launch Menu', launch_menu),
        MenuItem('Exit', exit_app)
    )
)
alarm = launch_script('components/alarm_runner')
icon.run()
