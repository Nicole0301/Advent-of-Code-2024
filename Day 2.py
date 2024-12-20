# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:18:39 2024

@author: WELMSN
"""


def get_values(filename):
    returnval = None
    with open(filename) as In:
        returnval = In.read().splitlines()
    print("Got {} lines from {}.".format(len(returnval),(filename)))
    return returnval

list_values = get_values("C:/Users/nicol/OneDrive/Desktop/Code/Advent of Code/input day 2.txt")

total_count = 0
count = 0

for report in list_values:
    result_list = []
    report_values = report.split()
    report_values = [int(x) for x in report_values]  
    if report_values[0] < report_values[1]:
        for i in range(len(report_values) - 1):
            diff = report_values[i + 1] - report_values[i]
            result_list.append(diff)
    else:
        for i in range(len(report_values) - 1):
            diff = report_values[i] - report_values[i + 1]
            result_list.append(diff)
    total_count += 1
    if any (x < 1 or x > 3 for x in result_list):
        # Try removing one value at a time and repeating checks
        for i in range(len(report_values)):
           dampener_list = report_values[:] 
           dampener_list.pop(i)
           if dampener_list[0] < dampener_list[1]:
               for i in range(len(dampener_list) - 1):
                   diff = dampener_list[i + 1] - dampener_list[i]
                   result_list.append(diff)
           else:
               for i in range(len(dampener_list) - 1):
                   diff = dampener_list[i] - dampener_list[i + 1]
                   result_list.append(diff)
           if any (x < 1 or x > 3 for x in dampener_list):
               print("Not Valid")
               status = "Not Safe"
           else:
                count += 1
                status = "Safe"
    else:
        count += 1
        status = "Safe"
        print("valid")
    f = open("C:/Users/nicol/OneDrive/Desktop/Code/Advent of Code/AOC day 2 Output.txt", "a")
    f.write(str(result_list))
    f.write(status + "\n")
    print(result_list)
print("Total number checked: " + str(total_count))
print("Safe number: " + str(count))
f.write("\nTotal number checked: " + str(total_count))
f.write("\nSafe number: " + str(count))
