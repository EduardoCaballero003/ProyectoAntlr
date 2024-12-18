# Generated from grammarcode.g4 by ANTLR 4.13.2
from antlr4 import *
import re
from grammarcodeLexer import grammarcodeLexer
from grammarcodeParser import grammarcodeParser
if "." in __name__:
    from .grammarcodeParser import grammarcodeParser
else:
    from grammarcodeParser import grammarcodeParser

from antlr4 import ParseTreeListener

from antlr4 import *
from grammarcodeParser import grammarcodeParser
from grammarcodeListener import grammarcodeListener

class Traductor3(ParseTreeListener):
    def __init__(self):
        self.code = []
        self.indent_level = 0
        self.inside_loop = False
        self.inside_while = False
        self.inside_if = False

    # Enter a parse tree produced by grammarcodeParser#program.
    def enterProgram(self, ctx:grammarcodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#program.
    def exitProgram(self, ctx:grammarcodeParser.ProgramContext):
        pass

    # Enter a parse tree produced by grammarcodeParser#inicioBloque.
    def enterInicioBloque(self, ctx:grammarcodeParser.InicioBloqueContext):
        self.code.append("def main():")
        self.indent_level += 1

    # Exit a parse tree produced by grammarcodeParser#inicioBloque.
    def exitInicioBloque(self, ctx:grammarcodeParser.InicioBloqueContext):
        self.code.append("")
        self.code.append("if __name__ == '__main__':")
        self.code.append("    main()")

    # Enter a parse tree produced by grammarcodeParser#definicionFuncion.
    def enterDefinicionFuncion(self, ctx:grammarcodeParser.DefinicionFuncionContext):
        nameFunction = ctx.getChild(1).getText()
        param_List = ''
        parameters = ctx.getChild(3)
        
        param_List = ''
        index = 0

        for i in range(parameters.getChildCount()):
            if parameters.getChild(i).getText() == ',':
                index -= 1

            if index % 2 == 1 and parameters.getChild(i).getText() != ',':
                if param_List == '':
                    param_List += parameters.getChild(i).getText()
                else:
                    param_List += (',' + parameters.getChild(i).getText())
            index += 1
        self.code.append(f"{self.get_indent()}def {nameFunction} ({param_List}):")
        self.indent_level += 1

    # Exit a parse tree produced by grammarcodeParser#definicionFuncion.
    def exitDefinicionFuncion(self, ctx:grammarcodeParser.DefinicionFuncionContext):
        self.indent_level -= 1
        self.code.append("")

    # Enter a parse tree produced by grammarcodeParser#returnStatement.
    def enterReturnStatement(self, ctx:grammarcodeParser.ReturnStatementContext):
        returnVaue = ctx.getChild(1).getText()
        self.code.append(f"{self.get_indent()}return {returnVaue}")

    # Exit a parse tree produced by grammarcodeParser#returnStatement.
    def exitReturnStatement(self, ctx:grammarcodeParser.ReturnStatementContext):
        pass

    # Enter a parse tree produced by grammarcodeParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:grammarcodeParser.LlamadaFuncionContext):
        function_name = ctx.getChild(0).getText()
        function_param = ''

        if(ctx.getChild(2).getText() != ')'):
            function_param = ctx.getChild(2).getText()

        self.code.append(f"{self.get_indent()}{function_name}({function_param})")

    # Exit a parse tree produced by grammarcodeParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:grammarcodeParser.LlamadaFuncionContext):
        pass

    # Enter a parse tree produced by grammarcodeParser#statement.
    def enterStatement(self, ctx:grammarcodeParser.StatementContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#statement.
    def exitStatement(self, ctx:grammarcodeParser.StatementContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#asignacion.
    def enterAsignacion(self, ctx:grammarcodeParser.AsignacionContext):
        tipo = ctx.getChild(0).getText()
        var_name = ctx.getChild(1).getText()
        valor_ctx = ctx.getChild(3)
        valor = self.translate_expression(valor_ctx)

        if tipo == "esVerdad":
            if valor.lower() in ["si", "verdadero"]:
                valor = "True"
            elif valor.lower() in ["no", "falso"]:
                valor = "False"
        elif tipo == "palabra":
            valor = f'{valor}'

        if "lee" in valor_ctx.getText().lower():
            self.code.append(f"{self.get_indent()}{var_name} = input('> ')")

        patron = r'\b([a-zA-Z][a-zA-Z0-9]*)\.[a-zA-Z][a-zA-Z0-9]*\(\)'
        match = re.search(patron, valor)

        if match:
            matchVoltear = re.search('Voltear()', valor)
            if matchVoltear:
                primer_id = match.group(1)
                new_statement = f"sorted({primer_id}, reverse=True)"
                valor = re.sub(patron, new_statement, valor)

            matchUltimo = re.search('Ultimo()', valor)
            if matchUltimo:
                primer_id = match.group(1)
                new_statement = f"{primer_id}[-1]"
                valor = re.sub(patron, new_statement, valor)

        self.code.append(f"{self.get_indent()}{var_name} = {valor}")

    # Exit a parse tree produced by grammarcodeParser#asignacion.
    def exitAsignacion(self, ctx:grammarcodeParser.AsignacionContext):
        pass

    # Enter a parse tree produced by grammarcodeParser#igualacion.
    def enterIgualacion(self, ctx:grammarcodeParser.IgualacionContext):
        var_name = ctx.getChild(0).getText()
        valor_ctx = ctx.getChild(2)
        valor = self.translate_expression(valor_ctx)

        print(valor)

        patron = r'\b([a-zA-Z][a-zA-Z0-9]*)\.[a-zA-Z][a-zA-Z0-9]*\(\)'
        match = re.search(patron, valor)

        if match:
            matchVoltear = re.search('Voltear()', valor)
            if matchVoltear:
                primer_id = match.group(1)
                new_statement = f"sorted({primer_id}, reverse=True)"
                valor = re.sub(patron, new_statement, valor)

            matchUltimo = re.search('Ultimo()', valor)
            if matchUltimo:
                primer_id = match.group(1)
                new_statement = f"{primer_id}[-1]"
                valor = re.sub(patron, new_statement, valor)

        self.code.append(f"{self.get_indent()}{var_name} = {valor}")
    

    # Exit a parse tree produced by grammarcodeParser#igualacion.
    def exitIgualacion(self, ctx:grammarcodeParser.IgualacionContext):
        pass

    # Enter a parse tree produced by grammarcodeParser#expression.
    def enterExpression(self, ctx:grammarcodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#expression.
    def exitExpression(self, ctx:grammarcodeParser.ExpressionContext):
        pass

    # Enter a parse tree produced by grammarcodeParser#repetirCiclo.
    def enterRepetirCiclo(self, ctx:grammarcodeParser.RepetirCicloContext):
        repeticiones = ctx.NUMBER().getText()
        self.code.append(f"{self.get_indent()}for actual in range({repeticiones}):")
        self.indent_level += 1
        self.inside_loop = True

    # Exit a parse tree produced by grammarcodeParser#repetirCiclo.
    def exitRepetirCiclo(self, ctx:grammarcodeParser.RepetirCicloContext):
        self.indent_level -= 1
        self.inside_loop = False

    # Enter a parse tree produced by grammarcodeParser#mientrasCiclo.
    def enterMientrasCiclo(self, ctx:grammarcodeParser.MientrasCicloContext):
        condicion = self.translate_expression(ctx.condition())
        self.code.append(f"{self.get_indent()}while ({condicion}):")
        self.indent_level += 1
        self.inside_while = True

    # Exit a parse tree produced by grammarcodeParser#mientrasCiclo.
    def exitMientrasCiclo(self, ctx:grammarcodeParser.MientrasCicloContext):
        self.indent_level -= 1
        self.inside_while = False

    # Enter a parse tree produced by grammarcodeParser#condicional.
    def enterCondicional(self, ctx:grammarcodeParser.CondicionalContext):
        condicion = self.translate_expression(ctx.condition())
        self.code.append(f"{self.get_indent()}if ({condicion}):")
        self.indent_level += 1
            
    # Exit a parse tree produced by grammarcodeParser#condicional.
    def exitCondicional(self, ctx:grammarcodeParser.CondicionalContext):
        self.indent_level -= 1
        self.inside_if = False
    
     # Enter a parse tree produced by grammarcodeParser#condicionalelse.
    def enterCondicionalelse(self, ctx:grammarcodeParser.CondicionalelseContext):
        self.indent_level -= 1
        self.code.append(f"{self.get_indent()}else:")
        self.indent_level += 1

    # Exit a parse tree produced by grammarcodeParser#condicionalelse.
    def exitCondicionalelse(self, ctx:grammarcodeParser.CondicionalelseContext):
        self.indent_level -= 1

    # Enter a parse tree produced by grammarcodeParser#condition.
    def enterCondition(self, ctx:grammarcodeParser.ConditionContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#condition.
    def exitCondition(self, ctx:grammarcodeParser.ConditionContext):
        pass

    # Enter a parse tree produced by grammarcodeParser#declaraArr.
    def enterDeclaraArr(self, ctx:grammarcodeParser.DeclaraArrContext):
        
        Arr_ID = ctx.getChild(2)
        Arr_Cont = ''

        if(ctx.getChildCount() == 7):
            Arr_Cont = f"[{ctx.getChild(5).getText()}]"
        elif(ctx.getChildCount() == 5):
            Arr_Cont = ctx.getChild(4).getText()
        else:
            Arr_Cont = f"[{Arr_Cont}]"

        self.code.append(f"{self.get_indent()}{Arr_ID} = {Arr_Cont}")

    # Exit a parse tree produced by grammarcodeParser#declaraArr.
    def exitDeclaraArr(self, ctx:grammarcodeParser.DeclaraArrContext):
        pass

    # Enter a parse tree produced by grammarcodeParser#operationArr.
    def enterOperationArr(self, ctx:grammarcodeParser.OperationArrContext):
        operation = ctx.getChild(2).getText()
        Arr_id = ctx.getChild(0).getText()

        if(ctx.getChildCount() == 6 and operation != 'Voltear'):
            valor_ctx = ctx.getChild(4)
            valor = self.translate_expression(valor_ctx)
            if(operation == 'Agregar'):
                self.code.append(f"{self.get_indent()}{Arr_id}.append({valor})")
            elif(operation == 'Agregar-en'):
                self.code.append(f"{self.get_indent()}{Arr_id}.insert({valor})")
            elif(operation == 'Elimina'):
                self.code.append(f"{self.get_indent()}{Arr_id}.remove({valor})")
            elif(operation == 'Elimina-en'):
                self.code.append(f"{self.get_indent()}del {Arr_id}[{valor}]")
        elif(operation == 'Voltear'):
            self.code.append(f"{self.get_indent()}{Arr_id}.sort(reverse=True)")
        
    # Exit a parse tree produced by grammarcodeParser#operationArr.
    def exitOperationArr(self, ctx:grammarcodeParser.OperationArrContext):
        pass

    # Enter a parse tree produced by grammarcodeParser#printStatement.
    def enterPrintStatement(self, ctx:grammarcodeParser.PrintStatementContext):
        mensaje = ctx.getChild(2).getText()

        self.code.append(f"{self.get_indent()}print({mensaje})")

    # Enter a parse tree produced by grammarcodeParser#entrada.
    def enterEntrada(self, ctx:grammarcodeParser.EntradaContext):
        var_name = ctx.getChild(ctx.getChildCount() - 1).getText()
        mesage = ctx.getChild(2).getText()
        tipe = ctx.getChild(5).getText()
        
        if(tipe == 'decimal'):
            self.code.append(f"{self.get_indent()}{var_name} = float(input({mesage}))")
        elif(tipe == 'entero'):
            self.code.append(f"{self.get_indent()}{var_name} = int(input({mesage}))")
        else:
            self.code.append(f"{self.get_indent()}{var_name} = input({mesage})")

        ###Metodos para la identacion###
    def get_indent(self):
        return "    " * self.indent_level

    def translate_expression(self, ctx):
        if ctx.getChildCount() > 1:
            izquierdo = self.translate_expression(ctx.getChild(0))
            operador = ctx.getChild(1).getText()
            derecho = self.translate_expression(ctx.getChild(2))

            operadores = {
                "mas": "+",
                "menos": "-",
                "por": "*",
                "entre": "/",
                "potencia": "**",
                "raiz": "sqrt",
                "sobrante": "%"
            }

            comparadores = {
                "menor": "<",
                "mayor": ">",
                "menorIgual": "<=",
                "mayorIgual": ">=",
                "igual": "==",
                "distinto": "!="
            }

            if operador in comparadores:
                return f"({izquierdo} {comparadores[operador]} {derecho})"

            if operador in operadores:
                return f"({izquierdo} {operadores[operador]} {derecho})"

        return ctx.getText()

    def translate_instrucciones(self, ctx):
        # Verificar si ctx es una lista
        if isinstance(ctx, list):
            for statement in ctx:
                if isinstance(statement, grammarcodeParser.StatementContext):
                    self.code.append(f"{self.get_indent()}{statement.getText()}")
        else:
            # Si no es una lista, tratarlo como un único StatementContext
            if isinstance(ctx, grammarcodeParser.StatementContext):
                self.code.append(f"{self.get_indent()}{ctx.getText()}")

    def get_code(self):
        return "\n".join(self.code)
