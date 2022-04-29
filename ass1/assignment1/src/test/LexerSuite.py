import unittest
from TestUtils import TestLexer
#8,28,31,37,92,93,99
class LexerSuite(unittest.TestCase):
    def test_identifier1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("""abc?xyzb""","abc,Error Token ?",100))
        
    def test_identifier2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("$abc","$abc,<EOF>",101))
        
    def test_identifier3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("?aCBbdch","Error Token ?",102))
        
    def test_identifier4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("aAsVN","aAsVN,<EOF>",103))
        
    def test_identifier5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("65460ASDE_1234","65460,ASDE_1234,<EOF>",104))
        
    def test_identifier6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc0123","abc0123,<EOF>",105))
        
    def test_identifier7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(".Abc0123",".,Abc0123,<EOF>",106))
        
    def test_identifier8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("+Abc0123","+,Abc0123,<EOF>",107))
    
    def test_identifier9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("$","Error Token $",108))
        
    def test_identifier10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("^Abc0123","Error Token ^",109))
        
    def test_identifier11(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Abc0123","Abc0123,<EOF>",110))
    def test_identifier12(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("$@Abc0123","Error Token $",111))
    def test_identifier13(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("12Abc0123","12,Abc0123,<EOF>",112))
    def test_identifier14(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("#Abc0123","Error Token #",113))
    def test_identifier15(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_2Abc0123","12,Abc0123,<EOF>",114))
    
    
    def test_real1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1.E-2","1.E-2,<EOF>",115))
    def test_real2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("0.33E-2","0.33E-2,<EOF>",116))
    def test_real3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("123E-24","123E-24,<EOF>",117))
        
    def test_real4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("12_3E-24","123E-24,<EOF>",118))
    def test_real5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1.2_3E+24","1.23E+24,<EOF>",119))
    
    def test_real6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1.2__3E+24","1.2,__3E,+,24,<EOF>",120))
    
    def test_real7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1.2_3","1.23,<EOF>",121))
    def test_real8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1.22_3_4","1.2234,<EOF>",122))
    
    def test_real9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_2_3.2_3E-24","123.23E-24,<EOF>",123))
    
    def test_real10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("01.2_3E-24","01,.2_3E-24,<EOF>",124))


    def test_bool(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("True","True,<EOF>",125))
    def test_bool1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("False_","False_,<EOF>",126))
    def test_bool2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("false","false,<EOF>",127))
    def test_bool3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("false True","false,True,<EOF>",128))
    def test_bool4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("@false","Error Token @",129))
    
    
    def test_int(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1","1,<EOF>",131))
    def test_int2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1__2","1,__2,<EOF>",132))
    def test_int3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_2_3","123,<EOF>",133))
    def test_int4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("0b011","0b0,11,<EOF>",134))
    def test_int5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("0001","00,01,<EOF>",135))
    def test_int(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("10B2","10,B2,<EOF>",130))
    
    def test_string1(self):
        """test string"""
        self.assertTrue(TestLexer.test("21321321321","21321321321,<EOF>",136))
    def test_string2(self):
        self.assertTrue(TestLexer.test("ahihi\\\\","ahihi\\\\,<EOF>",137))
    def test_string3(self):
        self.assertTrue(TestLexer.test("ngua nguoi","ngua,nguoi,<EOF>",138))
    def test_string4(self):
        self.assertTrue(TestLexer.test("kjadskasd*","kjadskasd,*,<EOF>",139))
    def test_string5(self):
        self.assertTrue(TestLexer.test("\n","<EOF>",140))
    def test_string6(self):
        self.assertTrue(TestLexer.test("",'<EOF>',141))
    def test_string7(self):
        self.assertTrue(TestLexer.test("dakd da","dakd,da,<EOF>",142))
    def test_string8(self):
        self.assertTrue(TestLexer.test("if(true)","if,(,true,),<EOF>",143))
    def test_escape(self):
        self.assertTrue(TestLexer.test("hoid","hoid,<EOF>",144))
    def test_string9(self):
        self.assertTrue(TestLexer.test('"    \\t\\t\\n"','    \\t\\t\\n,<EOF>',145))
    def test_escape1(self):
        self.assertTrue(TestLexer.test("if 123continue","if,123,continue,<EOF>",146))
    def test_string2(self):
        self.assertTrue(TestLexer.test('"ngua nguoi\\n  b \\t"',"ngua nguoi\\n  b \\t,<EOF>",147))
    def test_escape8(self):
        self.assertTrue(TestLexer.test("kjakd\nqakd","kjakd,qakd,<EOF>",148))
    def test_escape3(self):
        self.assertTrue(TestLexer.test('"\\t"','\\t,<EOF>',149)) 


    def test_operator(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("+","+,<EOF>",150))
    def test_operator1(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("++","+,+,<EOF>",151))
    
    def test_operator2(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("*","*,<EOF>",152))
    def test_operator3(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("||||","||,||,<EOF>",153))
    def test_operator4(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("====","==,==,<EOF>",154))
    def test_operator5(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("===","==,=,<EOF>",155))
    def test_operator6(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("&&","&&,<EOF>",156))
    def test_operator7(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("=&&","=,&&,<EOF>",157))
    def test_operator8(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("=&&","=,&&,<EOF>",158))
    def test_operator9(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("=&&,","=,&&,,,<EOF>",159))
    def test_operator10(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("=&&=,","=,&&,=,,,<EOF>",160))
    def test_operator13(self):
        """test Operator"""
        self.assertTrue(TestLexer.test(",",",,<EOF>",161))
    def test_operator11(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("[=,]","[,=,,,],<EOF>",161))
    def test_operator12(self):
        """test Operator"""
        self.assertTrue(TestLexer.test(",,,+-",",,,,,,+,-,<EOF>",163))
      
    def test_keyword(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("123continue","123,continue,<EOF>",164))
    def test_keyword1(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("123Break","123,Break,<EOF>",165))
    def test_keyword2(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("If","If,<EOF>",166))
    def test_keyword9(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("If1","If1,<EOF>",167))
    def test_keyword3(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("Return","Return,<EOF>",168))
    def test_keyword4(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("Do","Do,<EOF>",169))
    def test_keyword5(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("While","While,<EOF>",170))
    def test_keyword6(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("Continue","Continue,<EOF>",171))
    def test_keyword7(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("Break","Break,<EOF>",172))
    def test_keyword8(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("Else","Else,<EOF>",173))
       
    def test_comment(self):
        self.assertTrue(TestLexer.test('##abc##','<EOF>',174))
    def test_comment1(self):
        self.assertTrue(TestLexer.test('##abc/**/##','<EOF>',175))
    def test1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Val $a, number : Int = 5, 6;","Val,$a,,,number,:,Int,=,5,,,6,;,<EOF>",176))
    def test2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Val $x, num, $y, 9gh : Int = 51, 61, 71;","Val,$x,,,num,,,$y,,,9,gh,:,Int,=,51,,,61,,,71,;,<EOF>",177))
    def test3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Var $Dec, num: Int = 0b0101110, 0xAFF;","Var,$Dec,,,num,:,Int,=,0b0,101110,,,0xAFF,;,<EOF>",178))
    def test4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Var $dec: Int = -5910;","Var,$dec,:,Int,=,-,5910,;,<EOF>",179))
    def test5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Var $dec: Float = -1.562e-90;","Var,$dec,:,Float,=,-,1.562e-90,;,<EOF>",180))
    def test6(self):
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 181))
    def test7(self):
        self.assertTrue(TestLexer.test("123a##123##", "123,a,<EOF>", 182))
    def test8(self):
        self.assertTrue(TestLexer.test("_acb5", "_acb5,<EOF>", 183))
    def test9(self):
        self.assertTrue(TestLexer.test("$_free", "$_free,<EOF>", 184))
    def test10(self):
        self.assertTrue(TestLexer.test("$sad af1", "$sad,af1,<EOF>", 185)) 
    def test11(self):
        self.assertTrue(TestLexer.test("1_12343 _my $ad12", "112343,_my,$ad12,<EOF>", 186))
    def test12(self):
        self.assertTrue(TestLexer.test("1ABCxyz", "1,ABCxyz,<EOF>", 187))
    def test13(self):
        self.assertTrue(TestLexer.test("@abcd!ed", "Error Token @", 188))
    def test14(self):
        self.assertTrue(TestLexer.test("%eHi", "%,eHi,<EOF>", 189))
    def test15(self):
        self.assertTrue(TestLexer.test("*abcdery", "*,abcdery,<EOF>", 190))

        
    def test16(self):
        self.assertTrue(TestLexer.test("hoidlka\n","hoidlka,<EOF>",191))
    def test17(self):
        self.assertTrue(TestLexer.test('"hoidlka\\n"',"hoidlka\\n,<EOF>",192))
    def test18(self):
        self.assertTrue(TestLexer.test("do {} while","do,{,},while,<EOF>",193))
    def test19(self):
        self.assertTrue(TestLexer.test("if(a > b) k = 7","if,(,a,>,b,),k,=,7,<EOF>",194))
    def test20(self):
        self.assertTrue(TestLexer.test("break;","break,;,<EOF>",195))
    def test21(self):
        self.assertTrue(TestLexer.test("int[123];",'int,[,123,],;,<EOF>',196))
    def test22(self):
        self.assertTrue(TestLexer.test('"hoidlka \\n"','hoidlka \\n,<EOF>',197))
    def test23(self):
        self.assertTrue(TestLexer.test(" \"hoidlka\n \" ","Unclosed String: hoidlka",198))
    def test27(self):
        self.assertTrue(TestLexer.test(" \"vietnam\"s\" ","vietnam,s,Unclosed String:  ",199))

    def teste28(self):
        self.assertTrue(TestLexer.test("\"$ab_12\"\"\"\"","$ab_12,,Unclosed String: ",200))

    def test29(self):
        self.assertTrue(TestLexer.test("\"kali\nkakdjaskd\"","Unclosed String: kali",201))
