import matplotlib.pyplot as plt

x = ['1차수','2차수','3차수','4차수','5차수','6차수','7차수','8차수']
y = [81, 42, 79, 64, 59, 74, 26, 40]

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

bar = plt.bar(x, y, color = 'lightgreen')
# plt.plot(x, y, color='g', linestyle='--', marker='o')
## 선 그래프 출력
plt.title('2023 Case Conference 접속자 수', fontsize=20)

plt.ylim(0, 100)
# 숫자 넣는 부분
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % height, ha='center', va='bottom', size = 12)
#plt.axis('off'), plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()



