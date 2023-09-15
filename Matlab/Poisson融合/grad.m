function g=grad(data,k)
s=size(data);
gx=ones(s);
gy=ones(s);
% 边界采用向前差分和向后差分
gx(1,:,:)=data(2,:,:)-data(1,:,:);
gy(:,1,:)=data(:,2,:)-data(:,1,:);
gx(s(1),:,:)=abs(data(s(1),:,:)-data(s(1)-1,:,:));
gy(:,s(2),:)=abs(data(:,s(2),:)-data(:,s(2)-1,:));
if k==1 % x轴
    for i =2:(s(1)-1)
        gx(i,:,:)=(data(i+1,:,:)-data(i-1,:,:))/2;
    end
    g=gx;
end
if k==2 % y轴
    for j=2:(s(2)-1)
        gy(:,j,:)=(data(:,j+1,:)-data(:,j-1,:))/2;
    end
    g=gy;
end
end