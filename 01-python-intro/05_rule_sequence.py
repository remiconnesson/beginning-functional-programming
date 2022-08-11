def zero(s):
    if s[0] == "0":
        return s[1:]

def one(s):
    if s[0] == "1":
        return s[1:]

"""
Imperative Version
"""
def rule_sequence(s, rules):
    for rule in rules:
        s = rule(s)
        if s == None:
            break
    return s

print('Imperative version')
print('Should print 1    : ', rule_sequence('0101', [zero, one, zero]))
print('Should print None : ', rule_sequence('0101', [zero, zero]))
print('')

"""
Functional Version
"""
def rule_sequence(s, rules):
    if s == None or not rules:
        return s
    else:
        return rule_sequence(rules[0](s), rules[1:])

print('Functional version')
print('Should print 1    : ', rule_sequence('0101', [zero, one, zero]))
print('Should print None : ', rule_sequence('0101', [zero, zero]))
print('')
