import pandas as pd
import numpy as np
import math


def find_lift(num_a_and_b, total_a, total_b, total_overall):
    '''Calculate the lift of a ==> b'''
    prob_a_and_b = num_a_and_b/total_overall
    prob_a = total_a/total_overall
    prob_b = total_b/total_overall
    return prob_a_and_b/(prob_a * prob_b)

# support a -> b = p(a_and_b) = a_and_b/total
def support(num_a_and_b, total_overall):
    '''Calculate the support of a ==> b'''
    a = num_a_and_b/total_overall
    print("answer: ", a, " percentage: ", a * 100)

def confidence(num_a_and_b, total_a):
    '''Calculate the confidence of a ==> b'''
    a = num_a_and_b/total_a
    print("answer: ", a, " percentage: ", a * 100)

def bayes(n, num_lang, num_500, num_lang_and_500, num_genre, num_genre_and_500):
    '''Calculate the naive bayesian for film of a certain language and genre having over 500 user votes'''
    num_under = n - num_500
    prob_over_500 = num_500/n
    prob_under = (num_under)/n
    

    prob_lang_and_500 = num_lang_and_500/num_500
    prob_lang_under = (num_lang - num_lang_and_500) / num_under

    prob_genre_and_500 = num_genre_and_500/num_500
    prob_genre_under = (num_genre - num_genre_and_500)/num_under

    prob_lang_and_genre_500 = prob_lang_and_500 * prob_genre_and_500
    prob_lang_and_genre_under = prob_lang_under * prob_genre_under

    overall_over = prob_lang_and_genre_500 * prob_over_500
    overall_under = prob_lang_and_genre_under * prob_under

    return overall_over, overall_under

def infoD(pos, neg):
    '''info for full dataset'''
    n = pos + neg
    num1 = pos / n
    num2 = neg / n
    infonum1 = 0 - (num1 * math.log2(num1))
    infonum2 = num2 * math.log2(num2)
    return infonum1 - infonum2

def info_a(pos_category, neg_category):
    '''info for attribute a'''
    category_total = pos_category + neg_category
    num1 = pos_category / category_total
    num2 = neg_category / category_total
    infonum1 = 0 - (num1 * math.log2(num1))
    infonum2 = num2 * math.log2(num2)
    return infonum1 - infonum2

def infoa_D(cat1_n, cat1_info_a, cat2_n, cat2_info_a):
    '''info attribute a for dataset'''
    n = cat1_n + cat2_n
    num1 = cat1_n / n
    num2 = cat2_n / n
    return (num1 * cat1_info_a) + (num2 * cat2_info_a)

def info_gain(infod, infoad):
    '''info gain for att a, dataset'''
    return infod - infoad

def infoa_D3(cat1_n, cat1_info_a, cat2_n, cat2_info_a, cat3_n, cat3_info_a):
    '''info attribute a for dataset with three poss outcomes'''
    n = cat1_n + cat2_n + cat3_n
    num1 = cat1_n / n
    num2 = cat2_n / n
    num3 = cat3_n / n
    return (num1 * cat1_info_a) + (num2 * cat2_info_a) + (num3 * cat3_info_a)