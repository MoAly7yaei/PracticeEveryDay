#Normal Dis
var1 = as.integer(rnorm(10,5,6))
var
var2 = as.integer(runif(10,5,6))
var2
############
a = as.integer(c(1,2,'0',3))
a
############
b = matrix(c(1:10), nrow = 2, ncol = 5)
a = data.frame(b)
a = rbind(a,c(11:15))
a
############
cells = rnorm(9,58,20)
rnames = c('Ahmed','Mohammed','Jamal')
cnames = c('Math','Physics','Bio')

mark = matrix(cells, nrow = 3, ncol = 3 , byrow = TRUE, dimnames = list(rnames,cnames))
mark
mark = rbind(mark,'Total' = colSums(mark))
mark
mark = cbind(mark,'Total' = rowSums(mark),'Percent' = ((mark[,1] + mark[,2] + mark[,3])/300) )
mark = data.frame(mark)
mark
############
library(rio)
rio::export(mark, file = 'mark.xlsx', format = 'xlsx', rowNames = TRUE)
############
mark = mark[-4,]
