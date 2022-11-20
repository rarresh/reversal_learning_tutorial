
dv  = r-v[c] # compute prediction error
v[c]= v[c] + simPars['alpha']*dv    # update value
