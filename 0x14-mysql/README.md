## Alex Africa Assignment
0x14-mysql

## Author
Mikias Gedlu
AddisERP System Solutions

## Requirements


    MySQL distribution must be 5.7.x
    Make sure that task #3 of your SSH project is completed for web-01 and web-02. The checker will connect to your servers to check MySQL status
    Please make sure you have your README.md pushed to GitHub.

## Installing Mysql 5.7.*


# Download the MySQL repository by executing the following command:

$ wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb

$ sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb

- select ubuntu bionic
- select mysql 5.7 
- click ok

$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A8D3785C
$ sudo apt update
$ sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

Done !!


Note
If you encounter the "signature couldn't be verified" error like this one: NO_PUBKEY 467B942D3A79BD29, you will need to import the missing gpg key by running the following command:

this is becouse the key expired on 14/12/2023, so you shoud repace with this command

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A8D3785C


