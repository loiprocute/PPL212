# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#class_declare.
    def visitClass_declare(self, ctx:D96Parser.Class_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#body_class.
    def visitBody_class(self, ctx:D96Parser.Body_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#code_list.
    def visitCode_list(self, ctx:D96Parser.Code_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_declare.
    def visitAttribute_declare(self, ctx:D96Parser.Attribute_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data_types.
    def visitData_types(self, ctx:D96Parser.Data_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#values_list.
    def visitValues_list(self, ctx:D96Parser.Values_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mptype.
    def visitMptype(self, ctx:D96Parser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#body.
    def visitBody(self, ctx:D96Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcall.
    def visitFuncall(self, ctx:D96Parser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array.
    def visitArray(self, ctx:D96Parser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params_list_sametype.
    def visitParams_list_sametype(self, ctx:D96Parser.Params_list_sametypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_array.
    def visitMulti_array(self, ctx:D96Parser.Multi_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrays.
    def visitArrays(self, ctx:D96Parser.ArraysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_bool.
    def visitExp_bool(self, ctx:D96Parser.Exp_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_int.
    def visitExp_int(self, ctx:D96Parser.Exp_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_real.
    def visitExp_real(self, ctx:D96Parser.Exp_realContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_str.
    def visitExp_str(self, ctx:D96Parser.Exp_strContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp1.
    def visitExp1(self, ctx:D96Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp2.
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp3.
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#call_exp.
    def visitCall_exp(self, ctx:D96Parser.Call_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params_list.
    def visitParams_list(self, ctx:D96Parser.Params_listContext):
        return self.visitChildren(ctx)



del D96Parser