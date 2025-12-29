%input speeds
v_kmh = 0:1:700;            
v_ms = v_kmh * (5/18);
rho = 1.225;
Cd=0.36;
fa=1.9;
FD=dragf(fa,rho,v_ms,Cd);
plot(FD,v_kmh,'linewidth',2);
grid on;
xlabel=("Drag Force")
ylabel=("Speed Km/h")
title('Drag Force vs Speed')