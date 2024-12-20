import re
import json
import sys
import math

def evaluate_expression(expression):
    tokens = expression.split()
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            b, a = stack.pop(), stack.pop()
            stack.append(a / b)
        elif token == 'max()':
            if stack:
                max_val = max(stack)
                stack.clear()
                stack.append(max_val)
        elif token == 'sqrt()':
            if stack:
                stack.append(math.sqrt(stack.pop()))
        elif token.startswith('sqrt('):
            # Обработка выражения с sqrt(x)
            arg = int(token[5:-1])  # Извлекаем аргумент из строки, например, sqrt(25) -> 25
            stack.append(math.sqrt(arg))

    return stack[0] if stack else None

def parse_config(text):
    config = {}
    text = re.sub(r'#\|[\s\S]*?\|#', '', text)

    lines = text.splitlines()
    current_dict = None

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line == "begin":
            current_dict = {}
            continue
        elif line == "end":
            config.update(current_dict)
            current_dict = None
            continue

        # Обработка массивов
        list_match = re.match(r'(\w+)\s*:=\s*list\((.*?)\);?', line)
        if list_match:
            name, items = list_match.groups()
            items_list = [item.strip().strip("'") for item in items.split(',')]
            if current_dict is not None:
                current_dict[name] = items_list
            else:
                config[name] = items_list
            continue
        else:
            # Обработка выражений в фигурных скобках
            expr_match = re.match(r'(\w+)\s*:=\s*\{(.*?)\};?', line)
            if expr_match:
                name, expression = expr_match.groups()
                result = evaluate_expression(expression)
                if result is not None:
                    if current_dict is not None:
                        current_dict[name] = result
                    else:
                        config[name] = result
                else:
                    print("Error in line {", line, "}")
                continue
            else:
                # Обработка обычных ключ-значений
                kv_match = re.match(r'(\w+)\s*:=\s*(.+?);', line)
                if kv_match:
                    name, value = kv_match.groups()
                    value = value.strip()

                    if value == 'true':
                        value = True
                    elif value == 'false':
                        value = False
                    elif value.startswith("'") and value.endswith("'"):
                        value = value.strip("'")
                    elif value.isdigit():
                        value = int(value)

                    if current_dict is not None:
                        current_dict[name] = value
                    else:
                        config[name] = value
                else:
                    print("Error in line {", line, "}")

    return config

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <output_file.json>")
        sys.exit(1)

    output_file = sys.argv[1]
    input_text = sys.stdin.read()

    config = parse_config(input_text)

    with open(output_file, 'w') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)