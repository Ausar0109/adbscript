from ADB import AutoDatabank, t180, t365, somedays, swtime, namesstt
from ADB import two_check_time, checktime
from datetime import timedelta
from ADB import set_pause
aa = AutoDatabank()


def qllmain(tAs, tIs, tPLs, tpend, ts, te, typee='No', other_name=''):
    typename = ''

    def cp():
        nonlocal typename
        aa.cp()
        if typee == 'No':
            typename = '-基础'

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
        elif typee == '-SC':
            typename = '-收藏'
            aa.flpdp(2, False, ts, te, 3, erjileimu=ER)
        elif typee == '-JG':
            typename = '-加购'
            aa.flpdp(3, False, ts, te, 3, erjileimu=ER)
        elif typee == '-YS':
            typename = '-预售'
            aa.flpdp(4, False, ts, te, 3, erjileimu=ER)
        elif typee == '-GM':
            typename = '-购买'
            aa.flpdp(5, False, ts, te, 3, erjileimu=ER)
        elif typee == '-BG':
            typename = '-BG'
            aa.zszw([1, 99], ts, te, 3)
        else:  # 自定义名称 用以传入idd
            typename = typee
            aa.flpdp(5, idd, ts, te)

        typename = typename + other_name

    peoname = namesstt(tpend)

    # AAAAAA
    cp()
    aa.qll_erjileimu(234, ER, tIs, tpend, 3)
    aa.qll_erjileimu(1, ER, tAs, tpend, 3)
    aa.sp('%s-%s类-A人群%s' % (peoname, ER, typename))

    cp()
    aa.qll_erjileimu(234, ER, tIs, tpend, 3)
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
    aa.qll_erjileimu(234, ER, tIs, tpend, 3)
    aa.qll_erjileimu(1, ER, tAs, tpend, 3)
    aa.sp('%s-%s类-非旗A%s' % (peoname, ER, typename))

    # IIIIII
    cp()
    aa.qll_erjileimu(34, ER, tIs, tpend, 3)
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.sp('%s-%s类-I人群%s' % (peoname, ER, typename))

    cp()
    aa.flpdp(23, False, tIs, tpend, 3, erjileimu=ER)
    aa.qll_erjileimu(34, ER, tIs, tpend, 1)
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.dp(12345, tIs, tpend, 1)
    aa.tm(3, tIs, tpend, 2)
    aa.tm(1, tIs, tpend, 2)
    aa.sp('%s-%s类-深度I%s' % (peoname, ER, typename))

    cp()
    aa.flpdp(23, False, tIs, tpend, 3, erjileimu=ER)
    aa.qll_erjileimu(34, ER, tIs, tpend, 3)
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.dp(12345, tIs, tpend, 1)
    aa.tm(3, tIs, tpend, 2)
    aa.tm(1, tIs, tpend, 2)
    aa.sp('%s-%s类-浅度I%s' % (peoname, ER, typename))

    cp()
    aa.dp(12345, tIs, tpend, 3)
    aa.tm(3, tIs, tpend, 3)
    aa.tm(1, tIs, tpend, 3)
    aa.qll_erjileimu(34, ER, tIs, tpend, 3)
    aa.qll_erjileimu(2, ER, tIs, tpend, 3)
    aa.sp('%s-%s类-非旗I%s' % (peoname, ER, typename))

    # PLLLL
    cp()
    aa.qll_erjileimu(34, ER, tIs, tpend, 3)
    aa.sp('%s-%s类-P人群%s' % (peoname, ER, typename))

    cp()
    aa.flpdp(5, False, tPLs, tpend, 3, erjileimu=ER)
    aa.qll_erjileimu(34, ER, tIs, tpend, 1)
    aa.sp('%s-%s类-旗舰P%s' % (peoname, ER, typename))

    cp()
    aa.flpdp(5, False, tPLs, tpend, 3, erjileimu=ER)
    aa.qll_erjileimu(34, ER, tIs, tpend, 3)
    aa.sp('%s-%s类-非旗P%s' % (peoname, ER, typename))

    # 非二级类目AIPL
    cp()
    aa.qll_erjileimu(1, ER, tAs, tpend, 3)
    aa.qll_erjileimu(234, ER, tIs, tpend, 3)
    aa.qll(1, tAs, tpend, 3)
    aa.qll(234, tAs, tpend, 2)
    aa.sp('%s-非%s类-全部%s' % (peoname, ER, typename))

    cp()
    aa.qll(234, tIs, tpend, 2)
    aa.qll(1, tAs, tpend, 3)
    aa.qll_erjileimu(1, ER, tAs, tpend, 1)
    aa.qll_erjileimu(234, ER, tIs, tpend, 3)
    aa.qll(234, tIs, tpend, 3)
    aa.qll(1, tAs, tpend, 2)
    aa.sp('%s-非%s类-之A%s' % (peoname, ER, typename))

    cp()
    aa.qll(34, tIs, tpend, 1)
    aa.qll(2, tIs, tpend, 3)
    aa.qll_erjileimu(1, ER, tAs, tpend, 1)
    aa.qll_erjileimu(234, ER, tIs, tpend, 3)
    aa.qll(234, tIs, tpend, 3)
    aa.qll(1, tAs, tpend, 2)
    aa.sp('%s-非%s类-之I%s' % (peoname, ER, typename))

    cp()
    aa.qll(34, tIs, tpend, 1)
    aa.qll_erjileimu(1, ER, tAs, tpend, 1)
    aa.qll_erjileimu(234, ER, tIs, tpend, 3)
    aa.qll(234, tIs, tpend, 3)
    aa.qll(1, tAs, tpend, 2)
    aa.sp('%s-非%s类-之P%s' % (peoname, ER, typename))

    # 新增AIPL
    if two_check_time(ts, te):
        cp()
        aa.qll_erjileimu(1234, ER, ts, te, 3)
        aa.qll(234, tIs, tpend, 1)
        aa.zdy('【勿删】12210524IPL', 3)
        aa.zdy('【勿删】12031220IPL', 3)
        aa.qll(1, tAs, tpend, 3)
        aa.qll(1234, ts, te, 3)
        aa.sp('%s-新增-%s类%s' % (peoname, ER, typename))

        cp()
        aa.qll_erjileimu(1234, ER, ts, te, 3)
        aa.qll(234, tIs, tpend, 3)
        aa.zdy('【勿删】12210524IPL', 3)
        aa.zdy('【勿删】12031220IPL', 3)
        aa.qll(1, tAs, tpend, 3)
        aa.qll(1234, ts, te, 3)
        aa.sp('%s-新增-非%s类%s' % (peoname, ER, typename))


