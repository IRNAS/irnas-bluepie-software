from rich import print

from bluepie import BLEDevice

device = BLEDevice(mac_addr="CA:73:48:24:6C:AF", enable_logs=True)

device.connect()

print(device.list_services())

device.disconnect()
