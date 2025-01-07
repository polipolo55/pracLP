
(define (main)
  (display "Prova de l'if:")
  (newline)
  (display "Si 5 és major que 3, retorna 'Sí', altrament 'No': ")
  (display (if (> 5 3) "Sí" "No"))
  (newline)

  (display "Prova del cond:")
  (newline)
  (display "Condició: Si 2 és igual a 3, retorna 'Igual', si 2 és menor que 3, retorna 'Menor', altrament 'Diferent': ")
  (display 
    (cond
      ((= 2 3) "Igual")
      ((< 2 3) "Menor")
      (#t "Diferent")))
  (newline)

  (display "Prova del let:")
  (newline)
  (display "Assignant x=10 i y=20, suma: ")
  (display 
    (let ((x 10)
          (y 20))
      (+ x y)))
  (newline)

  (display "Prova del let amb múltiples definicions:")
  (newline)
  (display "Assignant a=5, b=15 i suma: ")
  (display 
    (let ((a 5)
          (b 15))
      (+ a b)))
  (newline)

  (display "Totes les proves de control han finalitzat!")
  (newline)
)