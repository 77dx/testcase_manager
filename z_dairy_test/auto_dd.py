import os

message  = os.popen("adb shell am start -W -n com.alibaba.android.rimet/.biz.LaunchHomeActivity")
# print("hahah")
# for line in message.readlines():
#     if "ThisTime" in line:
#         print(line.split(":")[1])


#冒泡排序法
"""
冒泡排序法，是通过2个嵌套循环实现排序的。外循环是排序趟数，列表的长度；内循环为每趟比较的次数，len-i次。相邻的两个元素比较，若逆序则交换位置。
"""
l = [5,89,245,45,25]

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(0,len(list)-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

ls = bubble_sort(l)
print(ls)