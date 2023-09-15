clc
clear all
back=imread('/Users/yucharlotte/Downloads/target1.jpg');
obj=imread('/Users/yucharlotte/Downloads/source4.jpg');
back=double(back);
obj=double(obj);
% 插入坐标
x=1;
y=1;
s=size(obj);
px=x:(s(1)+x-1);
py=y:(s(2)+y-1);
% Poisson融合
gbackx=grad(back,1);
gbacky=grad(back,2);
gobjx=grad(obj,1);
gobjy=grad(obj,2);
gfusionx=gbackx;
gfusiony=gbacky;
gfusionx(px,py,:)=gfusionx(px,py,:)+gobjx(:,:,:);
gfusiony(px,py,:)=gfusiony(px,py,:)+gobjy(:,:,:);
div=grad(gfusionx,1)+grad(gfusiony,2);
% mask处理
mask=zeros(s);
mask(:,:,:) = obj(:,:,:);
mask=rgb2gray(mask);
mask(1,:)=0;
mask(size(mask,1),:)=0;
mask(:,1)=0;
mask(:,size(mask,2))=0;
se = strel('disk',5);
mask = imerode(mask,se);
mask=(mask==1);
% Poisson重建
picfusion=recontruct(back,mask,div);
imshow(picfusion)

