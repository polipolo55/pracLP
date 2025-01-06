from SchemeVisitor import SchemeVisitor

class EvalVisitor(SchemeVisitor):
    def __init__(self):

        self.debug = False

        self.environment = {
            '#t': True,
            '#f': False
        } 

        self.operadors = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '>=': lambda x, y: x >= y,
            '<=': lambda x, y: x <= y,
            '>': lambda x, y: x > y,
            '<': lambda x, y: x < y,
            '=' : lambda x, y: x == y,
            '<>' : lambda x, y: x != y,
        }

    def visitProgram(self, ctx):
        results = []
        for expr in ctx.expression():
            result = self.visit(expr)
            if result is not None:
                results.append(result)
        return results

    def visitArOperation(self, ctx):
        [operador] = list(ctx.getChildren())
        return self.operadors[operador.getText()]

    def visitBoOperatio(self, ctx):
        [operador] = list(ctx.getChildren())
        return self.operadors[operador.getText()]

    def visitNum(self, ctx):
        return int(ctx.getText())

    def visitId(self, ctx):
        text = ctx.getText()
        return self.environment.get(text, f"Undefined variable: {text}")

    def visitStr(self, ctx):
        text = ctx.getText()
        return text.strip('"')

    def visitTrue(self, ctx):
        return True

    def visitFalse(self, ctx):
        return False

    def define_variable(self, var_node, value_node):
        nom = var_node.getText()
        valor = self.visit(value_node)
        self.environment[nom] = valor
        return f"Variable {nom} definida amb valor {valor}"

    def define_function(self, func_node, body_node):
        func_parts = list(func_node.getChildren())
        if len(func_parts) < 2:
            raise Exception("Definicio de funcio no valida: parametres")

        _, nom, *params, _ = func_parts
        self.environment[nom.getText()] = ([param.getText() for param in params], body_node)
        return f"Funcio {nom.getText()} definida."

    def handle_operation(self, operador, expressions):
        op = self.visit(operador)
        if len(expressions) != 2:
            raise Exception("Operacio no valida")
        return op(self.visit(expressions[0]), self.visit(expressions[1]))
    


    def call_function(self, funcio, expressions):
        if funcio not in self.environment:
            raise Exception(f"Funcio {funcio} no definida")
        
        func = self.environment[funcio]

        if not isinstance(func, tuple):
            raise Exception(f"{funcio} no es una funcio")
        
        params, cos = func
        if len(params) != len(expressions):
            raise Exception(f"La funcio {funcio} requereix {len(params)} parametres, pero n'ha rebut {len(expressions)}")
        
        temp_env = self.environment.copy()

        for param, expr in zip(params, expressions):
            temp_env[param] = self.visit(expr)


        original_env = self.environment
        self.environment = temp_env
        res = None
        for f in cos:
            res = self.visit(f)
        self.environment = original_env
        return res

    def handle_if_clause(self, cond_expr, true_expr, false_expr):
        condition_result = self.visit(cond_expr)
        return self.visit(true_expr) if condition_result else self.visit(false_expr)
    
    def define_list(self, expressions):
        l = []
        for expr in expressions:
            l.append(self.visit(expr))
        return l
    
    def car(self, lst):
        if not lst:  # Si la llista està buida
            raise Exception("Car no es pot aplicar a una llista buida")
        return lst[0]

    def cdr(self, lst):
        if not lst:  # Si la llista està buida
            raise Exception("Cdr no es pot aplicar a una llista buida")
        return lst[1:]

    def cons(self, element, lst):
        return [element] + lst
    
    def null(self, lst):
        return lst == []


    def handle_cond_clause(self, clauses):
        for clause in clauses:
            children = list(clause.getChildren())
            if len(children) >= 2:
                condition = children[1]
                expressions = children[2:]
                condition_result = self.visit(condition)
                if condition_result:
                    return self.visit(expressions[0])
        return None
    

    def handle_let_clause(self, bindings, expressions):
        if not isinstance(bindings, list):
            raise Exception("Let requereix una llista de definicions")
        local_env = self.environment.copy()

        for name, value in bindings:
            print(f"Definint LET {name} amb valor {value}")
            local_env[name] = value


        original_env = self.environment
        self.environment = local_env
        for expression in expressions:
            result = self.visit(expression)
        self.environment = original_env

        return result

    def handle_read(self):
        print("Toca llegir un valor")
        input_text = input()
        try:
            return int(input_text)
        except ValueError:
            return input_text


    def visitCalls(self, ctx):
        children = list(ctx.getChildren())
        _, operador, *expressions, _ = children
        operador_text = operador.getText()

        if (self.debug): print("call amb operador", operador_text)

        if operador_text == 'define':
            if len(expressions) < 1:
                raise Exception("Definicio no valida")
            first_expr = list(expressions[0].getChildren())
            if len(first_expr) == 1:
                return self.define_variable(expressions[0], expressions[1])
            else:
                return self.define_function(expressions[0], expressions[1:])
        
        elif operador_text == 'display':
            if len(expressions) != 1:
                raise Exception("Display requereix exactament un argument")
            result = self.visit(expressions[0])
            print(result)
            return result

        elif operador_text == 'newline':
            print()
            return None
        
        elif operador_text == 'read':
            if len(expressions) != 0:
                raise Exception("Read no requereix arguments")
            return self.handle_read()

        elif operador_text == 'let':              
            _, *bindings_exprs, _ = list(expressions[0].getChildren())
            if not isinstance(bindings_exprs, list):
                raise Exception("Let requereix una llista de definicions")
            bindings = [] 
            for binding_ctx in bindings_exprs:
                _, var, value, _ = list(binding_ctx.getChildren())
                bindings.append((var.getText(), self.visit(value)))
            expressions = expressions[1:]
            return self.handle_let_clause(bindings, expressions)

        ## Llistes

        elif operador_text == '(': 
            return self.define_list(expressions)


        elif operador_text == 'car':
            if len(expressions) != 1:
                raise Exception("Car requereix exactament un argument")
            lst = self.visit(expressions[0])
            if not isinstance(lst, list):
                raise Exception("Car només s'aplica a llistes")
            return self.car(lst)

        elif operador_text == 'cdr':
            if len(expressions) != 1:
                raise Exception("Cdr requereix exactament un argument")
            lst = self.visit(expressions[0])
            if not isinstance(lst, list):
                raise Exception("Cdr només s'aplica a llistes")
            return self.cdr(lst)

        elif operador_text == 'cons':
            if len(expressions) != 2:
                raise Exception("Cons requereix exactament dos arguments")
            element = self.visit(expressions[0])
            lst = self.visit(expressions[1])
            if not isinstance(lst, list):
                raise Exception("Cons només s'aplica a llistes com a segon argument")
            return self.cons(element, lst)

        elif operador_text == 'null?':
            if len(expressions) != 1:
                raise Exception("Null? requereix exactament un argument")
            lst = self.visit(expressions[0])
            if not isinstance(lst, list):
                raise Exception("Null? només s'aplica a llistes")
            return self.null(lst)

        
        ## Condicions

        elif operador_text == 'if':
            if len(expressions) != 3:
                raise Exception("If no valid")
            return self.handle_if_clause(expressions[0], expressions[1], expressions[2])

        elif operador_text == 'cond':
    
            return self.handle_cond_clause(expressions)
        
        ## Operacions
        
        elif hasattr(operador, 'arithmeticOperation') or hasattr(operador, 'booleanOperation'):
            return self.handle_operation(operador, expressions)
        
        else:
            return self.call_function(operador_text, expressions)