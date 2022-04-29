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
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);

    else:
        return super().emit();
}

/** 
 * 2 Program Structure
 */

program: class_declare+ EOF ;
//2.1 class declaration 

class_declare : CLASS ID (COLON ID)? LP body_class RP ;

// body_class
body_class : code_list ;
code_list : (attribute_declare|method)* ;

//2.2 Attribute declaration
attribute_declare :  (VAL|VAR) list_ID  (ASSIGN values_list)? SEMI ;
values_list : (','? (exp0|member_access))+ ;  

//2.3 Method declare
method :method_declare|destructor_declare|constructor_declare;
method_declare : (ID|Dollar_ID) LB list_IDs? RB block_stmt ;
destructor_declare : DESTRUC LB RB block_stmt ;
constructor_declare : CONSTRUC LB list_IDs? RB block_stmt ;


list_ID : (CM? (ID|Dollar_ID))+ COLON (TYPE|ID);
list_dollar_ID: (','? Dollar_ID)+ COLON (TYPE|ID);
list_IDs: (';'? list_ID)+ ;

/** 
 * 5 Expressions
 */



exp0 : exp1 | array ;
exp1: exp2 (STR_CAT | STR_CMP  ) exp2 | exp2 ;
exp2: exp3 ( EQ | NEQ | GT | LT | GE | LE ) exp3 | exp3;
exp3: exp3 ( AND | OR ) exp4 | exp4;
exp4: exp4 (ADD | SUB ) exp5 | exp5;
exp5: exp5 ( MUL | DIV | MOD) exp6 | exp6;
exp6:  NOT  exp6 | exp7;
exp7: SUB exp7 | exp8;
exp8: exp8 index_operator | exp9;
exp9: exp9 DOT exp10 | exp10 ;
exp10 : exp11 ACCESS Dollar_ID (LB list_exp RB)? | exp11;
exp11 : NEW exp11 | operands ;

index_operator: LSB exp1 RSB
              | LSB exp1 RSB index_operator;
//(LB list_exp RP)?
operands
	: literal
	| ID
	| call_func
	| LB exp0 RB
	| SELF
	;

literal
	: INT_LITERAL
	| FL_LITERAL
	| STRING_LITERAL
	| BOOL_LITERAL
	| array
	;


call_func: ID LB params_list? RB;
params_list: param (CM? param)* ;
param: literal | ID | exp0;

//Member access 
member_access : in_att | stt_att | in_method | stt_method;
in_att : exp0 DOT ID ;
in_method : exp0 DOT ID LB list_exp RB ;
stt_att: ID ACCESS Dollar_ID ;
stt_method: ID ACCESS Dollar_ID LB list_exp RB ;
//New
new_epx : NEW ID LP list_exp RP;
list_exp : exp0? (CM exp0)*;



// Statement
// Declare var and const
varconst_declare :  (VAL|VAR) list_ID  (ASSIGN values_list)? SEMI ;
// Assign statement
stmt_assign: lhs ASSIGN exp0 SEMI;
lhs: ID | exp7;

// If statement
stmt_if: IF LB exp0 RB block_stmt stmt_elif stmt_else;
stmt_elif: ELSEIF LB exp0 RB block_stmt stmt_elif
            | ;
stmt_else: ELSE block_stmt
            |;
//For/In statement
stmt_foreach : FOREACH LB ID IN exp0 '..' exp0 (BY exp0)? RB block_stmt;
// While statement
stmt_while: WHILE LB exp0 RB block_stmt;

// Break statement
stmt_break: BREAK SEMI;

// Continue statement
stmt_continue: CONTINUE SEMI;

// Call statement
stmt_call: call_func SEMI;

// Return statement
stmt_return: RETURN exp1? SEMI;


//Method Invocation statement
stmt_callMethod: ID ACCESS stmt_call;

// Block statement
block_stmt: LP stmt*  RP ;
stmt: varconst_declare
	| stmt_if 
	| stmt_assign 
	| stmt_while
	| stmt_break
	| stmt_continue
	| stmt_callMethod
	| stmt_call
	| stmt_return
	| stmt_foreach
	| member_access SEMI;





/** Lexers Declaration */




/********************* LITERALS ***********************/
//integer
INT_LITERAL : (OCT | DEC | HEX | BIN ){ self.text = self.text.replace("_", "") } ;
fragment OCT: '0'[0-7_]+;
fragment DEC: [1-9] [_0-9]*| '0' ;
fragment HEX: '0'('x'|'X')[0-9A-Fa-f_]+;
fragment BIN: '0'('b'|'B')('0' | '1' | '_')+;

//float .
FL_LITERAL:(DEC (FRACPART EXPPART? | EXPPART)) {self.text = self.text.replace("_", "")}| FRACPART EXPPART ;
fragment FRACPART: '.' DEC?;
fragment EXPPART: [eE] '-'? DEC; 





//bool
BOOL_LITERAL: TRUE | FALSE;
//string
STRING_LITERAL: '"' STR_CHAR* '"'
	{
		y = str(self.text)
		self.text = y[1:-1]
	}
	;

//array

array: i_array | m_array;
// Indexed Array
i_array: ARRAY LB listLIT RB;
// Multi-dimensional arrays
m_array: ARRAY LB listARRAY RB;
listLIT: (CM? (literal|exp0))* ;
listARRAY:(CM? array)* ;
/********************** TYPES  ************************/
TYPE :INTTYPE|FLOATTYPE|STRTYPE|BOOLTYPE|ARRAYTYPE;
INTTYPE: 'Int' ;
FLOATTYPE: 'Float';
STRTYPE: 'String';
BOOLTYPE: 'Boolean';
VOIDTYPE: 'Void' ;
ARRAYTYPE: ARRAY LSB TYPE CM INT_LITERAL RSB ;
/********************* KEY WORDS **********************/
CLASS : 'Class' ; 
VAL : 'Val' ;
VAR : 'Var' ;
BREAK : 'Break' ;
FOREACH : 'Foreach' ;
NULL : 'Null' ;
CONSTRUC : 'Constructor' ;
DESTRUC : 'Destructor' ;
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
WHILE : 'While' ;
ARRAY : 'Array' ;
SELF : 'Self' ;
/********************** COMMENT ***********************/

BLOCK_COMMENT: ('##' .*? '##' ) -> skip ;

/******************** IDENTIFIERS *********************/
ID:	[_a-zA-Z] [_a-zA-Z0-9]*;
Dollar_ID:'$'[_a-zA-Z] [_a-zA-Z0-9]*;
//ID: [a-zA-Z]+;

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
ACCESS : '::' ;
STR_CMP: '==.'; 
STR_CAT: '+.';
/*********************** SKIP *************************/




WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


UNTERMINATED_COMMENT: .;


/********************* FRAGMENTS **********************/
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
fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;

fragment ESC_SEQ: '\\' [btnfr"'\\] ;
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;
ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;
