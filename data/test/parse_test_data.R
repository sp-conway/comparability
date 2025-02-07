rm(list=ls())
library(tidyverse)
library(here)
library(fs)
f <- here("data/test") %>%
  dir_ls(regexp = ".csv")
d <- read_csv(f) %>%
  filter(!is.na(effect)) %>%
  select(participant,
         computer,
         date,
         thisTrialN, 
         thisRepN,
         blocks.thisTrialN,
         h_1_tmp, 
         h_2_tmp,
         h_3_tmp,
         w_1_tmp,
         w_2_tmp,
         w_3_tmp,
         effect,
         distance,
         order,
         config,
         diag,
         config_tmp,
         config_tmp_1,
         h_1,
         h_2,
         h_3,
         w_1,
         w_2,
         w_3,
         r_1_x,
         r_1_y,
         r_2_x,
         r_2_y,
         r_3_x,
         r_3_y,
         trials.rect_choice.keys,
         trials.rect_choice.rt,
         ) 

dcheck1 <- d %>%
  filter(effect=="critical") %>%
  mutate(across(c(h_1,h_2,h_3,w_1,w_2,w_3),as.numeric)) %>%
  mutate(check_h_1=h_1==h_1_tmp,
         check_w_1=w_1==w_1_tmp,
         check_h_2=h_2==h_2_tmp,
         check_w_2=w_2==w_2_tmp,
         check_h_3=h_3==h_3_tmp,
         check_w_3=w_3==w_3_tmp)
unique(dcheck1$check_h_1)
unique(dcheck1$check_h_2)
unique(dcheck1$check_h_3)
unique(dcheck1$check_w_1)
unique(dcheck1$check_w_2)
unique(dcheck1$check_w_3)
range(as.numeric(dcheck1$trials.rect_choice.rt),na.rm=T)
