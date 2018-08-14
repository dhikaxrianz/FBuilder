#!/system/xbin/bash
clear
echo -n "\033[33;1m "; date +"%d %B %Y"
sleep 1
echo " =================== Welcome To ===================";
figlet FBuilder
sleep 1
echo "\033[33;1m ============= Coded By RoBoSkIjR_404 =============";
sleep 1
echo ""
echo "\033[31;1m Tools  : FBuilder"
sleep 1
echo "\033[33;1m Author : RoBoSkIjR_404 "
sleep 1
echo "\033[32;1m Team   : Fox Cyber"
sleep 1
echo " "
echo "\033[33;1m[ ]------------- MENU -------------[ ]"
sleep 1
echo "\033[36;1m 1. Macam Macam Spam"
sleep 1
echo "\033[33;1m[ ]--------------------------------[ ]"
sleep 1
echo "\033[36;1m 2. Membuat Tools"
sleep 1
echo "\033[33;1m[ ]--------------------------------[ ]"
sleep 1
echo "\033[36;1m 3. Info Tools"
sleep 1
echo "\033[33;1m[ ]--------------------------------[ ]"
sleep 1
echo "\033[36;1m 4. Keluar "
sleep 1
echo "\033[33;1m[ ]----------- FBuilder -----------[ ]"
sleep 1
echo " "
read -p "FBuilder@tools:~# " command
if [ $command -eq 1 ];
	then
clear
echo "Tools Spammer Yang Tersedia :"
sleep 1
figlet 1. Tokopedia
sleep 1
figlet 2. Jd.id
sleep 1
figlet 3. Phd
sleep 5
sh FBuilder.sh
fi

if [ $command -eq 2 ];
	then
clear
python2 aww.py
fi

if [ $command -eq 3 ];
	then
	sleep 1
	echo "Tools Ini Untuk Kalian Yang Ingin Membuat Tools Tapi Tidak Bisa Bahasa Bash"
sleep 1
echo "Thanks To : All Member Fox Cyber Team And Banyumas Cyber Team"
sleep 3
sh FBuilder.sh
fi

if [ $command -eq 4 ];
then
sleep 2
toilet -f slant --gay Fox Cyber
echo "\033[31;1m Sedang Keluar Dari Tools Ini"
sleep 2
echo "\033[32;1m Terima Kasih Telah Menggunakan Tools Kami :)"
sleep 1
fi
