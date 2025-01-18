# create attraction effect stimuli for comparability exp
# exact same code as for circle experiment
# catch & fillers are created on the fly during experiment
# note that some needed very careful to tweaking to round to correct distances
# that's why percentages change from diagonal to diagonal
# winter 2025
# setup ======================================================================
# clear environment
rm(list=ls())

# libraries
library(tidyverse)
library(here)

# CONTROLS
save_stim <- T # whether to write stim values to a file

# necessary functions
distance <- function(a,b) sqrt( (a[1]-b[1])^2 + (a[2]-b[2])^2  )
compute_tdd <- function(stim,area) round((1-prod(stim)/area),digits=2)*100

# make stim ======================================================================

# three diagonals
a_3 <- c(125,200)
b_3 <- rev(a_3)

a_2 <- c(95,170)
b_2 <- rev(a_2)

a_1 <- c(57,133)
b_1 <- rev(a_1)

# distances are approximately the same across diagonals
distance(a_1,b_1)
distance(a_2,b_2)
distance(a_3,b_3)

# areas of each diagonal
area_1 <- prod(a_1)
area_2 <- prod(a_2)
area_3 <- prod(a_3)

# decoy areas - lower diagonal
area_1_02 <- area_1*.98
area_1_05 <- area_1*.95
area_1_09 <- area_1*.91
area_1_14 <- area_1*.85495

# make decoys - lower diagonal
d_1_02 <- round(rep(sqrt(area_1_02),2))
d_1_05 <- round(rep(sqrt(area_1_05),2))
d_1_09 <- round(rep(sqrt(area_1_09),2))
d_1_14 <- round(rep(sqrt(area_1_14),2))

# tdd check
compute_tdd(d_1_02, area_1)
compute_tdd(d_1_05, area_1)
compute_tdd(d_1_09, area_1)
compute_tdd(d_1_14, area_1)

# decoy areas - middle diagonal
area_2_02 <- area_2*.98
area_2_05 <- area_2*.95
area_2_09 <- area_2*.91
area_2_14 <- area_2*.86

# make decoys - middle diagonal
d_2_02 <- round(rep(sqrt(area_2_02),2))
d_2_05 <- round(rep(sqrt(area_2_05),2))
d_2_09 <- round(rep(sqrt(area_2_09),2))
d_2_14 <- round(rep(sqrt(area_2_14),2))

# tdd check
compute_tdd(d_2_02, area_2)
compute_tdd(d_2_05, area_2)
compute_tdd(d_2_09, area_2)
compute_tdd(d_2_14, area_2)

# decoy areas - upper diagonal
area_3_02 <- area_3*.98
area_3_05 <- area_3*.95
area_3_09 <- area_3*.91
area_3_14 <- area_3*.86

# make decoys - upper diagonal
d_3_02 <- round(rep(sqrt(area_3_02),2))
d_3_05 <- round(rep(sqrt(area_3_05),2))
d_3_09 <- round(rep(sqrt(area_3_09),2))
d_3_14 <- round(rep(sqrt(area_3_14),2))

# tdd check
compute_tdd(d_3_02, area_3)
compute_tdd(d_3_05, area_3)
compute_tdd(d_3_09, area_3)
compute_tdd(d_3_14, area_3)

# combine stim ======================================================================
# combine all stim in tmp matrix
stim_tmp <- rbind(
  "a_1_0"=a_1,
  "b_1_0"=b_1,
  "d_1_02"=d_1_02,
  "d_1_05"=d_1_05,
  "d_1_09"=d_1_09,
  "d_1_14"=d_1_14,
  "a_2_0"=a_2,
  "b_2_0"=b_2,
  "d_2_02"=d_2_02,
  "d_2_05"=d_2_05,
  "d_2_09"=d_2_09,
  "d_2_14"=d_2_14,
  "a_3_0"=a_3,
  "b_3_0"=b_3,
  "d_3_02"=d_3_02,
  "d_3_05"=d_3_05,
  "d_3_09"=d_3_09,
  "d_3_14"=d_3_14
)

# combine into nice df
all_stim <- tibble(
  name=rownames(stim_tmp),
  w=unname(stim_tmp[,1]),
  h=unname(stim_tmp[,2])
) %>%
  separate(name,into=c("name","diag","distance")) %>%
  mutate(across(c(diag,distance),as.numeric),
         distance=na_if(distance,0))

# plotting ======================================================================
p <- all_stim %>%
  mutate(name=toupper(name)) %>%
  ggplot(aes(w,h,col=name))+
  geom_point(size=2.5,alpha=.5,pch=16)+
  labs(x="Width",y="Height")+
  scale_color_discrete(name="Stimulus")+
  scale_x_continuous(breaks=c(0,150,300))+
  scale_y_continuous(breaks=c(0,150,300))+
  coord_fixed(xlim=c(0,300),ylim=c(0,300))+
  ggthemes::theme_few()
p

# saving stim ======================================================================
if(save_stim){
  p
  ggsave(filename=here("specs","stim.jpg"),width=4,height=4)
  write_csv(all_stim,file=here("specs","all_stim.csv"))
}

# catch stim ========================================================================
d1_w <- seq(a_1[1],b_1[1])
d1_h <- lm(a_1~b_1)$coefficients["(Intercept)"]-d1_w
d2_w <- seq(a_2[1],b_2[1])
d2_h <- lm(a_2~b_2)$coefficients["(Intercept)"]-d2_w
d3_w <- seq(a_3[1],b_3[1])
d3_h <- lm(a_3~b_3)$coefficients["(Intercept)"]-d3_w

par(pty='s')
plot(NA,NA,xlim=c(0,300),ylim=c(0,300),xlab="w",ylab="h")
points(d1_w,d1_h,pch=".")
points(d2_w,d2_h,pch=".")
points(d3_w,d3_h,pch=".")

# catch stim ========================================================================
min(all_stim$w)
max(all_stim$w)
min(all_stim$h)
max(all_stim$h)

w <- runif(10000, 56, 195)
h <- runif(10000, 56, 195)
par(pty='s')
plot(NA,NA,xlim=c(0,300),ylim=c(0,300),xlab="w",ylab="h")
points(w,h,pch=".")
a <- w*h
hist(a)

