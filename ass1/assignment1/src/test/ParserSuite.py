

import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
   
    def test1(self):
        input = """
                Class Shape {
                    Val $numOfShape: Int = 0;
    
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1))

    def test02(self):
        input = """
                Class Shape {
                    Val $numOfShape,y: Int = 0,3;
    
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2))

    def test03(self):
        input = """
                Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        
                    }
    
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,3))

    def test04(self):
        input = """
                Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val numOfShape,y: haha = 0,3;
                    }
    
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4))

    def test05(self):
        input = """
                Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val numOfShape,y: Int = 0,3;
                    }
    
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,5))

    def test06(self):
        input = """
                Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val numOfShape,y: Int = 0,3;
                        If(y <4){
                            Return 0;
                        }
                        
                    }
    
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,6))
        
    def test07(self):
        input = """
                Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val numOfShape,y: Int = 0,3;
                        If(y <4){
                            Return 0;
                        }
                        Else{
                            Return 1;
                        }
                        
                    }
    
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,7))

    def test08(self):
        input = """
                Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val numOfShape,y: Int = 0,3;
                        If(y <4){
                            Return 0;
                        }
                        Elseif(y==2){
                            Return 1;
                        }
                        Else{
                            Return Haha;
                        }
                        
                    }
    
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,8))
    
    def test09(self):
        input = """
                Class Shape {
                    Val $numOfShape,y: Int = 0,3;
                    get(){
                        Val $numOfShape,y: Int = 0,3;
                        If(y <4){
                            Return 0;
                        }
                        Elseif(y==2){
                            Return 1;
                        }
                        Else{
                            Return Haha;
                        }
                        
                    }
    
                }
                """
        expect = "Error on line 5 col 28: $numOfShape"
        self.assertTrue(TestParser.test(input,expect,9))
    
    def test10(self):
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
                        Else{
                            Return Haha;
                        }
                        
                    }
    
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,10))
    
    def test11(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,11))
    
    def test12(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,12))
        
    def test13(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,13))
            
    def test14(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2));

                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,14))

    def test15(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::methodAB(B.func(-2));

                }
                """
        expect = "Error on line 3 col 37: ::"
        self.assertTrue(TestParser.test(input,expect,15))

    def test16(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2));
                    Return $a;
                }
                """
        expect = "Error on line 4 col 20: Return"
        self.assertTrue(TestParser.test(input,expect,16))

    def test17(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: S = A::$methodA(B.func(-32));
                    $methodA(){
                        Return ays;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,17))

    def test18(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2));
                    $methodA(){
                        Var v1,v2: Int = A::$func(-a[2]),B.func(a[2]+a[3]);
                        Return a;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,18))

    def test19(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2));
                    $methodA(a,v,b : Int ; i,y : Float){
                        Var v1,$v2: Int = A::$func(-a[2]),B.func(a[2]+a[3]);
                        Return a;
                    }
                }
                """
        expect = "Error on line 5 col 31: $v2"
        self.assertTrue(TestParser.test(input,expect,19))

    def test20(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,20))
    
    def test21(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2));
                    $methodA(){
                        Var vang1,v2: Int = A::$func(-a[12]),B.func(a[62]+a[36]);
                        Var vang3: abv = New Triangle(1).funcA(2).funcB(3);
                        Var v4: Shape = Rectangle::$a;
                        Return a;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,21))

    


    def test22(self):
        input = """
            Class ahhaa: hi { }
            Class Tur {
                Val one1,two2,three4: Int = 1,2,3;
                __str1__() {
                    Var one,two,three: Int = 1,2,3;
                    Val four56,five_2: Int;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 22))

    def test23(self):
        input = """
            Class ahhaa: hi { }
            Class Tur {
                Val one1,two2,three4: Int = 1,2,3+4;
                __str1__() {
                    Var one,two,three: Int = 1,2,3;
                    Val four56,five_2: Int;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 23))

    def test24(self):
        input = """
            Class ahhaa: hi { }
            Class Tur {
                Val one1,two2,three4: Int  1,2;
                __str1__(a) {
                    Var one,two,three: Int = 1,2,3;
                    Val four56,five_2: Int;
                }
            }
            """
        expect = "Error on line 4 col 43: 1"
        self.assertTrue(TestParser.test(input, expect, 24))

    def test25(self):
        input = """
            Class Cat: Animal { }
            Class Rose: Flower { }
            Class Truuu {
                Val one,two,three: Int =;
                __str__() {
                    Var one,two,three: Int = 1,2,3;
                    Val four,five: Int;
                }
            }
            """
        expect = "Error on line 5 col 40: ;"
        self.assertTrue(TestParser.test(input, expect, 25))


    def test26(self):
        input = """
        Class A{
            Var attribute: Int;
            testif(){
                Var real : Array[Int,0x123] = Array();
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 26))

    def test27(self):
        input = """
        Class A{
            Var attribute: Int;
            testif(){
                Self::$a;
                
            }
        }
        """
        expect = "Error on line 5 col 20: ::"
        self.assertTrue(TestParser.test(input, expect, 26))

    def test27(self):
        input = """
        Class A{
            Var attribute: Int;
            testif(){
                Self.funcA().funcB().funcC().funcD();
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 27))

    def test28(self):
        input = """
        Class A{
            Var attribute: Int;
            testif(){
                {
                    a[c/d][b.getNumber()].setNumber = Name::$getName();
                }
                
            }
        }
        """
        expect = "Error on line 5 col 16: {"
        self.assertTrue(TestParser.test(input, expect, 28))

    def test29(self):
        input = """
        Class A{
            Var attribute: Int;
            testif(){
                Return Self.elf;                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 29))

    def test30(self):
        input = """
        Class A{
            Var attribute: Int;
            testif(){
                Return A::$Self; 
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 30))

    def test31(self):
        input = """
        Var attr1: Int = 10;
        Class A{
            Var attribute: Int;
            testif(){
                
            }
        }

        """
        expect = "Error on line 2 col 8: Var"
        self.assertTrue(TestParser.test(input, expect, 31))

    def test32(self):
        input = """
        Class ABX{
            Var conco: Int;
            funcn(){
                
            }
        }
        Foreach(Self.attr2 In New expr1(New expr2()) .. a[1] + a[2] By Array(1,2,3)){
        }
        """
        expect = "Error on line 8 col 8: Foreach"
        self.assertTrue(TestParser.test(input, expect, 32))

    def test33(self):
        input = """
            Class A{
                Class B{
                    Var attribute: Int;
                    testif(){
                        
                    }
                }
            }
            """
        expect = "Error on line 3 col 16: Class"
        self.assertTrue(TestParser.test(input, expect, 33))

    def test34(self):
        input = """
            Class Program {
                main() {
                    b = name::$test().b();
                }
            }
            Class A {
                Return New Bowling(A);
            }
        """
        expect = "Error on line 8 col 16: Return"
        self.assertTrue(TestParser.test(input, expect, 34))
        
    def test35(self):
        input = """
            Class Program {
                main() {
                    b = name::$test().b();
                }
            }
            Class A {
                Return New Bowling(A);
            }
        """
        expect = "Error on line 8 col 16: Return"
        self.assertTrue(TestParser.test(input, expect, 35))
    
    def test36(self):
        input = """
            Class gram {
                method() {
                    Return a[3][6][9] + className.foo()[3];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 36))

    def test37(self):
        input = """

            Class TEST {
                Constructor(a,b,c: Int) {
                    Return x+Self.ad + y + z3 + 4;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 37))

    def test38(self):
        input = """
        Class A{
            Var attribute: Int;
            testif(){
                Var real : Array[Int,0x123];
                If(a[1] + New A(2)){
                    b[a[1][2][3]] = New B(a);
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 38))

    def test38(self):
        input = """
        Class A{
            Var attribute: Int;
            testif(){
                Var real : Array[Int,0x123];
                If(a[1] + New A(2)){
                    b[a[1][2][3]] = New B(a);
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 38))

    def test39(self):
        input = """
        Class bole{
            Var abc: Int;
            foo(){
                Var real : Array[Float,0x12324];
                If(a[1] + New A(2)){
                    x=2;
                }
                Return 0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 39))

    def test40(self):
        input = """
        Class A{
            Var acb: String;
            foo(){
                Var real : Array[Float,0x123267];
                If(a[1] + New A(2)){
                    (ysc[a[1][2][3]]).attr1 = Array(Array(Array(Array())));
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 40))
        
    def test41(self):
        input = """
            Class myVarName {
                Constructor() {
                    Self.a = arr[3][4];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 41))

    def test42(self):
        input = """
            Class Program {

                Destructor() {
                    Std.ol().All(1);
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 42))
    
    def test43(self):
        input = """
            Class myVarName {
                Constructor() {
                    Self.a = arr[3][4+2];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 43))
    
    def test44(self):
        input = """
            Class myVarName {
                Constructor() {
                    Self.a = arr[3][4];
                    Self.d = arr[3+2*2][4+2];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 44))
        
    def test45(self):
        input = """
            Class myVarName {
                Constructor() {
                    Self.a = arr[3][4];
                    Self.a = arr[3][4+2]+arr[3][4];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 45))
        
    def test46(self):
        input = """
            Class myVarName {
                Constructor() {
                    Self.a = arr[3][4];
                    arr=arr[3][4] +2;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 46))
        
    def test47(self):
        input = """
            Class myVarName {
                Constructor() {
                    Self.a = arr[3][4];
                    arr=arr[3][4] +a;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 47))
    
    def test48(self):
        input = """
            Class myVarName {
                Constructor() {
                    Self.a = arr[3][4];
                    arr=arr[3][4] +a-b+a.bu;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 48))
    def test49(self):
        input = """
            Class myVarName {
                Constructor() {
                    Self.a = arr[3][4];
                    arr=arr[3][4] +a*2;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 49))
    def test50(self):
        input = """
            Class myVarName {
                Constructor() {
                    Self.a = arr[3][4];
                    arr=arr[3][4] +a+(b+2);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 50))
    
    def test51(self):
        input = """
        Class A{
            Var yu: Int;
            for(){
                Var real : Array[Int,0x123];
                If(!(B != 2))
                    Return NULL;
            }
        }
        """
        expect = "Error on line 7 col 20: Return"
        self.assertTrue(TestParser.test(input, expect, 51))
    
    def test52(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2));
                    $methodA(){
                        Return a+a;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,52))
        
    def test53(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2));
                    $methodA(){
                        Return a+2;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,53))
    
    def test54(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+2;
                    $methodA(){
                        Return a+2;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,53))
        
    def test55(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        Return a+2;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,55))
        
    def test56(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                        Return a+2;
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,56))
    
    def test57(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                        Else{
                            Return New a();
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,57))
    
    def test58(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,58))
    
    def test59(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                        Return a+2;
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,59))
    
    def test60(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                        Else{
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,60))
    
    def test61(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                        Else{
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                                i=3+i;
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,61))
    
    def test62(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                        Else{
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                                If(i==2){ Return 0;}
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,62))

    def test63(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                        Else{
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                                If(i==2){ Break;}
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,63))
    
    def test64(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                        Else{
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                                If(i==2){ Continue;}
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,64))

    def test65(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                        Else{
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                                If(i==2){ Continue;}
                                Else{
                                    i=New a(2_3+3);
                                }
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,65))
    
    def test66(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                        Else{
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                                If(i==2){ Continue;}
                                Else{
                                    i=New a(2_3+3)+(2-2);
                                }
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,66))
    
    def test67(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                        Else{
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                                If(i==2){ Continue;}
                                Else{
                                    i=New a(2_3+3)+a[2];
                                }
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,67))
    
    def test68(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                        Else{
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                                If(i==2){ Continue;}
                                Else{
                                    i=New a(2_3+3)+a[2][2];
                                }
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,68))
    
    def test69(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2);
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                        Else{
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                                If(i==2){ Continue;}
                                Else{
                                    i=New a(2_3+3)+a[2+3][2][2+ab[2]];
                                }
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,69))
    
    def test70(self):
        input = """
                Class Rectangle: Shape { 
                    Var $a: Shape = A::$methodA(B.func(-2))+a+(2+2)+a[ab[2]+2];
                    $methodA(){
                        If(a.c>3){
                            Return a+2;
                        }
                        Else{
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                                If(i==2){ Continue;}
                                Else{
                                    i=New a(2_3+3)+a[2+3][2][2+ab[2]];
                                }
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,70))

    
    def test71(self):
        input = """
            Class Cat {
                returnMethod() {
                }
                Constructor() {
                    Self.initial = valuenew;
                }
                Destructor() {
                    Cat.remove();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 71))
    
    def test72(self):
        input = """
            Class Cat {
                
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 72))
    
    def test73(self):
        input = """
            Class Cat {
                Constructor() {
                    Self.initial = valuenew+New a();
                }
                Destructor() {
                    Cat.remove();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 73))
        
    def test74(self):
        input = """
            Class Cat {

                Constructor() {
                    Self.initial = valuenew + New a() +(23+2);
                }
                Destructor() {
                    Self.initial =0;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 74))
    
    def test75(self):
        input = """
            Class Cat {
                returnMethod() {
                }
                Constructor() {
                    Self.initial = valuenew+ ad::$dhs;
                }

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 75))
    
    def test76(self):
        input = """
            Class Cat {
                returnMethod() {
                    Return New a(A[1]);
                }
                Constructor() {
                    Self.initial = valuenew;
                }
                Destructor() {
                    Cat.remove();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 76))
    
    def test77(self):
        input = """
            Class Cat {
                returnMethod() {
                    Return New a(A[1]);
                }
                Constructor() {
                    Self.initial = valuenew;
                }
                Destructor() {
                    Cat.remove(a[2],2);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 77))
    
    def test78(self):
        input = """
            Class Cat {
                returnMethod() {
                    Return New a(A[1]);
                }
                Constructor() {
                    Self.initial = valuenew;
                }
                Destructor() {
                    Cat.remove(a[2],2);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 78))
    def test79(self):
        input = """
            Class Cat {
                returnMethod() {
                    Return New a(A[1]);
                }
                Constructor() {
                    Self.initial = valuenew;
                }
                Destructor() {
                    Cat.remove(a[2],2);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 79))
    
    def test80(self):
        input = """
            Class Cat {
                returnMethod() {
                    Return New a(A[1]);
                }
                Constructor() {
                    Self.initial = valuenew;
                }
                Destructor() {
                    Cat.remove(a[2],2);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 80))
    
    def test81(self):
        input = """
            Class Hayate {
                main() {
                    If(k[2] > 5){
                        Return abc;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 81))
    
    def test82(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5+2){
                        Return abc;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 82))
    
    def test83(self):
        input = """
            Class haah{
                main() {
                    If(k[2][2] > 5){
                        Return abc;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 85))
    
    def test84(self):
        input = """
            Class haah{
                main() {
                    If(k[2][2] > 5+2){
                        Return abc;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 84))
    
    def test85(self):
        input = """
            Class Hayate {
                main() {
                    If(k+a.d > 5){
                        Return abc;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 85))
    
    def test86(self):
        input = """
            Class Hayate {
                main() {
                    If(k::$d(2)> 5){
                        Return abc;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 86))
        
    def test87(self):
        input = """
            Class Hayate {
                main() {
                
                    If(k[a.e] > 5){
                        Return abc;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 87))
        
    def test88(self):
        input = """
            Class Hayate {
                main() {
           
                    If(k > 5){
                        Return abc;
                    }
                    Else{
                        Return a[2]+2;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 88))
        
    def test89(self):
        input = """
            Class Hayate {
                main() {
                
                    If(k > 5){
                        Return abc;
                    }
                    Else{
                        Return a[2];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 89))
        
    def test90(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5){
                        Return abc;
                    }
                    Else{
                        Return a[2]+ab[2][2*2];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,90))
        
    def test91(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5){
                        Return abc;
                    }
                    Else{
                        Return a[2+a[2+2]];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 91))
    
    def test92(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5){
                        Foreach (x In 5 .. 2) {
                            Out.printInt(arr[x]);
                        }
                    }
                    Else{
                        Return a[2+a[2+2]];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 92))
    def test93(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5){
                        Foreach (x In 5 .. 2) {
                            Out.printInt(arr[x]);
                            i=i+2+a[2+a[2]];
                        }
                    }
                    Else{
                        Return a[2+a[2+2]];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 93))
    def test94(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5){
                        Foreach (x In 5 .. 2) {
                            Out.printInt(arr[x]);
                            i=i+2+a[2+a[2]+ad];
                        }
                    }
                    Else{
                        Return a[2+a[2+2]];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 94))
    def test95(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5){
                        Return abc+New a(2);
                    }
                    Else{
                        Return a[2+a[2+2]];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 95))
        
    def test96(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5+a::$da){
                        Return abc;
                    }
                    Else{
                        Return a[2+a[2+2]];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 96))
    def test97(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5+a::$da){
                        Foreach (x In 5 .. 2) {
                            Out.printInt(arr[x]);
                            i=i+2+a[2+a[2]];
                        }
                    }
                    Else{
                        Return a[2+a[2+2]];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 97))
    def test98(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5){
                        Foreach (x In 5+2 .. 2+2) {
                            Out.printInt(arr[x]);
                            i=i+2+a[2+a[2]];
                        }
                    }
                    Else{
                        Return a[2+a[2+2]];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 98))
    def test99(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5){
                        Foreach (x In 5 .. 2) {
                            Out.printInt(arr[x]);
                            i=i+2+a[2+a[2]];
                            If(i==2){
                                Break;
                            }
                        }
                    }
                    Else{
                        Return a[2+a[2+2]];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 99))
    def test100(self):
        input = """
            Class Hayate {
                main() {
                    If(k > 5){
                        Foreach (x In 5 .. 2) {
                            Out.printInt(arr[x]);
                            i=i+2+a[2+a[2]];
                            If(i==2){
                                i = i+ a[a[a[a]]] +s.a;
                                Break;
                            }
                        }
                    }
                    Else{
                        Return a[2+a[2+2]];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 100))
    
    def test101(self):
        input = """
        Class A
        { 
            $test()
            { 
                Var arr: float = 7E+10;
            } 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,101))
