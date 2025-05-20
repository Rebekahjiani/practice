x = input('请输出身高\体重（请用空格间隔开，单位分别是m\kg）:')
x1,x2 = x.split()
height = float(x1)
weight = float(x2)
BMI = weight / height ** 2
print('您的BMI指数为：', BMI)
if BMI < 18.5:
    print('过轻')
elif BMI <= 25:
    print('正常')
elif BMI <= 28:
    print('过重')
elif BMI <= 32:
    print('肥胖')
else:
    print('严重肥胖')