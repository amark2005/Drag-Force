function [Fd] = dragf(fa,rho,v,Cd)


%find frontal area m^2
%person_fa=0.6194;
%Bike_fa=0.5565;
%fa=Car's frontal area;


%Air Density of the Place in kg/m^3
 %erode
%Velocity m/s
% Drag Coefficient (no dimension or unit)

% Finds out the Drag Force
Fd=0.5*rho*(v.^2)*fa*Cd;


endfunction