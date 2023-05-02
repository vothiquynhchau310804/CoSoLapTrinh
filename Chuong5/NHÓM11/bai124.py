def trung_to_hau_to(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    operators = []
    hau_to = []

    for token in tokens:
        if token.isdigit():
            hau_to.append(token)
        elif token in precedence:
            while operators and operators[-1] != '(' and precedence[operators[-1]] >= precedence[token]:
                hau_to.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                hau_to.append(operators.pop())
            operators.pop()
    while operators:
        hau_to.append(operators.pop())
    return hau_to

trung_to_expr = input("Nhập biểu thức trung tố: ")
tokens =(trung_to_expr)
hau_to_expr = trung_to_hau_to(tokens)
print("Biểu thức hậu tố tương đương:", ' '.join(hau_to_expr))