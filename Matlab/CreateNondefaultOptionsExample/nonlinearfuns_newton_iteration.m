clear
clc
f1=@(x1,x2)(x1-0.7*sin(x1)-0.2*cos(x2));
f2=@(x1,x2)(x2-0.7*cos(x1)+0.2*sin(x2));
df11=@(x1,x2)(1-0.7*cos(x1));
df21=@(x1,x2)(0.7*sin(x1));
df12=@(x1,x2)(0.2*sin(x2));
df22=@(x1,x2)(1+0.2*cos(x2));
F=@(x1,x2)([f1(x1,x2)
    f2(x1,x2)]);
DF=@(x1,x2)([df11(x1,x2) df12(x1,x2)
    df21(x1,x2) df22(x1,x2)]);
epsilon=0.0000000001;
n=0;
x1=0.5;%初始值
x2=0.5;%初始值
x=[x1
    x2];
while vecnorm(F(x(1),x(2)),Inf)>epsilon
    n=n+1
    dx=-inv(DF(x(1),x(2)))*F(x(1),x(2))
    x=x+dx
end
delta=abs(F(x(1),x(2)))%误差
x%解




% function f=F(x1,x2)
% f=[f11(x1,x2) f12(x1,x2)
%     f21(x1,x2) f22(x1,x2)]
% end

