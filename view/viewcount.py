

class view:
    def view_us():
        with open('data/data/data_bk.txt', 'r') as bk:
            bk_ = str(bk.read())
        with open('data/data/data_dp.txt', 'r') as dp:
            dp_ = str(dp.read())
        with open('data/data/data_lunas.txt', 'r') as lunas:
            lunas_ = str(lunas.read())
        with open('data/data/data_total.txt', 'r') as total:
            total_ = str(total.read())
        with open('data/data/data_sisa.txt', 'r') as sisa:
            sisa_ = str(sisa.read())
        print(f'''
         [+] Booking : {bk_}
         [+] Dp : {dp_}
         [+] Lunas : {lunas_}
         [+] Total : {total_}
         [+] Sisa : {sisa_}
         
        ''')



