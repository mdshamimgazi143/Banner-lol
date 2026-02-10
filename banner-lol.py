#!/data/data/com.termux/files/usr/bin/python3
import os
import sys
import time
from datetime import datetime

def print_banner():
    # Clear screen
    os.system('clear')
    
    # Colors for Termux (ANSI escape codes)
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'end': '\033[0m'
    }
    
    # Your custom banner design
    banner = f"""
{colors['cyan']}╔════════════════════════════════════════╗
║                                            ║
║    {colors['green']}╔═╗╔═╗╦═╗╔═╗╔╦╗╔═╗╦  ╦        {colors['cyan']}║
║    {colors['green']}╚═╗║ ║╠╦╝║╣  ║ ║╣ ╚╗╔╝        {colors['cyan']}║
║    {colors['green']}╚═╝╚═╝╩╚═╚═╝ ╩ ╚═╝ ╚╝         {colors['cyan']}║
║                                            ║
╠════════════════════════════════════════╣
║    {colors['yellow']}• Termux User •                    {colors['cyan']}║
║    {colors['yellow']}• Python Powered •                 {colors['cyan']}║
║                                            ║
╚════════════════════════════════════════╝{colors['end']}
"""
    
    print(banner)
    
    # System information
    print(f"{colors['bold']}{colors['blue']}System Information:{colors['end']}")
    print(f"{colors['green']}• Time: {colors['white']}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{colors['green']}• User: {colors['white']}{os.getenv('USER', 'termux')}")
    print(f"{colors['green']}• Home: {colors['white']}{os.getenv('HOME', '/data/data/com.termux/files/home')}")
    
    # Python info
    print(f"\n{colors['bold']}{colors['purple']}Python Info:{colors['end']}")
    print(f"{colors['yellow']}• Python {colors['white']}{sys.version.split()[0]}")
    print(f"{colors['yellow']}• Platform: {colors['white']}{sys.platform}")
    
    # Tips
    print(f"\n{colors['bold']}{colors['cyan']}Quick Tips:{colors['end']}")
    print(f"{colors['white']}• Type {colors['green']}pkg list-all{colors['white']} to see available packages")
    print(f"• Type {colors['green']}python --help{colors['white']} for Python help")
    print(f"• Type {colors['green']}exit{colors['white']} to close session")

def main():
    print_banner()
    
    # Optional: Display for a few seconds then clear
    # time.sleep(5)
    # os.system('clear')
    
if __name__ == "__main__":
    main()