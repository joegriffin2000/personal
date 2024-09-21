#filesorting
filename = "modlist.txt"

with open(filename,"r") as f:
    this = f.readlines()

this.sort()

with open(filename,"w") as f:
    f.writelines(this)