clear all; close all; clc

load Freq_S11Abs.dat;

plot(Freq_S11Abs(:,1),Freq_S11Abs(:,2),'k-o');

Xmin = Freq_S11Abs(1,1);
Xmax = Freq_S11Abs(end,1);
Ymin = -30;
Ymax = 5;
grid on;
axis([Xmin Xmax Ymin Ymax]);

legend('S11');
xlabel('Frequency [GHz]')
ylabel('Magnitude of S11')
title('S11')


