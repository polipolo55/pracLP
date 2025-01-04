"hola"
(+ 2 3)
(> 5 3)


(define (suma x y) 
    (+ x y))

(suma 3 4)


(define cinc 5)

(suma cinc 3)


"prova del if"

(if (< 3 2)
    "tres es menor que dos"
    "tres no es menor que dos")

"prova del cond"

(cond
  ((> 3 5) "major")
  ((< 3 5) "menor")
  (#t "igual"))

"prova de la llista"

(define llista '(1 2 3 4 5))

(define llista2 '(12 10 3))

(car llista) ; Resultat: 1

(cdr llista) ; Resultat: (2 3 4 5)

(cons 0 llista) ; Resultat: (0 1 2 3 4 5)

(null? '()) ; Resultat: #t
(null? llista) ; Resultat: #f

"prova recursivitat"

(define (suma-llista llista)
  (if (null? llista)
      0
      (+ (car llista) (suma-llista (cdr llista)))))
(suma-llista llista2) ; Resultat: 15

"prova del let"