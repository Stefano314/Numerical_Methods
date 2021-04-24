#include<iostream>
#include<cmath>
#include<TGraph.h>
//#include<TH1.h>
using namespace std;

double Time = 10.;
double h = 0.1;
int steps = (Time/h);
double r0[2] = {0.,3.};//x0, y0
double v0 = 20.;
int i_pos = 0;

struct SpacePoint {
	int points=steps;
	double *x = new double[points];
	double *y = new double[points];
	double *vx = new double[points];
	double *vy = new double[points];
	SpacePoint(){};
	SpacePoint(int n, double x0, double y0, double v0, double theta){
		//points = n;
		x[0] = x0;
		y[0] = y0;
		vx[0] = v0*cos(theta*3.14/180.);
		vy[0] = v0*sin(theta*3.14/180.);
	}
};

SpacePoint Trajectory(double *r0, double v0, double theta, int steps, double inc){
	SpacePoint point(steps, r0[0], r0[1], v0, theta);
	
	double g = -9.81;
	//while(i<steps || point.y[i]<0.){
	for(i_pos=0; i_pos<steps; i_pos++){
		point.x[i_pos+1] = point.x[i_pos]+inc*point.vx[0];
		if(point.y[i_pos]<0.) break;
		point.y[i_pos+1] = point.y[i_pos]+inc*point.vy[i_pos];
		point.vx[i_pos+1] = point.vx[0];
		point.vy[i_pos+1] = point.vy[i_pos]+inc*g;
		//i++;
	}
	return point;
}

int main() {
	SpacePoint plot = Trajectory(r0,v0,30.,steps,h);
	double *x = new double[i_pos-1];
	double *y = new double[i_pos-1];
	for(int i=0; i<(i_pos-1); i++){
		x[i]=plot.x[i];
		y[i]=plot.y[i];
		cout<<"X position: "<<x[i]<<endl;
		cout<<"Y position: "<<y[i]<<endl<<endl;
		}
	TGraph *gr = new TGraph(i_pos-1,x,y);
	gr->SetMarkerColor(kRed);
	gr->SetMarkerSize(1);
	gr->SetMarkerStyle(8);
	gr->Draw("APE");
}

