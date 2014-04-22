---
layout: post
title: 혼자보기 아까운 숫자들
date: 2014-04-22 14:00
author: 김은규
tags:
  - data
  - globalmigration
---

디아스포라들과 이주자들의 움직임을 관찰하는 것은 전세계의 경제적/정치적 정책과 밀접한 관련이 있습니다. 작은 예를 들어서, 타국에 살고 있는 이주자가 본국으로 얼마나 많은 금액을 송금하는가(remittance)는 여러 경제연구기관의 관심사<sup>1</sup> 입니다. 각국의 [외교부](http://mofat.go.kr) 뿐만 아니라 World Bank 나 OECD 포럼 같은 대규모 기관에서도 디아스포라 관련 통계와 자료들을 정확하게 모으는데 노력과 자원을 아끼지 않고 있습니다. 

디아스포라 현상을 공부를 하는 사람들에게는 참 고마운 일이 아닐수가 없습니다! 누군가가 계속해서 전세계 디아스포라들의 움직임을 친절하게 Mapping 해주고 있는 것입니다.

'디아스포라들' 블로그에서 이런 데이터를 차곡차곡 모아서 공부하는데 밑거름으로 쓰면 어떨까 합니다. 수많은 통계와 자료들이 나오고 있어서 어디서 부터 시작할지 구분하는 것도 쉬운 작업은 아니겠습니다만, 

+ *Curation* - '혼자보기 아까운' 데이터를 수집/선별하고,
+ *Clean Up* - 여러 데이터를 일관적인 포맷으로 잘 다듬어 보관하는 것도

[![bilateral json](/img/posts/bilateral-json.jpg)](http://en.wikipedia.org/wiki/JSON)

좋은 시작점이 될수 있을 것 같습니다. 수집되고 다듬어진 데이터는 준비되는대로 다음과 URL 에 포스팅하도록 하겠습니다.

> 디아스포라 Data 공간 - [diasporas.cc/data](/data)

저희가 첫 포스팅으로 소개하는 데이터는 [Global Bilateral Migration Matrix](/data)<sup>2</sup> 입니다. 이름이 조금 거창하지만 간단하게 설명하면 세계 226개국을 대상으로 이주민들이 어디로 얼마나 많이 움직이는지 보여주는 NxN Matrix 입니다. 예를 들어, X 라는 나라에서 Y 라는 나라로 이동한 총 인구는 [X,Y] 에 표기됩니다. 1960년대 부터 각국의 인구조사를 토대로 모아져온 데이터라 디아스포라 관련 데이터 중에서는 가장 많이 쓰여지고 있는 입문용 자료라고 할수도 있습니다. 

![bilateral matrix](/img/posts/bilateral-matrix.jpg)

그럼 이 Matrix 가 답해줄 수 있는 질문들은 얼마나 될까요? 간단해 보이는 정보이지만 생각보다 많은 질문들을 답할 수 있다고 합니다. 자세한 분석들은 차츰 인터넷 글사이즈로(우리 집중력에 자비가 있기를) 잘게 썰어서 나누어서 올리겠습니다. 하지만 스포일러용으로 몇가지 나누어 보자면:

+ 세계적으로 디아스포라가 증가하는 속도; 1960년-2010년까지
+ 위도(Latitude)와 경도(Longitude)로 볼때 이주자들이 움직이는 방향은?
+ 지난 50년간 어느 나라로(혹은 나라에서) 가장 많은 사람들이 움직이고 있을까?
+ 석유생산과 이주자들 숫자의 관계는?
+ 한인 디아스포라는 전세계 얼마만큼 퍼져있나?

등등을 꼽을 수 있겠습니다. 사실 이 정도는 누구나 그렇게 많은 시간을 들이지 않아도, 쉽게 관찰할 수 있는 포인트들일 것입니다. 꼼꼼한 가계부쓰는 눈썰미나, 지하철에서 Sudoku 푸는 정신력 정도면 누구든지 분석이 가능한 데이터입니다. 

조금 더 솔직하게 말씀드리면 이런 데이터를 수집하고 공유하는 과정에서 독자 여러분의 다양한 관점과 분석을 또한 들을 수 있었으면 하는 속마음이 있습니다 ^^. 관심과 함께, 인포그래픽이나 재미있는 통계에 대한 아이디어가 있으신 분은 저희에게 언제든지 연락주시길 바랍니다 (Data Junkie 우대합니다!).


- - -
1. Wikipedia &mdash; [http://en.wikipedia.org/wiki/Remittance#Significance](http://en.wikipedia.org/wiki/Remittance#Significance)
2. World DataBank &mdash; [http://data.worldbank.org/data-catalog/global-bilateral-migration-database](http://data.worldbank.org/data-catalog/global-bilateral-migration-database)