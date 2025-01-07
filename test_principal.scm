(define (suma x y) 
    (+ x y))

(define (saluda)
    (display "Hola")
    (newline))

(define cinc 5)

(define (suma-llista llista)
  (if (null? llista)
      0
      (+ (car llista) (suma-llista (cdr llista)))))

(define (sumar-dos-valors)
  (display "Introdueix dos valors: ")
  (let ((val1 (read))
        (val2 (read)))
    (display "La suma és: ")
    (display (+ val1 val2))
    (newline)))

(define llista '(1 2 3 4 5))
(define llista2 '(12 10 3))

(define (main)
  ;; Introducció
  (display "Hola món, sóc el main")
  (newline)

  (display "hola")
  (newline)
  (display "Suma de 2 i 3: ")
  (display (+ 2 3))
  (newline)
  (display "Comparació de 5 > 3: ")
  (display (> 5 3))
  (newline)

  ;; Definició de funció
  (display "Prova de la definició de funció 'suma':")
  (newline)
  (display (suma 3 4))
  (newline)

  ;; Definició de funció sense paràmetres
  (display "Prova de la definició de funció 'saluda':")
  (newline)
  (saluda)
  (newline)

  ;; Definició de variable
  (display "Prova de la definició de la variable 'cinc':")
  (newline)
  (display (suma cinc 3))
  (newline)

  ;; If
  (display "Prova de l'if amb condició (< 3 2):")
  (newline)
  (display (if (< 3 2) "tres és menor que dos" "tres no és menor que dos"))
  (newline)

  ;; Cond
  (display "Prova del cond amb diverses condicions:")
  (newline)
  (display 
    (cond
      ((> 3 5) "major")
      ((< 3 5) "menor")
      (#t "igual")))
  (newline)

  ;; Llistes
  (display "Prova de les llistes 'llista' i 'llista2':")
  (newline)
  (display llista)
  (newline)
  (display llista2)
  (newline)
  (display "Car de 'llista': ")
  (display (car llista))
  (newline)
  (display "Cdr de 'llista': ")
  (display (cdr llista))
  (newline)
  (display "Cons de 0 a 'llista': ")
  (display (cons 0 llista))
  (newline)
  (display "Null? de '()': ")
  (display (null? '()))
  (newline)
  (display "Null? de 'llista': ")
  (display (null? llista))
  (newline)

  ;; Recursivitat
  (display "Prova de la recursivitat amb 'suma-llista' a 'llista2':")
  (newline)
  (display (suma-llista llista2))
  (newline)

  ;; Let
  (display "Prova del let amb variables x=10 i y=20:")
  (newline)
  (display 
    (let ((x 10)
          (y 20))
      (+ x y)))
  (newline)

  ;; Exemple de read
  (display "Prova del read per introduir dos valors i sumar-los:")
  (newline)
  (define userInput (read))
  (display "Has introduït: ")
  (display userInput)
  (newline)

  ;; Let amb funció
  (display "Prova del let amb funció 'sumar-dos-valors':")
  (newline)
  (sumar-dos-valors)
  (newline)

  ;; Proves lògiques
  (display "Proves lògiques amb and, or, not:")
  (newline)
  (display "and (> 3 2) (< 5 10) = ")
  (display (and (> 3 2) (< 5 10)))
  (newline)
  (display "or (> 3 2) (< 1 0) = ")
  (display (or (> 3 2) (< 1 0)))
  (newline)
  (display "not (> 3 2) = ")
  (display (not (> 3 2)))
  (newline)

  ;; Proves addicionals
  (display "Prova addicional de funcions personalitzades:")
  (newline)
  (display "suma-llista de '(10 20 30) = ")
  (display (suma-llista '(10 20 30)))
  (newline)

  (display "Prova de múltiples operacions combinades:")
  (newline)
  (display (+ (suma 1 2) (suma 3 4)))
  (newline)

  (display "Totes les proves principals han finalitzat correctament!")
  (newline)
)