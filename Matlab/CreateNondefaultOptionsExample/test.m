clear
clc
A=[2 e
    e 1]


% a=[2;-2];
% e1=[1;0];
% A=[ 2   -1  3
%     2   0   1
%     -2  1   4]
% w=a-2*sqrt(2)*e1;
% w=w/vecnorm(w);
% p=[1,0;0,1]-2*w*transpose(w)
% o=[0,0];
% to=[0;0];
% P=[1 o;
%     to p]
% P*A*P
% inv(P)






% A=[ 6   2   1
%     2   3   1
%     1   1   1];
% x=[ 1
%     1
%     1];
% I=[ 1   0   0
%     0   1   0
%     0   0   1];
% n=0;
% while n<10
%     n=n+1
%     x=A*x
%     m=x(1);
%     for i=1:2
%         if abs(x(i))<abs(x(i+1))
%             m=x(i+1);
%         end
%     end
%     x=x/m
% end
% [V,D]=eig(A)







% s2=sqrt(2);
% s3=sqrt(3);
% 
% 
% a=[1/s2 0   0   1/s2
%     0   1   0   0
%     0   0   1   0
%   -1/s2 0   0   1/s2]
% b=[s2/s3 0  1/s3   0
%     0   1   0   0
%     -1/s3   0   s2/s3   0
%     0   0   0   1]
% c=[s3/2 1/2   0   0
%     -1/2   s3/2   0   0
%     0   0   1   0
%     0   0   0   1]
% d=c*b*a
% clc
% a1=[1
%     2
%     2];
% a2=[1
%     -1
%     -4];
% a3=[1
%     -1
%     5];
% A=[a1,a2,a3];
% b1=a1;
% b2=a2-(a2'*a1/(a1'*a1))*a1;
% b3=a3-(a3'*a1/(a1'*a1))*a1-(a3'*b2/(b2'*b2))*b2;
% l1=b1'*b1;
% l2=b2'*b2;
% l3=b3'*b3;
% Q=[b1,b2,b3]
% Q=Q/3
% [q,r]=qr(A)
