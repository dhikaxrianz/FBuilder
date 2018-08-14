#!/system/xbin/bash
sleep 1
clear
echo "[36;1m Kiki Lala "
sleep 2
figlet Khila 
sleep 2
echo "[32;1mAuthor   : Kiki Lala"
sleep 2
echo "Team     : Khila Team"
sleep 2
echo "[33;1mFacebook : fb.com/KhilaTeam"
sleep 2
echo " "
echo "Tools Ini Menyediakan :"
sleep 2
echo " "
echo "[37;1m[ =================== ]"
sleep 1
echo "Tokped"
echo "[37;1m[ =================== ]"
sleep 1
echo "Jd.id"
echo "[37;1m[ =================== ]"
sleep 1
echo "Phd"
echo "[37;1m[ =================== ]"
sleep 1
echo " Keluar "
echo "[37;m[  =================== ]"
echo " "
read -p "Khila@tools:~#" command  
if [ $command -eq 1 ];
	then
clear
echo "[34;1m"
figlet Spam Tokopedia
php tokped.php
fi

if [ $command -eq 2 ];
	then
clear
toilet -f mono12 -F gay "Jd.Id"
echo "[33;1m"
php 5.php
fi

if [ $command -eq 3 ];
	then
	toilet -f slant --gay Spam PHD
echo "[31;1m "
php 
sleep 1
fi

if [ $command -eq 4 ];
	then
	toilet -f slant --gay Fox Cyber
echo "[31;1m Sedang Keluar Dari Tools Ini"
sleep 2
echo "[32;1m Terima Kasih Telah Menggunakan Tools Kami"
sleep 1
fi
