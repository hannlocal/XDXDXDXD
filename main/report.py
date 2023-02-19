""" 
Before changing the program and publishing it somewhere, please
Please note that this program is under GPLv3 license.
More information:
https://tr.wikipedia.org/wiki/gnu_genel_kamu_lisans%c4%b1
https://www.gnu.org/licenses/quick-guide-gplv3.html
"""

__author__ = "@runboichi"
__license__ = "GPLv3"
__version__ = "0.2"
__status__ = "bypass"

from time import time, sleep
from random import choice
from multiprocessing import Process

from libs.utils import CheckPublicIP, IsProxyWorking
from libs.utils import PrintStatus, PrintSuccess, PrintError
from libs.utils import PrintBanner, GetInput, PrintFatalError
from libs.utils import LoadUsers, LoadProxies, PrintChoices

from libs.instaclient import InstaClient

USERS = []
PROXIES = []

def MultiThread(username, userid, loginuser, loginpass, proxy, reasonid):
    client = None
    if (proxy != None):
        PrintStatus("[" + loginuser + "]", "Hesaba Giriş Yapıldı!")
        client = InstaClient(
            loginuser,
            loginpass,
            proxy["ip"],
            proxy["port"]
        )
    else:
        PrintStatus("[" + loginuser + "]", "Hesaba Giriş Yapıldı!")
        client = InstaClient(
            loginuser,
            loginpass,
            None,
            None
        )
        
    client.Connect()
    client.Login()
    client.Spam(userid, username, reasonid)
    print("")

def NoMultiThread():
    for user in USERS:
        client = None
        if (useproxy):
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Hesaba Giriş Yapılıyor!")
            client = InstaClient(
                user["user"],
                user["password"],
                proxy["ip"],
                proxy["port"]
            )
        else:
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Hesaba Giriş Yapılıyor!")
            client = InstaClient(
                user["user"],
                user["password"],
                None,
                None
            )
        
        client.Connect()
        client.Login()
        client.Spam(userid, username, reasonid)
        print("")


if __name__ == "__main__":
    PrintBanner()
    PrintStatus("Kullanıcılar Yükleniyor...")
    USERS = LoadUsers("./users.txt")
    PrintStatus("Proxy Yükleniyor...")
    PROXIES = LoadProxies("./proxy.txt")
    print("")

    username = GetInput("şikayet etmek istediğiniz hesabın kullanıcı adını girin :")
    userid = GetInput("Şikayet etmek istediğiniz rapor sayısı :")
    useproxy = GetInput("Proxy kullanmak istiyor musunuz? [Evet Hayır]:")
    if (useproxy == "evet"):
        useproxy = True
    elif (useproxy == "hayır"):
        useproxy = False
    else:
        PrintFatalError("Lütfen sadece 'evet' veya 'hayır' girin!")
        exit(0)
    usemultithread = GetInput("Çoklu iş parçacığı kullanmak istiyor musunuz? [Evet / Hayır] (Çok fazla kullanıcınız varsa veya bilgisayarınız yavaşsa bu özelliği kullanmayın!):")
    
    if (usemultithread == "evet"):
        usemultithread = True
    elif (usemultithread == "hayır"):
        usemultithread = False
    else:
        PrintFatalError("Lütfen sadece 'Evet' veya 'Hayır' girin!")
        exit(0)
    
    PrintChoices()
    reasonid = GetInput("Lütfen yukarıdaki şikayetin nedenlerinden birini seçin (ör: spam için 1):")

    
    
    
    print("")
    PrintStatus("Başlatılıyor!")
    print("")

    if (usemultithread == False):
        NoMultiThread()
    else:
        for user in USERS:
            p = Process(target=MultiThread,
                args=(username,
                    userid,
                    user["user"],
                    user["password"],
                    None if useproxy == False else choice(PROXIES),
                    reasonid
                )
            )
            p.start() 
   

