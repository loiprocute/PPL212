# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classes.
    def visitClasses(self, ctx:D96Parser.ClassesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declares.
    def visitClass_declares(self, ctx:D96Parser.Class_declaresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declare.
    def visitClass_declare(self, ctx:D96Parser.Class_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#body.
    def visitBody(self, ctx:D96Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#body_class.
    def visitBody_class(self, ctx:D96Parser.Body_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#body_classes.
    def visitBody_classes(self, ctx:D96Parser.Body_classesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_declare.
    def visitAttribute_declare(self, ctx:D96Parser.Attribute_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varible.
    def visitVarible(self, ctx:D96Parser.VaribleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl.
    def visitVardecl(self, ctx:D96Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#term.
    def visitTerm(self, ctx:D96Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method.
    def visitMethod(self, ctx:D96Parser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_declare.
    def visitMethod_declare(self, ctx:D96Parser.Method_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor_declare.
    def visitDestructor_declare(self, ctx:D96Parser.Destructor_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor_declare.
    def visitConstructor_declare(self, ctx:D96Parser.Constructor_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_IDs.
    def visitList_IDs(self, ctx:D96Parser.List_IDsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ids.
    def visitIds(self, ctx:D96Parser.IdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_ID.
    def visitList_ID(self, ctx:D96Parser.List_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp0.
    def visitExp0(self, ctx:D96Parser.Exp0Context):
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


    # Visit a parse tree produced by D96Parser#exp5.
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp6.
    def visitExp6(self, ctx:D96Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp7.
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp8.
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp9.
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp10.
    def visitExp10(self, ctx:D96Parser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp11.
    def visitExp11(self, ctx:D96Parser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operator.
    def visitIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_param.
    def visitList_param(self, ctx:D96Parser.List_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varconst_declare.
    def visitVarconst_declare(self, ctx:D96Parser.Varconst_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varible1.
    def visitVarible1(self, ctx:D96Parser.Varible1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl1.
    def visitVardecl1(self, ctx:D96Parser.Vardecl1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#term1.
    def visitTerm1(self, ctx:D96Parser.Term1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_assign.
    def visitStmt_assign(self, ctx:D96Parser.Stmt_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_if.
    def visitStmt_if(self, ctx:D96Parser.Stmt_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_elif.
    def visitStmt_elif(self, ctx:D96Parser.Stmt_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_else.
    def visitStmt_else(self, ctx:D96Parser.Stmt_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_foreach.
    def visitStmt_foreach(self, ctx:D96Parser.Stmt_foreachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_while.
    def visitStmt_while(self, ctx:D96Parser.Stmt_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_break.
    def visitStmt_break(self, ctx:D96Parser.Stmt_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_continue.
    def visitStmt_continue(self, ctx:D96Parser.Stmt_continueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_return.
    def visitStmt_return(self, ctx:D96Parser.Stmt_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_callMethod.
    def visitStmt_callMethod(self, ctx:D96Parser.Stmt_callMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_access.
    def visitMember_access(self, ctx:D96Parser.Member_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#in_method.
    def visitIn_method(self, ctx:D96Parser.In_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stt_method.
    def visitStt_method(self, ctx:D96Parser.Stt_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_stmt.
    def visitList_stmt(self, ctx:D96Parser.List_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmts.
    def visitStmts(self, ctx:D96Parser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array.
    def visitArray(self, ctx:D96Parser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#i_array.
    def visitI_array(self, ctx:D96Parser.I_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#m_array.
    def visitM_array(self, ctx:D96Parser.M_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listARRAY.
    def visitListARRAY(self, ctx:D96Parser.ListARRAYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listLIT.
    def visitListLIT(self, ctx:D96Parser.ListLITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_mem.
    def visitList_mem(self, ctx:D96Parser.List_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listval.
    def visitListval(self, ctx:D96Parser.ListvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typ.
    def visitTyp(self, ctx:D96Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arraytype.
    def visitArraytype(self, ctx:D96Parser.ArraytypeContext):
        return self.visitChildren(ctx)



del D96Parser