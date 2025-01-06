(display "Test de definició i crida de funcions")
(newline)

(display "Definició de la funció suma")
(define (suma x y) 
    (+ x y))
(display "Funció suma definida")
(newline)

(display "Crida a la funció suma amb arguments 3 i 4")
(display (suma 3 4)) ; Esperat: 7
(newline)

(display "Definició de la funció resta")
(define (resta x y)
    (- x y))
(display "Funció resta definida")
(newline)

(display "Crida a la funció resta amb arguments 10 i 4")
(display (resta 10 4)) ; Esperat: 6
(newline)

(display "Definició de la funció sense paràmetres")
(define (saluda)
    (display "Hola")
    (newline))
(display "Funció saluda definida")
(newline)

(display "Crida a la funció saluda")
(saluda) ; Esperat: Hola
(newline)

(display "Definició de la funció amb let")
(define (sumar-dos-valors)
  (display "Introdueix dos valors: ")
  (let ((val1 (read))
        (val2 (read)))
    (display "La suma és: ")
    (display (+ val1 val2))
    (newline)))
(display "Funció sumar-dos-valors definida")
(newline)

(display "Crida a la funció sumar-dos-valors")
(sumar-dos-valors) ; Esperat: Llegeix dos valors i mostra la seva suma
(newline)

