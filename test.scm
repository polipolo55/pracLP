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

(define llista '(12 2 3 4 5))

(car llista) ; Resultat: 1

(cdr llista) ; Resultat: (2 3 4 5)

(cons 0 llista) ; Resultat: (0 1 2 3 4 5)

(null? '()) ; Resultat: #t
(null? llista) ; Resultat: #f

"prova del let"