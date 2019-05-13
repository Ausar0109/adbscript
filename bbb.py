from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
from ADB import shan_renqun

set_pause(0.2, 0.2)
set_dglc(2, False, 'dp', 0, 0, 2, 2, 2, '颂拓')


tAs = '2019-3-3'
tIs = '2018-12-3'
tPLs = '2018-6-1'

tHs = somedays('2019-5-6', 90)

tpend = '2019-5-5'

sousuoci = '佳明手表,佳明235,佳明130,佳明运动手表,佳明935,佳明fenix3，佳明运动手表旗舰， \
garmin, garmin forerunner 935, garmin佳明fenix5, garmin男士, garmin佳明手表,apple watch 4,  \
apple watch series 4, iwatch4, iwatch 4, applewatch4, apple watch series4,苹果手表4,苹果手表 4,  \
苹果手表apple watch 4,华为手表 watch gt, 华为手表watch gt智能运动手表,华为手表gt,华为watch2 pro,华为手表watch2,'  
# '亚瑟男鞋,亚瑟女鞋,Asics,asics,ASICS,亚瑟士,亚瑟士跑鞋'

#fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
#input('......')
depths_of_aipl(tAs, tIs, tpend)


# t2bef = '2019-3-26'
# t2end = '2019-3-28'

# diaoyong_jindian(t2bef, t2end)
# diaoyong_tracking(t2bef, t2end, tpend, 'bg')
# diaoyong_tracking(t2bef, t2end, tpend, 'sc')
# diaoyong_tracking(t2bef, t2end, tpend, 'jg')
# diaoyong_tracking(t2bef, t2end, tpend, 'ys')
# diaoyong_tracking(t2bef, t2end, tpend, 'jd')
