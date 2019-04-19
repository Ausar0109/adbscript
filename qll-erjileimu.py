from ADB import AutoDatabank, t180, t365, somedays, swtime, namesstt
from datetime import timedelta


aa = AutoDatabank(4, False, 'dp')
ER = '口腔电子'


def qllmain(ts, te, idd, jbc=1):
    tpend = swtime(ts, False) - timedelta(1)
    peoname = namesstt(tpend)
    iddname = str(idd)[:4]
    jbcname = ''

    def cp():
        nonlocal jbcname
        aa.cp()
        if jbc == 2:
            pass
        else:
            aa.flpdp(5, idd, ts, te, jbc)
            jbcname = '【购'

    cp()
    aa.qll_erjileimu(34, ER, t180, tpend, jbc)
    aa.sp('%s-%s-二级类目PL%s' % (peoname, iddname, jbcname))

    cp()
    aa.qll_erjileimu(34, ER, t180, tpend, jbc)
    aa.qll(34, t180, tpend, 3)
    aa.sp('%s-%s-其他类目PL%s' % (peoname, iddname, jbcname))

    cp()
    aa.flpdp(123, idd, t180, tpend, jbc)
    aa.qll_erjileimu(34, ER, t180, tpend, 1)
    aa.qll_erjileimu(2, ER, t180, tpend, 3)
    aa.sp('%s-%s-单品兴趣I%s' % (peoname, iddname, jbcname))

    cp()
    aa.flpdp(123, idd, t180, tpend, jbc)
    aa.qll_erjileimu(34, ER, t180, tpend, 3)
    aa.qll_erjileimu(2, ER, t180, tpend, 3)
    aa.sp('%s-%s-单品非兴I%s' % (peoname, iddname, jbcname))

    cp()
    aa.qll_erjileimu(2, ER, t180, tpend, jbc)
    aa.qll(34, t180, tpend, 3)
    aa.qll(2, t180, tpend, 3)
    aa.sp('%s-%s-其他类目I%s' % (peoname, iddname, jbcname))

    t90 = somedays(ts)
    cp()
    aa.qll_erjileimu(234, ER, t180, tpend, jbc)
    aa.qll_erjileimu(1, ER, t90, tpend, 3)
    aa.sp('%s-%s-二级类目A%s' % (peoname, iddname, jbcname))

    cp()
    aa.qll_erjileimu(1, ER, t90, tpend, jbc)
    aa.qll(234, t180, tpend, 3)
    aa.qll(1, t90, tpend, 3)
    aa.sp('%s-%s-其他类目A%s' % (peoname, iddname, jbcname))

    cp()
    aa.qll(234, t180, tpend, jbc)
    aa.qll(1, t90, tpend, 3)
    aa.qll(1234, ts, te, 3)
    aa.sp('%s-%s-新增AIPL%s' % (peoname, iddname, jbcname))


if __name__ == '__main__':
    ts = '2019-3-3'
    te = '2019-3-9'    

    tasklist = ['13230519823','36416808624','44005916004','543442932644']

    for idd in tasklist:
        qllmain(ts, te, idd, jbc=2)
        qllmain(ts, te, idd, jbc=3)
