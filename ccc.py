from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
from ADB import shan_renqun

set_pause(0.101, 0.101)
set_dglc(3, True, 'gj', 0, 0, 0, 0, 4, 'swisse')

tAs = t180 #somedays('2019-1-10',90)  # '2019-3-2'
tIs = t180  # '2018-12-2'
tHs = t180#somedays('2019-1-10', 90)
tpend = '2019-1-9'
sousuoci = 'swisse'


#fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
#input('....')
#depths_of_aipl(tAs, tIs, tpend)


t2bef = '2019-1-10'
t2end = '2019-1-17'

#diaoyong_jindian(t2bef, t2end)
#diaoyong_tracking(t2bef, t2end, tpend, 'bg')
#diaoyong_tracking(t2bef, t2end, tpend, 'sc')
#diaoyong_tracking(t2bef, t2end, tpend, 'jg')
#diaoyong_tracking(t2bef, t2end, tpend, 'ys')
#diaoyong_tracking(t2bef, t2end, tpend, 'jd')
diaoyong_tracking(t2bef, t2end, tpend, 'gm')

tAs = somedays('2019-4-24',90)  # '2019-3-2'
tIs = t180  # '2018-12-2'
tHs = somedays('2019-4-24', 90)
tpend = '2019-4-23'
sousuoci = 'swisse'


#fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
#depths_of_aipl(tAs, tIs, tpend)