from us import sit
from ui.baner import ban
from view.viewcount import view
from utility.clear import cl
from utility.openfile import open_
import datetime
import os
import subprocess


while True:
    cl.cls()
    ban.b()
    menu = input('cutemi@host~# ')
    if menu == '1':
        while True:
            cl.cls()
            ban.menu_us()
            menuUs = input('cutemi@UpdateSiteplane~#')
            if menuUs == '1':
                sit.bk()
            elif menuUs == '2':
                sit.dp()
            elif menuUs == '3':
                sit.lunas()
            elif menuUs == '4':
                sit.bk_dp()
            elif menuUs == '5':
                sit.ck()
            elif menuUs == '6':
                sit.switch()
            elif menuUs == '7':
                sit.open()
            elif menuUs == 'n':
                open_.txt()
            else:
                break
    elif menu == '2':
        cl.cls()
        ban.banCount()
        view.view_us()
        os.system('timeout /t 10 /nobreak')

    elif menu == '3':
        cl.cls()
        ban.b()
        open_.py()
    else:
        exit()
