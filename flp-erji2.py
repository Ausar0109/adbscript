from ADB import AutoDatabank, t180, t365, somedays, swtime, namesstt
from ADB import two_check_time
from datetime import timedelta
from ADB import set_pause
aa = AutoDatabank()


def qllmain(tAs, tIs, tPLs, tpend, ts, te, typee='No'):
    typename = ''

    def cp():
        nonlocal typename
        aa.cp()
        if typee == 'No':
            pass

        elif typee == '-LM':
            typename = '-LM'
            aa.flpdp(5, False, ts, te, erjileimu=ER)
        elif typee == '-JD':
            typename = '-JD'
            aa.tm(1, ts, te, 3)
            aa.tm(3, ts, te, 3)
            aa.dp(12345, ts, te, 3)
        elif typee == '-LL':
            typename = '-LL'
            aa.flpdp(1, False, ts, te, 3, erjileimu=ER)
        elif typee == '-SCJG':
            typename = '-收加'
            aa.flpdp(23, False, ts, te, 3, erjileimu=ER)
        elif typee == '-YS':
            typename = '-预售'
            aa.flpdp(4, False, ts, te, 3, erjileimu=ER)
        elif typee == '-BG':
            typename = '-BG'
            aa.zszw([1, 99], ts, te, 3)
        else:
            typename = typee
            aa.flpdp(5, idd, ts, te)

    peoname = namesstt(tpend)

    # AAAAAA
    cp()
    aa.qll_erjileimu(234, ER, t180, tpend, 3)
    aa.qll_erjileimu(1, ER, tAs, tpend, 3)
    aa.sp('%s-%s类-A人群%s' % (peoname, ER, typename))

    cp()
    aa.qll_erjileimu(234, ER, t180, tpend, 3)
    aa.qll_erjileimu(1, ER, tAs, tpend, 3)
    aa.zszw([1, 99], tAs, tpend, 1, action=2)
    aa.zszw([1, 99], tAs, tpend, 2, action=1)
    aa.mxdp([1, 99], tAs, tpend, 2, action=2)
    aa.mxdp([1, 99], tAs, tpend, 2, action=1)
    aa.dp(12345, tAs, tpend, 2)
    aa.tm(3, tAs, tpend, 2)
    aa.tm(1, tAs, tpend, 2)
    aa.sp('%s-%s类-旗舰A%s' % (peoname, ER, typename))

    cp()
    aa.zszw([1, 99], tAs, tpend, 3, action=2)
    aa.zszw([1, 99], tAs, tpend, 3, action=1)
    aa.mxdp([1, 99], tAs, tpend, 3, action=2)
    aa.mxdp([1, 99], tAs, tpend, 3, action=1)
    aa.dp(12345, tAs, tpend, 3)
    aa.tm(3, tAs, tpend, 3)
    aa.tm(1, tAs, tpend, 3)
    aa.qll_erjileimu(234, ER, t180, tpend, 3)
    aa.qll_erjileimu(1, ER, tAs, tpend, 3)
    aa.sp('%s-%s类-非旗A%s' % (peoname, ER, typename))

    # IIIIII
    cp()
    aa.qll_erjileimu(34, ER, t180, tpend, 3)
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.sp('%s-%s类-I人群%s' % (peoname, ER, typename))

    cp()
    aa.flpdp(23, False, tIs, tpend, 3, erjileimu=ER)
    aa.qll_erjileimu(34, ER, t180, tpend, 1)
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.dp(12345, tIs, tpend, 1)
    aa.tm(3, tIs, tpend, 2)
    aa.tm(1, tIs, tpend, 2)
    aa.sp('%s-%s类-深度I%s' % (peoname, ER, typename))

    cp()
    aa.flpdp(23, False, tIs, tpend, 3, erjileimu=ER)
    aa.qll_erjileimu(34, ER, t180, tpend, 3)
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.dp(12345, tIs, tpend, 1)
    aa.tm(3, tIs, tpend, 2)
    aa.tm(1, tIs, tpend, 2)
    aa.sp('%s-%s类-浅度I%s' % (peoname, ER, typename))

    cp()
    aa.dp(12345, tIs, tpend, 3)
    aa.tm(3, tIs, tpend, 3)
    aa.tm(1, tIs, tpend, 3)
    aa.qll_erjileimu(34, ER, t180, tpend, 3)
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.sp('%s-%s类-非旗I%s' % (peoname, ER, typename))

    # PLLLL
    cp()
    aa.qll_erjileimu(34, ER, t180, tpend, 3)
    aa.sp('%s-%s类-P人群%s' % (peoname, ER, typename))

    cp()
    aa.flpdp(23, False, tPLs, tpend, 3, erjileimu=ER)
    aa.qll_erjileimu(34, ER, t180, tpend, 1)
    aa.sp('%s-%s类-旗舰P%s' % (peoname, ER, typename))

    cp()
    aa.flpdp(23, False, tPLs, tpend, 3, erjileimu=ER)
    aa.qll_erjileimu(34, ER, t180, tpend, 3)
    aa.sp('%s-%s类-非旗P%s' % (peoname, ER, typename))

    # 非二级类目AIPL
    cp()
    aa.qll_erjileimu(1234, ER, t180, tpend, 3)
    aa.dp(1234, t180, tpend, 3)
    aa.sp('%s-非%s类-全部%s' % (peoname, ER, typename))

    cp()
    aa.dp(234, t180, tpend, 3)
    aa.dp(1, tAs, tpend, 3)
    aa.qll_erjileimu(1234, ER, t180, tpend, 1)
    aa.dp(1234, t180, tpend, 3)
    aa.sp('%s-非%s类-之A%s' % (peoname, ER, typename))

    cp()
    aa.dp(34, t180, tpend, 3)
    aa.dp(2, tIs, tpend, 3)
    aa.qll_erjileimu(1234, ER, t180, tpend, 1)
    aa.dp(1234, t180, tpend, 3)
    aa.sp('%s-非%s类-之I%s' % (peoname, ER, typename))

    cp()
    aa.dp(34, t180, tpend, 3)
    aa.qll_erjileimu(1234, ER, t180, tpend, 1)
    aa.dp(1234, t180, tpend, 3)
    aa.sp('%s-非%s类-之P%s' % (peoname, ER, typename))

    # 新增AIPL
    if two_check_time(ts, te):
        cp()
        aa.qll_erjileimu(1234, ER, ts, te, 3)
        aa.dp(1234, t180, tpend, 1)
        aa.dp(1234, ts, te, 3)
        aa.sp('%s-新增-%s类%s' % (peoname, ER, typename))

        cp()
        aa.qll_erjileimu(1234, ER, ts, te, 3)
        aa.dp(1234, t180, tpend, 3)
        aa.dp(1234, ts, te, 3)
        aa.sp('%s-新增-非%s类%s' % (peoname, ER, typename))


