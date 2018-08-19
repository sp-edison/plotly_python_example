clear all; close all; clc

load Hy5500.dat;

[xmax,ymax] = size(Hy5500);
x = linspace(0,xmax-1,xmax);
y = linspace(0,ymax-1,ymax);

imagesc(x,y,abs(Hy5500'));
axis equal;
axis tight;

xlabel('x direction')
ylabel('y direction')
title('Magnetic field')




