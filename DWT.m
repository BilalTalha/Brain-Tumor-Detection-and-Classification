clc
clear all
%X1 = idwt2(cA3,cH3,cV3,cD3,'db4');
% % X = pca(X)
%[cA4,cH4,cV4,cD4] = dwt2(cD1,'db4');
%[cA5,cH5,cV5,cD5] = dwt2(cD4,'db4');
%X2 = idwt2(cA5,cH5,cV5,cD5,'db4');

%[cA6,cH6,cV6,cD6] = dwt2(cH1,'db4');
%[cA7,cH7,cV7,cD7] = dwt2(cH6,'db4');
%X3 = idwt2(cA7,cH7,cV7,cD7,'db4');

%[cA8,cH8,cV8,cD8] = dwt2(cV1,'db4');
%[cA9,cH9,cV9,cD9] = dwt2(cV8,'db4');
%X4 = idwt2(cA9,cH9,cV9,cD9,'db4');

%figure;
%First_Level_DecompositionHH=uint8(X1);
%imshow(First_Level_DecompositionHH,[]);title('First Level Decomposition H_H');
% % subplot(2,2,2)
% % % First_Level_DecompositionLL=uint8(X2);
% % % imshow(First_Level_DecompositionLL,[]);title('First Level Decomposition LL');
% % % % % subplot(2,2,3)
% % % First_Level_DecompositionLH=uint8(X3);
% % % imshow(First_Level_DecompositionLH,[]);title('First Level Decomposition LH');
% % % % % subplot(2,2,4)
% % % First_Level_DecompositionHL=uint8(X4);
% % % imshow(First_Level_DecompositionHL,[]);title('First_Level_DecompositionHL');
% % % figure;
% % % First_Level_DecompositionHH=uint8(X1);
% % % imshow(First_Level_DecompositionHH,[]);title('First Level Decomposition H_H');
% % % figure
% % % combImg =First_Level_DecompositionHH+ First_Level_DecompositionLH
% % % % % combImg = imfuse(First_Level_DecompositionHH, First_Level_DecompositionLH, 'montage');
% % %  imshow(combImg,[]);title('First_Level_DecompositionHL');
% % figure
% % combImg=cat(2,First_Level_DecompositionHH, First_Level_DecompositionLH);
% % imshow(combImg,[]);title('First_Level_DecompositionHL');
Arr=[];
D = 'C:\Users\Talha Bilal\Desktop\New folder (3)\cropped';
fileID = fopen('C:\\Users\\Talha Bilal\\Desktop\\New folder (3)\\menigiomia.txt','w');
for k = 1:20
    str1 = strcat('C:\\Users\\Talha Bilal\\Desktop\\New folder (3)\\cropped\\g',num2str(k));
    F = strcat(str1,'.jpg');
    I = imread(F);
    [cA1,cH1,cV1,cD1] = dwt2(I,'db4');
    [cA2,cH2,cV2,cD2] = dwt2(cA1,'db4');
    [cA3,cH3,cV3,cD3] = dwt2(cA2,'db4');
    cD1 = imresize(cD1,[20 28]);
    
    arr1=reshape(cD1,1,[]);
    length(arr1)
    fprintf(fileID,'%f ',arr1);
    fprintf(fileID,'\nNew message in new line\n');
end
fclose(fileID);


