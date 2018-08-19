clear all; close all; clc

load Time_Voltage_Current.dat;

plot(Time_Voltage_Current(:,1),Time_Voltage_Current(:,2),'k-','LineWidth',2);
hold on;
plot(Time_Voltage_Current(:,1),Time_Voltage_Current(:,3),'r:','LineWidth',3);
grid on;


legend('Time data');
xlabel('Time')
ylabel('Frequency')
title('Current and Voltage')

legend('Voltage', 'Current')


