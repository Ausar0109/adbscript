from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
from ADB import shan_renqun
import time


set_pause(0.3, 0.3)
set_dglc(2, False, 'dp', 0, 0, 2, 2, 2, '雅培')

tAs = '2019-2-24'
tIs = t180
tHs = somedays('2019-5-25', 90)
tpend = '2019-5-24'

sousuoci = '启赋'


fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
time.sleep(10*60)
depths_of_aipl(tAs, tIs, tpend)


t2bef = '2019-5-25'
t2end = '2019-5-27'

diaoyong_jindian(t2bef, t2end)
time.sleep(10*60)
diaoyong_tracking(t2bef, t2end, tpend, 'bg')
diaoyong_tracking(t2bef, t2end, tpend, 'sc')
diaoyong_tracking(t2bef, t2end, tpend, 'jg')
diaoyong_tracking(t2bef, t2end, tpend, 'ys')
diaoyong_tracking(t2bef, t2end, tpend, 'gm')
diaoyong_tracking(t2bef, t2end, tpend, 'jd')
