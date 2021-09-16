#include<iostream>
#include<iomanip>
#include<fstream>
#include<cmath>
using namespace std;

//Constants 
const double NGrid = 200.; //Should be an int, but I forgot how to obtain a double when dividing 2 ints.
const int tot_points = pow(NGrid,2);
const int steps = 1200, step_err = 800;
double t0 = 0. , tf = 7. , q0 = 2., p0 = 0., eps = 1e-10;
double perturb[2] = {eps*(2/5.),eps*(1/5.)}; //perturbative vector pointing to (2,1)
double state0[2] = {q0, p0};

double dq(double t, double q, double p) {
	return p;
}

double dp(double t, double q, double p) {
	return q - 0.1*p - pow(q,3);
}

int main(){
	ofstream file;
	file.open("orbits.dat");
	double h = (tf-t0)/steps;
	double *t = new double[steps+1];
	double *q = new double[steps+1];
	double *p = new double[steps+1];
	double *q_eps = new double[steps+1];
	double *p_eps = new double[steps+1];
	double I[4]; //for q
	double J[4]; //for p
	double I_eps[4]; //for q_eps
	double J_eps[4]; //for p_eps
	double error;

	//=================== Grid Simulation ===================
	for(int m=0; m<NGrid; m++){
		cout<< endl << m+1 << " / " <<NGrid<<endl;
		state0[0] = - 2. + 4. * m / NGrid;
		
		for(int k=0; k<NGrid; k++){
			state0[1] = - 2. + 4. * k / NGrid;
			
	//========================= INTEGRATION =========================
			//initial conditions
			t[0] = t0;
			q[0] = state0[0];
			p[0] = state0[1];
			q_eps[0] = state0[0]+perturb[0];
			p_eps[0] = state0[1]+perturb[1];
				
			//Runge Kutta 4th raw scheme
			for(int i=0; i<steps; i++) {
				I[0] = (h) * dq(t[i], q[i], p[i]);
     				J[0] = (h) * dp(t[i], q[i], p[i]);
				I_eps[0] = (h) * dq(t[i], q_eps[i], p_eps[i]);
     				J_eps[0] = (h) * dp(t[i], q_eps[i], p_eps[i]);
     				
     				I[1] = (h) * dq(t[i] + (h/2.), q[i] + (1/2.) * I[0], p[i] + (1/2.) * J[0]);
        			J[1] = (h) * dp(t[i] + (h/2.), q[i] + (1/2.) * I[0], p[i] + (1/2.) * J[0]);
				I_eps[1] = (h) * dq(t[i] + (h/2.), q_eps[i] + (1/2.) * I_eps[0], p_eps[i] + (1/2.) * J_eps[0]);
        			J_eps[1] = (h) * dp(t[i] + (h/2.), q_eps[i] + (1/2.) * I_eps[0], p_eps[i] + (1/2.) * J_eps[0]);

        			I[2] = (h) * dq(t[i] + (h/2.), q[i] + (1/2.) * I[1], p[i] + (1/2.) * J[1]);
        			J[2] = (h) * dp(t[i] + (h/2.), q[i] + (1/2.) * I[1], p[i] + (1/2.) * J[1]);
				I_eps[2] = (h) * dq(t[i] + (h/2.), q_eps[i] + (1/2.) * I_eps[1], p_eps[i] + (1/2.) * J_eps[1]);
        			J_eps[2] = (h) * dp(t[i] + (h/2.), q_eps[i] + (1/2.) * I_eps[1], p_eps[i] + (1/2.) * J_eps[1]);
        			
        			I[3] = (h) * dq(t[i] + (h), q[i] + I[2], p[i] + J[2]);
        			J[3] = (h) * dp(t[i] + (h), q[i] + I[2], p[i] + J[2]);
				I_eps[3] = (h) * dq(t[i] + (h), q_eps[i] + I_eps[2], p_eps[i] + J_eps[2]);
        			J_eps[3] = (h) * dp(t[i] + (h), q_eps[i] + I_eps[2], p_eps[i] + J_eps[2]);
        			
        			q[i+1] = q[i] + (1/6.) * (I[0] + (2. * I[1]) + (2. * I[2]) + I[3]);
        			p[i+1] = p[i] + (1/6.) * (J[0] + (2. * J[1]) + (2. * J[2]) + J[3]);
				q_eps[i+1] = q_eps[i] + (1/6.) * (I_eps[0] + (2. * I_eps[1]) + (2. * I_eps[2]) + I_eps[3]);
        			p_eps[i+1] = p_eps[i] + (1/6.) * (J_eps[0] + (2. * J_eps[1]) + (2. * J_eps[2]) + J_eps[3]);

     				//file << q[i] << " " << p[i] << endl; //This plots the orbit

     				t[i+1] = t[i] + h;

			}//=================== END INTEGRATION CYCLE ===================
			
			error = sqrt(pow(q_eps[step_err]-q[step_err],2) + pow(p_eps[step_err]-p[step_err],2)) / eps;
			file << setprecision(12) << q[0] << " " << setprecision(12) << p[0] << " " << error <<endl;
			
		}//=================== END X-GRID CYCLE ===================

	}//=================== END Y-GRID CYCLE ===================
	
}//=================== END MAIN ===================
