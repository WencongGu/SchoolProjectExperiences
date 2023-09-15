clc
clear
f=[2;3;1];
A=[1 4 2;3 2 0];
b=[8;6];
lb=zeros(3,1);
[x,y]=linprog(f,-A,-b,[],[],lb)
%lb表示向量x的下界,还可以有ub表示上界,x表示未知数,y表示目标函数的最值