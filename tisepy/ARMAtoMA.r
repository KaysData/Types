#! /usr/bin/Rscript

function (ar = numeric(), ma = numeric(), lag.max) 
.Call(C_ARMAtoMA, as.double(ar), as.double(ma), as.integer(lag.max))