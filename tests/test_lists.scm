(define (main)
  (display "Prova de creació de llistes:")
  (newline)
  (display "Creant llista '(1 2 3): ")
  (display '(1 2 3))
  (newline)

  (display "Prova de car amb llista '(1 2 3): ")
  (display (car '(1 2 3)))
  (newline)

  (display "Prova de cdr amb llista '(1 2 3): ")
  (display (cdr '(1 2 3)))
  (newline)

  (display "Prova de cons: cons (1 2 3): ")
  (display (cons 1 '(2 3)))
  (newline)

  (display "Prova de null? amb '()': ")
  (display (null? '()))
  (newline)

  (display "Prova de null? amb '(1 2 3)': ")
  (display (null? '(1 2 3)))
  (newline)

  (display "Totes les proves de llistes han finalitzat!")
  (newline)
)