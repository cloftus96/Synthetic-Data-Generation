clear
clc

% difference between images

a = imread('im2.jpg');
b = imread('im3.jpg');

obj = imabsdiff(a,b);
figure
imshow(obj,[])
saveas(gcf,'comp.jpg')
imshow(grayImage, []);

BW = imread('comp.jpg'); 
