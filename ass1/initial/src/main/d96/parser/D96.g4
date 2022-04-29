grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}
/** 
 * 2 Program Structure
 */


//2.1 class declaration 

class_declare : CLASS ID (COLON ID)? LP body_class RP ;

// body_class
body_class : code_list ;
code_list : (attribute_declare)+ ;

//2.2 Attribute declaration
attribute_declare : VAL ID COLON data_types '=' values_list SEMI 
					| VAR ID COLON data_types '=' values_list SEMI;
data_types	: INTLIT|FLOATTYPE|STRTYPE|BOOLTYPE;
values_list : (','? (Digit | Digit ADD Digit))+ ;  

//2.3 Method declare
//method_declare : ;



/*******************************************/
program: mptype 'main' LB RB LP body? RP EOF;

mptype: INTTYPE | VOIDTYPE;

body: funcall SEMI;

exp: funcall | INTLIT;

funcall: ID LB exp? RB;

/*******************************************/



/** Lexers Declaration */

/**
 * Keywords
 */






/********************* FRAGMENTS **********************/
fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;

fragment ESC_SEQ: '\\' [btnfr"'\\] ;


/********************* LITERALS ***********************/

//integer
INT_LITERAL     :  Dec | Bin | Otc| Hex { seft.text = seft.text.replace("_", "") } ;
Dec  :  Nonzerodigit (Digit )* | '0'+ ('0')* ;
Bin   :  '0' ('b' | 'B') (Bindigit)+ ;
Hex  : 	'0' ('x' | 'X') (Hexdigit)+ ;
Otc  :  '0' (Octdigit)+ ;
Nonzerodigit :  [1-9]; 
Digit        :  [0-9]; 
Bindigit     :  '0' | '1' ;  
Octdigit     : [0-7] ;
Hexdigit     : Digit | [a-f] | [A-F] ;

//float

FL_LITERAL: INTLIT (FRACPART EXPPART? | EXPPART) { self.text = self.text.replace("_", "") } ;
FRACPART: '.' [0-9]+;
EXPPART: ('e' | 'E') '-'? [0-9]+;

//bool
BOOL_LITERAL: TRUE | FALSE;
//string
STRING_LITERAL: '"' STR_CHAR* '"'
	{
		y = str(self.text)
		self.text = y[1:-1]
	}
	;

//Array
 
array : ARRAY LP params_list_sametype RP ;
params_list_sametype :   (CM? INT_LITERAL)+ 
						|(CM? FL_LITERAL)+
						|(CM? STRING_LITERAL)+
						|(CM? BOOL_LITERAL)+
						;

//Multi-dimensional arrays arrays
multi_array : ARRAY LP arrays RP ;
arrays : (CM? array)+ ;


/** 
 * 5 Expressions
 */

exp_bool: exp1;

exp_int: exp1;

exp_real: exp1;

exp_str: exp1;

// exp
// 	: operands
// 	| <assoc=right> (NOT | SUB) exp
// 	| exp ( DIV | MUL | MOD | DIV_INT | AND ) exp
// 	| exp ( ADD | SUB | OR ) exp
// 	| operands ( EQ | NEQ | GT | LT | GTE | LTE ) operands
// 	| exp ( op_and_then | op_or_else ) exp
// 	;


exp1: exp2 ( EQ | NEQ | GT | LT | GE | LE ) exp2 | exp2 ;

exp2: exp2 ( ADD | SUB | OR ) exp3 | exp3;

exp3: exp3 ( DIV | MUL | MOD | AND ) exp4 | exp4;

exp4: (NOT | SUB) exp4 | operands ;


operands
	: literal
	| ID
	| call_exp
	| LP exp RP
	;

literal
	: INT_LITERAL
	| FL_LITERAL
	| STRING_LITERAL
	| BOOL_LITERAL
	| array
	;


call_exp: ID LB params_list? RB;
params_list: literal (CM? literal) ;

/********************** TYPES  ************************/
INTTYPE: 'Int' ;
FLOATTYPE: 'Float';
STRTYPE: 'String';
BOOLTYPE: 'Boolean';
VOIDTYPE: 'Void' ;

/********************* KEY WORDS **********************/
CLASS : 'class' ; 
VAL : 'Val' ;
VAR : 'Var' ;
BREAK : 'Break' ;
FOREACH : 'Foreach ' ;
NULL : 'Null' ;
CONSTRUC : 'Constructor' ;
DESTRUC : ' Destructor' ;
CONTINUE : 'Continue' ;
TRUE : 'True' ;
IF : 'If' ;
FALSE : 'False' ;
NEW : 'New' ;
ELSE: 'Else' ;
ELSEIF : 'Elseif' ;
BY : 'By' ;
RETURN: 'Return' ;
IN : 'In' ;

ARRAY : 'Array' ;

/********************** COMMENT ***********************/

BLOCK_COMMENT: ('##' .*? '##' ) -> skip ;

/******************** IDENTIFIERS *********************/
ID:  '$'?[_a-zA-Z] [_a-zA-Z0-9]*;
//ID: [a-zA-Z]+;

INTLIT: [0-9]+;

/******************** SEPARATORS **********************/
LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

COLON: ':'; // Colon

CM: ',';

LSB: '['; // Left Square Bracket

RSB: ']'; // Right Square Bracket
/********************* OPERATORS **********************/
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
OR: '||';
AND: '&&';
NEQ: '!=';
EQ: '==';
ASSIGN: '=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
DOT: '.';
COMPARE_STRINGS: '==.';
CONCATENATE_STRINGS :  '+.';
ACCESS : '::' ;

/*********************** SKIP *************************/




WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	;
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;

fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;
ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;
UNTERMINATED_COMMENT: .;