if __name__ == '__main__':
    set_pause(0.12, 0.13)
    aa = AutoDatabank(4, False, 'dp')
    aa.mxdp_order = 2
    aa.zszw_order = 4
    aa.brand_name = '飞利浦'

    ER = '腔电'

    tAs = '2019-1-2'
    tIs = t180
    tPLs = t365
    tpend = '2019-3-2'
    ts = '2019-3-3'
    te = '2019-3-9'

    qllmain(tAs, tIs, tPLs, tpend, ts, te,  'No')
    qllmain(tAs, tIs, tPLs, tpend, ts, te,  '-LM')

    idd = '44005916004,538661026488,13756477016,529522757710,529522757710,554777849645,44375843798,38675037654,538581947182'
    qllmain(tAs, tIs, tPLs, tpend, ts, te,  '-刷头')

    idd = '13230519823,520815680412'
    qllmain(tAs, tIs, tPLs, tpend, ts, te,  '-亮白')

    idd = '36416808624,577389016969'
    qllmain(tAs, tIs, tPLs, tpend, ts, te,  '-钻石')

    #qllmain(tAs, tIs, tPLs, tpend, ts, te,  '-JD')
    #qllmain(tAs, tIs, tPLs, tpend, ts, te,  '-LL')
    #qllmain(tAs, tIs, tPLs, tpend, ts, te,  '-SCJG')
    #qllmain(tAs, tIs, tPLs, tpend, ts, te,  '-BG')
