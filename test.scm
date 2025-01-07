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
  (display (+ 2 3))
  (newline)
  (display (> 5 3))
  (newline)

  ;; Definició de funció
  (display "Prova de la definició de funció:")
  (newline)
  (display (suma 3 4))
  (newline)

  ;; Definició de funció sense paràmetres
  (display "Prova de la definició de funció sense paràmetres:")
  (newline)
  (saluda)

  ;; Definició de variable
  (display "Prova de la definició de variables:")
  (newline)
  (display (suma cinc 3))
  (newline)

  ;; If
  (display "Prova de l'if:")
  (newline)
  (display (if (< 3 2) "tres és menor que dos" "tres no és menor que dos"))
  (newline)

  ;; Cond
  (display "Prova del cond:")
  (newline)
  (display 
    (cond
      ((> 3 5) "major")
      ((< 3 5) "menor")
      (#t "igual")))
  (newline)

  ;; Llistes
  (display "Prova de les llistes:")
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

  ;; Recursivitat
  (display "Prova de la recursivitat:")
  (newline)
  (display (suma-llista llista2))
  (newline)

  ;; Let
  (display "Prova del let:")
  (newline)
  (display 
    (let ((x 10)
          (y 20))
      (+ x y)))
  (newline)

  ;; Exemple de read
  (display "Prova de read:")
  (newline)
  (define userInput (read))
  (display "Has introduït: ")
  (display userInput)
  (newline)

  ;; Let amb funció
  (display "Prova del let amb funció:")
  (newline)
  (sumar-dos-valors)

  (display "Proves lògiques:")
  (newline)
  (display (and (> 3 2) (< 5 10)))
  (newline)
  (display (or (> 3 2) (< 1 0)))
  (newline)
  (display (not (> 3 2)))
  (newline)
)