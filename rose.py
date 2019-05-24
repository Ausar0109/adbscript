from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
from ADB import shan_renqun
import time


set_pause(0.3, 0.3)
set_dglc(3, False, 'dp', 0, 0, 2, 2, 2, 'Olay')

tAs = somedays('2019-5-15', 90)
tIs = t180
tHs = somedays('2019-5-15', 90)

tpend = '2019-5-14'


sousuoci = 'olay'


#fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
#input('....')
#depths_of_aipl(tAs, tIs, tpend)



t2bef = '2019-5-15'
t2end = '2019-5-23'

diaoyong_jindian(t2bef, t2end)
diaoyong_tracking(t2bef, t2end, tpend, 'bg')
diaoyong_tracking(t2bef, t2end, tpend, 'sc')
diaoyong_tracking(t2bef, t2end, tpend, 'jg')
#diaoyong_tracking(t2bef, t2end, tpend, 'ys')
time.sleep(5*60)
diaoyong_tracking(t2bef, t2end, tpend, 'jd')
