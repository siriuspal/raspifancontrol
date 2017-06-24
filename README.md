# raspifancontrol
Simple script to control fan based on ARM temperature. This keeps fan off during light load.

This script uses Pyhton 3. Install Python 3 and pip 3 from repository.
All dependencies should be installed by default. If not install using pip3.

Edit Sudo's Crontab to run the script at startup.

Example - 
`sudo crontab -e`

`@reboot python3 /home/pi/raspifancontrol.py`

This script is set to turn on the fan at 55 deg C and turn it off at 50 deg C.
This gives 5 degrees hysterisis. The temperature is checked every 5 seconds.
