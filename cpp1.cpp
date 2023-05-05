#include <graphics.h>
#include <iostream>
#include <cmath>
using namespace std;
double verlet(double pos, double acc, double dt)
{
double prev_pos=pos;
time=0.0;
    while(pos>0)
    {
    time=time+dt;
    double temp_pos=pos;
    pos=pos*2-prev_pos+acc*dt*dt;
    prev_pos=temp_pos;
    }
return time;
}
double verlet1(double pos, double acc, double dt)
{
 double prev_pos=pos;
time=0.0;
double vel=0.0;
    while(pos>0)
    {
    time=time+dt;
    double temp_pos=pos;
    pos=pos*2-prev_pos+acc*dt*dt;
    prev_pos=temp_pos;
    vel=vel+acc*dt;
    }   
    return time;
}
double velocity_verlet(double pos, double acc, double dt)
{
    double prev_pos=pos;
time=0.0;
double vel=0.0;
    while(pos>0)
    {
    time=time+dt;
    double temp_pos=pos;
    pos+=vel*dt+0.5*acc*dt*dt;
    prev_pos=temp_pos;
    vel=vel+acc*dt;
    }   
    return time;
}
int main()