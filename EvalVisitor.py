from SchemeVisitor import SchemeVisitor
from SchemeParser import SchemeParser

class EvalVisitor(SchemeVisitor):
    # Inicialitza l'visitor amb variables d'entorn i operadors
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

        if self.debug:
            print("Initialized EvalVisitor with environment:", self.environment)


    # Processa el programa principal del parser
    def visitProgram(self, ctx):
        if self.debug:
            print("Entering visitProgram")
        for expr in ctx.expression():
            if self.debug:
                print(f"Processing expression: {expr.getText()}")
            if not isinstance(expr, SchemeParser.CallsContext):
                raise Exception("Només es poden fer definicions globals fora del main.")
            op = expr.getChild(1).getText()
            if op != 'define':
                raise Exception("Només es poden fer definicions globals fora del main.")
            self.visit(expr)
        
        if 'main' not in self.environment:
            raise Exception("Funció main no definida.")
        if self.debug:
            print("Calling 'main' function")
        return self.call_function('main', [])


    # Visita una operació aritmètica
    def visitArOperation(self, ctx):
        [operador] = list(ctx.getChildren())
        return self.operadors[operador.getText()]


    # Visita una operació booleana
    def visitBoOperatio(self, ctx):
        [operador] = list(ctx.getChildren())
        return self.operadors[operador.getText()]


    # Visita un número literal
    def visitNum(self, ctx):
        value = int(ctx.getText())
        if self.debug:
            print(f"Visited number: {value}")
        return value


    # Visita un identificador
    def visitId(self, ctx):
        text = ctx.getText()
        value = self.environment.get(text, f"Undefined variable: {text}")
        if self.debug:
            print(f"Visited identifier '{text}' with value: {value}")
        return value


    # Visita una cadena de text
    def visitStr(self, ctx):
        text = ctx.getText().strip('"')
        if self.debug:
            print(f"Visited string: {text}")
        return text


    # Visita el valor booleà True
    def visitTrue(self, ctx):
        if self.debug:
            print("Visited boolean: True")
        return True


    # Visita el valor booleà False
    def visitFalse(self, ctx):
        if self.debug:
            print("Visited boolean: False")
        return False


    # Defineix una variable en l'entorn
    def define_variable(self, var_node, value_node):
        nom = var_node.getText()
        valor = self.visit(value_node)
        if self.debug:
            print(f"Defining variable '{nom}' with value: {valor}")
        self.environment[nom] = valor
        return f"Variable {nom} definida amb valor {valor}"


    # Defineix una funció en l'entorn
    def define_function(self, func_node, body_node):
        func_parts = list(func_node.getChildren())
        if len(func_parts) < 2:
            raise Exception("Definicio de funcio no valida: parametres")

        _, nom, *params, _ = func_parts
        if self.debug:
            print(f"Defining function '{nom.getText()}' with parameters: {[param.getText() for param in params]}")
        self.environment[nom.getText()] = ([param.getText() for param in params], body_node)
        return f"Funcio {nom.getText()} definida."


    # Gestiona una operació binària
    def handle_operation(self, operador, expressions):
        if self.debug:
            print(f"Handling operation '{operador.getText()}' with expressions: {expressions}")
        op = self.visit(operador)
        if len(expressions) != 2:
            raise Exception("Operacio no valida")
        return op(self.visit(expressions[0]), self.visit(expressions[1]))
    


    # Crida una funció amb els arguments proporcionats
    def call_function(self, funcio, expressions):
        if self.debug:
            print(f"Calling function '{funcio}' with arguments: {expressions}")
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
        if self.debug:
            print(f"Function '{funcio}' returned: {res}")
        return res


    # Gestiona una condició 'if'
    def handle_if_clause(self, cond_expr, true_expr, false_expr):
        if self.debug:
            print("Handling 'if' clause")
            print(f"Condition: {cond_expr.getText()}")
            print(f"True expression: {true_expr.getText()}")
            print(f"False expression: {false_expr.getText()}")
        condition_result = self.visit(cond_expr)
        return self.visit(true_expr) if condition_result else self.visit(false_expr)
    

    # Define una llista a partir de les expressions
    def define_list(self, expressions):
        l = []
        for expr in expressions:
            l.append(self.visit(expr))
        return l
    

    # Retorna el primer element d'una llista
    def car(self, lst):
        if not lst: 
            raise Exception("Car no es pot aplicar a una llista buida")
        return lst[0]

    # Retorna la resta d'una llista
    def cdr(self, lst):
        if not lst: 
            raise Exception("Cdr no es pot aplicar a una llista buida")
        return lst[1:]


    # Afegeix un element a una llista
    def cons(self, element, lst):
        return [element] + lst
    

    # Comprova si una llista és buida
    def null(self, lst):
        return lst == []


    # Gestiona una clàusula 'cond'
    def handle_cond_clause(self, clauses):
        if self.debug:
            print("Handling 'cond' clause with clauses:", clauses)
        for clause in clauses:
            children = list(clause.getChildren())
            if len(children) >= 2:
                condition = children[1]
                expressions = children[2:]
                condition_result = self.visit(condition)
                if condition_result:
                    return self.visit(expressions[0])
        return None
    


    # Gestiona una clàusula 'let'
    def handle_let_clause(self, bindings, expressions):
        if self.debug:
            print("Handling 'let' clause with bindings:", bindings)
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


    # Llegeix una entrada de l'usuari
    def handle_read(self):
        input_text = input()
        try:
            return int(input_text)
        except ValueError:
            return input_text



    # Visita una crida a una funció
    def visitCalls(self, ctx):
        if self.debug:
            print("Entering visitCalls")
        children = list(ctx.getChildren())
        _, operador, *expressions, _ = children
        operador_text = operador.getText()
        if self.debug:
            print(f"Operator: {operador_text}, Expressions: {[expr.getText() for expr in expressions]}")

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
        elif operador_text == 'and':
            return all(self.visit(expr) for expr in expressions)
        elif operador_text == 'or':
            return any(self.visit(expr) for expr in expressions)
        elif operador_text == 'not':
            if len(expressions) != 1:
                raise Exception("Not requereix exactament un argument")
            return not self.visit(expressions[0])
        else:
            return self.call_function(operador_text, expressions)