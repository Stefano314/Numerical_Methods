#include<iostream>
#include<cmath>
#include<TGraph.h>
#include<TLegend.h>
using namespace std;

const double g = -9.81;
const double Time = 10.;//a.u.
const double h = 0.06;
const double Theta = 30.*3.14/180.;

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
	SpacePoint(double x0, double y0, double v0, double theta){
		x[0] = x0;
		y[0] = y0;
		vx[0] = v0*cos(theta);
		vy[0] = v0*sin(theta);
	}
};

SpacePoint Trajectory(double *r0, double v0, double theta, int Steps, double inc){
	SpacePoint point(r0[0], r0[1], v0, theta);
	for(i_pos=0; i_pos<Steps; i_pos++){
		point.x[i_pos+1] = point.x[i_pos]+inc*point.vx[0];
		if(point.y[i_pos]<0.) break;
		point.y[i_pos+1] = point.y[i_pos]+inc*point.vy[i_pos];
		point.vx[i_pos+1] = point.vx[0];
		point.vy[i_pos+1] = point.vy[i_pos]+inc*g;
	}
	return point;
}
   
int main() {
	SpacePoint plot = Trajectory(r0,v0,Theta,steps,h);
	double *x = new double[i_pos-1];
	double *y = new double[i_pos-1];
	double *y_real = new double[i_pos-1];
	cout<<i_pos<<endl;
	for(int i=0; i<(i_pos-1); i++){
		x[i]=plot.x[i];
		y[i]=plot.y[i];
      	y_real[i] = r0[1] + v0*sin(Theta)*i*h+0.5*g*i*i*h*h;
		}
	TCanvas *c1=new TCanvas;
	TGraph *gr = new TGraph(i_pos-1,x,y);
	TGraph *real = new TGraph(i_pos-1,x,y_real);
	gr->SetMarkerColor(kRed);
	gr->SetMarkerSize(1);
	gr->SetMarkerStyle(8);
      real->SetMarkerColor(kGreen);
      real->SetMarkerSize(1);
	real->SetMarkerStyle(8);
	real->Draw("APE");
	gr->Draw("p same");
	auto legend = new TLegend();
   	legend->AddEntry(real,"Real Motion");
   	legend->AddEntry(gr,"Euler Integration");
   	legend->Draw("same");
}

