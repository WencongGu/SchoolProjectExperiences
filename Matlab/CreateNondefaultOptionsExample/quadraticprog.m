% [X, FVAL] = quadprog(H,f,A,b,Aeq,beq,LB,UB,X0)
% clc
% clear
% close all
% [x,y]=meshgrid(-10:0.2:10)
% z=(x.^2-2*y.^2)*0.5+eps;
% plot3(x,y,z);
% axis([-10 10 -10 10 -100 100]);
% xlabel('x');
% ylabel('y');
% zlabel('z');
fun=@(x,y)fun53(x,y);%何で出来だ。。。
[t,y]=ode45(fun,[0,50],[0;1;2]);
plot3(y(:,1),y(:,2),y(:,3))
function dy=fun53(t,y)
dy=zeros(3,1);
dy(1)=-10*y(1)+10*y(2);
dy(2)=28*y(1)-y(2)-y(1)*y(3);
dy(3)=y(1)*y(2)-8*y(3)/3;
end
