
import matplotlib.pylab as plt
import numpy as np
import pandas as pd


def calc_emi(borrow, irate, months):
    emi = borrow*irate*((1+irate)**months)
    emi = emi/((1+irate)**months - 1)
    return emi

def amort_schedule(borrow, irate, months):
    emi = calc_emi(borrow, irate, months)
    amort_schedule = []
    remain_notional = borrow
    for m in range(months):
        payment = emi
        curr_notional = remain_notional
        int_paid = curr_notional*irate
        principal_paid = emi - int_paid
        remain_notional = curr_notional - principal_paid
        pdict = {'payment': payment,
                 'curr_notional': curr_notional,
                 'int_paid': int_paid,
                 'principal_paid': principal_paid,
                 'remain_notional': remain_notional}
        amort_schedule.append(pdict)
    amort_schedule_df = pd.DataFrame(amort_schedule)
    amort_schedule_df['cumulative_int_paid'] = np.cumsum(amort_schedule_df['int_paid'])
    amort_schedule_df['cumulatgive_principal_paid'] = np.cumsum(amort_schedule_df['principal_paid'])
    return amort_schedule_df


buy_price = 800000
downpay = 0.2
downpay_amount = downpay*buy_price
borrow_amount = buy_price*(1 - downpay)
irate = 3.5/100/12 # monthly
months = 30*12
rent  = 3000
buy_closing_cost = 20000
calc_emi(491250, 3.5/100/12, 12*30)
amort_schedule(borrow_amount, irate, months)

plt.plot(amort_schedule[['']])