#FILE SYSTEM WITH LOGGING

import os
import platform
import logging

#choose file to store logs and type of logs
logging.basicConfig(filename="pyFiles.log", level=logging.INFO, format='%(levelname)s : %(asctime)s :  %(message)s')


#Filesystem class with all its features as functions

class FileSystem:

    def __init__(self):
        pass

    #To change current directory
    @staticmethod
    def changeDir():
        dir = raw_input("Enter the path to directory: ")
        try:
            os.chdir(dir)               #directory changed
            print("Directory changed!")
        except:
            print("Invalid directory!")

    #To go back a directory
    @staticmethod
    def goBack():
        cmd = ".."
        os.chdir(cmd)       #Return to previous directory

    #To create a new file in current directory
    @staticmethod
    def createFile():
        while True:
            try:
                name = raw_input("Enter file name with extension: ")        #Name of the file
                f = open(name, 'r')                                         #open in read mode if file already exists
                print "File already exists"
            except:
                break
        cmd = 'touch ' + name
        os.system(cmd)
        path = os.getcwd()                                                  #File created
        print "File created successfully."
        logging.info(name + " file was created at " + path)                 #Logging details stored

    #To read a file from current directory
    @staticmethod
    def readFile():
        while True:
            try:
                name = raw_input("Enter file name with extension: ")        #Name of the file to open
                f = open(name, 'r')                                         #Open in read mode
                f.close()                                                   #close the file
                break
            except:
                print "File doesn't exists"                                 #If file doesnt exist
        path = os.getcwd()
        cmd = 'cat ' + name
        logging.info(name + " file was opened for reading from " + path)    #Logs have been stored
        os.system(cmd)

    #TO modify a file in current directory
    @staticmethod
    def modFile():
        while True:
            try:
                name = raw_input("Enter file name with extension: ")        #Name of the file to be modified
                f = open(name, 'r')                                         #check if file exists by opening it
                f.close()
                break
            except:
                print "File doesn't exists"
        path = os.getcwd()
        cmd = "gedit " + name
        os.system(cmd)
        logging.info(name + " file was opened for editing from " + path)    #Logs have been stored

    #To delete a file from current directory
    @staticmethod
    def delFile():
        while True:
            try:
                name = raw_input("Enter file name with extension: ")        #Name of the file to be deleted
                f = open(name, 'r')                                         #Check if file exists by opening it
                f.close()
                break
            except:                                                         #if file does not exist
                print "File doesn't exists"

        cmd = "rm " + name
        choice = raw_input("Are you sure you want to delete the file " + name + " y/n: ")       #confirm to delete the file
        if choice.lower() == "y":
            try:
                #os.system(cmd)
                os.remove(name)                                                                 #if yes then file has been deleted
                print "File deleted successfully."
                path = os.getcwd()
                logging.info(name + " file was deleted from " + path)                           #logs have been stored
            except:
                print "Unable to delete this file."                                             #if some error occurs then return this
        else:
            pass                                                                                #if no then return to main menu

    #To create a directory
    @staticmethod
    def createDir():
        dirname = raw_input("Enter directory name: ")           #Name of the directory
        path = os.getcwd()
        try:
            os.mkdir(dirname)                                   #Directory created
            logging.info(dirname + " directory was created at " + path)         #Logs have been stored
        except:
            print "Unable to create directory."

    #To delete a directory
    @staticmethod
    def delDir():
        dirname = raw_input("Enter directory name: ")           #Name of the directory to be deleted
        cmd = "rm -r " + dirname
        path = os.getcwd()
        choice = raw_input("Are you sure you want to delete the directory " + dirname + " y/n: ")       #Confirm to delete the directory and its files
        if choice.lower() == "y":
            try:
                os.system(cmd)                                                                          #if yes then file has been deleted
                logging.info(dirname + " directory was deleted from " + path)
                print "Directory deleted successfully."
            except:
                print "Unable to delete this directory."                                                #if some error occurs then return this
        else:
            pass                                                                                        #if no then return to main menu

    #To move a file from one directory to another
    @staticmethod
    def mov(flag=0):
        if flag == 0:
            while True:
                try:
                    oldname = raw_input("Enter file name with extension and path: ")                    #Name of the file to be moved with path
                    f = open(oldname, 'r')                                                              #Check if file exists
                    f.close()
                    break
                except:
                    print "File doesn't exists"                                                         #return this if file not found
            newname = raw_input("Enter new path and filename: ")                                        #Name of the new path and file
        else:
            while True:
                try:
                    oldname = raw_input("Enter file name with extension: ")                             #name of the file
                    f = open(oldname, 'r')
                    f.close()
                    break
                except:
                    print "File doesn't exists"
            newname = raw_input("Enter new file name with extention: ")                                 #new name of the file

        try:
            path = os.getcwd()
            os.rename(oldname, newname)                                                                 #Move the file to new path
            logging.info("File  " + oldname + " was renamed/moved to " + newname + "when in path " + path)      #Logs have been stored
        except:
            print "operation failed."                                                                   #If error occurs then return this

    #To shutdown the system upon Failure in Authentication
    @staticmethod
    def shutdown():
        if platform.system() == "Windows":      #if windows system
            os.system("shutdown -s -t 5")

        else:                                   #Other
            os.system("shutdown -h now")

    #To generate and keep logs of all the operations being performed
    @staticmethod
    def log():
        count = 0
        while count < 3:
            passw = raw_input("Enter admin password to view log files: ")                               #For authentication password is required with maximum 3 Attempts
            if passw == "123456":
                os.system("less /home/xerph/Desktop/OS/pyFiles.log")                                    #If right password is entered open the log file
                break
            else:
                count+=1
        if count>=3:                                                                                    #Upon failure in authentication shutdown function is called
            FileSystem.shutdown()


#MAIN PROGRAM

if __name__ == "__main__":
        os.system('clear')
        while True:
            print "\n\n"
            #Print the list of Options available to the user
            print '''
                    "+-------------------------------+"
                    "|   1) Create new directory     |"
                    "|   2) Change directory         |"
                    "|   3) Create new File          |"
                    "|   4) Rename File              |"
                    "|   5) Delete File              |"
                    "|   6) View Directory           |"
                    "|   7) Go to previous Directory |"
                    "|   8) Delete Directory         |"
                    "|   9) Rename Directory         |"
                    "|  10) Move File                |"
                    "|  11) Read File                |"
                    "|  12) Edit File                |"
                    "|  13) Open Log File            |"
                    "|   0) 0 or ctrl + c to Exit    |"
                    "+-------------------------------+"
            '''
            print os.getcwd()
            print "\n"
            while True:
                try:
                    choice = input("Enter your choice: ")               #Check for the users input option number
                    break
                except:
                    print "Invalid choice"                              #if string is given as input
            if choice == 1:
                FileSystem.createDir()
            elif choice == 2:
                FileSystem.changeDir()
            elif choice == 3:
                FileSystem.createFile()
            elif choice == 4:
                FileSystem.mov(1)
            elif choice == 5:
                FileSystem.delFile()
            elif choice == 6:
                cmd = "ls"
                os.system(cmd)
            elif choice == 7:
                FileSystem.goBack()
            elif choice == 8:
                FileSystem.delDir()
            elif choice == 9:
                FileSystem.mov(1)
            elif choice == 10:
                FileSystem.mov()
            elif choice == 11:
                FileSystem.readFile()
            elif choice == 12:
                FileSystem.modFile()
            elif choice == 13:
                FileSystem.log()
            else:                                                       #If none of the listed options has been selected then break
                break


