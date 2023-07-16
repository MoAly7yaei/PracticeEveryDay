#Matrix

y = matrix(1:20, nrow = 5, ncol = 4)
y
cells = c(1,26,24,68)
rnames = c('R1','R2')
cnames = c('C1','C2')

MyMatrix = matrix(cells, nrow = 2, ncol = 2 , byrow = TRUE, dimnames = list(rnames,cnames))
MyMatrix


###################################

m1 = matrix(1:6, nrow = 2, ncol = 3)
m2 = matrix(1:6, nrow = 3, ncol = 2)

m1 %*% m2
m2 %*% m1
