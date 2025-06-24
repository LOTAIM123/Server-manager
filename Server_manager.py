import os

clear = lambda: os.system("cls")
main = "/Server manager"
servers = "/Server manager/servers"
settings = "/Server manager/settings"

mod = "/Server manager/moded"
mloader = "/Server manager/moded/loader"
forge = "/Server manager/moded/loader/forge"
fabric = "/Server manager/moded/loader/fabric"
neoforge = "/Server manager/moded/loader/neoforge"
quilt = "/Server manager/moded/loader/quilt"

vanilla = "/Server manager/vanilla"
vloader = "/Server manager/vanilla/loader"
bukkit = "/Server manager/vanilla/loader/bukkit"
paper    = "/Server manager/vanilla/loader/paper"

again = 0

# mandatory folders

try:
    os.mkdir(main)
    print ("Server manager has been created at C:\Server manager, all server files will be stored here!")
except FileExistsError:
    pass

try:
    os.mkdir(servers)
except FileExistsError:
    pass

try:
    os.mkdir(settings)
except FileExistsError:
    pass

#mod loaders
try:
    os.mkdir(mod)
except FileExistsError:
    pass

try:
    os.mkdir(mloader)
except FileExistsError:
    pass

try:
    os.mkdir(forge)
except FileExistsError:
    pass

try:
    os.mkdir(fabric)
except FileExistsError:
    pass

try:
    os.mkdir(neoforge)
except FileExistsError:
    pass

try:
    os.mkdir(quilt)
except FileExistsError:
    pass


#vanilla loaders
try:
    os.mkdir(vanilla)
except FileExistsError:
    pass

try:
    os.mkdir(vloader)
except FileExistsError:
    pass

try:
    os.mkdir(bukkit)
except FileExistsError:
    pass

try:
    os.mkdir(paper)
except FileExistsError:
    pass

# mandatory folder end

while again == 0:
    clear()
    #start ups
    print ("Welcome to Server manager!")
    print ("")
    print ("What do you want to do?")
    print ("1. Select server to open")
    print ("2. Delete a server")
    print ("3. Create a server")
    print ("4. Open server folder")
    print ("5. INFO")
    print ("0. Exit")
    print ("")


    a1 = int(input("Enter a number from 1-5: "))

    #options
    #open server
    if a1 == 1 :
        print (os.listdir("\Server manager/servers/"))
        c1 = str(input("Select server to open and the open run.bat:"))
        try:
            os.startfile("\Server manager/servers/" + c1)
            con = input("Press enter to return to main menu!")
        except FileNotFoundError:
            print ("Server does not exist!")
            con = input("Press enter to return to main menu!")

    #Delete server
    elif a1 == 2 :
        print (os.listdir("\Server manager/servers/"))
        c1 = str(input("Select server to delete:"))
        try:
            os.rmdir("\Server manager/servers/" + c1)
            print ("Server ",c1,"deleted!")
            con = input("Press enter to return to main menu!")
        except FileNotFoundError:
            print ("Server does not exist!")
            con = input("Press enter to return to main menu!")
    
    #Create server
    elif a1 == 3 :
        c3 = input("Name the server:")
        
        try:
            os.mkdir(main + "/servers/" + c3)
            print ("Server ", c3 ," created succesfuly")
        except FileExistsError:
            print ("Server with this name already exists!")
            print("")
        
        print ("1. Vanilla")
        print ("2. Moded")
        print ("")
        print ("Which loader to use?")
        c4 = int(input())

    #Vanilla setup
        if c4 == 1 :
            print ("You selected Vanilla!")
            print (os.listdir("\Server manager/vanilla/loader"))
            print ("")
            print ("Which exact loader to use?")
            v1 = input()
            os.startfile("\Server manager/vanilla/loader/" + m1 + ".jar")
    
    #Modded setup
        elif c4 == 2 :
            print ("You selected Moded!")
            print (os.listdir("\Server manager/moded/loader"))
            print ("")
            print ("Which exact loader to use?")
            print ("PS:Ignore .log file if its there!")
            print ("")
            m1 = input()
            print (os.listdir("\Server manager/moded/loader/" + m1 + "/"))
            print ("Which version?")
            print ("Write full name and .jar")
            print ("")
            m2 = input()
            os.startfile("\Server manager/moded/loader/" + m1 + "/" + m2) 
            print ("")
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("Select Install server and in the target directory paste:")
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("")
            print ("C:\Server manager\servers/" + c3)
            print ("")
            
            con = input("Press enter when loading process is done!")
            
            try:
                os.rmdir("\Server manager/servers/" + c3 + "/installer.txt")
            except FileNotFoundError:
                pass
            print("Set RAM usage for the server")
            os.startfile("C:\Server manager\servers/" + c3 + "/user_jvm_args.txt")
            
            con = input("Press enter when you are done!")
            
            print("Open the start.bat file and wait for it to complete!")
            os.startfile("C:\Server manager\servers/" + c3)
            
            con = input("Press enter when 1. server start process is done!")
            
            print("")
            print("Do you accept minecraft EULA?")
            print("If you dont accept EULA you wont be able to use the server", c3 , "(Type in a number)")
            print("1.Y")
            print("2.N")
            print("")
            eula = int(input())
            
            if eula == 1 :
            
                file = open ("\Server manager/servers/" + c3 + "/eula.txt", "w")
                file.write("eula=true")
                file.close()
                con = input("You accepted EULA and are now free to start server when needed!")
            else :
                file = open ("\Server manager/servers/" + c3 + "/eula.txt", "w")
                file.write("eula=false")
                file.close()
                con = input("You declined EULA and wont be able to use the server!")

        con = input("Press enter to return to main menu!")
        
    #open server manager folder
    elif a1 == 4 :
        os.startfile ("C:\Server manager")
    
    #INFO
    elif a1 == 5 :
        print("Author: Martins R. Gūža")
        print("To input mods select option 4. and then find the server that you want to put mod in!")
        print("EULA has to be set to true for servers to work!")
        con = input("Press enter to return to main menu!")
    
    #exit
    elif a1 == 0 :
        again = 1
    
x = input("App has crashed! Report this error to https://github.com/LOTAIM123/Server-manager")
