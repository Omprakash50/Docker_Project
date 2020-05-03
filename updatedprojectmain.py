import os

print("\n\n\t\t\t***Welcome to docker project***")
print("\t\t---------------------------------------------")
os.system("systeactl restart docker")
os.system("systemctl stop firewalld")
os.system("setenforce 0")
while True:
    print("""\n\n\tMenu:
         \tpress 1:Create your own webserver in just one click 
         \tpress 2:Make your own container and make image of that container
         \tpress 3:To create your own network and  change the network of any container
         \tpress 4:To export your container image to another device
         \tpress 5:To upload  your container image to on docker hub
         \tpress 6:To create n numbers of webserver give comman name to all and attach one backup to it
         \tpress 7:Create Wordpress setup in one click with backup
         \tpress 8:To exit""")

    
    ch = int(input("\nPlz enter your choice:"))
    print(ch)
    
    if ch == 1:
        input("It will consume data(appox 250mb to download my image) press enter to continue :")
        print("please wait : ")
        os.system("docker pull omprakash1234/webserver10:v1")
        main_ip = input("\n\nPlease give ip of your system : ")
        name = input("Give any name to your OS : ")
        portno = int(input("please give any four digit unique number don't repeat this number anywhere : "))
        os.system("tput setaf 3")
        print("Write the content you want to show to your client and to save press ctrl+d : ")
        os.system("tput setaf 7")
        os.system("docker run -it --name {}  -p {}:80 omprakash1234/webserver10:v1".format(name ,portno))
        os.system("docker start {}".format(name))
        os.system("iptables -F")
        os.system("iptables -P FORWARD ACCEPT")
        os.system("tput setaf 2")
        print("This is your website ")
        os.system("curl {}:{}/myfile".format(main_ip, portno))
        os.system("tput setaf 7")
        print("you had successfully create your service ")
        os.system("tput setaf 3")
        print("Your URL : http://{}:{}/myfile".format(main_ip,portno))
        os.system("tput setaf 7")
        print("Try it on your mobile brower")


    elif ch == 2:
        name = input("Give any name to your docker container : ")
        wimage = input("Which image you want to use for {} container give image name with its tag : ".format(name))
        iname = input("What name you have to give your image : ")
        os.system("tput setaf 3")
        print(" You are now inside your {} container now you can update it and then exit new {} image will be created : ".format(name , iname))
        os.system("tput setaf 7")
        os.system("docker run -it --name {} {}".format(name, wimage))
        os.system("docker commit {} {}".format(name , iname))
        print("Image {} has successfully created check it :".format(iname))
        print("This is the image you created : ")
        os.system("docker images | grep {}".format(iname))
        
 
    elif ch ==  3:
        check  = int(input(""" 
                           press 1:To create your own network 
                           press 2:To change the network of any container """))
        if check == 1:
            name = input("Please give name to your network : ")
            os.system("docker network create {}".format(name))
            print("successfully created")                                                 
            os.system("docker network ls | grep {}".format(name))


        elif check == 2:
            os.system("docker ps")
            name_os = input("Of which container you have to change network :")
            
            name_net = input("Type the network name of {} to change  : ".format(name_os))
            
            os.system("docker network ls")
            
            name_netnew = input("Now give name of network from the above list that you want to keep instead of {}  :".format(name_net)) 
            os.system("docker network disconnect {} {} ".format(name_net, name_os))
            os.system("docker network connect {} {}".format(name_netnew, name_os))
            print("successfully network changed")
            

        else:
            print("wrong input : ")

    elif ch ==  4:
        ip = input("please give ip address of that device where you want to export : ")
        os.system("docker images")
        image =input("Please type the images along with its tag which you want to export : ")
        filename = input("what name would you like to give to your file : ")
        print("please wait let compelete it")
        os.system("docker save {} -o {}.tar".format(image,filename))
        print("succesfully saved in file {} ".format(filename))
        print("Give password of that device")
        os.system("scp {}.tar root@{}:/root".format(filename,ip))
        print("file has send to that device if that devices has docker then you can use {} image by running following command ".format(image))
        print("docker load -i {}.tar".format(filename))
        print("setenforce 0")
        print("docker run -it {}".format(image))
   
        
    elif ch ==  5:
        
    
        check  = input("Had you register to docker if yes press y else press n : ")
        if check == "y":
            os.system("systemctl start docker")
            os.system("docker login")
            os.system("docker images")
            image = input("which image you want to upload on docker hup type it with its tag :")
            user_name = input("Enter your docker id : ")
            os.system("docker tag {0} {1}/{0}".format(image, user_name))
            print("Please wait")
            os.system("docker push {}/{}".format(user_name, image))
        else:
            print("first go to docker hub and sign up : ")

    elif ch == 6:
        
        name = input("Give any name to the container :")
        no = int( input("How many webserver you want to create : "))
        vname = input("Give name to your storage device for backup : ")
        nick_name = input("Give common name to your all {} webserver : ".format(no))
        image_name = input("Which image you want to use for {} container give image name with its tag : ".format(name))

        print("Please wait : ")
        os.system("docker volume create {}".format(vname))
        os.system("docker network create net")
        for i in range(1, no+1):
            print("container", i)
            os.system("docker run -dit --name {0}{1} --network-alias {2} -v {3} --network net  {4}".format(name, i, nick_name, vname, image_name))
        
        print("successfully created :")

    elif ch == 7:
        main_ip = input("\n\nPlease give ip of your system : ")
        user_name = input("TO sign up give username :")
        passwd = input("Also create password : ") 
        portno = int(input("please give any four digit unique number don't repeat this number : "))

        os.system("docker volume create mysql_storage_{}".format(user_name))
        os.system("docker volume create wp_storage_{}".format(user_name))
        os.system("docker run -d -it -e MYSQL_ROOT_PASSWORD=rootpass              -e MYSQL_USER={0} -e MYSQL_PASSWORD={1}  -e MYSQL_DATABASE=database_{0}                 -v mysql_storage_{0}:/var/lib/mysql  --name myword_{0}     mysql:5.7".format(user_name, passwd))
        os.system("docker run -dit -e WORDPRESS_DB_HOST=myword_{0} -e WORDPRESS_DB_USER={0} -e WORDPRESS_DB_PASSWORD={1} -e WORDPRESS_DB_NAME=database_{0}               -v wp_storage_{0}:/var/www/html --name mysql_{0} -p {2}:80 --link myword_{0}                        wordpress:5.1.1-php7.3-apache".format(user_name, passwd, portno))
        os.system("tput setaf 3")
        print("Your URL : http://{}:{}/myfile".format(main_ip, portno))
        os.system("tput setaf 7")

        check = input("To see info of your webpress type info else press n :")
        if check == "info":
            print("""Username: {0} \n Password: {1} \n Database: database_{0}     \n OS_name: myword_{0} \n Port_no: {2} \n Mysql_volume: mysql_storage_{0}        \n wordprss_vloume: wp_storage_{0}""".format(user_name, passwd, portno))
            

        
    elif ch == 8:
        exit()
    else:
        print("option not supported")
    input("Enter to continue........")
    os.system("clear")






