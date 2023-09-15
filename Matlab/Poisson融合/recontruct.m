function imout=recontruct(back,mask,div)
s=size(mask);
imout=back;
map=zeros(s); % 寻找相关坐标的索引矩阵
n=size(find(mask==1),1);
c=0;
for x=1:s(1)
    for y=1:s(2)
        if mask(x,y)==1
            c=c+1;
            map(x,y)=c;
        end
    end
end
for i=1:3
    A=spalloc(n,n,n*5); % 存储稀疏矩阵
    b=zeros(n,1);
    c=0;
    for x=1:size(map,1)
        for y=1:size(map,2)
            if mask(x,y)==1
                c=c+1;
                A(c,c)=4;
                if mask(x-1,y)==0 % 边界检查
                    b(c)=back(x-1,y,i);
                                else
                                    A(c,map(x-1,y))=-1;
                end
                if mask(x+1,y)==0
                    b(c)=b(c)+back(x+1,y,i);
                else
                    A(c,map(x+1,y))=-1;
                end
                if mask(x,y-1)==0
                    b(c)=b(c)+back(x,y-1,i);
                else
                    A(c,map(x,y-1))=-1;
                end
                if mask(x,y+1)==0
                    b(c)=b(c)+back(x,y+1,i);
                else
                    A(c,map(x,y+1))=-1;
                end
                b(c)=b(c)-div(x,y);
            end
        end
    end
    im=A\b;
    for c=1:length(im)
        [index_x,index_y]=find(map==c);
        imout(index_x,index_y,i)=im(c);
    end
end
% 图像格式转化
imout=uint8(imout);