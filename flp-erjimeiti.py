from ADB import AutoDatabank, t180, t365, somedays, swtime, namesstt
from datetime import timedelta
from ADB import set_pause

aa = AutoDatabank(4, False, 'dp')
aa.mxdp_order = 5
aa.zszw_order = 7


def qllmain(ts, te, tpend, typee=1):
    # tpend 决定沉淀人群时间
    tAs = somedays('2019-5-31', (60 - 1))  # A人群计算时间60天
    tIs = somedays('2019-5-31', (180 - 1))  # t180

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
    aa.qll_erjileimu(1, ER, tAs, tpend, 3)
    aa.qll(234, t180, tpend, 1)
    aa.qll(1, tAs, tpend, 3)
    aa.sp('%s-%s类目A%s' % (peoname, ER, typename))

    cp()
    aa.qll_erjileimu(1, ER, tAs, tpend, 3)
    aa.qll(234, t180, tpend, 1)
    aa.qll(1, tAs, tpend, 3)

    aa.wt(1, tAs, tpend, 1)
    aa.mxdp([1, 99], tAs, tpend, 2, action=2)
    aa.mxdp([1, 99], tAs, tpend, 2, action=1)
    aa.zszw([1, 99], tAs, tpend, 2, action=2)
    aa.zszw([1, 99], tAs, tpend, 2, action=1)
    aa.dp(1, tAs, tpend, 2)
    aa.tm(1, tAs, tpend, 2)
    aa.sp('%s-%s旗舰A%s' % (peoname, ER, typename))

    cp()
    aa.wt(1, tAs, tpend, 3)
    aa.mxdp([1, 99], tAs, tpend, 3, action=2)
    aa.mxdp([1, 99], tAs, tpend, 3, action=1)
    aa.zszw([1, 99], tAs, tpend, 3, action=2)
    aa.zszw([1, 99], tAs, tpend, 3, action=1)
    aa.dp(1, tAs, tpend, 3)
    aa.tm(1, tAs, tpend, 3)

    aa.qll_erjileimu(1, ER, tAs, tpend, 3)
    aa.qll(234, t180, tpend, 1)
    aa.qll(1, tAs, tpend, 3)
    aa.sp('%s-%s非旗A%s' % (peoname, ER, typename))

    cp()
    aa.qll_erjileimu(1, ER, tAs, tpend, 3)
    aa.qll(234, t180, tpend, 3)
    aa.qll(1, tAs, tpend, 3)
    aa.sp('%s-非%s类目A%s' % (peoname, ER, typename))

    cp()
    aa.qll_erjileimu(1, ER, tAs, tpend, 3)
    aa.qll(234, t180, tpend, 3)
    aa.qll(1, tAs, tpend, 3)

    aa.wt(1, tAs, tpend, 1)
    aa.mxdp([1, 99], tAs, tpend, 2, action=2)
    aa.mxdp([1, 99], tAs, tpend, 2, action=1)
    aa.zszw([1, 99], tAs, tpend, 2, action=2)
    aa.zszw([1, 99], tAs, tpend, 2, action=1)
    aa.dp(1, tAs, tpend, 2)
    aa.tm(1, tAs, tpend, 2)
    aa.sp('%s-非%s旗舰A%s' % (peoname, ER, typename))

    cp()
    aa.wt(1, tAs, tpend, 3)
    aa.mxdp([1, 99], tAs, tpend, 3, action=2)
    aa.mxdp([1, 99], tAs, tpend, 3, action=1)
    aa.zszw([1, 99], tAs, tpend, 3, action=2)
    aa.zszw([1, 99], tAs, tpend, 3, action=1)
    aa.dp(1, tAs, tpend, 3)
    aa.tm(1, tAs, tpend, 3)

    aa.qll_erjileimu(1, ER, tAs, tpend, 3)
    aa.qll(234, t180, tpend, 3)
    aa.qll(1, tAs, tpend, 3)
    aa.sp('%s-非%s非旗A%s' % (peoname, ER, typename))

    # IIIII
    cp()
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.qll(34, t180, tpend, 1)
    aa.qll(2, tIs, tpend, 3)
    aa.sp('%s-%s类目I%s' % (peoname, ER, typename))

    cp()
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.qll(34, t180, tpend, 1)
    aa.qll(2, tIs, tpend, 3)
    aa.dp(123, tIs, tpend, 1)
    aa.tm(2, tIs, tpend, 2)
    aa.tm(1, tIs, tpend, 2)
    aa.sp('%s-%s旗舰I%s' % (peoname, ER, typename))

    cp()
    aa.flpdp(23, False, tIs, tpend, erjileimu=ER, jbc=3)
    aa.qll_erjileimu(2, ER, tIs, tpend, 1)
    aa.qll(34, t180, tpend, 1)
    aa.qll(2, tIs, tpend, 3)
    aa.dp(123, tIs, tpend, 1)
    aa.tm(2, tIs, tpend, 2)
    aa.tm(1, tIs, tpend, 2)
    aa.sp('%s-%s旗深度I%s' % (peoname, ER, typename))

    cp()
    aa.flpdp(23, False, tIs, tpend, erjileimu=ER, jbc=3)
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.qll(34, t180, tpend, 1)
    aa.qll(2, tIs, tpend, 3)
    aa.dp(123, tIs, tpend, 1)
    aa.tm(2, tIs, tpend, 2)
    aa.tm(1, tIs, tpend, 2)
    aa.sp('%s-%s旗浅度I%s' % (peoname, ER, typename))

    cp()
    aa.dp(123, tIs, tpend, 3)
    aa.tm(2, tIs, tpend, 3)
    aa.tm(1, tIs, tpend, 3)
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.qll(34, t180, tpend, 1)
    aa.qll(2, tIs, tpend, 3)
    aa.sp('%s-%s非旗I%s' % (peoname, ER, typename))

    cp()
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.qll(34, t180, tpend, 3)
    aa.qll(2, tIs, tpend, 3)
    aa.sp('%s-非%s类目I%s' % (peoname, ER, typename))

    cp()
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.qll(34, t180, tpend, 3)
    aa.qll(2, tIs, tpend, 3)
    aa.dp(123, tIs, tpend, 1)
    aa.tm(2, tIs, tpend, 2)
    aa.tm(1, tIs, tpend, 2)
    aa.sp('%s-非%s旗舰I%s' % (peoname, ER, typename))

    cp()
    aa.dp(123, tIs, tpend, 3)
    aa.tm(2, tIs, tpend, 3)
    aa.tm(1, tIs, tpend, 3)
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.qll(34, t180, tpend, 3)
    aa.qll(2, tIs, tpend, 3)
    aa.sp('%s-非%s非旗I%s' % (peoname, ER, typename))

    # PLLLL
    cp()
    aa.qll_erjileimu(34, ER, t180, tpend, 3)
    aa.qll(34, t180, tpend, 1)
    aa.sp('%s-%s类目PL%s' % (peoname, ER, typename))

    cp()
    aa.flpdp(5, False, t365, tpend, 3, erjileimu=ER)
    aa.qll_erjileimu(34, ER, t180, tpend, 1)
    aa.qll(34, t180, tpend, 1)
    aa.sp('%s-%s类目旗舰PL%s' % (peoname, ER, typename))

    cp()
    aa.flpdp(5, False, t365, tpend, 3, erjileimu=ER)
    aa.qll_erjileimu(34, ER, t180, tpend, 3)
    aa.qll(34, t180, tpend, 1)
    aa.sp('%s-%s类目非旗PL%s' % (peoname, ER, typename))

    cp()
    aa.qll_erjileimu(34, ER, t180, tpend, 3)
    aa.qll(34, t180, tpend, 3)
    aa.sp('%s-非%s类目PL%s' % (peoname, ER, typename))

    cp()
    aa.dp(5, t365, tpend, 3)
    aa.qll_erjileimu(34, ER, t180, tpend, 1)
    aa.qll(34, t180, tpend, 3)
    aa.sp('%s-非%s类目旗舰PL%s' % (peoname, ER, typename))

    cp()
    aa.dp(5, t365, tpend, 3)
    aa.qll_erjileimu(34, ER, t180, tpend, 3)
    aa.qll(34, t180, tpend, 3)
    aa.sp('%s-非%s类目非旗PL%s' % (peoname, ER, typename))


if __name__ == '__main__':
    set_pause(0.15, 0.15)
    ER = '剃须刀'

    tpend = '2019-4-17'
    ts = '2019-3-3'
    te = '2019-3-9'

    qllmain(ts, te, tpend, 'No')
    #qllmain(ts, te, tpend, '-LM')

    idd = '35257447217,559361633331,551067058794,567714272617,575033120742'
    #qllmain(ts, te, tpend, '-低端')

    #qllmain(ts, te, tpend, '-JD')
    #qllmain(ts, te, tpend, '-LL')
    #qllmain(ts, te, tpend, '-SCJG')
    #qllmain(ts, te, tpend, '-BG')
