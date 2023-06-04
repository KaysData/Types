#!usr/bin/python3

import math 
# AIC
def aic(x, p = list(range(0,6)), q = list(range(0,3)), type_ = "aic"):
    x = x - math.mean(x)
    aic = 99999
    bic = 99999
    aicc = 99999
    for j in p:
        for k in q: 
            #w = getOption("warn")
            #options(warn = -1)
            b = arima(x, [j, 0, k]) #try(arima(x, c(j, 0, k)), silent = TRUE)
            #options(warn = w)
            if (type(b) is list): #(is.list(b) == TRUE) {
                c = [b['coef']]#[coef(b)]
                if (j == 0):
                    phi = 0
                else:
                    phi = c[1:j]
                if (k == 0):
                    theta = 0
                else:
                    theta = -c[(j + 1):(j + k)]
                res = backcast(x, phi = phi, theta = theta, n_back = 50) # formerly n.back
                avar = 0
                n = len(x)
                for i in range(1,n+1):  
                    avar = avar + res[i] * res[i]
                
                avar = avar/n
                tempaic = math.log(avar) + 2 * (j + k + 1)/n
                tempbic = math.log(avar) + (j + k + 1) * math.log(n)/n
                tempaicc = math.log(avar) + (n + j + k + 1)/(n - j - k - 
                    3)
                if (type_ == "aic"):
                    if (tempaic < aic):
                        aic = tempaic
                        j_aic = j
                        k_aic = k
                        phi_aic = phi
                        theta_aic = theta
                        avar_aic = avar
                
                if (type_ == "aicc"):
                    if (tempaicc < aicc):
                        aicc = tempaicc
                        j_aicc = j
                        k_aicc = k
                        phi_aicc = phi
                        theta_aicc = theta
                        avar_aicc = avar
                    
                if (type_ == "bic"):
                    if (tempbic < bic):
                        bic = tempbic
                        j_bic = j
                        k_bic = k
                        phi_bic = phi
                        theta_bic = theta
                        avar_bic = avar
                    
            
    if (type_ == "aic"):
        out1 = {"type":type_, "value": aic, "p":j_aic, "q": k_aic, 
            "phi": phi_aic, "theta":theta_aic, "vara": avar_aic}
        return(out1)

    if (type_ == "aicc"):
        out1 = {"type":type_, "value": aicc, "p": j_aicc, "q": k_aicc, 
            "phi": phi_aicc, "theta": theta_aicc, "vara":avar_aicc}
        return(out1)

    if (type_ == "bic"):
        out1 = {"type":type_, "value":bic, "p": j_bic, "q": k_bic, 
            "phi": phi_bic, "theta": theta_bic, "vara": avar_bic}
        return(out1)
