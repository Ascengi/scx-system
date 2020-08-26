echo -e "\e[91mscx system by Ascen'gi\e[0m";
echo -e "";
python  logo.py
echo -e "\e[92m\e[0m";
read -p 'masukan password: ' userinput1;
#
if [ "${userinput1:-}" = "Daisha" ]
then
	cd mod
	python  scx.py
fi
if [ "${userinput1:-}" != "Daisha" ]
then
	echo -e "\e[31mSalah Bego\e[0m";
fi
