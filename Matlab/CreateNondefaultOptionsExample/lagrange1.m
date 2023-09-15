function l_x=lagrange1(t,f_t,x)%t为插值点的向量,f_t为插值点处的函数值向量,x为未知的点向量,返回值l_x为Lagrange函数在x点处的向量值
l_x=ones(1,length(x));
for k=1:length(x)
    s=0;
    for i=1:length(t)
        p=1.0;
        for j=1:length(t)
            if j~=i
                p=p.*(x(k)-t(j))./(t(i)-t(j));
            end
        end
        s=p*f_t(i)+s;
    end
    l_x(k)=s;
end
