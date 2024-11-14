
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left+-CONCATleft*/ALEATORIO CONCAT ENTRADA ESCREVER FIM FOLD FUNCAO LIST MAP NEG NUM STRING VARstart : statement\n                 | expressionstatement : VAR "=" expression ";"statement : expression ";"statement : ESCREVER "(" expression ")" ";"\n                     | ESCREVER "(" STRING ")" ";"\n                     | ESCREVER "(" VAR ")" ";"expression : expression \'+\' expression\n                      | expression \'-\' expression\n                      | expression \'*\' expression\n                      | expression \'/\' expressionexpression : expression CONCAT expressionexpression : "(" expression ")"expression : NUMexpression : VARexpression : STRINGexpression : LISTexpression : ENTRADA "(" ")"expression : ALEATORIO "(" NUM ")"\n                      | ALEATORIO "(" VAR ")"expression : FUNCAO VAR "(" params ")" "," ":" expression ";"params : VAR\n                  | VAR "," paramsexpression : VAR "(" arguments ")"arguments : expression\n                     | expression "," argumentsexpression : NEG "(" expression ")" ";"\n                    | NEG "(" VAR ")" ";"\n                    | NEG "(" NUM ")" ";"'
    
_lr_action_items = {'VAR':([0,6,12,15,16,17,18,19,20,21,22,26,28,44,50,65,72,],[4,24,27,24,24,24,24,24,24,24,39,43,46,56,24,56,24,]),'ESCREVER':([0,],[5,]),'(':([0,4,5,6,10,11,13,15,16,17,18,19,20,21,22,24,27,28,39,46,50,72,],[6,21,22,6,25,26,28,6,6,6,6,6,6,6,6,21,44,6,21,21,6,6,]),'NUM':([0,6,15,16,17,18,19,20,21,22,26,28,50,72,],[8,8,8,8,8,8,8,8,8,8,42,47,8,8,]),'STRING':([0,6,15,16,17,18,19,20,21,22,28,50,72,],[7,7,7,7,7,7,7,7,7,38,7,7,7,]),'LIST':([0,6,15,16,17,18,19,20,21,22,28,50,72,],[9,9,9,9,9,9,9,9,9,9,9,9,9,]),'ENTRADA':([0,6,15,16,17,18,19,20,21,22,28,50,72,],[10,10,10,10,10,10,10,10,10,10,10,10,10,]),'ALEATORIO':([0,6,15,16,17,18,19,20,21,22,28,50,72,],[11,11,11,11,11,11,11,11,11,11,11,11,11,]),'FUNCAO':([0,6,15,16,17,18,19,20,21,22,28,50,72,],[12,12,12,12,12,12,12,12,12,12,12,12,12,]),'NEG':([0,6,15,16,17,18,19,20,21,22,28,50,72,],[13,13,13,13,13,13,13,13,13,13,13,13,13,]),'$end':([1,2,3,4,7,8,9,14,24,29,30,31,32,33,40,41,48,49,54,55,62,63,64,67,68,69,74,],[0,-1,-2,-15,-16,-14,-17,-4,-15,-8,-9,-10,-11,-12,-13,-18,-3,-24,-19,-20,-5,-6,-7,-27,-28,-29,-21,]),';':([3,4,7,8,9,24,29,30,31,32,33,34,40,41,49,51,52,53,54,55,58,59,60,67,68,69,73,74,],[14,-15,-16,-14,-17,-15,-8,-9,-10,-11,-12,48,-13,-18,-24,62,63,64,-19,-20,67,68,69,-27,-28,-29,74,-21,]),'+':([3,4,7,8,9,23,24,29,30,31,32,33,34,36,37,38,39,40,41,45,46,47,49,54,55,67,68,69,73,74,],[15,-15,-16,-14,-17,15,-15,-8,-9,-10,-11,-12,15,15,15,-16,-15,-13,-18,15,-15,-14,-24,-19,-20,-27,-28,-29,15,-21,]),'-':([3,4,7,8,9,23,24,29,30,31,32,33,34,36,37,38,39,40,41,45,46,47,49,54,55,67,68,69,73,74,],[16,-15,-16,-14,-17,16,-15,-8,-9,-10,-11,-12,16,16,16,-16,-15,-13,-18,16,-15,-14,-24,-19,-20,-27,-28,-29,16,-21,]),'*':([3,4,7,8,9,23,24,29,30,31,32,33,34,36,37,38,39,40,41,45,46,47,49,54,55,67,68,69,73,74,],[17,-15,-16,-14,-17,17,-15,17,17,-10,-11,17,17,17,17,-16,-15,-13,-18,17,-15,-14,-24,-19,-20,-27,-28,-29,17,-21,]),'/':([3,4,7,8,9,23,24,29,30,31,32,33,34,36,37,38,39,40,41,45,46,47,49,54,55,67,68,69,73,74,],[18,-15,-16,-14,-17,18,-15,18,18,-10,-11,18,18,18,18,-16,-15,-13,-18,18,-15,-14,-24,-19,-20,-27,-28,-29,18,-21,]),'CONCAT':([3,4,7,8,9,23,24,29,30,31,32,33,34,36,37,38,39,40,41,45,46,47,49,54,55,67,68,69,73,74,],[19,-15,-16,-14,-17,19,-15,-8,-9,-10,-11,-12,19,19,19,-16,-15,-13,-18,19,-15,-14,-24,-19,-20,-27,-28,-29,19,-21,]),'=':([4,],[20,]),')':([7,8,9,23,24,25,29,30,31,32,33,35,36,37,38,39,40,41,42,43,45,46,47,49,54,55,56,57,61,67,68,69,70,74,],[-16,-14,-17,40,-15,41,-8,-9,-10,-11,-12,49,-25,51,52,53,-13,-18,54,55,58,59,60,-24,-19,-20,-22,66,-26,-27,-28,-29,-23,-21,]),',':([7,8,9,24,29,30,31,32,33,36,40,41,49,54,55,56,66,67,68,69,74,],[-16,-14,-17,-15,-8,-9,-10,-11,-12,50,-13,-18,-24,-19,-20,65,71,-27,-28,-29,-21,]),':':([71,],[72,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'statement':([0,],[2,]),'expression':([0,6,15,16,17,18,19,20,21,22,28,50,72,],[3,23,29,30,31,32,33,34,36,37,45,36,73,]),'arguments':([21,50,],[35,61,]),'params':([44,65,],[57,70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> statement','start',1,'p_start','grammar.py',29),
  ('start -> expression','start',1,'p_start','grammar.py',30),
  ('statement -> VAR = expression ;','statement',4,'p_statement_assign','grammar.py',34),
  ('statement -> expression ;','statement',2,'p_statement_expr','grammar.py',38),
  ('statement -> ESCREVER ( expression ) ;','statement',5,'p_statement_write','grammar.py',42),
  ('statement -> ESCREVER ( STRING ) ;','statement',5,'p_statement_write','grammar.py',43),
  ('statement -> ESCREVER ( VAR ) ;','statement',5,'p_statement_write','grammar.py',44),
  ('expression -> expression + expression','expression',3,'p_expression_binop','grammar.py',48),
  ('expression -> expression - expression','expression',3,'p_expression_binop','grammar.py',49),
  ('expression -> expression * expression','expression',3,'p_expression_binop','grammar.py',50),
  ('expression -> expression / expression','expression',3,'p_expression_binop','grammar.py',51),
  ('expression -> expression CONCAT expression','expression',3,'p_expression_concat','grammar.py',55),
  ('expression -> ( expression )','expression',3,'p_expression_group','grammar.py',59),
  ('expression -> NUM','expression',1,'p_expression_num','grammar.py',63),
  ('expression -> VAR','expression',1,'p_expression_var','grammar.py',67),
  ('expression -> STRING','expression',1,'p_expression_string','grammar.py',71),
  ('expression -> LIST','expression',1,'p_expression_list','grammar.py',75),
  ('expression -> ENTRADA ( )','expression',3,'p_expression_entrada','grammar.py',79),
  ('expression -> ALEATORIO ( NUM )','expression',4,'p_expression_aleatorio','grammar.py',83),
  ('expression -> ALEATORIO ( VAR )','expression',4,'p_expression_aleatorio','grammar.py',84),
  ('expression -> FUNCAO VAR ( params ) , : expression ;','expression',9,'p_expression_function','grammar.py',88),
  ('params -> VAR','params',1,'p_params','grammar.py',92),
  ('params -> VAR , params','params',3,'p_params','grammar.py',93),
  ('expression -> VAR ( arguments )','expression',4,'p_expression_func_call','grammar.py',100),
  ('arguments -> expression','arguments',1,'p_arguments','grammar.py',104),
  ('arguments -> expression , arguments','arguments',3,'p_arguments','grammar.py',105),
  ('expression -> NEG ( expression ) ;','expression',5,'p_expression_neg','grammar.py',112),
  ('expression -> NEG ( VAR ) ;','expression',5,'p_expression_neg','grammar.py',113),
  ('expression -> NEG ( NUM ) ;','expression',5,'p_expression_neg','grammar.py',114),
]