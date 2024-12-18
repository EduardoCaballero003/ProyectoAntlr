grammar grammarcode;

// Reglas léxicas
INICIO: 'Inicio';
TERMINAR: 'Terminar';
ESCRIBE: 'Escribe';
LEE: 'Lee';
EN: 'en';
SI: 'SI';
SINO: 'SINO';
HACER: 'Hacer';
FIN: 'Fin';
REPETIR: 'Repetir';
VECES: 'veces';
MIENTRAS: 'Mientras';
ENTERO: 'entero';
DECIMAL: 'decimal';
PALABRA: 'palabra';
ESVERDAD: 'esVerdad';
ARREGLO: 'Arreglo';
REGRESAR: 'regresar';
RECIPE: 'Receta';
MAS: 'mas';
MENOS: 'menos';
POR: 'por';
ENTRE: 'entre';
POTENCIA: 'potencia';
RAIZ: 'raiz';
RESIDUO: 'sobrante';
AGREGA:'Agregar';
AGREGAEN: 'Agregar-en';
ELIMINA:'Elimina';
ELIMINAEN:'Elimina-en';
VOLTEAR: 'Voltear';
ULTIMO: 'Ultimo';
IDENTIFIER: [a-zA-Z][a-zA-Z0-9]* ('[' [0-9]+ (':' [0-9]+)? ']')?;
NUMBER: [0-9]+;
DECIMAL_NUMBER: [0-9]+ '.' [0-9]+; // Números con punto decimal
STRING: ('"' (~["\\] | '\\' .)* '"') | ('\'' (~['\\] | '\\' .)* '\''); // Cadena entre comillas
BOOLEAN_TRUE: 'si'; // Valores booleanos "verdadero" o "si"
BOOLEAN_FALSE: 'no'; // Valores booleanos "falso" o "no"
WS: [ \t\r\n]+ -> skip; // Ignorar espacios en blanco
LPAREN: '(';
RPAREN: ')';
ARROW: '->';
COMMA: ',';
POINT:'.';
LESS: '<';
GREATER: '>';
LEQ: '<=';
GEQ: '>=';
EQ: '==';
NEQ: '!=';
LBRACKET: '[';
RBRACKET: ']';

// Reglas sintácticas
program: (inicioBloque | statement)*;

inicioBloque: INICIO LPAREN RPAREN statement+ TERMINAR;

statement: asignacion
         | igualacion
         | ciclo
         | condicional
         | definicionFuncion
         | llamadaFuncion
         | printStatement
         | entrada
         | declaraArr
         | operationArr;

asignacion: tipo IDENTIFIER ARROW expression;

igualacion: IDENTIFIER ARROW expression;

tipo: ENTERO | DECIMAL | PALABRA | ESVERDAD;

expression: expression MAS expression
          | expression MENOS expression
          | expression POR expression
          | expression ENTRE expression
          | expression POTENCIA expression
          | expression RESIDUO expression
          | expression RAIZ expression
          | IDENTIFIER
          | valor
          | llamarMetodo
          | llamadaFuncion;

valor: DECIMAL_NUMBER
     | NUMBER
     | STRING
     | BOOLEAN_TRUE
     | BOOLEAN_FALSE;

declaraArr: ARREGLO tipo IDENTIFIER ARROW (IDENTIFIER | LBRACKET arguments* RBRACKET);

posiblesOper: AGREGA | ELIMINA | ELIMINAEN | AGREGAEN | VOLTEAR;
operationArr: IDENTIFIER POINT posiblesOper LPAREN arguments* RPAREN;

llamarMetodo: IDENTIFIER POINT (IDENTIFIER | VOLTEAR | ULTIMO) LPAREN arguments? RPAREN;

ciclo: repetirCiclo | mientrasCiclo;

repetirCiclo: REPETIR NUMBER VECES HACER statement+ FIN;

mientrasCiclo: MIENTRAS LPAREN condition RPAREN HACER statement+ FIN;

condicional: SI LPAREN condition RPAREN HACER statement+ FIN condicionalelse?;

condicionalelse: (SINO HACER statement+ FIN);

condition: expression (LESS | GREATER | LEQ | GEQ | EQ | NEQ) expression;

definicionFuncion: RECIPE IDENTIFIER LPAREN parameters? RPAREN HACER statement+ returnStatement? FIN;
returnStatement: REGRESAR expression;

parameters: tipo IDENTIFIER (COMMA tipo IDENTIFIER)*;

llamadaFuncion: IDENTIFIER LPAREN arguments? RPAREN;

arguments: expression (COMMA expression)*;

printStatement: ESCRIBE LPAREN arguments RPAREN;

entrada : LEE LPAREN STRING RPAREN EN tipo IDENTIFIER;
