import argparse
import math


def annuity_payment(principal, periods, interest):
    i = (interest / 100) / 12
    i_n = math.pow(1 + i, periods)
    annuity_payment = principal * ((i * i_n) / (i_n - 1))
    overpayment = (math.ceil(annuity_payment) * periods) - principal
    print(f'Your annuity payment = {math.ceil(annuity_payment)}!')
    print(f'Overpayment = {int(overpayment)}')


def annuity_period(principal, payment, interest):
    i = (interest / 100) / 12
    x = payment / (payment - i * principal)
    base = 1 + i
    n = math.log(x, base)
    n = math.ceil(n)
    if n < 12:
        print(f'You need {n} months to repay this credit!')
    elif n >= 12:
        n_years = n // 12
        n_months = n % 12
        year_s = "years"
        if n_months == 0:
            if n_years == 1:
                year_s = "year"
            print(f'You need {n_years} {year_s} to repay this credit!')
        else:
            print(f'You need {n_years} {year_s} and {n_months} months to repay this credit!')
    overpayment = (n * payment) - principal
    print(f'Overpayment = {int(overpayment)}')


def annuity_principal(payment, periods, interest):
    i = (interest / 100) / 12
    i_n = math.pow(1 + i, periods)
    principal = payment / ((i * i_n) / (i_n - 1))
    overpayment = (payment * periods) - principal
    print(f'Your credit principal = {math.floor(principal)}!')
    print(f'Overpayment = {math.ceil(overpayment)}')


def diff_payment(principal, periods, interest):
    i = (interest / 100) / 12
    total_d_m = 0
    overpayment = 0
    for m in range(1, periods + 1):
        d = (principal / periods) + (i * (principal - ((principal * (m - 1)) / periods)))
        d_m = math.ceil(d)
        total_d_m += d_m
        print(f'Month {m}: paid out {d_m}')
        overpayment = total_d_m - principal
    print(f'\nOverpayment = {int(overpayment)}')


parser = argparse.ArgumentParser(description="Credit calculator")
parser.add_argument("--type", help="annuity or differentiated", type=str, choices=['annuity', 'diff'])
parser.add_argument("--payment", help="monthly payment", type=float)
parser.add_argument("--principal", help="credit principal", type=float)
parser.add_argument("--periods", help="number of months", type=int)
parser.add_argument("--interest", help="interest rate", type=float)
args = parser.parse_args()
args_list = [args.type, args.payment, args.principal, args.periods, args.interest]


count = 0
negative_count = 0
for i in range(0, 5):
    if args_list[i] == None or type(args_list[i]) == str:
        count += 1
    else:
        if args_list[i] < 0:
            negative_count += 1
if count > 2 or negative_count > 0:
    print("Incorrect parameter")
    exit()
elif args.interest == None or args.type == None:
    print("Incorrect parameter")
    exit()


if args.type == 'annuity':
    if args.payment == None:
        annuity_payment(args.principal, args.periods, args.interest)
    elif args.periods == None:
        annuity_period(args.principal, args.payment, args.interest)
    elif args.principal == None:
        annuity_principal(args.payment, args.periods, args.interest)
elif args.type == 'diff':
    if args.payment != None or args.interest <= 0:
        print("Incorrect parameter")
        exit()
    else:
        diff_payment(args.principal, args.periods, args.interest)

