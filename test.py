import os 

dir = r"C:\Users\jiang-laptop\Downloads\test"

listDir = os.listdir(dir) 
for fileName in listDir: 
    origName = os.path.join(dir, fileName)
    replName = os.path.join(dir, fileName.lower()).replace("_", " ")
    replName = replName.replace("（", "").replace("）", "").replace("(", "").replace(")", "")
    replName = replName.replace("《", "").replace("》", "").replace("<", "").replace(">", "")
    replName = replName.replace("〔", "").replace("〕", "")
    replName = replName.replace("][", "-")
    replName = replName.replace("[", "-").replace("]", "-")
    replName = replName.replace("“", "").replace("”", "")
    replName = replName.replace("\"", "")
    replName = replName.replace("、", "").replace("！", "").replace("!", "")
    replName = replName.replace("：", "").replName.replace(":", "").replace("；", "")
    replName = replName.replace(". ", " ")
    replName = replName.replace(" - ", "-").replace("－", "-")
    replName = replName.replace(", ", " ").replace("，", "").replace("．", "")
    replName = replName.replace("'", "").replace("’", "").replace("‘", "")
    # for specific article abbrevations.
    replNameSuffix, replNamePrefix = replName[-7:], replName[:-7]
    replNamePrefix = replNamePrefix.replace(".-", "-").replace(".", " ")
    replName = replNamePrefix + replNameSuffix
    # special rule
    replName = replName.replace("ieeetrans", "ieee trans").replace("smartgrid", "smart grid").replace("powersyst", "power syst")
    isSame = origName == replName
    if not isSame:
        print(fileName)
        os.rename(origName, replName)
        # ans = input("lower this file and remove _? Y/N \n")
        # if ans == "Y":
            # os.rename(origName, replName)
    else:
        pass

