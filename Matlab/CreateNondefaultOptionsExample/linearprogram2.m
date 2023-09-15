f=[2;3;-5];
A=[-2,5,-1];
b=-10;
aeq=[1,1,1];
beq=7;
lb=zeros(3,1);
x=linprog(-f,A,b,aeq,beq,lb)
