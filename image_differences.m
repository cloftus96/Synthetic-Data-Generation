clear
clc

% difference between images

a = imread('im2.jpg');
b = imread('im3.jpg');

obj = imabsdiff(a,b);
figure(1)
imshow(obj,[])
saveas(gcf,'comp.jpg')


BW = imread('comp.jpg'); 
I = rgb2gray(BW);
figure(2)
imshow(I);
YourArray = imbinarize(I,.3);
figure(3)
imshow(YourArray);
cc = bwlabel(YourArray,8);
figure(4)
imagesc(cc);
figure(5)
hist(cc(:),[1:max(cc(:))]);
y = cc==240;
[row,col]= find(y);
k = convhull(row,col);
figure(6)
plot(row(k),col(k),'r-',row,col,'b*')



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