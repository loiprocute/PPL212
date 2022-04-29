import unittest
from TestUtils import TestLexer
#8,28,31,37,92,93,99
class LexerSuite(unittest.TestCase):
    def test_identifier211(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("""abc?xyzb""","abc,Error Token ?",10))
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("$abc","$abc,<EOF>",101))
    def test_iden(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("?aCBbdc","aCBbdc,<EOF>",102))
    def test_identifier1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("aAsVN","aAsVN,<EOF>",103))
    def test_identifier2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("65460ASDE_1234","65460,ASDE_1234,<EOF>",104))
    def test_identifier4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc0123","abc0123,<EOF>",105))
    def test_identifier3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Abc0123","Abc0123,<EOF>",106))
    
    '''def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123123","123123,<EOF>",107))
    def test_integer1(self):
        """test integers"""
        self.assertTrue(TestLexer.test("1","1,<EOF>",108)) 
     
    def test_real(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("123e-10","123e-10,<EOF>",109))
    def test_real1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("123.2","123.2,<EOF>",110))
    def test_real2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("123.","123.,<EOF>",111))
    def test_real3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(".1",".1,<EOF>",112))
    def test_real4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1e2","1e2,<EOF>",113))
    def test_real5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1.e-2","1.e-2,<EOF>",114))
    def test_real6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1.E-2","1.E-2,<EOF>",115))
    def test_real7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("0.33E-2","0.33E-2,<EOF>",116))
    def test_real8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("123E-24","123E-24,<EOF>",117))
        
    def test_real9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("12_3E-24","123E-24,<EOF>",118))
    def test_real10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1.2_3E-24","1.23E-24,<EOF>",119))


    def test_bool(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("True","True,<EOF>",120))
    def test_bool1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("False_","False_,<EOF>",121))
    def test_bool2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("false","false,<EOF>",122))
    def test_string(self):
        """test string"""
        self.assertTrue(TestLexer.test('"string"','string,<EOF>',135))
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
        self.assertTrue(TestLexer.test("",'<EOF>',154))
    def test_string7(self):
        self.assertTrue(TestLexer.test("dakd da","dakd,da,<EOF>",157))
    def test_string8(self):
        self.assertTrue(TestLexer.test("if(true)","if,(,true,),<EOF>",158))
    def test_escape(self):
        self.assertTrue(TestLexer.test("hoid","hoid,<EOF>",159))
    def test_string9(self):
        self.assertTrue(TestLexer.test('"    \\t\\t\\n"','    \\t\\t\\n,<EOF>',160))
    def test_escape1(self):
        self.assertTrue(TestLexer.test("if 123continue","if,123,continue,<EOF>",161))
    def test_string2(self):
        self.assertTrue(TestLexer.test('"ngua nguoi\\n  b \\t"',"ngua nguoi\\n  b \\t,<EOF>",162))
    def test_escape8(self):
        self.assertTrue(TestLexer.test("kjakd\nqakd","kjakd,qakd,<EOF>",163))
    def test_escape3(self):
        self.assertTrue(TestLexer.test('"\\t"','\\t,<EOF>',164)) 


    def test_operator(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("+","+,<EOF>",122))
    def test_operator1(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("++","+,+,<EOF>",123))
    
    def test_operator2(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("*","*,<EOF>",124))
    def test_operator3(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("||||","||,||,<EOF>",125))
    def test_operator5(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("====","==,==,<EOF>",126))
    def test_operator4(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("===","==,=,<EOF>",127))
    def test_operator6(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("&&","&&,<EOF>",128))
    def test_operator7(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("=&&","=,&&,<EOF>",129))
    def test_operator13(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("=&&","=,&&,<EOF>",130))
    def test_operator8(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("=&&,","=,&&,,,<EOF>",131))
    def test_operator14(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("=&&=,","=,&&,=,,,<EOF>",132))
    def test_operator10(self):
        """test Operator"""
        self.assertTrue(TestLexer.test(",",",,<EOF>",133))
    def test_operator11(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("[=,]","[,=,,,],<EOF>",134))
    def test_operator12(self):
        """test Operator"""
        self.assertTrue(TestLexer.test(",,",",,,,<EOF>",135))
        
    def test_keyword(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("123continue","123,continue,<EOF>",141))
    def test_keyword1(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("123Break","123,Break,<EOF>",142))
    def test_keyword2(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("If","If,<EOF>",143))
    def test_keyword9(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("If1","If1,<EOF>",144))
    def test_keyword3(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("Return","Return,<EOF>",145))
    def test_keyword4(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("Do","Do,<EOF>",146))
    def test_keyword5(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("While","While,<EOF>",147))
    def test_keyword6(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("Continue","Continue,<EOF>",148))
    def test_keyword7(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("Break","Break,<EOF>",149))
    def test_keyword8(self):
        """test Operator"""
        self.assertTrue(TestLexer.test("Else","Else,<EOF>",150))
        
    def test_comment(self):
        self.assertTrue(TestLexer.test('##abc##','<EOF>',151))
    def test_comment1(self):
        self.assertTrue(TestLexer.test('##abc/**/##','<EOF>',152))
    def test_comment2(self):
        self.assertTrue(TestLexer.test('##/abc\n##12_3','123,<EOF>',153))
    def test_comment3(self):
        self.assertTrue(TestLexer.test('##/abc\r##90','90,<EOF>',155))
    def test_comment4(self):
        self.assertTrue(TestLexer.test('##abc\t90##','<EOF>',156))
    def test_comment5(self):
        self.assertTrue(TestLexer.test('##/abc\f90##','<EOF>',165))
    def test_comment6(self):
        self.assertTrue(TestLexer.test("##/*\r*/",'#,#,/,*,*,/,<EOF>',166))
    def test_comment7(self):
        self.assertTrue(TestLexer.test('##/*abc\f9\n0*/##','<EOF>',167))
    def test_comment8(self):
        self.assertTrue(TestLexer.test('1_243535','1243535,<EOF>',178))
        
    def test_escape12(self):
        self.assertTrue(TestLexer.test("hoidlka\n","hoidlka,<EOF>",169))
    def test_escape18(self):
        self.assertTrue(TestLexer.test('"hoidlka\\n"',"hoidlka\\n,<EOF>",170))
    def test_escape19(self):
        self.assertTrue(TestLexer.test("do {} while","do,{,},while,<EOF>",171))
    def test_escape100(self):
        self.assertTrue(TestLexer.test("if(a <= b) k = 7","if,(,a,<=,b,),k,=,7,<EOF>",172))
    def test_escape21(self):
        self.assertTrue(TestLexer.test("break;","break,;,<EOF>",154))
    def test_escape20(self):
        self.assertTrue(TestLexer.test("int[123];",'int,[,123,],;,<EOF>',172))
    def test_escape22(self):
        self.assertTrue(TestLexer.test('"hoidlka \\n"','hoidlka \\n,<EOF>',173))
    def test_escape23(self):
        self.assertTrue(TestLexer.test(" \"hoidlka\n \" ","Unclosed String: hoidlka",174))
    def test_escape27(self):
        self.assertTrue(TestLexer.test(" \"viemkhongquayve\"s\" ","viemkhongquayve,s,Unclosed String:  ",175))
    
    def test_string_escape26(self):
        self.assertTrue(TestLexer.test("\"Tran\"\"\"\"","Tran,,Unclosed String: ",176))
    
    def test_string_escape25(self):
        self.assertTrue(TestLexer.test("\"kadkjs\nkakdjaskd\"","Unclosed String: kadkjs",177))
    
    def test_string_escape24(self):
        self.assertTrue(TestLexer.test("\"unclose \t \"","Unclosed String: unclose ",178))
    def test_escape28(self):
        self.assertTrue(TestLexer.test('"hoidlka \\i"','Illegal Escape In String: hoidlka \i',179))
    def test_escape29(self):
        self.assertTrue(TestLexer.test('"hoidlka \\i kjdasd"','Illegal Escape In String: hoidlka \i',180))
    
    def test_string_escape30(self):
            self.assertTrue(TestLexer.test("\"unclose \n \"","Unclosed String: unclose ",181))
    def test_string_escape31(self):
        self.assertTrue(TestLexer.test('"kjdaksjd9123&((*(&&^("','kjdaksjd9123&((*(&&^(,<EOF>',182))
    def test_string_escape32(self):
        self.assertTrue(TestLexer.test('"kjdaksj d9123&((*(&&^("','kjdaksj d9123&((*(&&^(,<EOF>',183))
    def test_string_escape33(self):
        self.assertTrue(TestLexer.test('"kjdaksjd \\k9123&((*(&&^("','Illegal Escape In String: kjdaksjd \k',184))
    def test_string_escape34(self):
        self.assertTrue(TestLexer.test('"kjdaksj \\n kjkad"','kjdaksj \\n kjkad,<EOF>',185))
    def test_string_escape36(self):
        self.assertTrue(TestLexer.test('"kjdaksj \\f kjkad"',"kjdaksj \\f kjkad,<EOF>",186))
    def test_string_escape37(self):
        self.assertTrue(TestLexer.test('"^"','^,<EOF>',187))
    def test_string_escape38(self):
        self.assertTrue(TestLexer.test("^",'Error Token ^',188))
    def test_string_escape100(self):
        self.assertTrue(TestLexer.test("^%^&*",'Error Token ^',189))
    def test_string_escape39(self):
        self.assertTrue(TestLexer.test("if else do while 1234return break1e-2",'if,else,do,while,1234,return,break1e,-,2,<EOF>',190))
    def test_ereal100(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("123E24","123E24,<EOF>",191))
    def test_identifier6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("aAs[VN","aAs,[,VN,<EOF>",192))
    def test_identifier7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("aAs[=,VN","aAs,[,=,,,VN,<EOF>",193))
    def test_identifier8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("aAs[<=VN","aAs,[,<=,VN,<EOF>",194))
    def test_identifier8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("aAs[<=VN","aAs,[,<=,VN,<EOF>",195))
    def test_identifier9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(";aAs[<=VN",";,aAs,[,<=,VN,<EOF>",196))
    def test_identifier10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(";stringaAs[<=VN",";,stringaAs,[,<=,VN,<EOF>",197))
    def test_identifier11(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("21 e-10","21,e-10,<EOF>",198))
    def test_identifier12(self):
        """test identifiers"""
        input = r""" "kajd
            lad" """;
        self.assertTrue(TestLexer.test(input,"Unclosed String: kajd",199))
    def test_identifier13(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("int [132]","int,[,132,],<EOF>",200))'''
    