from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
from ADB import shan_renqun
import time

set_pause(0.3, 0.3)
set_dglc(3, False, 'dp', 0, 0, 2, 2, 2, '维多利亚的秘密')

tAs = t180  # somedays('2019-1-10',90)  # '2019-3-2'
tIs = t180  # '2018-12-2'
tHs = somedays('2019-5-27', 90)
tpend = '2019-5-26'
sousuoci = '维多利亚的秘密,维多利亚,维秘'


#fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
#input('....')
depths_of_aipl(tAs, tIs, tpend)


t2bef = '2019-4-1'
t2end = '2019-4-30'

#input('....')
#diaoyong_jindian(t2bef, t2end)
#diaoyong_tracking(t2bef, t2end, tpend, 'bg')
#diaoyong_tracking(t2bef, t2end, tpend, 'sc')
#diaoyong_tracking(t2bef, t2end, tpend, 'jg')
#diaoyong_tracking(t2bef, t2end, tpend, 'ys')
#diaoyong_tracking(t2bef, t2end, tpend, 'gm')
#diaoyong_tracking(t2bef, t2end, tpend, 'jd')
