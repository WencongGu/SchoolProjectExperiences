clc
clear
f=@(x)(3*x*x-exp(x));%函数接口（Newton法和割线法）
df=@(x)(6*x-exp(x));%导函数接口
f2=@(x)(4+2*cos(x)/3);%函数接口（迭代法）
fundiff=@(x)(x-f(x)/df(x));
funsecant=@(xk1,xk2)(xk2-f(xk2)*(xk2-xk1)/(f(xk2)-f(xk1)));
epsilon=0.001;%误差允许范围

%secant_method
n=0;
x1=0.5;%初始值
x2=1;%初始值
while abs(f(x2))>epsilon
    n=n+1
    xs=funsecant(x1,x2)
    x1=x2;
    x2=xs;
end
abs(f(xs))%误差
xs%解

%newton_method
xn=0.5;%初始值
n=0;
while abs(f(xn))>epsilon
    n=n+1
    xn=fundiff(xn)
end
abs(f(xn))%误差
xn%解

%iteration
xi=3;%初始值
n=0;
while abs(f2(xi)-xi)>epsilon
    n=n+1
    xi=f2(xi)
end
abs(f2(xi)-xi)%误差
xi%解
