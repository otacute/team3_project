import numpy as np
import pandas as pd

tour_total = pd.read_csv('pre_data/total_tour.csv',  encoding = 'cp949')
tour_total.info()

import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

## 각 연도별  TOP 10 관광지 구하기
# 'year'과 'spot' 열로 그룹화하여 'search_count' 합계 구하기 및 정렬
top10_spots_total = tour_total.groupby(['year', 'spot']) \
                              .agg(count_tour=('search_count', 'sum')) \
                              .reset_index() \
                              .sort_values(['year', 'count_tour'], ascending=[True, False])

# 각 연도별로 top10 관광지 추출
years = range(2018, 2023)
top10_spots_total_list = []

for year in years:
    top10_spots_year = top10_spots_total[top10_spots_total['year'] == year].head(1)
    top10_spots_total_list.append(top10_spots_year)

# 시각화를 위해 데이터 재구성
top_spots = pd.concat(top10_spots_total_list)['spot'].unique()
plot_data = pd.DataFrame(index=years, columns=top_spots)

for year in years:
    yearly_data = top10_spots_total[top10_spots_total['year'] == year].set_index('spot')
    for spot in top_spots:
        if spot in yearly_data.index:
            plot_data.at[year, spot] = yearly_data.at[spot, 'count_tour']
        else:
            plot_data.at[year, spot] = 0

# 그래프 그리기
plt.figure(figsize=(4, 2))
for spot in top_spots:
    plt.plot(plot_data.index, plot_data[spot], marker='o', label=spot)

plt.title('상위 5개 관광지 5년 추이')
plt.xlabel('년도')
plt.ylabel('검색수')
plt.legend(title='Spot', bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 5})
plt.grid(True)
plt.tight_layout()
plt.xticks(years)  # x축 눈금 설정
plt.show()
plt.clf()

#중분류 추이
# 'year'과 'category_m' 열로 그룹화하여 'search_count' 합계 구하기 및 정렬
top10_categories_total = tour_total.groupby(['year', 'category_m']) \
                                   .agg(count_tour=('search_count', 'sum')) \
                                   .reset_index() \
                                   .sort_values(['year', 'count_tour'], ascending=[True, False])

# 각 연도별로 top10 카테고리 추출
years = range(2018, 2023)
top10_categories_total_list = []

for year in years:
    top10_categories_year = top10_categories_total[top10_categories_total['year'] == year].head(3)
    top10_categories_total_list.append(top10_categories_year)

# 시각화를 위해 데이터 재구성
top_categories = pd.concat(top10_categories_total_list)['category_m'].unique()
plot_data = pd.DataFrame(index=years, columns=top_categories)

for year in years:
    yearly_data = top10_categories_total[top10_categories_total['year'] == year].set_index('category_m')
    for category in top_categories:
        if category in yearly_data.index:
            plot_data.at[year, category] = yearly_data.at[category, 'count_tour']
        else:
            plot_data.at[year, category] = 0

# 그래프 그리기
plt.figure(figsize=(4, 2))
for category in top_categories:
    plt.plot(plot_data.index, plot_data[category], marker='o', label=category)

plt.title('<2018~2022 관광지 중분류 Top 3>')
plt.xlabel('년도')
plt.ylabel('검색수 (단위: 천만 회)')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 7})
plt.grid(True)
plt.tight_layout()
plt.show()
plt.clf()

# 소분류 추이
import pandas as pd
import matplotlib.pyplot as plt

# 예시 데이터프레임 (실제 데이터로 대체해야 함)
# tour_total = pd.read_csv('tour_data.csv')

# 'year'과 'category_s' 열로 그룹화하여 'search_count' 합계 구하기 및 정렬
top10_categories_s_total = tour_total.groupby(['year', 'category_s']) \
                                     .agg(count_tour=('search_count', 'sum')) \
                                     .reset_index() \
                                     .sort_values(['year', 'count_tour'], ascending=[True, False])

# 각 연도별로 top10 소분류 추출
years = range(2018, 2023)
top10_categories_s_total_list = []

for year in years:
    top10_categories_s_year = top10_categories_s_total[top10_categories_s_total['year'] == year].head(3)
    top10_categories_s_total_list.append(top10_categories_s_year)

# 시각화를 위해 데이터 재구성
top_categories_s = pd.concat(top10_categories_s_total_list)['category_s'].unique()
plot_data = pd.DataFrame(index=years, columns=top_categories_s)

for year in years:
    yearly_data = top10_categories_s_total[top10_categories_s_total['year'] == year].set_index('category_s')
    for category in top_categories_s:
        if category in yearly_data.index:
            plot_data.at[year, category] = yearly_data.at[category, 'count_tour']
        else:
            plot_data.at[year, category] = 0

# 그래프 그리기
plt.figure(figsize=(4, 2))
for category in top_categories_s:
    plt.plot(plot_data.index, plot_data[category], marker='o', label=category)

plt.title('<2018~2022 관광지 소분류 Top 3>')
plt.xlabel('년도')
plt.ylabel('총 검색 수 (단위: 백만 회)')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 6})
plt.grid(True)
plt.xticks(years)  # x축 눈금 설정
plt.tight_layout()
plt.show()

plt.clf()
# 단위: 백만