% x=[1:0.001:5];
% y=1./x;
% t=0:0:0
% set(gca,'xtick',t)
% set(gca,'ytick',t)
% xlabel('价格')
% ylabel('满意度')
% box off
% grid off
% hold on
% y0=1./(6-x)
% plot(x,y,'k',LineWidth=5)
% plot(x,y0,'k',LineWidth=5)
% set(gca,'fontsize',20)
% x1=[1:0.001:4.6]
% y1=1./(6-x1-0.2)+0.2
% x2=[1.5:0.01:5.2]
% y2=1./(6-x2+0.2)-0.2
% plot(x1,y1,'k',LineWidth=3)
% plot(x2,y2,'k',LineWidth=3)
% x1=[1.3:0.001:5]
% y1=1./(x1-0.3)+0.3
% x2=[1:0.01:5.2]
% y2=1./(x2+0.3)-0.3
% plot(x1,y1,'k',LineWidth=3)
% plot(x2,y2,'k',LineWidth=3)
% annotation("arrow",[0.25,0.2],[0.50,0.50])
% annotation("arrow",[0.3,0.35],[0.65,0.65])


% 
% H=[1 1 1 1 1 1 1
%     0 1 2 3 4 5 6 
%     0 1 4 2 2 4 1
%     0 1 1 6 1 6 6];
% y=[1
%     4
%     6
%     3
%     3
%     0
%     0];
% 
% b=[17
%     37
%     40
%     31];
% b=H*y
% e=H\b
% H*e
% rank(H)
% Hb=[H,b]
% rank(Hb)
% rref(Hb)



A=[3,-1
    -1,1];
b=[-2
    0];
x=[-2
    4];

A*x
















