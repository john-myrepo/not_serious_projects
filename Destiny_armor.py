import math
import os
import csv

HELMETS = [[20, 2, 12], [17, 8, 18], [11, 10, 13]]
GLOVES  = [[8, 7, 8], [18, 11, 6], [17, 18, 11]]
BOOTS   = [[14, 2, 18], [10, 11, 10], [6, 19, 10]]

def add_boots_stats(helmet_item, gloves_item, total_stat_list):
    no_boots = len(BOOTS)
    helm_and_gloves = [helmet_item[i] + gloves_item[i] for i in range(len(helmet_item))]
    for item in range(no_boots):
        print('For boots number {}: '.format(item))
        stat_total = [helm_and_gloves[j] + BOOTS[item][j] for j in range(len(helm_and_gloves))]
        print('Stat total is: {}'.format(stat_total))
        total_stat_list.append(stat_total)
    return total_stat_list
        
def add_gloves_stats(helmet_item, total_stat_list):
    no_gloves = len(GLOVES)
    for item in range(no_gloves):
        print('For gloves number {}: '.format(item))
        total_stat_list = add_boots_stats(helmet_item, GLOVES[item], total_stat_list)
    return total_stat_list

def find_equipment_set_totals(total_stat_list):
    no_helmets = len(HELMETS)
    for item in range(no_helmets):
        print('For Helmet number {}: '.format(item+1))
        total_stat_list = add_gloves_stats(HELMETS[item], total_stat_list)
    return total_stat_list

class ThisClass():
    def runthisclass():
        total_stat_list = []
        total_stat_list = find_equipment_set_totals(total_stat_list)

        with open('Results/equipment_stats.csv','w', newline='') as f:
            header = ['Resilience', 'Recovery', 'Discipline']
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(total_stat_list)
        # for stat in total_stat_list:
        #     print('{}'.format(stat))


ThisClass.runthisclass()
