# python3 -m install speedtest-cli
# py -m pip install speedtest-cli

import math
import speedtest

def bytes_to_mb(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} Mpbs"

wifi = speedtest.Speedtest()

print("Getting Download Speed...")
download_speed = wifi.download()

print("Getting Upload Speed...")
upload_speed = wifi.upload()

print("Download:", bytes_to_mb(download_speed))
print("Upload", bytes_to_mb(upload_speed))