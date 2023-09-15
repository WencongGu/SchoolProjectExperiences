clc
clear
t=(0:10)./5-1;
x = linspace(-100,200)
f=@(x)(1./(1+9.*x.*x));
% a=[];
% for i=0:10
%     a=[a,{[i,f(i)]}];
% end
% a
ft=f(t);
% for i=0:10
lx=@(x)lagrange1(t,ft,x);
plot(x,lx(x),x,f(x))
% z=ones(1,5)




