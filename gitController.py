import os
import subprocess






# function to check for a substring in a string - returns true or false
def isSubString(string, subString):
    lengthOfSubString = len(subString)
    try:
        for i, j in enumerate(string):
            if(j == subString[0]):
                if(subString == string[i:i+lengthOfSubString]):
                    return True
                else:
                    pass
        return False
    except Exception:
        return False



# function to compare two strings ignoring case changes
def isSubStringsNoCase(string , subString):
    string = string.upper()
    subString = subString.upper()

    subStringList = subString.split()

    count1 = 0
    count2 = 0

    for i in subStringList:
        i = i.strip()
        count1 += 1
        if(isSubString(string , i)):
            count2 += 1
        else:
            return False


    if((count1 == count2) and count1 > 0):
        return True
    else:
        return False









def executeGit(command):

    message = "no message"

    messageFrom = 0

    for i,j in enumerate(command):
        if(j == "-"):
            messageFrom = i
            if(command[i+1] == "m"):
                message = command[i+3:]  
                break      

    if(messageFrom == 0):
        commandForCompare = command
    else:
        commandForCompare = command[:messageFrom]

    if((isSubStringsNoCase(commandForCompare , "log"))):
        print("Generating logs ... , press q to quit , or press ENTER to see more\n\n")
        os.system("git log --graph --oneline --all --decorate")
        return True

    
    if(isSubStringsNoCase(commandForCompare , "commit")):

        # initialising repo
        try:
            result = subprocess.check_output("git init", shell=True)
        except Exception:
            print("failed to git init")
            return True

        if(not(result == b'')):
            print(result)
        print("\n\ninitialised repo..\n")


        # adding
        try:
            result = subprocess.check_output("git add .", shell=True)
        except Exception:
            print("failed to git add .")
            return True

        if(not(result == b'')):
            print(result)
        print("\n\nadded to repo..\n")

        
        # commiting
        stringToPass = "git commit -m " + '"' + message + '"'

        try:
            result = subprocess.check_output(stringToPass, shell=True)
        except Exception:
            print("failed to git commit with message = {}".format(message))
            return True
            
        if(not(result == b'')):
            print(result)
        print("\n\ncommited to repo..\n")

        print("process completed (^_^)")
        return True
        
        

    elif(isSubStringsNoCase(commandForCompare , "all")):
        
        # adding
        try:
            result = subprocess.check_output("git add .", shell=True)
        except Exception:
            print("failed to git add .")
            return True

        if(not(result == b'')):
            print(result)
        print("\n\nadded to repo..\n")

        
        # commiting
        stringToPass = "git commit -m " + '"' + message + '"'

        try:
            result = subprocess.check_output(stringToPass, shell=True)
        except Exception:
            print("failed to git commit with message = {}".format(message))
            return True
            
        if(not(result == b'')):
            print(result)
        print("\n\ncommited to repo..\n")
        
        #pushing
        print("pushing to repo, make sure you are connected to internet ...\n\n")

        try:
            result = subprocess.check_output("git push", shell=True)
        except Exception:
            print("failed to git push")
            return True

        if(not(result == b'')):
            print(result)
        print("\n\npushed to repo..\n")


        print("process completed (^_^)")
        return True

    return False

