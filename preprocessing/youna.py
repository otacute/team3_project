import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

route = pd.read_excel("C:/Users/USER/Documents/LS빅데이터스쿨/team3_project/younadata.xlsx")
route.head(10)

# 변수 변경
route = route.rename(columns = {"시점":"year", "항목":"access_path", "소계" : "total", "남자" : "man", "여자" : "female"})

route.head()

# 항목
route.loc[route["access_path"]=="과거 방문 경험", "access_path"] = "experience"
route.loc[route["access_path"]=="주변인(친지/친구/동료 등)", "access_path"] = "acquaintance"
route.loc[route["access_path"]=="인터넷 사이트/모바일 앱(PC/스마트폰)", "access_path"] = "internet_mobile_app"
route.loc[route["access_path"]=="광고(TV/라디오/ 신문/잡지/ 지하철/옥외 광고판 등)", "access_path"] = "advertising"
route.loc[route["access_path"]=="기사 및 방송 프로그램(TV/라디오/ 신문/잡지)", "access_path"] = "article_broadcast"
route.loc[route["access_path"]=="관광 안내 서적", "access_path"] = "guidebook"
route.loc[route["access_path"]=="여행사(방문, 전화)", "access_path"] = "travel_agency"
route.loc[route["access_path"]=="정보 없이 방문", "access_path"] = "no_information"
route.loc[route["access_path"]=="기타", "access_path"] = "etc"
route.head()

# 결측치 제거
route.replace('-', np.nan, inplace=True)
route

# 연령대
#route = route.rename(columns = {"15~19세":"teens", "20대":"20years", "30대" : "30years", 
#                                "40대":"40years", "50대":"50years", "60대":"60years",
#                               "70세 이상":"70years+"})
  
route["teens"] = df["15~19세"]                             
route["young_adults"] = route["20대"] + route["30대"]
route["middle_adults"] = route["40대"] + route["50대"]
route["seniors"] = route["60대"] + route["70세 이상"]
route = route.drop(['15~19세', '20대', '30대', '40대', '50대', '60대', '70세 이상'], axis=1)
route.info()


# 월급
route["l_sal"] = route["100만원 미만"] + route["100~200만원 미만"]
route["m_sal"] = route["200~300만원 미만"] + route["300~400만원 미만"] + route["400~500만원 미만"]
route["h_sal"] = route["500~600만원 미만"] + route["600만원 이상"]
route["nr"]= route["무응답"]

route = route.drop(['100만원 미만', '100~200만원 미만', '200~300만원 미만', '300~400만원 미만', '400~500만원 미만',\
                '500~600만원 미만', '600만원 이상'], axis=1)
                

# 가구
route = route.rename(columns = { '1인' : 'per1',
						 '2인' : 'per2',
						'3인이상' : 'per3+'})

# 학벌
route = route.rename(columns = { '초졸 이하' : 'elmt',
						 '중학교' : 'mid',
						'고등학교' : 'high',
						'대학교이상' : 'univ+',
						})
route.info()

# 직업
route = route.drop(['임금봉급근로자', '고용원있는사업주', '고용원없는자영업자', 
                    '무급가족 종사자', '사무전문', '기술생산노무', '판매서비스',
                    "자영업","전업주부","학생","무직은퇴","기타"], axis=1)
route

