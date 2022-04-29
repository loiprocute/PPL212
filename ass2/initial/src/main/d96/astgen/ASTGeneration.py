from calendar import c
from lib2to3.pgen2.token import COLON
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce

#from main.d96.utils.AST import Static 

class ASTGeneration(D96Visitor):
    #program: classes EOF ;
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(self.visit(ctx.classes()))
    #classes: class_declare class_declares ;
    def visitClasses(self, ctx: D96Parser.ClassesContext):
        return self.visit(ctx.class_declare())+self.visit(ctx.class_declares())
    #class_declares:class_declare class_declares|;
    def visitClass_declares(self, ctx: D96Parser.Class_declaresContext):
        if ctx.getChildCount()==0:
            return []
        return self.visit(ctx.class_declare())+self.visit(ctx.class_declares())
    
    #class_declare : CLASS ID (COLON ID)? LP body RP ;
    def visitClass_declare(self, ctx: D96Parser.Class_declareContext):
        body=self.visit(ctx.body())
        if Id(ctx.ID(0).getText()).name=="Program":
            for i in body:
                if isinstance(i,MethodDecl) and i.name.name == "main" and i.param == []:
                    i.kind=Static()
        if ctx.COLON():
            return [ClassDecl(Id(ctx.ID(0).getText()),body,Id(ctx.ID(1).getText()))]
        return [ClassDecl(Id(ctx.ID(0).getText()),body)]
 
    #body: body_class | ;        
    def visitBody(self, ctx: D96Parser.BodyContext):
        if ctx.getChildCount()==0:
            return []
        return self.visit(ctx.body_class())
    
    #body_class : member body_classes; 
    def visitBody_class(self, ctx: D96Parser.Body_classContext):
        return self.visit(ctx.member())+self.visit(ctx.body_classes())
    #body_classes: member body_classes |;
    def visitBody_classes(self, ctx: D96Parser.Body_classesContext):
        if ctx.getChildCount()==0:
            return []
        return self.visit(ctx.member())+self.visit(ctx.body_classes())
    
    #member :attribute_declare|method|  ;
    def visitMember(self, ctx: D96Parser.MemberContext):
        if ctx.method():
            return self.visit(ctx.method())
        return self.visit(ctx.attribute_declare())
    #attribute_declare: varible SEMI;
    def visitAttribute_declare(self, ctx: D96Parser.Attribute_declareContext):
        return self.visit(ctx.varible())
    '''
    varible: (VAL | VAR ) (vardecl | term COLON typ);
    vardecl: (ID | Dollar_ID) CM vardecl CM  (exp0 | member_access) | 
                (ID | Dollar_ID)  COLON typ ASSIGN (exp0 | member_access);
    term: (ID | Dollar_ID) CM term | (ID | Dollar_ID);
    '''
    #varible: (VAL | VAR ) (vardecl | term COLON typ);
    def visitVarible(self, ctx: D96Parser.VaribleContext):
        if  ctx.vardecl() :
            listvar=self.visit(ctx.vardecl())
            res=[]
            for i in range(0,len(listvar[0])):
                if listvar[0][i].name[0]=='$':
                    if ctx.VAL():
                        res+=[AttributeDecl(Static(),ConstDecl(listvar[0][i],listvar[2],listvar[1][i]))]
                    else:
                        res+=[AttributeDecl(Static(),VarDecl(listvar[0][i],listvar[2],listvar[1][i]))]
                else:
                    if ctx.VAL():
                        res+=[AttributeDecl(Instance(),ConstDecl(listvar[0][i],listvar[2],listvar[1][i]))]
                    else:
                        res+=[AttributeDecl(Instance(),VarDecl(listvar[0][i],listvar[2],listvar[1][i]))]
            return res
        ids=self.visit(ctx.term())
        typ=self.visit(ctx.typ())
        if isinstance(typ, ClassType):
            return [AttributeDecl(Static() if i.name[0]=='$' else Instance(),ConstDecl(i,typ,NullLiteral()) if ctx.VAL() else VarDecl(i,typ,NullLiteral())) for i in ids]
        return  [AttributeDecl(Static() if i.name[0]=='$' else Instance(),ConstDecl(i,typ) if ctx.VAL() else VarDecl(i,typ)) for i in ids]
    
    '''
    vardecl: (ID | Dollar_ID) CM vardecl CM  exp0 | 
                (ID | Dollar_ID)  COLON typ ASSIGN exp0 ;
    '''
    def visitVardecl(self, ctx: D96Parser.VardeclContext):
        if ctx.COLON():
            typ=self.visit(ctx.typ())
            id=[Id(ctx.ID().getText())] if ctx.ID() else [Id(ctx.Dollar_ID().getText())]
            value=self.visit(ctx.exp0()) 
            return [id,[value],typ]
        else:
            var=self.visit(ctx.vardecl())
            id=[Id(ctx.ID().getText())] if ctx.ID() else [Id(ctx.Dollar_ID().getText())]
            value=self.visit(ctx.exp0()) 
            return [id+var[0],var[1]+[value],var[2]]
    #term: (ID | Dollar_ID) CM term | (ID | Dollar_ID);
    def visitTerm(self, ctx: D96Parser.TermContext):
        if ctx.CM():
            return [Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.Dollar_ID().getText())] + self.visit(ctx.term())
        else:
            return [Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.Dollar_ID().getText())]
    #method :method_declare|destructor_declare|constructor_declare;
    def visitMethod(self, ctx: D96Parser.MethodContext):
        if ctx.method_declare():
            return self.visit(ctx.method_declare())
        elif ctx.destructor_declare():
            return self.visit(ctx.destructor_declare())
        elif ctx.constructor_declare():
            return self.visit(ctx.constructor_declare())

    #method_declare : (ID|Dollar_ID) LB list_IDs? RB block_stmt ;
    def visitMethod_declare(self, ctx: D96Parser.Method_declareContext):
        name=Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.Dollar_ID().getText())
        kind=Instance() if ctx.ID() else Static()
        param=[item for sublist in self.visit(ctx.list_IDs()) for item in sublist] if ctx.list_IDs() else []
        return [MethodDecl(kind,name,param,self.visit(ctx.block_stmt()))]
    
    #destructor_declare : DESTRUC LB RB block_stmt ;
    def visitDestructor_declare(self, ctx: D96Parser.Destructor_declareContext):
        name=Id(ctx.DESTRUC().getText())
        return [MethodDecl(Instance(),name,[],self.visit(ctx.block_stmt()))]
    #constructor_declare : CONSTRUC LB list_IDs? RB block_stmt ;
    def visitConstructor_declare(self, ctx: D96Parser.Constructor_declareContext):
        name=Id(ctx.CONSTRUC().getText())
        pram= [item for sublist in self.visit(ctx.list_IDs()) for item in sublist] if ctx.list_IDs() else []
        return [MethodDecl(Instance(),name,pram,self.visit(ctx.block_stmt()))]
    
    '''
   stmt: varconst_declare
	| stmt_if 
	| stmt_assign 
	| stmt_while
	| stmt_break
	| stmt_continue
	| stmt_callMethod
	| stmt_return
	| stmt_foreach
    | block_stmt 
    ''' 
    def visitStmt(self, ctx: D96Parser.StmtContext):
        if ctx.stmt_if():
            return self.visit(ctx.stmt_if())
        if ctx.varconst_declare():
            return self.visit(ctx.varconst_declare())
        elif ctx.stmt_assign():
            return self.visit(ctx.stmt_assign())
        elif ctx.stmt_foreach():
            return self.visit(ctx.stmt_foreach())
        elif ctx.stmt_while():
            return self.visit(ctx.stmt_while())
        elif ctx.stmt_break():
            return self.visit(ctx.stmt_break())
        elif ctx.stmt_continue():
            return self.visit(ctx.stmt_continue())
        elif ctx.stmt_callMethod():
            return self.visit(ctx.stmt_callMethod())
        elif ctx.stmt_return(): return self.visit(ctx.stmt_return())
        else: return [self.visit(ctx.block_stmt())]



    #varconst_declare: varible1 SEMI;
    def visitVarconst_declare(self, ctx:D96Parser.Varconst_declareContext):     
        return self.visit(ctx.varible1())
    #varible1: (VAL | VAR ) (vardecl1 | term1 COLON typ);
    def visitVarible1(self, ctx: D96Parser.Varible1Context):
        if ctx.vardecl1():
            listvar=self.visit(ctx.vardecl1())
            res=[]
            for i in range(0,len(listvar[0])):
                if ctx.VAL():
                    res+=[ConstDecl(listvar[0][i],listvar[2],listvar[1][i])]
                else:
                    res+=[VarDecl(listvar[0][i],listvar[2],listvar[1][i])]
            return res
        ids=self.visit(ctx.term1())
        typ=self.visit(ctx.typ())
        if isinstance(typ, ClassType):
            return [ConstDecl(i,typ,NullLiteral()) if ctx.VAL() else VarDecl(i,typ,NullLiteral()) for i in ids]
        return [ConstDecl(i,typ) if ctx.VAL() else VarDecl(i,typ) for i in ids]
         
    '''
    vardecl1: ID CM vardecl1 CM  exp0| 
                ID COLON typ ASSIGN exp0 ;
    '''
    def visitVardecl1(self, ctx: D96Parser.Vardecl1Context):
        if ctx.COLON():
            typ=self.visit(ctx.typ())
            id=[Id(ctx.ID().getText())] 
            value=self.visit(ctx.exp0()) 
            return [id,[value],typ]
        else:
            var=self.visit(ctx.vardecl1())
            id=[Id(ctx.ID().getText())] 
            value=self.visit(ctx.exp0()) 
            return [id+var[0],var[1]+[value],var[2]]
    #term1: ID CM term1 | ID;
    def visitTerm1(self, ctx: D96Parser.Term1Context):
        name=Id(ctx.ID().getText())
        if  ctx.CM():
            return [name] + self.visit(ctx.term1())
        else:
            return [name]
        
    '''
    stmt_assign: exp0 ASSIGN exp0 SEMI;
    '''
    def visitStmt_assign(self, ctx:D96Parser.Stmt_assignContext):
        lhs = self.visit(ctx.exp0(0))
        rhs = self.visit(ctx.exp0(1))
        return [Assign(lhs, rhs)]

        
    #stmt_if: IF LB exp0 RB block_stmt stmt_elif;
    def visitStmt_if(self, ctx:D96Parser.Stmt_ifContext):
        if_expr = self.visit(ctx.exp0())
        if_listStmt = self.visit(ctx.block_stmt())
        ifthenStmt = self.visit(ctx.stmt_elif())
        return [If(if_expr,if_listStmt,ifthenStmt)]


    # stmt_elif: ELSEIF LB exp0 RB block_stmt stmt_elif| stmt_else|; ;
    def visitStmt_elif(self, ctx:D96Parser.Stmt_elifContext):
        if ctx.stmt_elif():
            expr = self.visit(ctx.exp0())
            thenstmt=self.visit(ctx.block_stmt())
            elsestmt=self.visit(ctx.stmt_elif())
            return If(expr,thenstmt,elsestmt)
        elif ctx.stmt_else():
            return self.visit(ctx.stmt_else())
        else: return None


    # stmt_else: ELSE block_stmt|;
    def visitStmt_else(self, ctx:D96Parser.Stmt_elseContext):
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        else: return None
        
    #stmt_while: WHILE LB exp0 RB block_stmt;
    def visitStmt_while(self, ctx: D96Parser.Stmt_whileContext):
        cond = self.visit(ctx.exp0())
        body = self.visit(ctx.block_stmt())
        return [While(cond, body)]


    # stmt_break: BREAK SEMI;
    def visitStmt_break(self, ctx:D96Parser.Stmt_breakContext):
        return [Break()]


    # stmt_continue: CONTINUE SEMI;
    def visitStmt_continue(self, ctx:D96Parser.Stmt_continueContext):
        return [Continue()]


    #stmt_foreach : FOREACH LB ID IN exp0 '..' exp0 (BY exp0)? RB block_stmt;
    def visitStmt_foreach(self, ctx:D96Parser.Stmt_foreachContext):
        name=Id(ctx.ID().getText())
        if ctx.BY():
            return [For(name,self.visit(ctx.exp0(0)),self.visit(ctx.exp0(1)),self.visit(ctx.block_stmt()),self.visit(ctx.exp0(2)))]
        return [For(name,self.visit(ctx.exp0(0)),self.visit(ctx.exp0(1)),self.visit(ctx.block_stmt()),IntLiteral(1))]
    # stmt_return: RETURN exp1? SEMI;
    def visitStmt_return(self, ctx:D96Parser.Stmt_returnContext):
        if ctx.exp1():
            return [Return(self.visit(ctx.exp1()))]
        elif ctx.NULL():
            return [Return(NullLiteral())]
        else: return [Return(None)]
    
    #stmt_callMethod: member_access SEMI;
    def visitStmt_callMethod(self, ctx:D96Parser.Stmt_callMethodContext):
        return [self.visit(ctx.member_access())]
    
    #block_stmt: LP list_stmt  RP ;
    #list_stmt : stmt stmts| ;
    #stmts : stmt stmts|
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        res=self.visit(ctx.list_stmt())
        return Block(res)
    def visitList_stmt(self, ctx:D96Parser.List_stmtContext):
        if ctx.getChildCount()==0:
            return []
        return self.visit(ctx.stmt())+ self.visit(ctx.stmts())
    def visitStmts(self, ctx:D96Parser.StmtsContext):
        if ctx.getChildCount()==0:
            return []
        return self.visit(ctx.stmt())+ self.visit(ctx.stmts())
        
    '''
    member_access : in_method | stt_method;
    in_method : exp0 DOT ID LB list_param RB ;
    stt_method: ID ACCESS Dollar_ID LB list_param RB ;
    '''
    def visitMember_access(self, ctx:D96Parser.Member_accessContext):
        if ctx.in_method():
            return self.visit(ctx.in_method())
        elif ctx.stt_method():
            return self.visit(ctx.stt_method())
    def visitIn_method(self, ctx:D96Parser.In_methodContext):
        return CallStmt(self.visit(ctx.exp0()),Id(ctx.ID().getText()),self.visit(ctx.list_param()))
    def visitStt_method(self, ctx:D96Parser.Stt_methodContext):
        return CallStmt(Id(ctx.ID().getText()),Id(ctx.Dollar_ID().getText()),self.visit(ctx.list_param()))
    
    #array: i_array | m_array;
    def visitArray(self, ctx:D96Parser.ArrayContext):
        if ctx.i_array():
            return self.visit(ctx.i_array())
        else:
            return self.visit(ctx.m_array())
        
    '''
    listARRAY:array CM listARRAY
            | array;
    '''
    def visitListARRAY(self, ctx:D96Parser.ListARRAYContext):
        if ctx.listARRAY():
            return [self.visit(ctx.array())] + self.visit(ctx.listARRAY())
        else: return [self.visit(ctx.array())]
        
    #i_array: ARRAY LB listLIT RB;
    def visitI_array(self, ctx:D96Parser.I_arrayContext):
        return ArrayLiteral(self.visit(ctx.listLIT()))

    # m_array: ARRAY LB listARRAY RB;
    def visitM_array(self, ctx:D96Parser.M_arrayContext):
        return ArrayLiteral(self.visit(ctx.listARRAY()))
    

    #listLIT: list_mem |;  
    def visitListLIT(self, ctx:D96Parser.ListLITContext):
        if ctx.getChildCount()==0:
            return []
        return self.visit(ctx.list_mem())
    #list_mem : exp0 listval;
    def visitList_mem(self, ctx:D96Parser.List_memContext):
        return [self.visit(ctx.exp0())] + self.visit(ctx.listval())
    #listval : CM exp0 listval|;
    def visitListval(self, ctx:D96Parser.ListvalContext):
        if ctx.getChildCount()==0:
            return []
        return [self.visit(ctx.exp0())] + self.visit(ctx.listval())

    #exp0 : exp1 | array ;
    def visitExp0(self, ctx:D96Parser.Exp0Context):
        return self.visit(ctx.exp1())

    #exp1: exp2 (STR_CAT | STR_CMP ) exp2 | exp2 ;
    def visitExp1(self, ctx: D96Parser.Exp1Context):
        operand = ctx.exp2()
        if ctx.STR_CAT() or ctx.STR_CMP():
            left = self.visit(operand[0])
            right = self.visit(operand[1])
            op = ctx.STR_CAT().getText() if ctx.STR_CAT() else ctx.STR_CMP().getText()
            return BinaryOp(op, left, right)
        else:
            return self.visit(operand[0])
    #exp2: exp3 ( EQ | NEQ | GT | LT | GE | LE ) exp3 | exp3;
    def visitExp2(self, ctx: D96Parser.Exp2Context):
        operand = ctx.exp3()
        if ctx.EQ() or ctx.NEQ() or ctx.GT() or ctx.LT() or ctx.GE() or ctx.LE() :
            left = self.visit(operand[0])
            right = self.visit(operand[1])
            if ctx.EQ():
                op=ctx.EQ().getText()
            elif ctx.NEQ():
                op=ctx.NEQ().getText()
            elif ctx.GT():
                op=ctx.GT().getText()
            elif ctx.LT():
                op=ctx.LT().getText()
            elif ctx.GE():
                op=ctx.GE().getText()
            else: op=ctx.LE().getText()
            return BinaryOp(op, left, right)
        else:
            return self.visit(operand[0])
    #exp3: exp3 ( AND | OR ) exp4 | exp4;
    def visitExp3(self, ctx: D96Parser.Exp3Context):
        if ctx.AND() or ctx.OR():
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            op = ctx.AND().getText() if ctx.AND() else ctx.OR().getText()
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.exp4())
    #exp4: exp4 (ADD | SUB ) exp5 | exp5;
    def visitExp4(self, ctx: D96Parser.Exp4Context):
        if ctx.ADD() or ctx.SUB():
            left = self.visit(ctx.exp4())
            right = self.visit(ctx.exp5())
            op = ctx.ADD().getText() if ctx.ADD() else ctx.SUB().getText()
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.exp5())
    #exp5: exp5 ( MUL | DIV | MOD) exp6 | exp6;
    def visitExp5(self, ctx: D96Parser.Exp5Context):
        if ctx.MUL() or ctx.DIV() or ctx.MOD():
            left = self.visit(ctx.exp5())
            right = self.visit(ctx.exp6())
            if ctx.MUL():
                op=ctx.MUL().getText()
            elif ctx.DIV():
                op=ctx.DIV().getText()
            else:
                op=ctx.MOD().getText()
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.exp6())
    #exp6:  NOT  exp6 | exp7;
    def visitExp6(self, ctx: D96Parser.Exp6Context):
        if ctx.NOT():
            exp = self.visit(ctx.exp6())
            op = ctx.NOT().getText()
            return UnaryOp(op, exp)
        else:
            return self.visit(ctx.exp7())
    #exp7: SUB exp7 | exp8;
    def visitExp7(self, ctx: D96Parser.Exp7Context):
        if ctx.SUB():
            exp = self.visit(ctx.exp7())
            op = ctx.SUB().getText()
            return UnaryOp(op, exp)
        else:
            return self.visit(ctx.exp8())
    #exp8: exp9 index_operator | exp9;
    def visitExp8(self, ctx: D96Parser.Exp8Context):
        if ctx.index_operator():
            idx = self.visit(ctx.index_operator())
            exp=self.visit(ctx.exp8())
            return ArrayCell(exp,idx)
        else:
            return self.visit(ctx.exp9())
    #exp9: exp9 DOT ID (LB list_param RB)? | exp10 ;
    def visitExp9(self, ctx: D96Parser.Exp9Context):
        if ctx.DOT():
            name = self.visit(ctx.exp9())
            id= Id(ctx.ID().getText())
            if ctx.LB():
                return CallExpr(name,id,self.visit(ctx.list_param()))
            return FieldAccess(name,Id(ctx.ID().getText()))
        else:
            return self.visit(ctx.exp10())
    #exp10 : ID ACCESS Dollar_ID (LB list_param RB)? | exp11;
    def visitExp10(self, ctx: D96Parser.Exp10Context):
        if ctx.ACCESS():
            if ctx.LB():
                return CallExpr(Id(ctx.ID().getText()),Id(ctx.Dollar_ID().getText()),self.visit(ctx.list_param()))
            return FieldAccess(Id(ctx.ID().getText()),Id(ctx.Dollar_ID().getText()))
        return self.visit(ctx.exp11())
    #exp11 : NEW ID LB list_param RB | operands ;
    def visitExp11(self, ctx: D96Parser.Exp11Context):
        if ctx.NEW():
            exp = self.visit(ctx.list_param())
            name = Id(ctx.ID().getText())
            return NewExpr(name, exp)
        else:
            return self.visit(ctx.operands())
    
    #index_operator: LSB exp0 RSB | LSB exp0 RSB index_operator;
    def visitIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        if ctx.getChildCount()==3:
            return [self.visit(ctx.exp0())]
        return [self.visit(ctx.exp0())] + self.visit(ctx.index_operator())

    
    '''
    operands
	: literal
	| ID
	//| call_func
	| LB exp0 RB
	| SELF
	;
    '''
    def visitOperands(self, ctx: D96Parser.OperandsContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.exp0(): 
            return self.visit(ctx.exp0())
        else:
            return SelfLiteral()
    
    '''
    literal
	: INT_LITERAL
	| FL_LITERAL
	| STRING_LITERAL
	| BOOL_LITERAL
	| array
	;
    '''
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        if ctx.FL_LITERAL():
            flcase = ctx.FL_LITERAL().getText()
            if flcase[0] == '.':
                return FloatLiteral(float('0'+ctx.FL_LITERAL().getText()))
            return  FloatLiteral(float(ctx.FL_LITERAL().getText()))
        elif ctx.BOOL_LITERAL():
            return BooleanLiteral(True if ctx.BOOL_LITERAL().getText()=='True' else False)
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.INT_LITERAL(): 
            intcase = ctx.INT_LITERAL().getText()
            if len(intcase) > 1 and intcase[0] == '0':
                if intcase[1] in ('x', 'X'):
                    return IntLiteral(int(intcase, 16))
                elif intcase[1] in ('b', 'B'):
                    return IntLiteral(int(intcase, 2))
                else:
                    return IntLiteral(int(intcase, 8))
            else:
                return IntLiteral(int(intcase, 10))
        else:
            return self.visit(ctx.array())
    

    #call_func: ID LB list_param RB;
    '''def visitCall_func(self, ctx:D96Parser.Call_funcContext):
        id = Id(ctx.ID().getText())
        param = self.visit(ctx.list_param())
        return [id] + param'''
    
    '''
    list_param: param CM list_param
          | param
          | ;
    '''
    def visitList_param(self, ctx:D96Parser.List_paramContext):
        if ctx.list_param():
            return [self.visit(ctx.param())] + self.visit(ctx.list_param())
        elif ctx.param():
            return [self.visit(ctx.param())]
        else: return []


    # param: literal | ID | exp0;
    def visitParam(self, ctx:D96Parser.ParamContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else: return self.visit(ctx.exp0())
    '''
    list_IDs:list_ID SEMI list_IDs|list_ID;
    ids : ID CM ids |ID;
    list_ID :ids COLON typ ;
    '''
    #list_IDs:list_ID SEMI list_IDs|list_ID;
    def visitList_IDs(self, ctx:D96Parser.List_IDsContext):
        if  ctx.SEMI():
            return [self.visit(ctx.list_ID())]+ self.visit(ctx.list_IDs())
        return [self.visit(ctx.list_ID())]
    #list_ID :ids COLON typ;
    def visitList_ID(self, ctx:D96Parser.List_IDContext):   
        return [VarDecl(x,self.visit(ctx.typ())) for x in  self.visit(ctx.ids())]
    #ids : ID CM ids |ID;
    def visitIds(self, ctx:D96Parser.IdsContext):
        if  ctx.CM():
            return [Id(ctx.ID().getText())]+ self.visit(ctx.ids())
        return [Id(ctx.ID().getText())]
    
    #typ :INTTYPE|FLOATTYPE|STRTYPE|BOOLTYPE|arraytype|ID;
    def visitTyp(self, ctx:D96Parser.TypContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.STRTYPE():
            return StringType()
        elif ctx.BOOLTYPE():
            return BoolType()
        elif ctx.arraytype():
            return self.visit(ctx.arraytype())
        else:
            return ClassType(Id(ctx.ID().getText()))
            
            
    #arraytype: ARRAY LSB typ CM INT_LITERAL RSB ;
    def visitArraytype(self, ctx:D96Parser.ArraytypeContext):
        intcase = ctx.INT_LITERAL().getText()
        if len(intcase) > 1 and intcase[0] == '0':
            if intcase[1] in ('x', 'X'):
                size =int(intcase, 16)
            elif intcase[1] in ('b', 'B'):
                size =int(intcase, 2)
            else:
                size =int(intcase, 8)
        else:
            size =int(intcase, 10)
        return ArrayType(size,self.visit(ctx.typ()))