import os

message  = os.popen("adb shell am start -W -n com.alibaba.android.rimet/.biz.LaunchHomeActivity")
print("hahah")
# for line in message.readlines():
#     if "ThisTime" in line:
#         print(line.split(":")[1])