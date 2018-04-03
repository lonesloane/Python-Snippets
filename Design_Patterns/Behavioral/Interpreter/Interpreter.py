class Expression:
    def interpret(self, text): pass


class TerminalExpression(Expression):
    def __init__(self, word):
        self.word = word

    def interpret(self, text):
        words = text.split()
        if self.word in words:
            return True
        else:
            return False


class OrExpression(Expression):
    def __init__(self, exp1: Expression, exp2: Expression):
        self.exp1 = exp1
        self.exp2 = exp2

    def interpret(self, text):
        return self.exp1.interpret(text) or self.exp2.interpret(text)


class AndExpression(Expression):
    def __init__(self, exp1:Expression, exp2:Expression):
        self.exp1 = exp1
        self.exp2 = exp2

    def interpret(self, text):
        return self.exp1.interpret(text) and self.exp2.interpret(text)


# === usage ===


john = TerminalExpression('John')
henry = TerminalExpression('Henry')
mary = TerminalExpression('Mary')
sarah = TerminalExpression('Sarah')

# construct the rule sarah and ( mary or (john and henry))
rule1 = AndExpression(john, henry)
rule2 = OrExpression(mary, rule1)
rule3 = AndExpression(sarah, rule2)

to_be_interpreted = ['Sarah', 'Sarah Mary', 'Sarah John', 'Sarah Henry', 'Sarah John Henry']
for expression in to_be_interpreted:
    print("rule3.interpret({}): ".format(expression))
    print(rule3.interpret(expression))
    print('-'*15)
