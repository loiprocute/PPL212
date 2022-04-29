//1914047
//jja
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

/** 
 * 2 Program Structure
 */


program: classes EOF ;
classes: class_declare class_declares ;
class_declares:class_declare class_declares|;
//2.1 class declaration 
class_declare : CLASS ID (COLON ID)? LP body RP ;

// body_class
body: body_class | ;
body_class : member body_classes;
body_classes: member body_classes |;
member :attribute_declare|method ;

//2.2 Attribute declaration
attribute_declare: varible SEMI;

varible: (VAL | VAR ) (vardecl | term COLON typ);

vardecl: (ID | Dollar_ID) CM vardecl CM  exp0 | 
			(ID | Dollar_ID)  COLON typ ASSIGN exp0 ;
term: (ID | Dollar_ID) CM term | (ID | Dollar_ID);
//2.3 Method declare
method :method_declare|destructor_declare|constructor_declare;
method_declare : (ID|Dollar_ID) LB list_IDs? RB block_stmt ;
destructor_declare : DESTRUC LB RB block_stmt ;
constructor_declare : CONSTRUC LB list_IDs? RB block_stmt ;

list_IDs:list_ID SEMI list_IDs|list_ID;
ids : ID CM ids |ID;
list_ID :ids COLON typ ;
/** 
 * 5 Expressions
 */



exp0 : exp1 ;
exp1: exp2 (STR_CAT | STR_CMP  ) exp2 | exp2 ;
exp2: exp3 ( EQ | NEQ | GT | LT | GE | LE ) exp3 | exp3;
exp3: exp3 ( AND | OR ) exp4 | exp4;
exp4: exp4 (ADD | SUB ) exp5 | exp5;
exp5: exp5 ( MUL | DIV | MOD) exp6 | exp6;
exp6: NOT  exp6 | exp7;
exp7: SUB exp7 | exp8;
exp8: exp8 index_operator | exp9;
exp9: exp9 DOT ID (LB list_param RB)? | exp10 ;
exp10 : ID ACCESS Dollar_ID (LB list_param RB)? | exp11;
exp11 : NEW ID LB list_param RB | operands ;


index_operator: LSB exp0 RSB index_operator|LSB exp0 RSB;
operands
	: literal
	| ID
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

//call_func: ID LB list_param RB;
list_param: param CM list_param
          | param
          | ;
param: literal | ID | exp0;

// Statement
// Declare var and const

varconst_declare: varible1 SEMI;

varible1: (VAL | VAR ) (vardecl1 | term1 COLON typ);

vardecl1: ID CM vardecl1 CM  exp0  | 
			ID COLON typ ASSIGN exp0 ;
term1: ID CM term1 | ID;	
// Assign statement
stmt_assign: exp0 ASSIGN exp0 SEMI;

// If statement
stmt_if: IF LB exp0 RB block_stmt stmt_elif;
stmt_elif: ELSEIF LB exp0 RB block_stmt stmt_elif
            | stmt_else|;
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
//stmt_call: call_func SEMI;

// Return statement
stmt_return: RETURN exp1? SEMI|RETURN NULL SEMI;


//Method Invocation statement
stmt_callMethod: member_access SEMI;

//Member access 
member_access : in_method | stt_method;
in_method : exp0 DOT ID LB list_param RB ;
stt_method: ID ACCESS Dollar_ID LB list_param RB ;


// Block statement
block_stmt: LP list_stmt  RP ;
list_stmt : stmt stmts| ;
stmts : stmt stmts|;

stmt: varconst_declare
	| stmt_if 
	| stmt_assign 
	| stmt_while
	| stmt_break
	| stmt_continue
	| stmt_callMethod
	| stmt_return
	| stmt_foreach
	| block_stmt;






/** Lexers Declaration */




/********************* LITERALS ***********************/
/* */
//integer
INT_LITERAL : (OCT | DEC | HEX | BIN ){ self.text = self.text.replace("_", "") } ;
fragment BIN: '0'('b'|'B')'1' ('_'?[01])*| ('0b0'|'0B0') ;
fragment OCT: '0' [1-7]('_'?[0-7])* | '00' ;
fragment DEC: [1-9] ('_'? [0-9])* | '0' ;
fragment HEX: '0' ('x'|'X') [1-9A-Fa-f] ('_'?[0-9A-Fa-f_])* | ('0x0'|'0X0') ;
//float .
FL_LITERAL:(DEC (FRACPART EXPPART? | EXPPART)) {self.text = self.text.replace("_", "")}| FRACPART EXPPART ;
fragment FRACPART: '.' DEC?;
fragment EXPPART: [eE] ('-'|'+')? DEC; 





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
//listLIT: (CM? (literal|exp0))* ;
listARRAY:(CM? array)* ;

listLIT: list_mem |;  
list_mem : exp0 listval;
listval : CM exp0 listval|;





/********************** TYPES  ************************/
typ :INTTYPE|FLOATTYPE|STRTYPE|BOOLTYPE|arraytype|ID;
INTTYPE: 'Int' ;
FLOATTYPE: 'Float';
STRTYPE: 'String';
BOOLTYPE: 'Boolean';
VOIDTYPE: 'Void' ;
arraytype: ARRAY LSB typ CM INT_LITERAL RSB ;
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
ID: ([a-zA-Z] | '_') ([a-zA-Z0-9] | '_')*;
Dollar_ID: '$' ([a-zA-Z0-9] | '_')+ ;

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


/********************* FRAGMENTS **********************/
fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;
fragment ESC_SEQ: '\\' [btnfr"'\\] ;
/*attri_method: var_method SEMI;

var_method: (VAL | VAR ) (vardecl_method | id_method CO (typ | ID));

vardecl_method: ID CM vardecl CM exp | ID CO (typ | ID) EQ exp;

id_method: ID CM id_method | ID; */