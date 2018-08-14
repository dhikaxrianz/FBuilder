#!/usr/bin/python
#######################
#  http://fb.com/foxcybertm
import time
time.sleep(1)   
# Delays untuk 1 detik . Kalian dapat ganti angkanya

mess = """\033[31;1m============================================================\033[31;1m
 _  ___ _         ____        _ _     _
| |/ (_) | __ _  | __ ) _   _(_) | __| | ___ _ __
| ' /| | |/ _` | |  _ \| | | | | |/ _` |/ _ \ '__|
\033[37;1m| . \| | | (_| | | |_) | |_| | | | (_| |  __/ |
|_|\_\_|_|\__,_| |____/ \__,_|_|_|\__,_|\___|_|

\033[37;1m============================================================"""
	
print(mess)
print "\033[32;1mFox Tools Builder"
print "\033[32;1mRoBoSkIjR_404 With Lala `Ceper"
print "\033[33;1mMy Team    : Fox Cyber Team "
print "\033[33;1mHalaman FB : http://www.facebook.com/foxcybertm"
print "\033[36;1mHalaman IG : instagram.com/foxcyberteam"
print "\033[36;1mThanks To  : Banyumas Cyber Team | Panda7W7 | Indonesia Security Lite"
print " "
print "               [+]Mulai Buat Tools Builder[+]"
print ""
Nama = raw_input("\033[31;1mNama Tools : ")
Figlet = raw_input("\033[31;1mFiglet     : ")
Author = raw_input("\033[31;1mAuthor     : ")
Team = raw_input("\033[31;1mTeam       : ")
Facebook = raw_input("\033[31;1mFacebook   : ")
Tools = raw_input("\033[31;1mTools No.1 : ")
Tools2 = raw_input("\033[31;1mTools No.2 : ")
Tools3 = raw_input("\033[31;1mTools No.3 : ")
Tag = raw_input("\033[31;1mTag Tools  : ")
Tokped = raw_input("\033[31;1mTokped No  : ")
Jdid = raw_input("\033[31;1mJd.id No   : ")
Phd = raw_input("\033[31;1mPhd No     : ")
keluar = raw_input("\033[31;1mKeluar No   : ")


#Open the Bash
fo = open("Tools.sh","w")

bash1 = """#!/system/xbin/bash
sleep 1
clear
echo "\033[36;1m """

bash2 = Nama

bash3 = """ "
sleep 2
figlet """

bash4 = Figlet
""""""

bash5 = """ 
sleep 2
echo "\033[32;1mAuthor   : """

bash6 = Author

bash7 = """"
sleep 2
echo "Team     : """

bash8 = Team

bash9 = """"
sleep 2
echo "\033[33;1mFacebook : """

bash10 = Facebook

bash11 = """"
sleep 2
echo " "
echo "Tools Ini Menyediakan :"
sleep 2
echo " "
echo "\033[37;1m[ =================== ]"
sleep 1
echo "1. """

bash12 = Tools

bash13 = """ "
echo "\033[37;1m[ =================== ]"
sleep 1
echo "2. """

bash14 = Tools2

bash15 = """ "
echo "\033[37;1m[ =================== ]"
sleep 1
echo "3. """

bash16 = Tools3

bash17 = """ "
echo "\033[37;1m[ =================== ]"
sleep 1
echo " Keluar "
echo "\033[37;1m[ =================== ]"
echo " "
read -p " """

bash18 = Tag

bash19 = """@tools:~#" command """

bash20 = """ 
if [ $command -eq """

bash21= Tokped 

bash22 = """ ];
	then
clear
echo "\033[34;1m"
figlet Spam Tokopedia
php tokped.php
fi

if [ $command -eq """

bash23 = Jdid

bash24 = """ ];
	then
clear
toilet -f mono12 -F gay "Jd.Id"
echo "\033[33;1m"
php 5.php
fi

if [ $command -eq """

bash25 = Phd

bash26 = """ ];
	then
	toilet -f slant --gay Spam PHD
echo "\033[31;1m "
php 4.php
sleep 1
fi

if [ $command -eq """

bash27 = keluar

bash28 = """ ];
	then
	toilet -f slant --gay Fox Cyber
echo "\033[31;1m Sedang Keluar Dari Tools Ini"
sleep 2
echo "\033[32;1m Terima Kasih Telah Menggunakan Tools Kami"
sleep 1
fi
"""
fo.write(bash1)
fo.write(bash2)
fo.write(bash3)
fo.write(bash4)
fo.write(bash5)
fo.write(bash6)
fo.write(bash7)
fo.write(bash8)
fo.write(bash9)
fo.write(bash10)
fo.write(bash11)
fo.write(bash12)
fo.write(bash13)
fo.write(bash14)
fo.write(bash15)
fo.write(bash16)
fo.write(bash17)
fo.write(bash18)
fo.write(bash19)
fo.write(bash20)
fo.write(bash21)
fo.write(bash22)
fo.write(bash23)
fo.write(bash24)
fo.write(bash25)
fo.write(bash26)
fo.write(bash27)
fo.write(bash28)


print " "
print " "
print "\033[33;1mTools.sh Sukses Di Buat"
print " "
print "\033[37;1mTerima Kasih Sudah Menggunakan Tools Kami :')"