def qlltracking(tAs, tIs, tPLs, tpend, ts, te, typee, other_name):
    '''
    tPLs 没有影响，用于习惯补位
    tAs,tIs,用于修正活动期新增人群的逻辑，对主方法没有影响

    ER是全局变量,函数外的参数会传入进来
    typename 固定为 typee + other_name 的组合
    typee为 ‘No’ 引发 typename = '-基础' ,此为锁死写定
    '''
    assert two_check_time(ts, te)  # 非法时间直接报错
    peoname = namesstt(tpend)
    typename = '-基础'
    typename += other_name

    peoplelist = ['%s-%s类-A人群%s' % (peoname, ER, typename),
                  '%s-%s类-旗舰A%s' % (peoname, ER, typename),
                  '%s-%s类-非旗A%s' % (peoname, ER, typename),
                  '%s-%s类-I人群%s' % (peoname, ER, typename),
                  '%s-%s类-深度I%s' % (peoname, ER, typename),
                  '%s-%s类-浅度I%s' % (peoname, ER, typename),
                  '%s-%s类-非旗I%s' % (peoname, ER, typename),
                  '%s-%s类-P人群%s' % (peoname, ER, typename),
                  '%s-%s类-旗舰P%s' % (peoname, ER, typename),
                  '%s-%s类-非旗P%s' % (peoname, ER, typename),
                  '%s-非%s类-全部%s' % (peoname, ER, typename),
                  '%s-非%s类-之A%s' % (peoname, ER, typename),
                  '%s-非%s类-之I%s' % (peoname, ER, typename),
                  '%s-非%s类-之P%s' % (peoname, ER, typename)]

    typename2 = ''

    def cp():
        nonlocal typename2
        aa.cp()

        if typee == '-JD':  # 进店
            typename2 = '-JD'
            aa.tm(1, ts, te, 3)
            aa.tm(3, ts, te, 3)
            aa.dp(12345, ts, te, 3)
        elif typee == '-LL':  # 浏览
            typename2 = '-LL'
            aa.flpdp(1, False, ts, te, 3, erjileimu=ER)
        elif typee == '-SCJG':  # 收藏加够
            typename2 = '-收加'
            aa.flpdp(23, False, ts, te, 3, erjileimu=ER)
        elif typee == '-SC':
            typename2 = '-收藏'
            aa.flpdp(2, False, ts, te, 3, erjileimu=ER)
        elif typee == '-JG':
            typename2 = '-加购'
            aa.flpdp(3, False, ts, te, 3, erjileimu=ER)
        elif typee == '-YS':  # 预售
            typename2 = '-预售'
            aa.flpdp(4, False, ts, te, 3, erjileimu=ER)
        elif typee == '-GM':  # 购买
            typename2 = '-购买'
            aa.flpdp(5, False, ts, te, 3, erjileimu=ER)
        elif typee == '-BG':
            typename2 = '-BG'
            aa.zszw([1, 99], ts, te, 3)
        typename2 += other_name

    # 主方法loop ★★★
    for xy in peoplelist:
        cp()
        aa.zdy(xy, 3)
        xyname = '-'.join(xy.split('-')[:-1]) + typename2
        aa.sp(xyname)

    # 新增AIPL
    aa.cp()
    aa.qll_erjileimu(1234, ER, ts, te, 3)
    aa.qll(234, tIs, tpend, 1)
    aa.zdy('【勿删】12210524IPL', 3)
    aa.zdy('【勿删】12031220IPL', 3)
    aa.qll(1, tAs, tpend, 3)
    aa.qll(1234, ts, te, 3)
    aa.sp('%s-新增-%s类%s' % (peoname, ER, typename))

    aa.cp()
    aa.qll_erjileimu(1234, ER, ts, te, 3)
    aa.qll(234, tIs, tpend, 3)
    aa.zdy('【勿删】12210524IPL', 3)
    aa.zdy('【勿删】12031220IPL', 3)
    aa.qll(1, tAs, tpend, 3)
    aa.qll(1234, ts, te, 3)
    aa.sp('%s-新增-非%s类%s' % (peoname, ER, typename))

    cp()
    aa.qll_erjileimu(1234, ER, ts, te, 3)
    aa.qll(234, tIs, tpend, 1)
    aa.zdy('【勿删】12210524IPL', 3)
    aa.zdy('【勿删】12031220IPL', 3)
    aa.qll(1, tAs, tpend, 3)
    aa.qll(1234, ts, te, 3)
    aa.sp('%s-新增-%s类%s' % (peoname, ER, typename2))

    cp()
    aa.qll_erjileimu(1234, ER, ts, te, 3)
    aa.qll(234, tIs, tpend, 3)
    aa.zdy('【勿删】12210524IPL', 3)
    aa.zdy('【勿删】12031220IPL', 3)
    aa.qll(1, tAs, tpend, 3)
    aa.qll(1234, ts, te, 3)
    aa.sp('%s-新增-非%s类%s' % (peoname, ER, typename2))


