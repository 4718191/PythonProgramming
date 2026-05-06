import numpy as np
import matplotlib.pyplot as plt



plt.figure(figsize=(10,8))


# xticks()

year = [2006, 2009, 2012, 2015, 2018]
kor = [547, 546, 554, 524, 526]

ind = np.arange(len(year))

plt.subplot(4,2,1)
plt.plot(ind, kor)
plt.xticks(ind, year)
plt.ylim(500, 580)
plt.xlabel('year')
plt.ylabel('score')





# 여러 개의 막대 그래프

nation = ['Korea', 'USA', 'Japan', 'France']
men = [175.5, 176.9, 172.1, 178.6]
women = [163.2, 163.3, 158.5, 164.5]
ind = np.arange(len(nation))

plt.subplot(4,2,2)
plt.bar(ind, men, color='b', label='men')
plt.bar(ind, women, color='r', label='women')
plt.xticks(ind, nation)
plt.ylim(130, 190)
plt.ylabel('cm')
plt.legend()



#

nation = ['Korea', 'USA', 'Japan', 'France']
men = [175.5, 176.9, 172.1, 178.6]
women = [163.2, 163.3, 158.5, 164.5]
ind = np.arange(len(nation))

plt.subplot(4,2,3)
plt.bar(ind-0.2, men, color='b', width=0.4, label='men')
plt.bar(ind+0.2, women, color='r', width=0.4, label='women')
plt.xticks(ind, nation)
plt.ylim(130, 190)
plt.ylabel('cm')
plt.legend()








# 누적 막대 그래프

year = [2017, 2018, 2019, 2020, 2021]
spring = np.array([124.9, 383.5, 175.0, 173.7, 330.5])
summer = np.array([612.7, 620.6, 508.2, 1037.6, 612.8])
autumn = np.array([177.9, 351.3, 440.8, 270.4, 256.4])
winter = np.array([75.2, 68.7, 168.8, 47.8, 13.3])

plt.subplot(4,2,4)
plt.bar(year, spring, label='spring')
plt.bar(year, summer, bottom=spring, label='summer')
plt.bar(year, autumn, bottom=spring+summer, label='autumn')
plt.bar(year, winter, bottom=spring+summer+autumn, label='winter')
plt.ylabel('mm')
plt.legend()




x = np.linspace(-np.pi, np.pi*2, 100)

plt.subplot(4,2,5) # 중요
plt.plot(x, np.sin(x), label='sin') # sin()
plt.legend()

plt.subplot(4,2,6) # 중요
plt.plot(x, np.cos(x), label='cos') # cos()
plt.legend()





math = np.array([75, 89, 75, 65, 79])
english = np.array([85, 80, 90, 75, 88])
korean = np.array([72, 90, 70, 88, 93])
x = ['math', 'english', 'korean']

plt.subplot(4,2,7) # 중요
plt.bar(x, [np.mean(math), np.mean(english), np.mean(korean)]) # mean() : 배열 각 요소에 평균 구하기
plt.ylim(0,100)
plt.ylabel('score')






x = np.random.randn(1000) # randn() : 평균이 0이고 분산이 1인 표준정규분포를 따르는 난수

plt.subplot(4,2,8) # 중요
plt.hist(x, bins=40, alpha=0.5)
plt.ylabel('frequency')

plt.show()