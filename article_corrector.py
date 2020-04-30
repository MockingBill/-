import pycorrector
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

text_data = "为进一支撑重要场景保障(如：国庆庆春节等重点节假日保障性能数据输出，疫情等重大事件性能数据保障等)，用户画像精细化分析和用户感知精细化提升工作（配合网优完成无限质差及投诉小区的用户业务回溯及分析功能等。。），同事支撑起他生产业务系统（如控大屏，呈现现网网络性能情况；输出性能数据到集中故障，可以进一步对集中故障进行诊断；通过客户业务感知溯源，追溯区性能数据给投诉前移系统，可以更准确的定位问题，支撑投诉分析等），需对现网性能管理系统进行深度优化。现启动本项目进行希同升级优化等技术支持服务进行采购。"
idx_error = pycorrector.detect(text_data)

resu_data = []
last_index = 0
for item in idx_error:
    normal = text_data[last_index:item[1]]
    if str(normal).strip() != "":
        resu_data.append([normal, 'b'])
    resu_data.append([text_data[item[1]:item[2]], 'r'])
    last_index = item[2]
print(resu_data)
