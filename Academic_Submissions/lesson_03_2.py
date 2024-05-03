import numpy 
import matplotlib.pyplot as plt

# x軸の定義域
x = numpy.linspace(-numpy.pi, numpy.pi, 100)

# グラフのタイトル
plt.title('y = cos(tan(x)) & y = tan(x^2)')

# グラフの描画
plt.plot(x, numpy.cos(numpy.tan(x)), label='y = cos(tan(x))', color='red')
plt.plot(x, numpy.tan(x**2), label='y = tan(x^2)', color='blue')

plt.grid()

# x軸を黒線で表示
plt.axhline(0, color='black', linewidth=0.5)
# y軸を黒線で表示
plt.axvline(0, color='black', linewidth=0.5)

# 凡例の表示
plt.legend()

# 軸のラベル
plt.xlabel('x')
plt.ylabel('y')

# グラフの表示
plt.show()