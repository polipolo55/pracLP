
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

(define llista '(1 2 3 4 5))
(define llista2 '(12 10 3))

(define (sumar-dos-valors)
  (display "Introdueix dos valors: ")
  (let ((val1 (read))
        (val2 (read)))
    (display "La suma és: ")
    (display (+ val1 val2))
    (newline)))

(define (main)
  (display "Hola món soc el main")
  (newline)
  (display "hola")
  (newline)
  (display (+ 2 3))
  (newline)
  (display (> 5 3))
  (newline)

  (display "prova definicio de funció")
  (newline)
  (display (suma 3 4))
  (newline)

  (display "prova deifinició de funció sense paràmetres")
  (newline)
  (saluda)

  (display "prova de la definició de variables")
  (newline)
  (display (suma cinc 3))
  (newline)

  (display "prova del if")
  (newline)
  (display (if (< 3 2) "tres es menor que dos" "tres no es menor que dos"))
  (newline)

  (display "prova del cond")
  (newline)
  (display
    (cond
      ((> 3 5) "major")
      ((< 3 5) "menor")
      (#t "igual")))
  (newline)

  (display "prova de la llista")
  (newline)
  (display llista)
  (newline)
  (display llista2)
  (newline)
  (display (car llista))
  (newline)
  (display (cdr llista))
  (newline)
  (display (cons 0 llista))
  (newline)
  (display (null? '()))
  (newline)
  (display (null? llista))
  (newline)

  (display "prova recursivitat")
  (newline)
  (display (suma-llista llista2))
  (newline)

  (display "prova del let")
  (newline)
  (display 
    (let ((x 10)
          (y 20))
      (+ x y)))
  (newline)

  (display "prova del read")
  (newline)
  (define x (read))
  (display x)
  (newline)

  (display "prova del let amb funció")
  (newline)
  (sumar-dos-valors)

  (display (and (> 3 2) (< 5 10)))
  (newline)
  (display (or (> 3 2) (< 1 0)))
  (newline)
  (display (not (> 3 2)))
  (newline)
)