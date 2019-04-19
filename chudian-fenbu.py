from ADB.personal.aiplandqudao import set_dglc, xinzeng_aipl, yuanyou_aipl, qudaofenbu_aipl
from ADB.personal.aiplandqudao import qudaofenbu_huizong
from ADB import set_pause

set_pause(0.101,0.155)
set_dglc(2, False, 'dp', 1, 1, 2, 2, 2, '雅培')

ts = '2019-1-1'
te = '2019-1-31'
namess = '1月'

#xinzeng_aipl(ts, te, namess)
#yuanyou_aipl(ts, te, namess)

#qudaofenbu_huizong(ts, te, namess)

#qudaofenbu_aipl(ts, te, '新增A人群', 1, namess)
qudaofenbu_aipl(ts, te, '新增I人群', 2, namess)
qudaofenbu_aipl(ts, te, '新增PL人群', 34, namess)

qudaofenbu_aipl(ts, te, '原有A人群', 1, namess)
qudaofenbu_aipl(ts, te, '原有I人群', 2, namess)
qudaofenbu_aipl(ts, te, '原有PL人群', 34, namess)




