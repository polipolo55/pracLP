(display "hola")
(display (+ 2 3))
(display (> 5 3))



(display "prova definicio de funció")
(define (suma x y) 
    (+ x y))

(display (suma 3 4))


(display "prova deifinició de funció sense paràmetres")
(define (saluda)
    (display "Hola")
    (newline))

(saluda)

(display "prova de la definició de variables")
(define cinc 5)

(display (suma cinc 3))

(display "prova del if")

(display 
  (if (< 3 2)
      "tres es menor que dos"
      "tres no es menor que dos"))

(display "prova del cond")

(display 
  (cond
    ((> 3 5) "major")
    ((< 3 5) "menor")
    (#t "igual")))

(display "prova de la llista")

(define llista '(1 2 3 4 5))

(define llista2 '(12 10 3))

(display llista)

(display llista2)

(display (car llista)) ; Resultat: 1

(display (cdr llista)) ; Resultat: (2 3 4 5)

(display (cons 0 llista)) ; Resultat: (0 1 2 3 4 5)

(display (null? '())) ; Resultat: #t
(display (null? llista)) ; Resultat: #f

(display "prova recursivitat")

(define (suma-llista llista)
  (if (null? llista)
      0
      (+ (car llista) (suma-llista (cdr llista)))))
(display (suma-llista llista2)) ; Resultat: 25

(display "prova del let")

(display 
  (let ((x 10)
        (y 20))
    (+ x y)))


(display "prova del read")
(define x (read))
(display x)

(display "prova del let amb funció")
(define (sumar-dos-valors)
  (display "Introdueix dos valors: ")
  (let ((val1 (read))
      (val2 (read)))
    (display "La suma és: ")
    (display (+ val1 val2))
    (newline)))

(sumar-dos-valors)


(display (and (> 3 2) (< 5 10)) ) ; Resultat: #t
(display (or (> 3 2) (< 1 0))   ) ; Resultat: #t
(display (not (> 3 2))          ) ; Resultat: #f