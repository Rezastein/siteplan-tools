from ui.baner import ban
from data.count import sc
from data.count import op
import datetime
file1 = open('data/data/data.txt', 'a')
date = datetime.datetime.now()


class sit:
    def bk():
        z = 'Zamrud'
        r = 'Ruby'
        s = 'Sapphire'
        k = 'Kalimaya'
        t = 'Topaz'
        while True:
            ban.type_()
            menu_type = input('Type: ~# ')
            if menu_type == '1':
                type_ = z
                break
            elif menu_type == '2':
                type_ = r
                break
            elif menu_type == '3':
                type_ = s
                break
            elif menu_type == '4':
                type_ = k
                break
            elif menu_type == '5':
                type_ = t
                break
            else:
                exit()
        bk_b = input("[Booking] Blok => ")
        bk_n = input("[Booking] No => ")
        bk_print = [
            f'{date}\nTipe *({type_})* Blok *{bk_b}* No. *{bk_n}* *_BOOKING_*\n']
        sc.bk()
        file1.writelines(bk_print)
        file1.close()

    def dp():
        z = 'Zamrud'
        r = 'Ruby'
        s = 'Sapphire'
        k = 'Kalimaya'
        t = 'Topaz'
        while True:
            ban.type_()
            menu_type = input('Type: ~# ')
            if menu_type == '1':
                type_ = z
                break
            elif menu_type == '2':
                type_ = r
                break
            elif menu_type == '3':
                type_ = s
                break
            elif menu_type == '4':
                type_ = k
                break
            elif menu_type == '5':
                type_ = t
                break
            else:
                exit()
        dp_b = input("[Dp] Blok => ")
        dp_n = input("[Dp] No => ")
        dp_print = [
            f'{date}\nTipe *({type_})* Blok *{dp_b}* No. *{dp_n}* *_DP_*\n']
        sc.dp()
        file1.writelines(dp_print)
        file1.close()

    def lunas():
        z = 'Zamrud'
        r = 'Ruby'
        s = 'Sapphire'
        k = 'Kalimaya'
        t = 'Topaz'
        while True:
            ban.type_()
            menu_type = input('Type: ~# ')
            if menu_type == '1':
                type_ = z
                break
            elif menu_type == '2':
                type_ = r
                break
            elif menu_type == '3':
                type_ = s
                break
            elif menu_type == '4':
                type_ = k
                break
            elif menu_type == '5':
                type_ = t
                break
            else:
                exit()
        lunas_b = input("[Lunas] Blok => ")
        lunas_n = input("[Lunas] No => ")
        lunas_print = [
            f'{date}\nTipe *({type_})* Blok *{lunas_b}* No. *{lunas_n}* *_LUNAS_*\n']
        sc.lunas()
        file1.writelines(lunas_print)
        file1.close()

    def bk_dp():
        z = 'Zamrud'
        r = 'Ruby'
        s = 'Sapphire'
        k = 'Kalimaya'
        t = 'Topaz'
        while True:
            ban.type_()
            menu_type = input('Type: ~# ')
            if menu_type == '1':
                type_ = z
                break
            elif menu_type == '2':
                type_ = r
                break
            elif menu_type == '3':
                type_ = s
                break
            elif menu_type == '4':
                type_ = k
                break
            elif menu_type == '5':
                type_ = t
                break
            else:
                exit()
        bk_dp_b = input("[Booking + Dp] Blok => ")
        bk_dp_n = input("[Booking + Dp] No => ")
        bk_dp_print = [
            f'{date}\nTipe *({type_})* Blok *{bk_dp_b}* No. *{bk_dp_n}* *_BOOKING + DP_*\n']
        sc.bk_dp()
        file1.writelines(bk_dp_print)
        file1.close()

    def ck():
        z = 'Zamrud'
        r = 'Ruby'
        s = 'Sapphire'
        k = 'Kalimaya'
        t = 'Topaz'
        while True:
            ban.type_()
            menu_type = input('Type: ~# ')
            if menu_type == '1':
                type_ = z
                break
            elif menu_type == '2':
                type_ = r
                break
            elif menu_type == '3':
                type_ = s
                break
            elif menu_type == '4':
                type_ = k
                break
            elif menu_type == '5':
                type_ = t
                break
            else:
                exit()
        ck_b = input("[Cash Keras] Blok => ")
        ck_n = input("[Cash Keras] No => ")
        ck_print = [
            f'{date}\nTipe *({type_})* Blok *{ck_b}* No. *{ck_n}* *_CASH KERAS_*\n']
        file1.writelines(ck_print)
        file1.close()
        sc.ck()
        while True:
            verify_ = input("[ck] Open [y/n]")
            if verify_ == 'y':
                ban.us()
                type_open = input('\n==>')
                if type_open == '1':
                    op.bk()
                elif type_open == '2':
                    op.dp()
                elif type_open == '3':
                    op.lunas()
            else:
                break

    def switch():
        z = 'Zamrud'
        r = 'Ruby'
        s = 'Sapphire'
        k = 'Kalimaya'
        t = 'Topaz'
        while True:
            ban.type_()
            menu_type = input('Type: ~# ')
            if menu_type == '1':
                type_ = z
                break
            elif menu_type == '2':
                type_ = r
                break
            elif menu_type == '3':
                type_ = s
                break
            elif menu_type == '4':
                type_ = k
                break
            elif menu_type == '5':
                type_ = t
                break
            else:
                exit()
        type_awal = input('[Pindah] Tipe Awal =>')
        a_switch = input('[Pindah] Blok Awal =>')
        b_switch = input('[Pindah] No Awal =>')
        switch_b = input("[Pindah] Blok => ")
        switch_n = input("[Pindah] No => ")
        switch_print = [
            f'{date}\nTipe *({type_awal})* Blok *{a_switch}* No. *{b_switch}* \n *_PINDAH_* \n Tipe *({type_})* Blok *{switch_b}* No. *{switch_n}*\n']

        file1.writelines(switch_print)
        file1.close()

    def open():
        z = 'Zamrud'
        r = 'Ruby'
        s = 'Sapphire'
        k = 'Kalimaya'
        t = 'Topaz'
        while True:
            ban.type_()
            menu_type = input('Type: ~# ')
            if menu_type == '1':
                type_ = z
                break
            elif menu_type == '2':
                type_ = r
                break
            elif menu_type == '3':
                type_ = s
                break
            elif menu_type == '4':
                type_ = k
                break
            elif menu_type == '5':
                type_ = t
                break
            else:
                exit()
        open_b = input("[Open] Blok => ")
        open_n = input("[Open] No => ")
        open_print = [
            f'{date}\nTipe *({type_})* Blok *{open_b}* No. *{open_n}* *_OPEN_*\n']
        file1.writelines(open_print)
        file1.close()

        ban.us()
        type_open = input('\n==>')
        if type_open == '1':
            op.bk()
        elif type_open == '2':
            op.dp()
        elif type_open == '3':
            op.lunas()
        else:
            file1.close()
            exit()
