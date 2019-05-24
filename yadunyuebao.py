from ADB import aalc, set_pause, swtime, timedelta
from ADB.actionfunc import datetime

set_pause(0.2, 0.2)
dt = datetime.now() - timedelta(20)

year, month = dt.year, dt.month
yuefen = month

t1 = '%s-%s-1' % (year, month)
t2 = '%s-%s-1' % (year, month + 1)
t1, t2 = swtime(t1), swtime(swtime(t2, False) - timedelta(1))


def run(with_goumai=False):

    names = '购买' if with_goumai else ''

    def cp2():
        aalc.cp()
        if with_goumai:
            aalc.dp(5, t1, t2)

    cp2()
    aalc.wt(1, t1, t2, 1)
    aalc.cnxh(1, t1, t2, 2)
    aalc.shyjs(1, t1, t2, 2)
    aalc.bmqd(1, t1, t2, 2)
    aalc.yhh(1, t1, t2, 2)
    aalc.sp(str(yuefen) + '月份全部内容' + names)

    cp2()
    aalc.wt(1, t1, t2, 1)
    aalc.wt(1, t1, t2, 3)
    aalc.cnxh(1, t1, t2, 2)
    aalc.shyjs(1, t1, t2, 2)
    aalc.bmqd(1, t1, t2, 2)
    aalc.yhh(1, t1, t2, 2)
    aalc.sp(str(yuefen) + '月份x微淘' + names)

    cp2()
    aalc.cnxh(1, t1, t2, 1)
    aalc.wt(1, t1, t2, 3)
    aalc.cnxh(1, t1, t2, 2)
    aalc.shyjs(1, t1, t2, 2)
    aalc.bmqd(1, t1, t2, 2)
    aalc.yhh(1, t1, t2, 2)
    aalc.sp(str(yuefen) + '月份x猜你喜欢' + names)

    cp2()
    aalc.shyjs(1, t1, t2, 1)
    aalc.wt(1, t1, t2, 3)
    aalc.cnxh(1, t1, t2, 2)
    aalc.shyjs(1, t1, t2, 2)
    aalc.bmqd(1, t1, t2, 2)
    aalc.yhh(1, t1, t2, 2)
    aalc.sp(str(yuefen) + '月份x生活研究所' + names)

    cp2()
    aalc.bmqd(1, t1, t2, 1)
    aalc.wt(1, t1, t2, 3)
    aalc.cnxh(1, t1, t2, 2)
    aalc.shyjs(1, t1, t2, 2)
    aalc.bmqd(1, t1, t2, 2)
    aalc.yhh(1, t1, t2, 2)
    aalc.sp(str(yuefen) + '月份x必买清单' + names)

    cp2()
    aalc.yhh(1, t1, t2, 1)
    aalc.wt(1, t1, t2, 3)
    aalc.cnxh(1, t1, t2, 2)
    aalc.shyjs(1, t1, t2, 2)
    aalc.bmqd(1, t1, t2, 2)
    aalc.yhh(1, t1, t2, 2)
    aalc.sp(str(yuefen) + '月份x有好货' + names)

aalc.cp()
aalc.tm(3, t1, t2)
aalc.sp(str(yuefen) + '月份-粉丝')


aalc.cp()
aalc.dp(5, t1, t2)
aalc.tm(3, t1, t2)
aalc.sp(str(yuefen) + '月份-粉丝购买')


run(with_goumai=False)
run(with_goumai=True)
