import os
import Configuration
from Classes.ServerConnection import ServerConnection
from Static.StaticData import StaticData

print(r"""
    ____                      __   _____ __                 
   / __ )_________ __      __/ /  / ___// /_____ ___________
  / __  / ___/ __ `/ | /| / / /   \__ \/ __/ __ `/ ___/ ___/
 / /_/ / /  / /_/ /| |/ |/ / /   ___/ / /_/ /_/ / /  (__  ) 
/_____/_/   \__,_/ |__/|__/_/   /____/\__/\__,_/_/  /____/  
                                                            
    """)

if not os.path.exists(f"HexDumpV{Configuration.settings['DumpMajor']}"):
    os.mkdir(f"HexDumpV{Configuration.settings['DumpMajor']}")

StaticData.Preload()

ServerConnection(("0.0.0.0", 9339))