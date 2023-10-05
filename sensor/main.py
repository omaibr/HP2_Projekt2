import machine
import json
import time
import onewire
import ds18x20

pico_id = machine.unique_id()

with open("config.json", "r") as config_file:
    config_data = json.load(config_file)

pin = config_data.get("pin")
interval = config_data.get("interval")

ds_pin = machine.Pin(pin)
sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = sensor.scan()

while True:

    sensor.convert_temp() # Starta temperaturmätningen
    time.sleep_ms(interval)

    for rom in roms: 
        temp = sensor.read_temp(rom)# Läs temperaturen från den aktuella sensorn
        print(f"{pico_id.hex()} {rom.hex()} {temp:.2f}")