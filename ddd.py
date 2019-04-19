from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
from ADB import shan_renqun

set_pause(0.15, 0.15)
set_dglc(5, True, 'dp', 0, 0, 1, 1, 1, '斯凯奇')


tAs = '2018-12-1'
tIs = '2018-12-1'
tHs = '2019-3-1'

tpend = '2019-4-14'

sousuoci = '运动鞋,Adidas,阿迪达斯,fila,童鞋,巴拉巴拉,安踏,NB,耐克,puma,彪马'

fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
input('...')
depths_of_aipl(tAs, tIs, tpend, tPLs='2018-6-1')


# t2bef = '2019-3-26'
# t2end = '2019-3-28'

# diaoyong_jindian(t2bef, t2end)
# diaoyong_tracking(t2bef, t2end, tpend, 'bg')
# diaoyong_tracking(t2bef, t2end, tpend, 'sc')
# diaoyong_tracking(t2bef, t2end, tpend, 'jg')
# diaoyong_tracking(t2bef, t2end, tpend, 'ys')
# diaoyong_tracking(t2bef, t2end, tpend, 'jd')
