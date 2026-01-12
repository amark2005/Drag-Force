%input speeds
v_kmh_plot= 0:1:700;            
v_ms_plot = v_kmh_plot * (5/18);
v_kmh = 60;
v_ms = v_kmh * (5/18);
rho = 1.1950;
Cd=0.35;
fa=1.955;
FD=dragf(fa,rho,v_ms,Cd);
FD_plot=dragf(fa,rho,v_ms_plot,Cd);
printf("Drag Force for %d km/h = %.3f N\n",v_kmh,FD)
plot(FD_plot,v_kmh_plot,'linewidth',2);
grid on;
xlabel=("Drag Force")
ylabel=("Speed Km/h")
title('Drag Force vs Speed')