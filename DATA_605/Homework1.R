x=c(rep(0,500),seq(0,1,length.out=1000), rep(1,500))

y=c(seq(-1,1,length.out=500),rep(0,1000), seq(-1,1,length.out=500))

#z=rbind(x,y)

plot(y~x, xlim=c(-3,3), ylim=c(-3,3))

