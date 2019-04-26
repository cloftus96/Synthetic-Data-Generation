clear all
clc
close all
n = 1;

while n < 1000000
% difference between images
first = sprintf('%d_blank.png', n);
second = sprintf('%d.png', n);
a = imread(first);
b = imread(second);

obj = imabsdiff(a,b);
figure(1)
imshow(obj,[])
saveas(gcf,'comp.jpg')


BW = imread('comp.jpg'); 
I = rgb2gray(BW);
figure(2)
imshow(I);
YourArray = imbinarize(I,.05);
figure(3)
imshow(YourArray);
cc = bwlabel(YourArray,8);
figure(4)
imagesc(cc);
figure(5)
hist(cc(:),[1:max(cc(:))]);
m = mode(cc,'all');
cc(cc==m) = NaN;
m = mode(cc,'all');
cc(cc==m) = NaN;
m = mode(cc,'all');
y = cc==m;
z = cc;
figure(6)
imagesc(cc==m);
[row,col]= find(y);
k = convhull(row,col);
figure(7)
plot(row(k),col(k),'r-',row,col,'b*')
value =[row(k) col(k)];
minimums = min(value);
maximums = max(value);
maximums = maximums + 10;
minimums = minimums - 10;
plot(row(k),col(k),'r-',row,col,'b*',maximums(1,1),maximums(1,2),'k*',minimums(1,1),minimums(1,2),'k*')

y(minimums(1,1):maximums(1,1),maximums(1,2)) = 1;
y(minimums(1,1):maximums(1,1),minimums(1,2)) = 1;
y(minimums(1,1),minimums(1,2):maximums(1,2)) = 1;
y(maximums(1,1),minimums(1,2):maximums(1,2)) = 1;
figure(8)
imshow(y);
figure(9)
z(minimums(1,1):maximums(1,1),maximums(1,2)) = 1;
z(minimums(1,1):maximums(1,1),minimums(1,2)) = 1;
z(minimums(1,1),minimums(1,2):maximums(1,2)) = 1;
z(maximums(1,1),minimums(1,2):maximums(1,2)) = 1;
imshow(z);
[d1,d2, existingData] = xlsread('AnnotationData.csv');
BR = sprintf('%d %d',maximums(1,1),maximums(1,2));
TR = sprintf('%d %d',minimums(1,1),minimums(1,2));
TL = sprintf('%d %d',maximums(1,1),minimums(1,2));
BL = sprintf('%d %d',minimums(1,1),maximums(1,2));
BR = cellstr(BR);
TR = cellstr(TR);
TL = cellstr(TL);
BL = cellstr(BL);
existingData(n+1,11) = (BR);
existingData(n+1,12) = (BR);
existingData(n+1,13) = (TL);
existingData(n+1,14) = (BL);
xlswrite('AnnotationData.csv',existingData)
n = n + 1;
end
