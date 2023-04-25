def tokenize(expression):
    # Chuyển đổi biểu thức trung tố thành danh sách các token
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            # Nếu kí tự hiện tại là một chữ số, chuyển đổi nó và các kí tự liền sau nó thành một số nguyên
            j = i + 1
            while j < len(expression) and expression[j].isdigit():
                j += 1
            tokens.append(expression[i:j])
            i = j
        else:
            # Nếu kí tự hiện tại không phải là chữ số, thêm nó vào danh sách token
            tokens.append(expression[i])
            i += 1
    return tokens

def trung_to_hau_to(tokens):
    # Định nghĩa một từ điển để lưu trữ độ ưu tiên của các toán tử
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Tạo danh sách rỗng để lưu trữ các toán tử và biểu thức hậu tố
    operator_stack = []
    postfix_expression = []

    for token in tokens:
        if token.isdigit():
            postfix_expression.append(token)
        elif token in precedence:
            while operator_stack and operator_stack[-1] != '(' and precedence[operator_stack[-1]] >= precedence[token]:
                postfix_expression.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix_expression.append(operator_stack.pop())
            operator_stack.pop()
    while operator_stack:
        postfix_expression.append(operator_stack.pop())
    return postfix_expression
