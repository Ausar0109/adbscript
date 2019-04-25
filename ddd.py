from ADB.personal.skqaipl import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.personal.skqaipl import diaoyong_jindian, diaoyong_tracking
from ADB.personal.skqaipl import set_namesstt_sign

from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta

set_pause(0.2, 0.3)

tAs = '2018-12-1'
tIs = '2018-12-1'
tPLs = '2018-6-1'
tHs = '2019-3-1'

tpend = '2019-4-21'
sousuoci = '运动鞋,Adidas,阿迪达斯,fila,童鞋,巴拉巴拉,安踏,NB,耐克,puma,彪马'

set_namesstt_sign('T')
set_dglc(2, True, 'dp', 0, 0, 4, 4, 4, '斯凯奇')
fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
#depths_of_aipl(tAs, tIs, tpend, tPLs=tPLs)

set_namesstt_sign('N')
set_dglc(3, True, 'dp', 0, 0, 5, 5, 5, '斯凯奇')
fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
#depths_of_aipl(tAs, tIs, tpend, tPLs=tPLs)

set_namesstt_sign('Y')
set_dglc(4, True, 'dp', 0, 0, 3, 3, 3, '斯凯奇')
fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
#depths_of_aipl(tAs, tIs, tpend, tPLs=tPLs)

set_namesstt_sign('G')
set_dglc(5, True, 'dp', 0, 0, 2, 2, 2, '斯凯奇')
fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
#depths_of_aipl(tAs, tIs, tpend, tPLs=tPLs)


# t2bef = '2019-3-26'
# t2end = '2019-3-28'

# diaoyong_jindian(t2bef, t2end)
# diaoyong_tracking(t2bef, t2end, tpend, 'bg')
# diaoyong_tracking(t2bef, t2end, tpend, 'sc')
# diaoyong_tracking(t2bef, t2end, tpend, 'jg')
# diaoyong_tracking(t2bef, t2end, tpend, 'ys')
# diaoyong_tracking(t2bef, t2end, tpend, 'jd')
