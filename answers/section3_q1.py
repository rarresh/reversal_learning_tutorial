

ev  = np.exp(simPars['beta']*v)     # exponentiate the value
sev = np.sum(ev)		            # compute the sum of the values
p   = ev/sev 		                # probability each choice i.e. ratio of each of the values and their sum.
