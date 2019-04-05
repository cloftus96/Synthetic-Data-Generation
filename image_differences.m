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

%%%%Centroid%%%%%%%%%
% s = regionprops(BW,'centroid');
% centroids = cat(1,s.Centroid);
% imshow(BW)
% hold on
% plot(centroids(:,1),centroids(:,2),'b*')
% hold off

%%%%Perimeter%%%%%%%%
s = regionprops(BW,'centroid')


% L=logical(BW);
% box=regionprops(L,'Area', 'BoundingBox'); 
% box(2)

 
% URL list from Friday, Mar. 29 2019 9:49 AM
% To copy this list, type [Ctrl] A, then type [Ctrl] C. 
% 
% Status Reports - 431L Neural Networks - Google Drive
% https://drive.google.com/drive/u/0/folders/1ULsuzeLsd4A5WKVTciWEy4vWRy1IhkZ7
% 
% Table of Contents Outline - Google Docs
% https://docs.google.com/document/d/1TYo-NfwjNzjpKGbJUBoJ_0eyK0ncwdxRz15hEWgwuXI/edit#
% 
% Absolute difference of two images - MATLAB imabsdiff
% https://www.mathworks.com/help/images/ref/imabsdiff.html
% 
% Measure properties of image regions - MATLAB regionprops
% https://www.mathworks.com/help/images/ref/regionprops.html
% 
% Region and Image Properties - MATLAB & Simulink
% https://www.mathworks.com/help/images/pixel-values-and-image-statistics.html
% 
% Concatenate arrays - MATLAB cat
% https://www.mathworks.com/help/matlab/ref/cat.html
% 
% Save figure to specific file format - MATLAB saveas
% https://www.mathworks.com/help/matlab/ref/saveas.html
% 
% regionprops (Image Processing Toolbox)
% https://edoras.sdsu.edu/doc/matlab/toolbox/images/regionprops.html
% 
% How can I locate a specific object in an image and make a box around it? - MATLAB Answers - MATLAB Central
% https://www.mathworks.com/matlabcentral/answers/453270-how-can-i-locate-a-specific-object-in-an-image-and-make-a-box-around-it
% 
% Inbox (2,880) - kerthj1@udayton.edu - University of Dayton Mail
% https://mail.google.com/mail/u/0/#inbox
