import numpy as np
import scipy.stats as spy
import matplotlib.pyplot as plt

#Constants and (Real)Parameters
N = 10000
μ = 2.
σ = 1.2

#Acquisition of real data
exp_data = spy.norm.rvs(loc = μ, scale = σ, size = N)

#Likelihood: guess the distribution (norm) and guess the parameters μ,σ
μ_guess = 3.
σ_guess = 1.
#This is the likelihood distribution, X is the set of data measured,
#while the two parameters are the variables now. 
#               np.log(spy.norm.pdf(X, loc = μ_guess, 
#                                   scale = σ_guess)).sum()

#Maximization of the μ parameter
μ_range = np.linspace(1.,3,100)
log_likelihoods = []

for μ_i in μ_range:
    log_likelihoods.append(np.log(spy.norm.pdf(exp_data, loc = μ_i, 
                                     scale = σ_guess)).sum())
    
plt.plot(μ_range, log_likelihoods, linestyle = 'dotted')
plt.xlabel('μ')
plt.ylabel('log L ( μ | X)')
plt.title('Log-Likelihood')
plt.show()

#Now we choose the best parameter
maxlogL = max(log_likelihoods)
max_index = log_likelihoods.index(maxlogL)
print('μ best: ', μ_range[max_index])
print('sample mean: ', np.mean(exp_data))
#Now we could put this value inside the likelihood and perform the same
#procedure for the variance

#Uncertainty σ_μ of μ_best, using the simple graphical method:
#           logL(μ_best +/- σ_μ) ≈ logL(μ_best) - 1/2
σ_μ_index = np.argmin(np.abs(np.array(log_likelihoods)-(maxlogL-0.5)))
σ_μ = abs(μ_range[max_index] - μ_range[σ_μ_index])
print('μ best =','[',μ_range[max_index],'+/-',σ_μ,']')

