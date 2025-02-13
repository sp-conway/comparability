rm(list=ls())
library(tidyverse)
library(here)
library(fs)
library(glue)

f_all <- here("data","raw") %>%
  dir_ls(regexp = ".csv")


read <- function(f){
  print(f)
  d <- data.table::fread(f) %>%
    filter(effect %in% c("critical","catch","filler_random","filler_square")) %>%
    select(participant, blocks.thisN,
           trials.thisN,
           effect,order,distance, diag,
           config_tmp,config_tmp_1,
           h_1_tmp,w_1_tmp,
           h_2_tmp,w_2_tmp,
           h_3_tmp,w_3_tmp,
           trials.rect_choice.keys,
           trials.rect_choice.rt) %>%
    rename(block=blocks.thisN,
           trial=trials.thisN,
           config_1=config_tmp,
           config_2=config_tmp_1,
           choice=trials.rect_choice.keys,
           rt=trials.rect_choice.rt,
           h_1=h_1_tmp,
           h_2=h_2_tmp,
           h_3=h_3_tmp,
           w_1=w_1_tmp,
           w_2=w_2_tmp,
           w_3=w_3_tmp) %>%
    mutate(block=block+1,
           trial=trial+1,
           across(c(order,effect,diag,distance), ~na_if(.x, "None"))) %>%
    mutate(across(c(h_1,h_1,h_2,w_2,h_3,w_3,distance,choice,rt),as.numeric),
           choice_name=case_when(
             effect=="critical"~str_sub(order,choice,choice),
             T~NA_character_
           ))
  d$a_max <- pmap_int(list(d$h_1*d$w_1,d$h_2*d$w_2,d$h_3*d$w_3),function(x,y,z) which.max(c(x,y,z)))
  dd <- d %>%
     mutate(correct=case_when(
       effect=="critical" & choice_name !="d" ~ 1,
       effect=="critical" & choice_name =="d" ~ 0,
       effect!="critical" & choice == a_max ~ 1,
       effect!="critical" & choice != a_max ~ 0
     )) %>%
    select(-a_max) %>%
    relocate(choice_name,.after=choice) %>%
    relocate(rt, .before=correct)
  # FILTER OUT FAST & SLOW RTS
  ddd <- dd %>%
    filter(rt>=.1 & rt<=10)
  return(ddd)
}

d <- map(f_all, read) %>%
  list_rbind()
write_csv(d, file=here("data","clean","data.csv"))