if __name__ == '__main__':
    set_pause(0.31, 0.31)

    aa = AutoDatabank(5, False, 'dp')
    aa.zhanghao = '1'
    aa.mxdp_order = 5
    aa.zszw_order = 7
    aa.brand_name = '飞利浦'

    tAs = '2019-4-2'
    tIs = '2018-12-3' if checktime('2018-12-3') else t180
    tPLs = t365
    tpend = '2019-5-24'

    ts = '2019-5-25'
    te = '2019-5-27'  # 代表活动期间时间

    ER, er = '腔电', 'O'
    # qllmain(tAs, tIs, tPLs, tpend, ts, te,  'No', other_name=er)
    # qllmain(tAs, tIs, tPLs, tpend, ts, te,  '-LM')  # 类目
    # qllmain(tAs, tIs, tPLs, tpend, ts, te,  '-BG')  # 曝光
    # qllmain(tAs, tIs, tPLs, tpend, ts, te,  '-SC')  # 收藏
    # qllmain(tAs, tIs, tPLs, tpend, ts, te,  '-JG')  # 加购

    #qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-LL', other_name=er)  # 浏览
    #qlltracking(tAs, tIs, tPLs, tpend, ts, te,
    #            '-SCJG', other_name=er)  # 收藏加够
    #qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-YS', other_name=er)  # 预售
    #qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-GM', other_name=er)  # 购买
    #qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-JD', other_name=er)  # 进店

    ER, er = '剃须', 'M'
    #qllmain(tAs, tIs, tPLs, tpend, ts, te,  'No', other_name=er)

    ER, er = '塑身', 'I'
    #qllmain(tAs, tIs, tPLs, tpend, ts, te,  'No', other_name=er)

    ER, er = '腔电', 'O' 
    #qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-LL', other_name=er)  # 浏览
    qlltracking(tAs, tIs, tPLs, tpend, ts, te,
                '-SCJG', other_name=er)  # 收藏加够
    qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-YS', other_name=er)  # 预售
    qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-GM', other_name=er)  # 购买
    qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-JD', other_name=er)  # 进店

    ER, er = '剃须', 'M'
    qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-LL', other_name=er)  # 浏览
    qlltracking(tAs, tIs, tPLs, tpend, ts, te,
                '-SCJG', other_name=er)  # 收藏加够
    qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-YS', other_name=er)  # 预售
    qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-GM', other_name=er)  # 购买
    qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-JD', other_name=er)  # 进店
    
    ER, er = '塑身', 'I'
    
    #qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-LL', other_name=er)  # 浏览
    #qlltracking(tAs, tIs, tPLs, tpend, ts, te,
    #            '-SCJG', other_name=er)  # 收藏加够
    #qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-YS', other_name=er)  # 预售
    #qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-GM', other_name=er)  # 购买
    #qlltracking(tAs, tIs, tPLs, tpend, ts, te,  '-JD', other_name=er)  # 进店

    
