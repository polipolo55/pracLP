grammar Scheme;

program: expression+ EOF;

expression
    : arithmeticOperation           #ArOperation
    | booleanOperation              #BoOperatio
    | NUMBER                        #Num
    | STRING                        #Str
    | TRUE                          #True
    | FALSE                         #False
    | IDENTIFIER                    #Id
    | '\''? '(' expression* ')'     #calls
    ;

arithmeticOperation
    : ('*' | '/' | '+' | '-')
    ;

booleanOperation
    : ('>=' | '<=' | '=' | '<>' | '>' | '<' )
    ;

TRUE: '#t';
FALSE: '#f';
STRING: '"' ~["\r\n]* '"';
IDENTIFIER: [a-zA-Z_?][a-zA-Z0-9_?]*;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;
COMMENT: ';' ~[\r\n]* -> skip;