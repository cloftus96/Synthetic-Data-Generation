clear all
clc
close all

% difference between images

a = imread('blank.png');
b = imread('filled.png');

obj = imabsdiff(a,b);
figure(1)
imshow(obj,[])
saveas(gcf,'comp.jpg')


BW = imread('comp.jpg'); 
I = rgb2gray(BW);
figure(2)
imshow(I);
YourArray = imbinarize(I,.1);
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
% region_minsize = 5;   %for example
% uvals = unique(YourArray(:));
% accumulated_list = struct('label', {}, 'props', {});
% for K = 1 : length(uvals)
%    U = uvals(K);
%    accumulated_list(K).label = U;
%    BW = YourArray == U;
%    BW2 = bwareafilt(BW, [region_minsize, inf]);  %discard areas that are too small
%     theseprops = regionprops(BW2, 'PixelList', 'Orientation');
%     accumulated_list(K).props = theseprops;
% end
%  
% objectofinterest = theseprops(29);
% pixellist = objectofinterest.PixelList;
% plot(pixellist(:,1),pixellist(:,2))