grammar StoreDSL;

start: program EOF;

program: statement*;

statement
    : define
    | create
    | delete
    | update
    | list
    | discount
    ;

define
    : 'define' '{'
        'entity' ':' entityName ','
        'attributes' '{' attribute (',' attribute)* '}'
      '}';

create
    : 'create' '{'
        'entity' ':' entityName ','
        'attributes' '{' keyValuePair (',' keyValuePair)* '}'
      '}';

delete
    : 'delete' '{'
        'entity' ':' entityName ','
        'attributes' '{' keyValuePair '}'
      '}';

update
    : 'update' '{'
        'entity' ':' entityName ','
        'attributes' '{' keyValuePair (',' keyValuePair)* '}'
      '}';

list
    : 'list' '{'
        'entity' ':' entityName
      '}';

discount
    : 'discount' '{'
        'entity' ':' entityName ','
        'attributes' '{' keyValuePair ',' 'discount_value' ':' value '}'
      '}';

attribute
    : name ':' type;

keyValuePairs
    : '{' keyValuePair (',' keyValuePair)* '}';

keyValuePair
    : name ':' value;

name
    : ID;

type
    : 'String' | 'Integer' | 'Float';

value
    : STRING | INT | FLOAT;

entityName
    : ID;

STRING: '"' (ESC | .)*? '"';
FLOAT: DIGIT+ '.' DIGIT* | DIGIT* '.' DIGIT+;
INT: DIGIT+;
ID: LETTER (LETTER | DIGIT | '_')*;

fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];
fragment ESC: '\\"' | '\\\\';

COMMENT: ('//'.*?'\n' | '/*'.*?'*/');
WS: [ \t\r\n]+ -> skip;
NEWLINE: ('\n' | '\r\n' | '\r') -> skip;
