from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
from ADB import shan_renqun

set_pause(0.12,0.15)
set_dglc(3, False, 'dp', 0, 0, 0, 3, 3, 'olay')

tAs = '2019-3-2'
tIs = '2018-12-2'
tHs = somedays('2019-4-1', 90)
tpend = '2019-3-25'

#sousuoci = '精华,面霜,雅诗兰黛,兰蔻,娇韵诗'
#sousuoci = 'now0irds'


#fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
#input('....')
#depths_of_aipl(tAs, tIs, tpend)


t2bef = '2019-3-26'
t2end = '2019-4-21'

diaoyong_jindian(t2bef, t2end)
diaoyong_tracking(t2bef, t2end, tpend, 'bg')
diaoyong_tracking(t2bef, t2end, tpend, 'sc')
diaoyong_tracking(t2bef, t2end, tpend, 'jg')
diaoyong_tracking(t2bef, t2end, tpend, 'ys')
diaoyong_tracking(t2bef, t2end, tpend, 'jd')
