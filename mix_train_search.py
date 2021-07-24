""" Generate commands for pre-train phase. """
import os


def run_exp(lr=0.05, gamma=0.5, step_size=20, pre_batch_size=8):
    max_epoch = 120
    shot = 20
    query = 10
    way = 4
    gpu = 0
    base_lr = 0.1
    
    the_command = 'python3 lauch.py' \
        + ' --pre_max_epoch=' + str(max_epoch) \
        + ' --shot=' + str(shot) \
        + ' --train_query=' + str(query) \
        + ' --way=' + str(way) \
        + ' --pre_step_size=' + str(step_size) \
        + ' --pre_gamma=' + str(gamma) \
        + ' --gpu=' + str(gpu) \
        + ' --base_lr=' + str(base_lr) \
        + ' --pre_lr=' + str(lr) \
        + ' --pre_batch_size=' + str(pre_batch_size) \
        + ' --phase=dependent' \
        + ' --model_type=Search' \
        + ' --exp_spc=Mix_Search_Formal_1'

    os.system(the_command)


run_exp(lr=0.05, gamma=0.5, step_size=20, pre_batch_size=8)


