from ADB import set_pause, AutoDatabank
from ADB import t180, t365, somedays
from datetime import datetime, timedelta

set_pause(0.101, 0.102)
xx = AutoDatabank(4, False, 'dp')
xx.brand_name = '飞利浦'
xx.zszw_order = 4

ts = '2018-10-20'
te = '2018-11-11'

tb = '2018-10-19'


def xinke_and_laoke_baoguang(people_name, namess):
    xx.cp()
    xx.zdy(people_name)
    xx.zszw([1, 99], ts, te, 1)
    xx.sp(namess + '--全部曝光')

    for i in range(1, 16, 1):
        xx.cp()
        xx.zdy(people_name)
        xx.zszw([i, i], ts, te, 1)
        xx.zszw([1, 99], ts, te, 3)
        xx.sp(namess + '--全部曝光X%s' % i)


def xinke_and_laoke_YJJ(people_name, namess):
    for i in range(9, 16, 1):
        xx.cp()
        xx.qll(1, te, te)
        xx.flpdp(5, 123, ts, te, jbc=2, erjileimu='美体塑身')
        xx.zdy(people_name, jbc=1)
        xx.zszw([i, i], ts, te, 1)
        xx.sp(namess + '--曝光%s次' % i + '【G')


if __name__ == '__main__':
    #xinke_and_laoke_baoguang('D11钻展曝光新客','新客')
    #xinke_and_laoke_YJJ('D11钻展曝光新客','新客')

    #xinke_and_laoke_baoguang('D11钻展曝光老客','老客')
    xinke_and_laoke_YJJ('D11钻展曝光老客','老客')
