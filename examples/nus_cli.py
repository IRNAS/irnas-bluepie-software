from bluepie import NUSDevice


device = NUSDevice(
    mac_addr="CA:73:48:24:6C:AF",
    enable_logs=True,
    eol="\r\n",
    max_lines_read=3,
    timeout=0.2,
)

device.nus_send("get_serial")
print(device.nus_read_lines(max_lines_read=2))
device.nus_send("get_serial")
print(device.nus_read_lines(max_lines_read=2))
device.nus_send("get_serial")
print(device.nus_read_lines(max_lines_read=2))
device.nus_send("get_serial")
print(device.nus_read_lines(max_lines_read=3))

device.disconnect()
