def evaluate_logical_expression(expression):
    stack = []
    i = 0
    n = len(expression)
    
    while i < n:
        char = expression[i]
        if char == ' ':
            i += 1
            continue
        elif char == 'T':
            # Проверяем, что это отдельный T
            if i + 1 < n and expression[i+1] not in [' ', ')', 'A', 'X', 'O', '>']:
                raise ValueError(f"Unexpected character after 'T': {expression[i+1]}")
            stack.append(True)
            i += 1
        elif char == 'F':
            # Проверяем, что это отдельный F
            if i + 1 < n and expression[i+1] not in [' ', ')', 'A', 'X', 'O', '>']:
                raise ValueError(f"Unexpected character after 'F': {expression[i+1]}")
            stack.append(False)
            i += 1
        elif char == '<':
            # Обрабатываем операнд в угловых скобках
            i += 1
            operand_start = i
            while i < n and expression[i] != '>':
                i += 1
            if i >= n:
                raise ValueError("Unclosed angle bracket '>'")
            operand = expression[operand_start:i]
            if operand == 'T':
                stack.append(True)
            elif operand == 'F':
                stack.append(False)
            else:
                raise ValueError(f"Unknown operand inside angle brackets: {operand}")
            i += 1  # Пропускаем '>'
        elif char == '(':
            stack.append(char)
            i += 1
        elif char == 'N':
            # Разрешаем N с угловыми скобками или без
            stack.append('N')
            i += 1
        elif char in ['A', 'X', 'O']:
            stack.append(char)
            i += 1
        elif char == ')':
            # Выполняем операцию
            if len(stack) < 1:
                raise ValueError("Stack underflow")
            operand = stack.pop()
            
            if len(stack) < 1:
                raise ValueError("Missing operator")
            operator = stack.pop()
            
            if operator == 'N':
                result = not operand
            else:
                # Для бинарных операций
                if len(stack) < 1:
                    raise ValueError("Missing left operand")
                operand_left = stack.pop()
                if operator == 'A':
                    result = operand_left and operand
                elif operator == 'X':
                    result = operand_left ^ operand
                elif operator == 'O':
                    result = operand_left or operand
                else:
                    raise ValueError(f"Unknown operator: {operator}")
            
            # Удаляем '('
            if not stack or stack[-1] != '(':
                raise ValueError("Mismatched parentheses")
            stack.pop()
            stack.append(result)
            i += 1
        else:
            raise ValueError(f"Unknown character: {char}")
    
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    
    return stack[0]

def main():
    input_file = "input.txt"
    
    try:
        with open(input_file, 'r') as file:
            content = file.read().strip()
        
        expressions = [expr.strip() for expr in content.split('|') if expr.strip()]
        
        for expr in expressions:
            try:
                result = evaluate_logical_expression(expr)
                print(f"Expression: {expr} => Result: {result}")
            except ValueError as e:
                print(f"Error in expression '{expr}': {e}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found. Please create the file.")

if __name__ == "__main__":
    main()