import sys, re

if len(sys.argv) != 3 or sys.argv[1] == "":
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    result = re.findall(keyword, text) # ผลลัพธ์ออกมาเป็น list
    print(len(result))