clear
clc
A=[10 -1 0
    -1 10 -2
    0 -2 10];
b=[9
    7
    6];
x=[0
    0
    0];
D=diag(diag(A));
L=-tril(A,-1)
U=-triu(A,1)
% Jccobi迭代法法
% Bj=inv(D)*(L+U)
% fj=inv(D)*b
% n=0;
% delta=1;
% while n<5&&delta>0.00001
%     n=n+1
%     x=Bj*x+fj
%     delta=vecnorm(x-Bj*x-fj,Inf);
% end
% delta

% Gauss-Seidel迭代法
Bgs=inv(D-L)*U
fgs=inv(D-L)*b
delta=1;
n=0;
while n<5&&delta>0.00001
    n=n+1
    x=Bgs*x+fgs
    delta=vecnorm(x-Bgs*x-fgs,Inf);
end
delta