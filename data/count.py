

class sc:
    def bk():
        with open("data/data/data_bk.txt", 'r') as bk:
            bk_ = int(bk.read())
        ttlbk = int(input("[Booking] Total Kav=> "))
        tbk = bk_ + ttlbk
        print(tbk)
        with open("data/data/data_bk.txt", 'w') as wbk:
            wbk.write(str(tbk))
        with open("data/data/data_total.txt", 'r') as total:
            total_ = int(total.read())
        ttotal = total_ + ttlbk
        with open("data/data/data_total.txt", 'w') as wtotal:
            wtotal.write(str(ttotal))
        with open("data/data/data_sisa.txt", 'r') as sisa:
            sisa_ = int(sisa.read())
        tsisa = sisa_ - ttlbk
        with open("data/data/data_sisa.txt", 'w') as wsisa:
            wsisa.write(str(tsisa))

    def dp():
        with open("data/data/data_bk.txt", 'r') as bk:
            bk_ = int(bk.read())
        ttlbk = int(input("[Dp] Total Kav=> "))
        tbk = bk_ - ttlbk
        print(tbk)
        with open("data/data/data_bk.txt", 'w') as wbk:
            wbk.write(str(tbk))
        with open("data/data/data_dp.txt", 'r') as dp:
            dp_ = int(dp.read())
        tdp = dp_ + ttlbk
        with open("data/data/data_dp.txt", 'w') as wbk:
            wbk.write(str(tdp))

    def lunas():
        with open("data/data/data_dp.txt", 'r') as dp:
            dp_ = int(dp.read())
        ttldp = int(input("[Lunas] Total Kav=> "))
        tldp = dp_ - ttldp
        with open("data/data/data_dp.txt", 'w') as wdp:
            wdp.write(str(tldp))
        with open("data/data/data_lunas.txt", 'r') as lunas:
            lunas_ = int(lunas.read())
        tlunas = lunas_ + ttldp
        with open("data/data/data_lunas.txt", 'w') as wlunas:
            wlunas.write(str(tlunas))

    def bk_dp():
        with open("data/data/data_dp.txt", 'r') as dp:
            dp_ = int(dp.read())
        ttldp = int(input("[Booking + Dp] Total Kav=> "))
        tdp = dp_ + ttldp
        with open("data/data/data_dp.txt", 'w') as wdp:
            wdp.write(str(tdp))
        with open("data/data/data_total.txt", 'r') as total:
            total_ = int(total.read())
        ttotal = total_ + ttldp
        with open("data/data/data_total.txt", 'w') as wtotal:
            wtotal.write(str(ttotal))
        with open("data/data/data_sisa.txt", 'r') as sisa:
            sisa_ = int(sisa.read())
        tsisa = sisa_ - ttldp
        with open("data/data/data_sisa.txt", 'w') as wsisa:
            wsisa.write(str(tsisa))

    def ck():
        with open("data/data/data_lunas.txt", 'r') as lunas:
            lunas_ = int(lunas.read())
        ttllunas = int(input("[CashKeras] Total Kav=> "))
        tlunas = lunas_ + ttllunas
        with open("data/data/data_lunas.txt", 'w') as wlunas:
            wlunas.write(str(tlunas))
        with open("data/data/data_total.txt", 'r') as total:
            total_ = int(total.read())
        ttotal = total_ + ttllunas
        with open("data/data/data_total.txt", 'w') as wtotal:
            wtotal.write(str(ttotal))
        with open("data/data/data_sisa.txt", 'r') as sisa:
            sisa_ = int(sisa.read())
        tsisa = sisa_ - ttllunas
        with open("data/data/data_sisa.txt", 'w') as wsisa:
            wsisa.write(str(tsisa))


class op:
    def bk():
        with open("data/data/data_bk.txt", 'r') as bk:
            bk_ = int(bk.read())
        opbk = int(input("[Booking] Total Open Kav=> "))
        tbk = bk_ - opbk
        print(tbk)
        with open("data/data/data_bk.txt", 'w') as wbk:
            wbk.write(str(tbk))
        with open("data/data/data_total.txt", 'r') as total:
            total_ = int(total.read())
        ttotal = total_ - opbk
        with open("data/data/data_total.txt", 'w') as wtotal:
            wtotal.write(str(ttotal))
        with open("data/data/data_sisa.txt", 'r') as sisa:
            sisa_ = int(sisa.read())
        tsisa = sisa_ + opbk
        with open("data/data/data_sisa.txt", 'w') as wsisa:
            wsisa.write(str(tsisa))

    def dp():
        with open("data/data/data_dp.txt", 'r') as dp:
            dp_ = int(dp.read())
        opdp = int(input("[Dp] Total Open Kav=> "))
        tdp = dp_ - opdp
        with open("data/data/data_dp.txt", 'w') as wdp:
            wdp.write(str(tdp))
        with open("data/data/data_total.txt", 'r') as total:
            total_ = int(total.read())
        ttotal = total_ - opdp
        with open("data/data/data_total.txt", 'w') as wtotal:
            wtotal.write(str(ttotal))
        with open("data/data/data_sisa.txt", 'r') as sisa:
            sisa_ = int(sisa.read())
        tsisa = sisa_ + opdp
        with open("data/data/data_sisa.txt", 'w') as wsisa:
            wsisa.write(str(tsisa))

    def lunas():
        with open("data/data/data_lunas.txt", 'r') as lunas:
            lunas_ = int(lunas.read())
        oplunas = int(input("[Booking] Total Open Kav=> "))
        tlunas = lunas_ - oplunas
        with open("data/data/data_lunas.txt", 'w') as wlunas:
            wlunas.write(str(tlunas))
        with open("data/data/data_total.txt", 'r') as total:
            total_ = int(total.read())
        ttotal = total_ - oplunas
        with open("data/data/data_total.txt", 'w') as wtotal:
            wtotal.write(str(ttotal))
        with open("data/data/data_sisa.txt", 'r') as sisa:
            sisa_ = int(sisa.read())
        tsisa = sisa_ + oplunas
        with open("data/data/data_sisa.txt", 'w') as wsisa:
            wsisa.write(str(tsisa))
