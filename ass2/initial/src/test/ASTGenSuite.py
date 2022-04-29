import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """
            Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val numOfShape,y: Int = 0,3+2;
                        If(y <4){
                            Return 0;
                        }
                        Elseif(y==2){
                            Return 1;
                        }

                        
                    }
    
                }
            """
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(y),IntType,IntLit(3))),MethodDecl(Id(get),Instance,[],Block([ConstDecl(Id(numOfShape),IntType,IntLit(0)),ConstDecl(Id(y),IntType,BinaryOp(+,IntLit(3),IntLit(2))),If(BinaryOp(<,Id(y),IntLit(4)),Block([Return(IntLit(0))]),If(BinaryOp(==,Id(y),IntLit(2)),Block([Return(IntLit(1))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test2(self):
        input = """
            Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val numOfShape,y: Int = 0,3+2;
                        If(y <4){
                            Return 0;
                        }
                        Elseif(y==2){
                            Return 1+2;
                        }

                        
                    }
    
                }
            """
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(y),IntType,IntLit(3))),MethodDecl(Id(get),Instance,[],Block([ConstDecl(Id(numOfShape),IntType,IntLit(0)),ConstDecl(Id(y),IntType,BinaryOp(+,IntLit(3),IntLit(2))),If(BinaryOp(<,Id(y),IntLit(4)),Block([Return(IntLit(0))]),If(BinaryOp(==,Id(y),IntLit(2)),Block([Return(BinaryOp(+,IntLit(1),IntLit(2)))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,302))
    
    def test3(self):
        input = """
            Class Shape {
                    Val $numOfShape,y,x: Int = 0,3,3+2;
                    get(){
                        Val numOfShape,y: Int = 0,3+2;
                        If(y <4){
                            Return 0;
                        }
                        Elseif(y==2){
                            Return 1+a;
                        }

                        
                    }
    
                }
            """
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(y),IntType,IntLit(3))),AttributeDecl(Instance,ConstDecl(Id(x),IntType,BinaryOp(+,IntLit(3),IntLit(2)))),MethodDecl(Id(get),Instance,[],Block([ConstDecl(Id(numOfShape),IntType,IntLit(0)),ConstDecl(Id(y),IntType,BinaryOp(+,IntLit(3),IntLit(2))),If(BinaryOp(<,Id(y),IntLit(4)),Block([Return(IntLit(0))]),If(BinaryOp(==,Id(y),IntLit(2)),Block([Return(BinaryOp(+,IntLit(1),Id(a)))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,303))
    def test4(self):
        input = """
            Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val numOfShape,y: Int = 0,3+2;
                        If(y <4){
                            Return 0;
                        }
                        Elseif(y==2){
                            Return 1+a.id;
                        }
                    
                    }
    
                }
            """
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(y),IntType,IntLit(3))),MethodDecl(Id(get),Instance,[],Block([ConstDecl(Id(numOfShape),IntType,IntLit(0)),ConstDecl(Id(y),IntType,BinaryOp(+,IntLit(3),IntLit(2))),If(BinaryOp(<,Id(y),IntLit(4)),Block([Return(IntLit(0))]),If(BinaryOp(==,Id(y),IntLit(2)),Block([Return(BinaryOp(+,IntLit(1),FieldAccess(Id(a),Id(id))))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,304))
    
    def test5(self):
        input = """
            Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val numOfShape,y: Int = 0,3+2;
                        If(y <4){
                            Return 0+af::$a;
                        }
                        Elseif(y==2){
                            Return 1;
                        }

                        
                    }
    
                }
            """
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(y),IntType,IntLit(3))),MethodDecl(Id(get),Instance,[],Block([ConstDecl(Id(numOfShape),IntType,IntLit(0)),ConstDecl(Id(y),IntType,BinaryOp(+,IntLit(3),IntLit(2))),If(BinaryOp(<,Id(y),IntLit(4)),Block([Return(BinaryOp(+,IntLit(0),FieldAccess(Id(af),Id($a))))]),If(BinaryOp(==,Id(y),IntLit(2)),Block([Return(IntLit(1))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,305))
        
    def test6(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a: Int; 
                Break; 
                Continue; 
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Break,Continue]))])])"""
        self.assertTrue(TestAST.test(input,expect,306))
    
    def test7(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a: Int; 
                Return 1+2 ;
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,IntLit(1),IntLit(2)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,307))
    
    def test8(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a: Int; 
                Break; 
                Continue; 
            }
            $test(b, c:Int)
            { 
                Var a: Int; 

            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Break,Continue])),MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType)]))])])"""
        self.assertTrue(TestAST.test(input,expect,308))
    
    def test9(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a: Int; 
                Break; 
                Continue; 
            }
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a;
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Break,Continue])),MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(Id(a))]))])])"""
        self.assertTrue(TestAST.test(input,expect,309))
        
    def test10(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a: Int; 
                Break; 
                Continue; 
            }
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5];
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Break,Continue])),MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5)])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,310))
    def test11(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a: Int; 
                Break; 
                Continue; 
            }
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6];
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Break,Continue])),MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),IntLit(6)])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,311))
    
    def test12(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a: Int; 
                Break; 
                Continue; 
            }
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6+2];
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Break,Continue])),MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),BinaryOp(+,IntLit(6),IntLit(2))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,312))
    def test13(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a: Int; 
                Break; 
                Continue; 
            }
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6+2+v];
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Break,Continue])),MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),BinaryOp(+,BinaryOp(+,IntLit(6),IntLit(2)),Id(v))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,313))
    def test14(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a: Int; 
                Break; 
                Continue; 
            }
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6+2+v[2]];
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Break,Continue])),MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),BinaryOp(+,BinaryOp(+,IntLit(6),IntLit(2)),ArrayCell(Id(v),[IntLit(2)]))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,314))
    def test15(self):
        input = """
        Class Dog : Animal 
        { 
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6+2+v[2]]+ad.id;
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),BinaryOp(+,BinaryOp(+,IntLit(6),IntLit(2)),ArrayCell(Id(v),[IntLit(2)]))])),FieldAccess(Id(ad),Id(id))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,315))
    def test16(self):
        input = """
        Class Dog : Animal 
        { 
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6+2+v[2][2]]+ad.id;
            }  
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),BinaryOp(+,BinaryOp(+,IntLit(6),IntLit(2)),ArrayCell(Id(v),[IntLit(2),IntLit(2)]))])),FieldAccess(Id(ad),Id(id))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,316))
    def test17(self):
        input = """
        Class Dog : Animal 
        { 
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6+2+v[2]]+ad.id(a);
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),BinaryOp(+,BinaryOp(+,IntLit(6),IntLit(2)),ArrayCell(Id(v),[IntLit(2)]))])),CallExpr(Id(ad),Id(id),[Id(a)])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,317))
    def test18(self):
        input = """
        Class Dog : Animal 
        { 
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6+2+v[2]]+ad.id+2+4;
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),BinaryOp(+,BinaryOp(+,IntLit(6),IntLit(2)),ArrayCell(Id(v),[IntLit(2)]))])),FieldAccess(Id(ad),Id(id))),IntLit(2)),IntLit(4)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,318))
    def test19(self):
        input = """
        Class Dog : Animal 
        { 
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6+2+v[2]]+ad.id+2+4*a[6];
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),BinaryOp(+,BinaryOp(+,IntLit(6),IntLit(2)),ArrayCell(Id(v),[IntLit(2)]))])),FieldAccess(Id(ad),Id(id))),IntLit(2)),BinaryOp(*,IntLit(4),ArrayCell(Id(a),[IntLit(6)]))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,319))
    def test20(self):
        input = """
        Class Dog : Animal 
        { 
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6*a[2]+2+v[2]]+ad.id+2+4;
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),BinaryOp(+,BinaryOp(+,BinaryOp(*,IntLit(6),ArrayCell(Id(a),[IntLit(2)])),IntLit(2)),ArrayCell(Id(v),[IntLit(2)]))])),FieldAccess(Id(ad),Id(id))),IntLit(2)),IntLit(4)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,320))
    def test21(self):
        input = """
        Class Dog : Animal 
        { 
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6*a[2+2]+2+v[2]]+ad.id+2+4;
            }
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),BinaryOp(+,BinaryOp(+,BinaryOp(*,IntLit(6),ArrayCell(Id(a),[BinaryOp(+,IntLit(2),IntLit(2))])),IntLit(2)),ArrayCell(Id(v),[IntLit(2)]))])),FieldAccess(Id(ad),Id(id))),IntLit(2)),IntLit(4)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,321))
    def test22(self):
        input = """
        Class Dog : Animal 
        { 
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6*a[2+2+ab]+2+v[2]]+ad.id+2+4;
            }
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),BinaryOp(+,BinaryOp(+,BinaryOp(*,IntLit(6),ArrayCell(Id(a),[BinaryOp(+,BinaryOp(+,IntLit(2),IntLit(2)),Id(ab))])),IntLit(2)),ArrayCell(Id(v),[IntLit(2)]))])),FieldAccess(Id(ad),Id(id))),IntLit(2)),IntLit(4)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,322))
    def test23(self):
        input = """
        Class Dog : Animal 
        { 
            $test(b, c:Int)
            { 
                Var a: Int; 
                Return  a+b[5][6*a[2+2+ab][a]+2+v[2]]+ad.id+2+4;
            }
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),ArrayCell(Id(b),[IntLit(5),BinaryOp(+,BinaryOp(+,BinaryOp(*,IntLit(6),ArrayCell(Id(a),[BinaryOp(+,BinaryOp(+,IntLit(2),IntLit(2)),Id(ab)),Id(a)])),IntLit(2)),ArrayCell(Id(v),[IntLit(2)]))])),FieldAccess(Id(ad),Id(id))),IntLit(2)),IntLit(4)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,323))
    def test24(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a: Int; 
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType)]))])])"""
        self.assertTrue(TestAST.test(input,expect,324))
    def test25(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a,b,c: Int; 
            }
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType)]))])])"""
        self.assertTrue(TestAST.test(input,expect,325))
    def test26(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Var a,b,c: Int;Val ab,ac : Int; 
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),ConstDecl(Id(ab),IntType,None),ConstDecl(Id(ac),IntType,None)]))])])"""
        self.assertTrue(TestAST.test(input,expect,326))
    def test27(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Continue; 
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([Continue]))])])"""
        self.assertTrue(TestAST.test(input,expect,327))
    def test28(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Break; 
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([Break]))])])"""
        self.assertTrue(TestAST.test(input,expect,328))
    
    def test29(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                Break; 
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([Break]))])])"""
        self.assertTrue(TestAST.test(input,expect,329))
    def test30(self):
        input = """
        Class Dog : Animal 
        { 
            $test(a, b, c:Int)
            { 
                If (a==2){
                    Return a;
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($test),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([If(BinaryOp(==,Id(a),IntLit(2)),Block([Return(Id(a))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,330))
    
    def test31(self):
        input = """
            Class Program {
                main() {
                    b = name::$test();
                }
            }
            Class Truuu: Paper {
                Love(){
                    Truu.nameMethod();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(b),CallExpr(Id(name),Id($test),[]))]))]),ClassDecl(Id(Truuu),Id(Paper),[MethodDecl(Id(Love),Instance,[],Block([Call(Id(Truu),Id(nameMethod),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 331))

    def test32(self):
        input = """
            Class Program {
                main() {
                    Foreach (index In 0 .. 100 By 1 * 2 / 3 + a - b.name()) {
                        Continue;
                    }
                    Return New B(A);
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(index),IntLit(0),IntLit(100),BinaryOp(-,BinaryOp(+,BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),Id(a)),CallExpr(Id(b),Id(name),[])),Block([Continue])]),Return(NewExpr(Id(B),[Id(A)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 332))

    def test33(self):
        input = """
            Class myVarName {
                Constructor(arr: Array[String, 20]) {
                    Self.atest = q.arr[7];
                    Self.btest = q.arr[9];
                    Self.ctest = q.arr[3][4];
                }
            }
        """
        expect = "Program([ClassDecl(Id(myVarName),[MethodDecl(Id(Constructor),Instance,[param(Id(arr),ArrayType(20,StringType))],Block([AssignStmt(FieldAccess(Self(),Id(atest)),ArrayCell(FieldAccess(Id(q),Id(arr)),[IntLit(7)])),AssignStmt(FieldAccess(Self(),Id(btest)),ArrayCell(FieldAccess(Id(q),Id(arr)),[IntLit(9)])),AssignStmt(FieldAccess(Self(),Id(ctest)),ArrayCell(FieldAccess(Id(q),Id(arr)),[IntLit(3),IntLit(4)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 333))

    def test34(self):
        input = """
            Class Program {
                main(){
                    test = ABC::$testtest()[7] <= 9;
                }
            }
            Class Design {
                Destructor() {
                    Standar.Del().All(1);
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(test),BinaryOp(<=,ArrayCell(CallExpr(Id(ABC),Id($testtest),[]),[IntLit(7)]),IntLit(9)))]))]),ClassDecl(Id(Design),[MethodDecl(Id(Destructor),Instance,[],Block([Call(CallExpr(Id(Standar),Id(Del),[]),Id(All),[IntLit(1)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 334))

    def test35(self):
        input = """
            Class Main {
                dethodlove() {
                    Return Self.namemethod();
                }
                menuNew() {
                    test = ABC::$testtest()[7] <= 9;
                    Return Self.hehe;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Main),[MethodDecl(Id(dethodlove),Instance,[],Block([Return(CallExpr(Self(),Id(namemethod),[]))])),MethodDecl(Id(menuNew),Instance,[],Block([AssignStmt(Id(test),BinaryOp(<=,ArrayCell(CallExpr(Id(ABC),Id($testtest),[]),[IntLit(7)]),IntLit(9))),Return(FieldAccess(Self(),Id(hehe)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 335))

    def test36(self):
        input = """
            Class BUF {
                Val xyz: Float;
                Var gui, abc, def: Array[Int, 5] = 0xFF, 1, 2;
            }
            Class Program {
                dethodlove() {
                    {}
                    Return Self.namemethod();
                }
            }
        """
        expect = "Program([ClassDecl(Id(BUF),[AttributeDecl(Instance,ConstDecl(Id(xyz),FloatType,None)),AttributeDecl(Instance,VarDecl(Id(gui),ArrayType(5,IntType),IntLit(255))),AttributeDecl(Instance,VarDecl(Id(abc),ArrayType(5,IntType),IntLit(1))),AttributeDecl(Instance,VarDecl(Id(def),ArrayType(5,IntType),IntLit(2)))]),ClassDecl(Id(Program),[MethodDecl(Id(dethodlove),Instance,[],Block([Block([]),Return(CallExpr(Self(),Id(namemethod),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 336))

    def test37(self):
        input = """
            Class Cat {
                returnMethod() {
                    Val xyz: Float;
                    Var gui, abc, def: Array[Int, 5] = 0xFFF, 123, "huuloi";
                }
                Constructor() {
                    Self.initial = valuenew.test;
                }
                Destructor() {
                    Cat.remove();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Cat),[MethodDecl(Id(returnMethod),Instance,[],Block([ConstDecl(Id(xyz),FloatType,None),VarDecl(Id(gui),ArrayType(5,IntType),IntLit(4095)),VarDecl(Id(abc),ArrayType(5,IntType),IntLit(123)),VarDecl(Id(def),ArrayType(5,IntType),StringLit(huuloi))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(initial)),FieldAccess(Id(valuenew),Id(test)))])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(Cat),Id(remove),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 337))

    def test38(self):
        input = """
            Class BUF {
                Val xyz: Float;
                Var gui: Array[Int, 5] = 0xFF;
            }
        """
        expect = "Program([ClassDecl(Id(BUF),[AttributeDecl(Instance,ConstDecl(Id(xyz),FloatType,None)),AttributeDecl(Instance,VarDecl(Id(gui),ArrayType(5,IntType),IntLit(255)))])])"
        self.assertTrue(TestAST.test(input, expect, 338))

    def test39(self):
        input = """
            Class Airi: Name {
                Constructor(airi, batman : Int)
                {
                    result.print("Cons");
                }
                Destructor()
                {
                    result.print("Dest");
                }
                $_getMethodTest() {
                    Return 22 + 8.8 - rt + !gh >= 8 || 9 || (2 + 3);
                }
            }
            Class Program {
                main() {
                    a = (Lubo + DieuThuyen) && Nakroth + Laviel + Veres;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Airi),Id(Name),[MethodDecl(Id(Constructor),Instance,[param(Id(airi),IntType),param(Id(batman),IntType)],Block([Call(Id(result),Id(print),[StringLit(Cons)])])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(result),Id(print),[StringLit(Dest)])])),MethodDecl(Id($_getMethodTest),Static,[],Block([Return(BinaryOp(>=,BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(22),FloatLit(8.8)),Id(rt)),UnaryOp(!,Id(gh))),BinaryOp(||,BinaryOp(||,IntLit(8),IntLit(9)),BinaryOp(+,IntLit(2),IntLit(3)))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(&&,BinaryOp(+,Id(Lubo),Id(DieuThuyen)),BinaryOp(+,BinaryOp(+,Id(Nakroth),Id(Laviel)),Id(Veres))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 339))

    def test40(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5){
                        Return result.print("Aoi");
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Hayate),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(>,Id(k),IntLit(5)),Block([Return(CallExpr(Id(result),Id(print),[StringLit(Aoi)]))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 340))
    

    def test41(self):
        input = """
        Class School
        {
            Val $maxStudent: Int = 500;
            Var student_number: Int = 0;
            add(x: Int)
            {
                Self.student_number = Self.student_number + x;
            }
        }"""
        expect = "Program([ClassDecl(Id(School),[AttributeDecl(Static,ConstDecl(Id($maxStudent),IntType,IntLit(500))),AttributeDecl(Instance,VarDecl(Id(student_number),IntType,IntLit(0))),MethodDecl(Id(add),Instance,[param(Id(x),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(student_number)),BinaryOp(+,FieldAccess(Self(),Id(student_number)),Id(x)))]))])])"
        self.assertTrue(TestAST.test(input,expect,341))
    def test42(self):
        input = """
        Class Test{
            Val $x: Int = -1;
            test(){
                arr[20][10+2] = 2;
                Return Self.x;
            }
        }"""
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Static,ConstDecl(Id($x),IntType,UnaryOp(-,IntLit(1)))),MethodDecl(Id(test),Instance,[],Block([AssignStmt(ArrayCell(Id(arr),[IntLit(20),BinaryOp(+,IntLit(10),IntLit(2))]),IntLit(2)),Return(FieldAccess(Self(),Id(x)))]))])])"
        self.assertTrue(TestAST.test(input,expect,342))
    def test43(self):
        input = """
        Class Student{
            Constructor(name, class: String; age: Int)
            {
                Self.name = name;
                Self.class = class;
                Self.age = age;
            }
        }"""
        expect = "Program([ClassDecl(Id(Student),[MethodDecl(Id(Constructor),Instance,[param(Id(name),StringType),param(Id(class),StringType),param(Id(age),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(class)),Id(class)),AssignStmt(FieldAccess(Self(),Id(age)),Id(age))]))])])"
        self.assertTrue(TestAST.test(input,expect,343))
    def test44(self):
        input = """Class Name{
                Var first_name : String = "Hieu";
                Var middle_name : String = "Minh";
                Var last_name : String = "Loc";

                checkName(string: String)
                {
                    Return (((Self.last_name +. Self.middle_name) +. Self.first_name) ==. string);
                }
        }
        """
        expect = "Program([ClassDecl(Id(Name),[AttributeDecl(Instance,VarDecl(Id(first_name),StringType,StringLit(Hieu))),AttributeDecl(Instance,VarDecl(Id(middle_name),StringType,StringLit(Minh))),AttributeDecl(Instance,VarDecl(Id(last_name),StringType,StringLit(Loc))),MethodDecl(Id(checkName),Instance,[param(Id(string),StringType)],Block([Return(BinaryOp(==.,BinaryOp(+.,BinaryOp(+.,FieldAccess(Self(),Id(last_name)),FieldAccess(Self(),Id(middle_name))),FieldAccess(Self(),Id(first_name))),Id(string)))]))])])"
        self.assertTrue(TestAST.test(input,expect,344))
    def test45(self):
        input = """
        Class Test{
            Test(x, y: Int){
                Var a: Int = x; 
                a = 1 + 2 * A.getMethod(x,y);
            }
        }"""
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Test),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([VarDecl(Id(a),IntType,Id(x)),AssignStmt(Id(a),BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),CallExpr(Id(A),Id(getMethod),[Id(x),Id(y)]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,345))
        
    def test46(self):
        input = """
        Class Test{
            Val a,b: Student;
            test(){
                Foreach(i In 1 .. 10 By 2)
                {
                    If(i == a.ID)
                    {
                        Continue;
                    } 
                    Else
                    {
                        Break;
                    }
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(Student)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(b),ClassType(Id(Student)),NullLiteral())),MethodDecl(Id(test),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),IntLit(2),Block([If(BinaryOp(==,Id(i),FieldAccess(Id(a),Id(ID))),Block([Continue]),Block([Break]))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,346))
        
    def test47(self):
        input = """Class Program{
                main(){ 
                    If(flag == True)
                    {
                        Foreach (i In 2 .. 100 )
                        {
                            Out.printInt(i);
                        }
                    }
                }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,Id(flag),BooleanLit(True)),Block([For(Id(i),IntLit(2),IntLit(100),IntLit(1),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,347))
        
    def test48(self):
        input = """
            Class Pro {
                MainMenu(a: Int; b: Int) {
                    Self.arr[4] = b.getName() + a.exp();
                }
            }
            Class ProMax {
                iPhone13(){
                    Return 40000000;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Pro),[MethodDecl(Id(MainMenu),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(arr)),[IntLit(4)]),BinaryOp(+,CallExpr(Id(b),Id(getName),[]),CallExpr(Id(a),Id(exp),[])))]))]),ClassDecl(Id(ProMax),[MethodDecl(Id(iPhone13),Instance,[],Block([Return(IntLit(40000000))]))])])"""
        self.assertTrue(TestAST.test(input,expect,348))
    def test49(self):
        input = """
            Class Program {
                main() {
                    a[1][2][3+b.g()] = b.c(d[1][2+4][0x5 * 0b1]);
                }
                method () { }
            }
            """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),BinaryOp(+,IntLit(3),CallExpr(Id(b),Id(g),[]))]),CallExpr(Id(b),Id(c),[ArrayCell(Id(d),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(4)),BinaryOp(*,IntLit(5),IntLit(1))])]))])),MethodDecl(Id(method),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,349))
    def test50(self):
        input = """
            Class E {
                method() {
                    Return a[1][2][3] + className.b()[4];
                }
            }
            """
        expect = """Program([ClassDecl(Id(E),[MethodDecl(Id(method),Instance,[],Block([Return(BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(CallExpr(Id(className),Id(b),[]),[IntLit(4)])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,350))
        
    
    def test51(self):
        input = """
            Class Name {
                Constructor(name: String; age: Int) {
                    Self.name = name;
                    Self.age = age;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Name),[MethodDecl(Id(Constructor),Instance,[param(Id(name),StringType),param(Id(age),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(age)),Id(age))]))])])"""
        self.assertTrue(TestAST.test(input,expect,351))
    def test52(self):
        input = """
            Class B: C {
                he() {
                    wall = smoke + he.explore();
                }
            }
            Class Program {
                main(a: Int) {
                    Return a * b;
                }
            }
            """
        expect = """Program([ClassDecl(Id(B),Id(C),[MethodDecl(Id(he),Instance,[],Block([AssignStmt(Id(wall),BinaryOp(+,Id(smoke),CallExpr(Id(he),Id(explore),[])))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([Return(BinaryOp(*,Id(a),Id(b)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,352))
    def test53(self):
        input = """
            Class Func {
                f() {
                    Foreach (a In b - 1 .. c By 2) {
                        Foreach (b In c - 1 .. d) {

                        }
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(Func),[MethodDecl(Id(f),Instance,[],Block([For(Id(a),BinaryOp(-,Id(b),IntLit(1)),Id(c),IntLit(2),Block([For(Id(b),BinaryOp(-,Id(c),IntLit(1)),Id(d),IntLit(1),Block([])])])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,353))

    def test54(self):
        input = """
        Class main{
            Var x: Float = 5.25;
            test()
            {
                If(Self.x >= 5)
                {
                    Return "";
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(x),FloatType,FloatLit(5.25))),MethodDecl(Id(test),Instance,[],Block([If(BinaryOp(>=,FieldAccess(Self(),Id(x)),IntLit(5)),Block([Return(StringLit())]))]))])])"
        self.assertTrue(TestAST.test(input,expect,354))
    def test55(self):
        input = """
        Class Shape{
            Var length,width : Int;
            test()
            {
                Return Self.width * Self.length;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id(test),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(width)),FieldAccess(Self(),Id(length))))]))])])"
        self.assertTrue(TestAST.test(input,expect,355))
    def test56(self):
        input = """
            Class Test {
                    Constructor(a,b: Int; c: Float){
                        c = 3.14 * a * b;
                    }
                    Destructor(){ }
                    isGreater(a,b: Int){
                        Return a > b;
                    }
                    isLess(a,b: Int)
                    {
                        Return a < b;
                    }
                    isEqual(a,b:Int)
                    {
                        Return a == b;
                    }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([AssignStmt(Id(c),BinaryOp(*,BinaryOp(*,FloatLit(3.14),Id(a)),Id(b)))])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(isGreater),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(>,Id(a),Id(b)))])),MethodDecl(Id(isLess),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(<,Id(a),Id(b)))])),MethodDecl(Id(isEqual),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(==,Id(a),Id(b)))]))])])"
        self.assertTrue(TestAST.test(input,expect,356))
    def test57(self):
        input = """
            Class Test {
                    Constructor(a,b: Int; c: Float){
                        c = 3.14 * a * b;
                    }
                    Destructor(){ }
                    concatTwoString(a,b: String){
                        Return a +. b;
                    }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([AssignStmt(Id(c),BinaryOp(*,BinaryOp(*,FloatLit(3.14),Id(a)),Id(b)))])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(concatTwoString),Instance,[param(Id(a),StringType),param(Id(b),StringType)],Block([Return(BinaryOp(+.,Id(a),Id(b)))]))])])"
        self.assertTrue(TestAST.test(input,expect,357))
    def test58(self):
        input = """
            Class Test {
                    Constructor(a,b: Int){
                        Var x: Array[Int,2];
                        x[0] = a;
                        x[1] = b;
                    }
                    Destructor(){ }
                    getArray()
                    {
                        Return x;
                    }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([VarDecl(Id(x),ArrayType(2,IntType)),AssignStmt(ArrayCell(Id(x),[IntLit(0)]),Id(a)),AssignStmt(ArrayCell(Id(x),[IntLit(1)]),Id(b))])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(getArray),Instance,[],Block([Return(Id(x))]))])])"
        self.assertTrue(TestAST.test(input,expect,358))
    
    def test59(self):
        input = """
            Class Test {
                    Constructor(a,b: Int){
                        Var x: Array[Int,2];
                        x[0] = a;
                        x[1] = b;
                    }
                    Destructor(){ }
                    getArray()
                    {
                        Return x+a[0];
                    }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([VarDecl(Id(x),ArrayType(2,IntType)),AssignStmt(ArrayCell(Id(x),[IntLit(0)]),Id(a)),AssignStmt(ArrayCell(Id(x),[IntLit(1)]),Id(b))])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(getArray),Instance,[],Block([Return(BinaryOp(+,Id(x),ArrayCell(Id(a),[IntLit(0)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,359))
    
    def test60(self):
        input = """
            Class Test {
                    Constructor(a,b: Int){
                        Var x: Array[Int,2];
                        x[0] = a-2 -b[0];
                        x[1] = b;
                    }
                    Destructor(){ }
                    getArray()
                    {
                        Return x;
                    }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([VarDecl(Id(x),ArrayType(2,IntType)),AssignStmt(ArrayCell(Id(x),[IntLit(0)]),BinaryOp(-,BinaryOp(-,Id(a),IntLit(2)),ArrayCell(Id(b),[IntLit(0)]))),AssignStmt(ArrayCell(Id(x),[IntLit(1)]),Id(b))])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(getArray),Instance,[],Block([Return(Id(x))]))])])"
        self.assertTrue(TestAST.test(input,expect,360))

    
    def test61(self):
        input = """
                Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val numOfShape,y: Int = 0,3+2;
                        If(y <4){
                            Return 0;
                        }
                        Elseif(y==2){
                            Return 1;
                        }

                        
                    }
    
                }
                """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(y),IntType,IntLit(3))),MethodDecl(Id(get),Instance,[],Block([ConstDecl(Id(numOfShape),IntType,IntLit(0)),ConstDecl(Id(y),IntType,BinaryOp(+,IntLit(3),IntLit(2))),If(BinaryOp(<,Id(y),IntLit(4)),Block([Return(IntLit(0))]),If(BinaryOp(==,Id(y),IntLit(2)),Block([Return(IntLit(1))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,361))
    
    def test62(self):
        input = """
                Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val numOfShape,y: Int = 0,3+2;
                        If(y <4){
                            Foreach (i In 1 .. 100 By 2+2) {
                                    Out.printInt(i);
                                }
                        }
                        Elseif(y==2){
                            Return 1;
                        }

                        
                    }
    
                }
                """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(y),IntType,IntLit(3))),MethodDecl(Id(get),Instance,[],Block([ConstDecl(Id(numOfShape),IntType,IntLit(0)),ConstDecl(Id(y),IntType,BinaryOp(+,IntLit(3),IntLit(2))),If(BinaryOp(<,Id(y),IntLit(4)),Block([For(Id(i),IntLit(1),IntLit(100),BinaryOp(+,IntLit(2),IntLit(2)),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]),If(BinaryOp(==,Id(y),IntLit(2)),Block([Return(IntLit(1))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,362))
        
    def test63(self):
        input = """
                Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val numOfShape,y: Int = 0,3+2;
                        If(y <4){
                            Foreach (i In 1+2 .. 100 By 2+2) {
                                    Out.printInt(i);
                                }
                        }
                        Elseif(y==2){
                            Return 1;
                        }

                        
                    }
    
                }
                """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(y),IntType,IntLit(3))),MethodDecl(Id(get),Instance,[],Block([ConstDecl(Id(numOfShape),IntType,IntLit(0)),ConstDecl(Id(y),IntType,BinaryOp(+,IntLit(3),IntLit(2))),If(BinaryOp(<,Id(y),IntLit(4)),Block([For(Id(i),BinaryOp(+,IntLit(1),IntLit(2)),IntLit(100),BinaryOp(+,IntLit(2),IntLit(2)),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]),If(BinaryOp(==,Id(y),IntLit(2)),Block([Return(IntLit(1))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,363))
        
    def test64(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2));

                }
                """
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[AttributeDecl(Static,VarDecl(Id($a),ClassType(Id(Shape)),CallExpr(Id(A),Id($methodA),[CallExpr(Id(B),Id(func),[UnaryOp(-,IntLit(2))])])))])])"
        self.assertTrue(TestAST.test(input,expect,364))
    def test65(self):
        input = """
                Class Rectangle: Shape { 
                    Var a : Int = A::$methodAB(B.func(-2));

                }
                """
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType,CallExpr(Id(A),Id($methodAB),[CallExpr(Id(B),Id(func),[UnaryOp(-,IntLit(2))])])))])])"
        self.assertTrue(TestAST.test(input,expect,365))
    def test66(self):
        input = """
                Class Rectangle: Shape { 
                    Var a : Int = A::$methodAB(B.func(-2))+2;
                }
                """
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,CallExpr(Id(A),Id($methodAB),[CallExpr(Id(B),Id(func),[UnaryOp(-,IntLit(2))])]),IntLit(2))))])])"
        self.assertTrue(TestAST.test(input,expect,366))

    def test67(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: S = A::$methodA(B.func(-32));
                    $methodA(){
                        Return ays;
                    }
                }
                """
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[AttributeDecl(Static,VarDecl(Id($a),ClassType(Id(S)),CallExpr(Id(A),Id($methodA),[CallExpr(Id(B),Id(func),[UnaryOp(-,IntLit(32))])]))),MethodDecl(Id($methodA),Static,[],Block([Return(Id(ays))]))])])"
        self.assertTrue(TestAST.test(input,expect,367))

    def test68(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2));
                    $methodA(){
                        Var v1,v2: Int = A::$func(-a[2]),B.func(a[2]+a[3]);
                        Return a;
                    }
                }
                """
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[AttributeDecl(Static,VarDecl(Id($a),ClassType(Id(Shape)),CallExpr(Id(A),Id($methodA),[CallExpr(Id(B),Id(func),[UnaryOp(-,IntLit(2))])]))),MethodDecl(Id($methodA),Static,[],Block([VarDecl(Id(v1),IntType,CallExpr(Id(A),Id($func),[UnaryOp(-,ArrayCell(Id(a),[IntLit(2)]))])),VarDecl(Id(v2),IntType,CallExpr(Id(B),Id(func),[BinaryOp(+,ArrayCell(Id(a),[IntLit(2)]),ArrayCell(Id(a),[IntLit(3)]))])),Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input,expect,368))

    def test69(self):
        input = """
            Class myClassname {
                Val vari: Int = MainTEST.a.getat();
            }
        """
        expect = "Program([ClassDecl(Id(myClassname),[AttributeDecl(Instance,ConstDecl(Id(vari),IntType,CallExpr(FieldAccess(Id(MainTEST),Id(a)),Id(getat),[])))])])"
        self.assertTrue(TestAST.test(input,expect,369))

    def test70(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2));
                    $methodA(){
                        Var vang1,v2: Int = A::$func(-a[12]),B.func(a[62]+a[36]);
                        Var vang3: abv = New Triangle(1).funcA(2).funcB(3);
                        Return a;
                    }
                }
                """
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[AttributeDecl(Static,VarDecl(Id($a),ClassType(Id(Shape)),CallExpr(Id(A),Id($methodA),[CallExpr(Id(B),Id(func),[UnaryOp(-,IntLit(2))])]))),MethodDecl(Id($methodA),Static,[],Block([VarDecl(Id(vang1),IntType,CallExpr(Id(A),Id($func),[UnaryOp(-,ArrayCell(Id(a),[IntLit(12)]))])),VarDecl(Id(v2),IntType,CallExpr(Id(B),Id(func),[BinaryOp(+,ArrayCell(Id(a),[IntLit(62)]),ArrayCell(Id(a),[IntLit(36)]))])),VarDecl(Id(vang3),ClassType(Id(abv)),CallExpr(CallExpr(NewExpr(Id(Triangle),[IntLit(1)]),Id(funcA),[IntLit(2)]),Id(funcB),[IntLit(3)])),Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input,expect,370))
    def test71(self):
        input = """
        Class Program {
        }
        """
        expect = """Program([ClassDecl(Id(Program),[])])"""
        self.assertTrue(TestAST.test(input,expect,371))
    def test72(self):
        input = """
        Class Program { }
        Class B:Program {}
        """
        expect = """Program([ClassDecl(Id(Program),[]),ClassDecl(Id(B),Id(Program),[])])"""
        self.assertTrue(TestAST.test(input,expect,372))
    def test73(self):
        input = """
        Class Dog { 
            $test(){
                Var a: Int;
            }
        }"""
        expect = """Program([ClassDecl(Id(Dog),[MethodDecl(Id($test),Static,[],Block([VarDecl(Id(a),IntType)]))])])"""
        self.assertTrue(TestAST.test(input,expect,373))

    def test74(self):
        input = """Class Program : Animal { 
            Var a : String;
            Var b, c: Int = 1,2; 
        }"""
        expect = """Program([ClassDecl(Id(Program),Id(Animal),[AttributeDecl(Instance,VarDecl(Id(a),StringType)),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(2)))])])"""
        self.assertTrue(TestAST.test(input,expect,374))
        
    def test75(self):
        input = """Class Dog : Animal {
            main(){
                
            } 
            Constructor(a:Int; b:Float){}
            Destructor(){}
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,375))
        
    def test76(self):
        input = """Class Program{ 
            Var r: Float = 0xA001;
            Val $a, $b: Boolean = True, True;
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(r),FloatType,IntLit(40961))),AttributeDecl(Static,ConstDecl(Id($a),BoolType,BooleanLit(True))),AttributeDecl(Static,ConstDecl(Id($b),BoolType,BooleanLit(True)))])])"""
        self.assertTrue(TestAST.test(input,expect,376))
        
    def test77(self):
        input = """Class Program { 
        main(){
            a = b[0][1][2];
        }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(0),IntLit(1),IntLit(2)]))]))])])"""
                    
        self.assertTrue(TestAST.test(input,expect,377))

    def test78(self):
        input = """
        Class Dog : Animal 
        { 
            $_A(a, b, c:Int)
            { 
                Var a: String = "Hello"; 
                Break; 
            } 
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($_A),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(a),StringType,StringLit(Hello)),Break]))])])"""
        self.assertTrue(TestAST.test(input,expect,378))
    def test79(self):
        input = """
        Class A : B {
            $sum(a, b, c:Int){
                Return a + b + c;
            } 
            
        }"""
        expect = """Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id($sum),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([Return(BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,379))
    def test80(self):
        input = """
        Class A : A 
        { 
            $testParam(a,b,c:Bool; d:Int)
            { 
            {{}}
            } 
        }"""
        expect = """Program([ClassDecl(Id(A),Id(A),[MethodDecl(Id($testParam),Static,[param(Id(a),ClassType(Id(Bool))),param(Id(b),ClassType(Id(Bool))),param(Id(c),ClassType(Id(Bool))),param(Id(d),IntType)],Block([Block([Block([])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,380))
    def test81(self):
        input = """
        Class Dog : Animal 
        { 
            Val $a : String;
            Var b, $c: Int;
            Var d : Bool = True;
        }"""
        expect = """Program([ClassDecl(Id(Dog),Id(Animal),[AttributeDecl(Static,ConstDecl(Id($a),StringType,None)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Static,VarDecl(Id($c),IntType)),AttributeDecl(Instance,VarDecl(Id(d),ClassType(Id(Bool)),BooleanLit(True)))])])"""
        self.assertTrue(TestAST.test(input,expect,381))
    
    def test82(self):
        input = """
            Class A{
                method1(a,b: String; c: Float; d: X) {
                    test22::$name = X::$name;
                }
            }
            """
        expect = """Program([ClassDecl(Id(A),[MethodDecl(Id(method1),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),FloatType),param(Id(d),ClassType(Id(X)))],Block([AssignStmt(FieldAccess(Id(test22),Id($name)),FieldAccess(Id(X),Id($name)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,382))

    def test83(self):
        input = """
        Class Program
        { 
            $test_if_stmt()
            { 
                If (a == b)
                {
                    a = 1;
                }
                Else
                {
                    a = -1;
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($test_if_stmt),Static,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))]),Block([AssignStmt(Id(a),UnaryOp(-,IntLit(1)))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,383))
    def test84(self):
        input = """
        Class a 
        { 
            $test_if_stmt()
            { 
                Var a: Int = 0;
                If (a > 0)
                {
                   a = a + 1;

                }
                Elseif (a <= 0)
                {
                    a = a * 3;
                }
                Else
                {
                    a = Program.get(a);
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(a),[MethodDecl(Id($test_if_stmt),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),If(BinaryOp(>,Id(a),IntLit(0)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),If(BinaryOp(<=,Id(a),IntLit(0)),Block([AssignStmt(Id(a),BinaryOp(*,Id(a),IntLit(3)))]),Block([AssignStmt(Id(a),CallExpr(Id(Program),Id(get),[Id(a)]))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,384))
    def test85(self):
        input = """
        Class D
        { 
            $test_if_stmt()
            { 
                Var a, b, c : Int = 0, 0, 0;
                If (a == b)
                {
                    b = c;
                }
                Elseif (a != b)
                {
                    b = 0;
                }
                Elseif (c == a)
                {
                    b = a;
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(D),[MethodDecl(Id($test_if_stmt),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(b),Id(c))]),If(BinaryOp(!=,Id(a),Id(b)),Block([AssignStmt(Id(b),IntLit(0))]),If(BinaryOp(==,Id(c),Id(a)),Block([AssignStmt(Id(b),Id(a))]))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,385))  
    
        
    def test86(self):
        input = """
        Class D
        { 
            $test_if_stmt()
            { 
                Var a, b, c : Int = 0, 0, 0;
                If (a == b)
                {
                    b = c;
                }
                Elseif (c == a)
                {
                    b = a;
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(D),[MethodDecl(Id($test_if_stmt),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(b),Id(c))]),If(BinaryOp(==,Id(c),Id(a)),Block([AssignStmt(Id(b),Id(a))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,386)) 
    def test87(self):
        input = """
        Class D
        { 
            $test_if_stmt()
            { 
                Var a, b, c : Int = 0, 0, 0;
                If (a == b)
                {
                    b = c;
                }
                Elseif (a != b)
                {
                    b = 0;
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(D),[MethodDecl(Id($test_if_stmt),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(b),Id(c))]),If(BinaryOp(!=,Id(a),Id(b)),Block([AssignStmt(Id(b),IntLit(0))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,387)) 
    def test88(self):
        input = """
        Class D
        { 
            $test_if_stmt()
            { 
                Var a, b, c : Int = 0, 0, 0;
                If (a == b)
                {
                    b = c;
                }
                Elseif (a != b)
                {
                    b = 0+b[2];
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(D),[MethodDecl(Id($test_if_stmt),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(b),Id(c))]),If(BinaryOp(!=,Id(a),Id(b)),Block([AssignStmt(Id(b),BinaryOp(+,IntLit(0),ArrayCell(Id(b),[IntLit(2)])))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,388)) 
    def test89(self):
        input = """
        Class D
        { 
            $test_if_stmt()
            { 
                Var a, b, c : Int = 0, 0, 0;
                If (a == b)
                {
                    b = c;
                }
                Elseif (c == a)
                {
                    b = a[2][2];
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(D),[MethodDecl(Id($test_if_stmt),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(b),Id(c))]),If(BinaryOp(==,Id(c),Id(a)),Block([AssignStmt(Id(b),ArrayCell(Id(a),[IntLit(2),IntLit(2)]))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,389)) 
    
    def test90(self):
        input = """
        Class D
        { 
            $test_if_stmt()
            { 
                Var a, b, c : Int = 0, 0, 0;
                If (a == b)
                {
                    b = c[2+a[3]];
                }

            } 
        }"""
        expect = """Program([ClassDecl(Id(D),[MethodDecl(Id($test_if_stmt),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(b),ArrayCell(Id(c),[BinaryOp(+,IntLit(2),ArrayCell(Id(a),[IntLit(3)]))]))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,390)) 
        
    def test91(self):
        input = """
        Class D
        { 
            $test_if_stmt()
            { 
                Var a, b, c : Int = 0, 0, 0;
                If (a == b)
                {
                    b = c;
                }
                Elseif (a != b)
                {
                    b = 0;
                }
                Elseif (c == a)
                {
                    b = a+n+ m[2];
                }
            } 
        }"""
        expect = """Program([ClassDecl(Id(D),[MethodDecl(Id($test_if_stmt),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(b),Id(c))]),If(BinaryOp(!=,Id(a),Id(b)),Block([AssignStmt(Id(b),IntLit(0))]),If(BinaryOp(==,Id(c),Id(a)),Block([AssignStmt(Id(b),BinaryOp(+,BinaryOp(+,Id(a),Id(n)),ArrayCell(Id(m),[IntLit(2)])))]))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,391))   
    def test92(self):
        input = """
        Class _ { 
            $For(a: Float; b: Int){
                Foreach(a In 27 .. 2) {
                Var temp: Int;
                 temp = b - a;
                }
            }
        }"""
        expect = """Program([ClassDecl(Id(_),[MethodDecl(Id($For),Static,[param(Id(a),FloatType),param(Id(b),IntType)],Block([For(Id(a),IntLit(27),IntLit(2),IntLit(1),Block([VarDecl(Id(temp),IntType),AssignStmt(Id(temp),BinaryOp(-,Id(b),Id(a)))])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,392))
    def test93(self):
        input = """
        Class D 
        { 
            Val d,b: Int = 9, 5;
        }"""
        expect = """Program([ClassDecl(Id(D),[AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(9))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(5)))])])"""
        self.assertTrue(TestAST.test(input,expect,393))
    def test394(self):
        input = """
            Class Program {
                main() {
                    a[1][2][3][4] = b.c(d[1][2+4][0x5 * 0b1]);
                }
                method () { }
            }
            """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]),CallExpr(Id(b),Id(c),[ArrayCell(Id(d),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(4)),BinaryOp(*,IntLit(5),IntLit(1))])]))])),MethodDecl(Id(method),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,394))
    def test95(self):
        input = """
            Class E {
                method() {
                    Return a[1][2][3] + className.b()[4];
                }
            }
            """
        expect = """Program([ClassDecl(Id(E),[MethodDecl(Id(method),Instance,[],Block([Return(BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(CallExpr(Id(className),Id(b),[]),[IntLit(4)])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,395))
    def test96(self):
        input = """
        Class Program{
                main(){
                    Var flag: Boolean = True;
                    If(flag == True)
                    {
                        Foreach (i In 2 .. 100 By 2)
                        {
                            Out.printInt(i);
                        }
                    }
                }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(flag),BoolType,BooleanLit(True)),If(BinaryOp(==,Id(flag),BooleanLit(True)),Block([For(Id(i),IntLit(2),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,396))
    
    def test97(self):
        input = """
            Class E {
                method() {
                    Return a[1][2][3] + className.b()[4+a];
                }
            }
            """
        expect = """Program([ClassDecl(Id(E),[MethodDecl(Id(method),Instance,[],Block([Return(BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(CallExpr(Id(className),Id(b),[]),[BinaryOp(+,IntLit(4),Id(a))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,397))
    
    def test98(self):
        input = """
            Class E {
                method() {
                    Return a[1][2][3] + className.b()[4+a[2]];
                }
            }
            """
        expect = """Program([ClassDecl(Id(E),[MethodDecl(Id(method),Instance,[],Block([Return(BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(CallExpr(Id(className),Id(b),[]),[BinaryOp(+,IntLit(4),ArrayCell(Id(a),[IntLit(2)]))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,398))
    def test99(self):
        input = """
            Class E {
                method() {
                    Return a[1][2][3+a*2] + className.b()[4];
                }
            }
            """
        expect = """Program([ClassDecl(Id(E),[MethodDecl(Id(method),Instance,[],Block([Return(BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2),BinaryOp(+,IntLit(3),BinaryOp(*,Id(a),IntLit(2)))]),ArrayCell(CallExpr(Id(className),Id(b),[]),[IntLit(4)])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,399))
    
    def test100(self):
        input = """
            Class E {
                method() {
                    Return a[1][2+a.id][3] + className.b()[4];
                }
            }
            """
        expect = """Program([ClassDecl(Id(E),[MethodDecl(Id(method),Instance,[],Block([Return(BinaryOp(+,ArrayCell(Id(a),[IntLit(1),BinaryOp(+,IntLit(2),FieldAccess(Id(a),Id(id))),IntLit(3)]),ArrayCell(CallExpr(Id(className),Id(b),[]),[IntLit(4)])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,400))