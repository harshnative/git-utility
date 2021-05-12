print("\nexecuting ...\n\n")

import sys
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


    # extracting message from command , message is text after -m 
    message = "no message"

    messageFrom = 0

    for i,j in enumerate(command):

        # finding were is -m
        if(j == "-"):
            messageFrom = i
            if(command[i+1] == "m"):

                # extracting the message
                message = command[i+3:]  
                break
            else:
                messageFrom = 0  

    # if no message is found command will be exact
    if(messageFrom == 0):
        commandForCompare = command

    # if the message is found remove message from the command
    else:
        commandForCompare = command[:messageFrom]


    # if the log command is passed
    if((isSubStringsNoCase(commandForCompare , "log"))):
        print("Generating logs ... , press q to quit , or press ENTER to see more\n\n")
        os.system("git log --graph --oneline --all --decorate")
        return True

    
    # if commit command is passed
    # operations , git init if not , git add . , git commit -m "message"
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
        stringToPass = 'git commit -m ' + '"' + message + '"'

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
        
        
    # all command
    # operations , add , commit , push
    elif(isSubStringsNoCase(commandForCompare , "all")):


        # running the test script first if required
        if((isSubStringsNoCase(commandForCompare , "-t"))):

            exec(open("gituTest.py").read())

            try:
                input("\nContinue ?\n")
            except KeyboardInterrupt:
                print("\nprocess cancelled\n")
                return True

        
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


    # git setup online repo process for setting up online repos
    elif(isSubStringsNoCase(commandForCompare , "setup repo")):

        linkToPush = input("Enter link of online repo : ")
        commitMessage = input("Enter commit message or leave to use default : ")

        linkToPushSplitted = linkToPush.split("/")
        repoName = linkToPushSplitted[-1]
        repoName = "# " + repoName[:-4]
        
        
        # add something to repo if nothing is already present
        try:
            result = subprocess.check_output('echo "{}" >> README.md'.format(repoName), shell=True)
        except Exception:
            print("\nfailed to git init\n")
            return True

        # initialising repo
        try:
            result = subprocess.check_output("git init", shell=True)
        except Exception:
            print("\nfailed to git init\n")
            return True

        if(not(result == b'')):
            print(result)
        print("\n\ninitialised repo..\n")


        # adding
        try:
            result = subprocess.check_output("git add README.md", shell=True)
        except Exception:
            print("\nfailed to git add README.md\n")
            return True

        if(not(result == b'')):
            print(result)
        print("\n\nadded README.md to repo..\n")



        if(commitMessage == ""):
            commitMessage = "first commit"



        # commit
        try:
            result = subprocess.check_output('git commit -m "{}"'.format(commitMessage), shell=True)
        except Exception:
            print('\nfailed to git commit -m "{}""\n'.format(commitMessage))
            return True

        if(not(result == b'')):
            print(result)
        print("\ncommited README.md to repo..\n")


        # change branch to main
        try:
            result = subprocess.check_output('git branch -M main', shell=True)
        except Exception:
            print('failed to git branch -M main')
            return True

        if(not(result == b'')):
            print(result)
        print("\nchanged branch to main\n")



        # setup online repo
        try:
            result = subprocess.check_output('git remote add origin {}'.format(linkToPush), shell=True)
        except Exception:
            print('failed to git remote add origin {}'.format(linkToPush))
            return True

        if(not(result == b'')):
            print(result)
        print("\nadded online repo link\n")



        # pushing first commit
        try:
            result = subprocess.check_output('git push -u origin main', shell=True)
        except Exception:
            print('failed to git push -u origin main')
            return True

        if(not(result == b'')):
            print(result)
        print("\nPushed to repo\n")


        print("\nprocess completed (^_^)\n")





    

    return False


if __name__ == "__main__":
        

    commandListFromCmd = sys.argv

    # deleting first argument
    trimmedCommandListFromCmd = commandListFromCmd[1:]

    # generating string from list arguments
    seperator = " "
    commandString = seperator.join(trimmedCommandListFromCmd)


    if(executeGit(commandString)):
        pass
    else:
        print("\nNo command found")
