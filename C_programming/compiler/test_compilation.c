#include <stdio.h>

int main() {
    int n;
    printf("Fibonacci index: ");
	scanf("%d", &n);
    int temp;
    int t1 = 0;
    int t2 = 1;
    for (int i = 2; i < n; i++) {
        temp = t1 + t2;
        t1 = t2;
        t2 = temp;
        i++;
    }
    printf("The %d'th element of the fibonacci sequence is %d.\n", n, t2);
    return 0;
}

/*
    <functionDeclaration> ::= <type> <identifier> '(' <declaredArgs>? ')' '{' <statements> '}'
    <type> ::= 'int' | 'char' | 'boolean' | 'void'
    <identifier> ::= [a-zA-Z_][a-zA-Z0-9_]*
    <declaredArgs> ::= <type> <identifier> (',' <type> <identifier>)*
    <statements> (<ifStatement> | <whileStatement> | <doStatement> | <forStatement> | <returnStatement> | <varDeclaration> | <assignment> | <functionCall>)*
    <ifStatement> ::= 'if' '(' <expression> ')' '{' <statements> '}' <elsifStatement>+ <elseStatement>?
    <expression> ::= (unaryOp expression) | (expression binaryOp expression) | term
    <unaryOp> ::= '!' | '~'
    <binaryOp> ::= <conditionalOp> | '+' | '-' | '*' | '/' | '&&' | '||' | '&' | '|' | '^' | '<<' | '>>'
    <conditionalOp> ::= '==' | '!=' | '<' | '>' | '<=' | '>='
    <term> ::= <identifier> | <intConst> | 'null' | 'true' | 'false'
    <intConst> ::= [0-9]*
    <elsifStatement> ::= 'elsif' '(' <expression> ')' '{' <statements> '}'
    <elseStatement> ::= 'else' '{' <statements> '}' 
    <whileStatement> ::= 'while' '(' <expression> ')' '{' <statements> '}'
    <doWhileStatement> ::= 'do' '{' <statements> '}' 'while' '(' <expression> ')'
    <forStatement> ::= 'for' '(' <forExpression> ')' '{' <statements> '}'
    <forExpression> ::= <assignment> <conditionalTerm> ';' <assignment>
    <conditionalTerm> ::= <term> <conditionalOp> <term>
    <returnStatement> ::= return (<intConst> | 'null') ';'
    <varDeclaration> ::= <type> <identifier>;
    <assignment> ::= <type> <identifier> '=' (<expression> | <strConst>) ';'
    <strConst> ::= ^[\s!#-~]+$
    <functionCall> ::= <identifier> '(' <passedArgs> ')';
    <passedArgs> ::= (<passedArg> (',' <passedArg>)*)?
    <passedArg> ::= <identifier> | <strConst> | <intConst> | 'null'
*/