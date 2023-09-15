clc
clear
options=optimset;
fun=@(x)fun1(x);
x0=rand(2,1);
A=[1 4;3 2];
b=[8;6];
aeq=[1,1];
beq=7;
lb=zeros(3,1);
ub=ones(3,1);
nonlcon=@(x)fun2(x);
% 非线性约束，指定为函数句柄或函数名称。nonlcon 是一个函数，接受向量或数组 x，并返回两个数组 c(x) 和 ceq(x)。
% c(x) 是由 x 处的非线性不等式约束组成的数组。fmincon 尝试满足
% 对于 c 的所有项，有 c(x) <= 0。
% ceq(x) 是 x 处的非线性等式约束的数组。fmincon 尝试满足
% 对于 ceq 的所有项，有 ceq(x) = 0。
% 例如，
% x = fmincon(@myfun,x0,A,b,Aeq,beq,lb,ub,@mycon)
% 其中 mycon 是一个 MATLAB 函数，例如
% function [c,ceq] = mycon(x)
% c = ...     % Compute nonlinear inequalities at x.
% ceq = ...   % Compute nonlinear equalities at x.
% 如果约束的梯度也可以计算且 SpecifyConstraintGradient 选项是 true，设置如下：
% options = optimoptions('fmincon','SpecifyConstraintGradient',true)
% 则 nonlcon 还必须在第三个输出参数 GC 中返回 c(x) 的梯度，在第四个输出参数 GCeq 中返回 ceq(x) 的梯度。GC 和 GCeq 可以是稀疏的或稠密的。
% 如果 GC 或 GCeq 较大，非零项相对较少，则通过将它们表示为稀疏矩阵，可以节省 interior-point 算法的运行时间和内存使用量。
% 有关详细信息，请参阅非线性约束。

[x, y]=fmincon (fun,x0,A,b,aeq,beq,lb,ub,nonlcon,options)
function f=fun1(x)
f=x(1)^2+x(2)^2+8;
end
function [g,h]=fun2(x)
g=-x(1)^2+x(2);
h=-x(1)-x(2)^2+2;
end