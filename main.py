from balancing import balans

balanced_1 = '(((([{}]))))'
balanced_2 = '[([])((([[[]]])))]{()}'
balanced_3 = '{{[()]}}'

unbalanced_1 = '}{}'
unbalanced_2 = '{{[(])]}}'
unbalanced_3 = '[[{())}]'

if __name__ == '__main__':
    print(balans(balanced_1))
    print(balans(balanced_2))
    print(balans(balanced_3))
    print(balans(unbalanced_1))
    print(balans(unbalanced_2))
    print(balans(unbalanced_3))