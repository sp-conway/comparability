rm(list=ls())
library(tidyverse)
library(here)
stim <- here("specs","all_stim.csv") %>%
  read_csv()

order <- c("dhw","dwh","wdh","whd","hwd","hdw")
distance <- c(2,5,14)
config <- c(1,2,3)
diag <- c("lower","upper")

crit_trials <- expand_grid(order,distance,config,diag) %>%
  mutate(effect="critical") %>%
  relocate(effect,.before=everything()) %>%
  mutate(h_1=numeric(nrow(.)),
         w_1=numeric(nrow(.)),
         h_2=numeric(nrow(.)),
         w_2=numeric(nrow(.)),
         h_3=numeric(nrow(.)),
         w_3=numeric(nrow(.)))


for(i in 1:nrow(crit_trials)){
  cat(paste0("\n",i,"/",nrow(crit_trials),"\n"))
  crit_tmp <- crit_trials[i,]
  stim_tmp <- filter(stim, (distance==crit_tmp$distance|is.na(distance)) & diag==crit_tmp$diag)
  s_1 <- str_sub(crit_tmp$order,1,1)
  s_2 <- str_sub(crit_tmp$order,2,2)
  s_3 <- str_sub(crit_tmp$order,3,3)
  crit_trials$h_1[i] <- filter(stim_tmp, name==s_1)$h
  crit_trials$w_1[i] <- filter(stim_tmp, name==s_1)$w
  crit_trials$h_2[i] <- filter(stim_tmp, name==s_2)$h
  crit_trials$w_2[i] <- filter(stim_tmp, name==s_2)$w
  crit_trials$h_3[i] <- filter(stim_tmp, name==s_3)$h
  crit_trials$w_3[i] <- filter(stim_tmp, name==s_3)$w
}

crit_trials_1 <- bind_rows(crit_trials,crit_trials) %>%
  arrange(desc(config)) %>%
  group_by(order,distance, diag, config) %>%
  mutate(tmp=1:n()) %>%
  ungroup() %>%
  mutate(config1=case_when(
    config==2 & tmp==1 ~ 2.1,
    config==2 & tmp==2 ~ 2.2,
    T ~ config
  )) %>%
  select(-c(tmp,config)) %>%
  rename(config=config1) %>%
  relocate(config, .after=distance)
all_trials <- bind_rows(
  crit_trials_1,
  tibble(effect=rep("catch",5)),
  tibble(effect=rep("filler",15))
)

write_csv(all_trials,file=here("specs","trials.csv"))
write_csv(all_trials,file=here("experiment_code","trials.csv"))

