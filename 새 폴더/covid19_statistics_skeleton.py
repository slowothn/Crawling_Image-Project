# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:52:56 2024

@author: piipwon
"""

def normalize_data(n_cases, n_people, scale):
    # 인구 대비 확진자 수를 계산하고, 백만 명 단위로 조정
    norm_cases = []
    for idx, n in enumerate(n_cases):
        norm_cases.append(n / n_people[idx] * scale)
    return norm_cases

regions  = ['Seoul', 'Gyeongi', 'Busan', 'Gyeongnam', 'Incheon', 'Gyeongbuk', 'Daegu', 'Chungnam', 'Jeonnam', 'Jeonbuk', 'Chungbuk', 'Gangwon', 'Daejeon', 'Gwangju', 'Ulsan', 'Jeju', 'Sejong']
n_people = [9550227,  13530519, 3359527,     3322373,   2938429,     2630254, 2393626,    2118183,   1838353,   1792476,    1597179,   1536270,   1454679,   1441970, 1124459, 675883,   365309] # 2021-08
n_covid  = [    644,       529,      38,          29,       148,          28,      41,         62,        23,        27,         27,        33,        16,        40,      20,      5,        4] # 2021-09-21

sum_people = sum(n_people)  # 총 인구 수 계산
sum_covid  = sum(n_covid)   # 총 코로나 확진자 수 계산
norm_covid = normalize_data(n_covid, n_people, 1000000)  # 백만 명당 확진자 수 계산

# 인구 출력
print('### Korean Population by Region')
print('* Total population:', sum_people)
print()  # 빈 줄 출력
print('| Region | Population | Ratio (%) |')
print('| ------ | ---------- | --------- |')
for idx, pop in enumerate(n_people):
    ratio = (pop / sum_people) * 100  # 각 지역 인구의 비율을 백분율로 계산
    print('| %s | %d | %.1f |' % (regions[idx], pop, ratio))
print()

# 코로나 신규 확진자 출력
print('### Korean COVID-19 New Cases by Region')
print('* Total new cases:', sum_covid)
print()  # 빈 줄 출력
print('| Region | New Cases | Ratio (%) | New Cases/1M |')
print('| ------ | ---------- | --------- | ------------ |')
for idx, cases in enumerate(n_covid):
    rati = (cases / sum_covid) * 100  # 각 지역의 확진자 비율을 백분율로 계산
    print('| %s | %d | %.1f | %.1f |' % (regions[idx], cases, rati, norm_covid[idx]))
