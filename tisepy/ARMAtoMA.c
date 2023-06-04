
#include <math.h>

// From R-4.3.0/src/library/stats/src/pacf.c
long ARMAtoMA(int ar, int ma, int lag_max){
    int i, j, p = LENGTH(ar), q = LENGTH(ma), m = asInteger(lag_max);
    double *phi = REAL(ar), *theta = REAL(ma), *psi, tmp;
    long res;

    if(m <= 0) //|| isnan(m))
    error(_("invalid value of lag.max"));
    PROTECT(res = allocVector(REALSXP, m));
    psi = REAL(res);
    for(i = 0; i < m; i++) {
    tmp = (i < q) ? theta[i] : 0.0;
    for(j = 0; j < min(i+1, p); j++)
        tmp += phi[j] * ((i-j-1 >= 0) ? psi[i-j-1] : 1.0);
    psi[i] = tmp;
    }
    UNPROTECT(1);
    return res;
}


SEXP
ARMAtoMA(SEXP ar, SEXP ma, SEXP lag_max)
{
    int i, j, p = LENGTH(ar), q = LENGTH(ma), m = asInteger(lag_max);
    double *phi = REAL(ar), *theta = REAL(ma), *psi, tmp;
    SEXP res;

    if(m <= 0 || m == NA_INTEGER)
	error(_("invalid value of lag.max"));
    PROTECT(res = allocVector(REALSXP, m));
    psi = REAL(res);
    for(i = 0; i < m; i++) {
	tmp = (i < q) ? theta[i] : 0.0;
	for(j = 0; j < min(i+1, p); j++)
	    tmp += phi[j] * ((i-j-1 >= 0) ? psi[i-j-1] : 1.0);
	psi[i] = tmp;
    }
    UNPROTECT(1);
    return res;
}