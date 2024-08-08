file1 = "file1.txt"
file2 = "file2.txt"

f1_name = "file1"
f2_name = "file2"

#file reading
f1 = open(file1).readlines()
f2 = open(file2).readlines()

#file list processing
min_len = len(f1) if len(f1) < len(f2) else len(f2)
compare_list = [[f1[i],f2[i]] for i in range(min_len)]

line_num=0
for i,j in compare_list:
    line_num+=1
    if i != j:
        print(f"Contrast on line {line_num}")
        print(f"{f1_name}:{i}{f2_name}:{j}")
        print("")

#printing how many lines of difference between the two files
print(f"{len(f1)-min_len} lines unchecked") if len(f1) > min_len else print(f"{len(f2)-min_len} lines unchecked")
