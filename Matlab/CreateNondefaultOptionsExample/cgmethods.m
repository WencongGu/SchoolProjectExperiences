clc
clear
epsilon=0.0001;
A=[4 3 0
    3 4 -1
    0 -1 4];
b=[3
    5
    -5];
x=[0
    0
    0];
r=b-A*x;
p=r;
n=0;
while n<4&&vecnorm(r)>epsilon
    n=n+1
    a=(r'*r)/(p'*A*p)
    x=x+a*p
    k=r;
    r=r-a*A*p
    w=r'*r/(k'*k)
    p=r+w*p
end
