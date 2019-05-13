from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
from ADB import shan_renqun


set_pause(0.3, 0.3)
set_dglc(2, False, 'dp', 0, 0, 2, 2, 2, '亚瑟士')

tAs = t180
tIs = t180
tHs = somedays('2019-4-1', 90)

tpend = '2019-3-31'


sousuoci = '亚瑟男鞋,亚瑟女鞋,tiger男鞋,tiger女鞋,tiger鞋,asics tiger,asicstiger,ASICSTIGER,AsicsTiger,鬼冢虎'


fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
input('....')
depths_of_aipl(tAs, tIs, tpend)

input('....')
t2bef = '2019-4-1'
t2end = '2019-4-30'

diaoyong_jindian(t2bef, t2end)
diaoyong_tracking(t2bef, t2end, tpend, 'bg')
#diaoyong_tracking(t2bef, t2end, tpend, 'sc')
#diaoyong_tracking(t2bef, t2end, tpend, 'jg')
diaoyong_tracking(t2bef, t2end, tpend, 'gm')
diaoyong_tracking(t2bef, t2end, tpend, 'jd')
