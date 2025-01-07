# Intèrpret de MiniScheme

## Visió General del Projecte
Aquest projecte implementa un intèrpret bàsic per al llenguatge de programació Scheme. Utilitza ANTLR per a l'anàlisi sintàctica i Python per a l'execució del codi Scheme. Aquesta és una implementació de [lp-mini-scheme](https://github.com/jordi-petit/lp-mini-scheme).




## Compilació i Execució

El projecte assumeix que ANTLR4 i python3 estan instal·lats

Per instal·lar ANTLR4

```bash
pip install antlr4-tools
antlr4
pip install antlr4-python3-runtime
```

### Compilar
```bash
make all
```

### Executar un fitxer

```bash
python3 Scheme.py <nom-del-fitxer>.scm
```

### Compilar i executar un fitxer

```bash
make run SCHEME_FILE=<nom-del-fitxer>.scm
```

## Jocs de Proves

Aquest projecte inclou una sèrie de tests per verificar la correcta funcionalitat de l'intèrpret. Els tests es troben al directori `tests/` i comencen amb `test_*.scm`.

### Executar Tests

Per executar tots els tests, utilitza la comanda següent:

```bash
make test
```

Aquesta comanda executarà tots els arxius de prova que comencen amb `test_*.scm` al directori `tests/`. Alguns tests poden tenir fitxers d'entrada corresponents amb l'extensió `.in`. Si aquests existeixen, seran redireccionats com a entrada a l'intèrpret.

## Detalls dels fitxers

### Components Principals

- **Scheme.g4**: Gramàtica d'ANTLR per al llenguatge Scheme.
- **SchemeLexer.py**: Lexer generat per ANTLR.
- **SchemeParser.py**: Parser generat per ANTLR.
- **SchemeVisitor.py**: Visitor generat per ANTLR.
- **EvalVisitor.py**: Implementació de l'intèrpret utilitzant el patró Visitor.
- **Scheme.py**: Script principal per executar l'intèrpret.
- **Makefile**: Fitxer de configuració per gestionar la compilació, execució i tests.
- **tests/**: Directori que conté els arxius de prova en Scheme.

### Detalls del Makefile

- **all**: Genera les classes del Lexer, Parser i Visitor utilitzant ANTLR.
- **clean**: Neteja els fitxers generats per ANTLR.
- **run**: Executa un arxiu Scheme especificat o el fitxer per defecte `test_principal.scm`.
- **test**: Executa tots els tests del directori `tests/`.
- **help**: Mostra les instruccions d'ús del Makefile.

### Jocs de prova
Hi ha diversos jocs de prova, tots tenen el seu ```.out``` per a comparar la sortida amb una correcta i els que ho requereixen tenen un ```.in```. El codi dels tests està documentat per a la seva comprensió.
- **test_principal.scm**: Prova de forma general l'intèrpret, mirant una mica totes les funcionalitats.
- **test_control.scm**: Prova el control de flux de l'intèrpret executant funcionalitats com if o cond.
- **test_functions.scm**: Declara i prova múltiples funcions, algunes d'alt nivell o recursives
- **test_higher_order.scm**: Posa a prova més a fons funcions d'alt nivell.
- **test_recursions**: Posa a prova més a fons funcions recursives.
- **test_lists**: Prova les declaracions de les llistes, el seu ús i també algunes de les seves funcions com ara car, cdr, cons i null.
- **test_operators**: Executa nombroses operacions amb operadors tant aritmètics com lògics.

## Depuració

Per activar el mode de depuració, s'ha de configurar la variable `debug` a `True` en la classe `EvalVisitor` dins de `EvalVisitor.py`. Això permetrà que l'intèrpret imprimeixi missatges addicionals durant l'execució, facilitant la identificació de problemes.

```python
class EvalVisitor(SchemeVisitor):
    def __init__(self):
        self.debug = True
        # ...
```


