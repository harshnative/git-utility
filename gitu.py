print("\nexecuting ...\n\n")

import sys
import gitController

commandListFromCmd = sys.argv

# deleting first argument
trimmedCommandListFromCmd = commandListFromCmd[1:]

# generating string from list arguments
seperator = " "
commandString = seperator.join(trimmedCommandListFromCmd)


if(gitController.executeGit(commandString)):
    pass
else:
    print("\nNo command found")
