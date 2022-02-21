from bluepie import NUSDevice


device = NUSDevice(
    mac_addr="FC:AF:B8:E2:3C:DE",
    enable_logs=False,
    eol="\r\n",
    max_lines_read=3,
)

device.connect(timeout=20)

device.nus_send("get_serial")
print(device.nus_read_lines(max_lines_read=2))
device.nus_send("get_serial")
print(device.nus_read_lines(max_lines_read=2))
device.nus_send("get_serial")
print(device.nus_read_lines(max_lines_read=2))
device.nus_send("get_serial")
print(device.nus_read_lines(max_lines_read=3))

device.disconnect()
