#!usr/bin/python3

import numpy as np
import copy
import pandas as pd

def aic5 (x, p = list(range(0,6)), q = list(range(0,3)), type = "aic"):
    pmax = max(p)
    pmin = min(p)
    qmax = max(q)
    qmin = min(q)
    nr = (pmax - pmin + 1) * (qmax - qmin + 1)
    aval = np.zeros((nr,3)) #matrix(0, nrow = nr, ncol = 3) #CHECK SYNTAX AND TRANSLATION
    mytype = type
    print("---------WORKING... PLEASE WAIT...", "\n")
    print("\n")
    print("\n")
    indx = 0
    for ip in range(pmin,pmax+1): 
        for iq in range(qmin,qmax+1): 
            indx = indx + 1
            try:
                ret = aic(x, p = ip, q = iq, type_ = mytype)
            except: 
                pass
            #ret = try(aic.wge(x, p = ip, q = iq, type = mytype), 
            #    silent = TRUE)

            if (ret == list): 
                aval[indx, ] = [ret["p"], ret["q"], ret["value"]]
            else:
                error_content = ["Error in aic calculation at", ip, iq, "\n"]
                error_report = " ".join(error_content)
                print(error_report)
                aval[indx, ] = [ip, iq, 999999]
        
    
    dat = copy.deepcopy(aval) #data.frame(aval)
    sorted_aval = dat[dat[:,2].argsort()] #sorted_aval = dat[order(dat[, 3], decreasing = F), ]
    aic5_report = " ".join("Five Smallest Values of ", mytype, "\n")
    print(aic5_report)
    aic5_df = pd.DataFrame(sorted_aval, columns=["p", "q", mytype])
    print(aic5_df.iloc[0:6])
    return(aic5_df.iloc[0:6]) #return(sorted_aval[1:5, , ])
