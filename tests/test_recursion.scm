(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(define (fibonacci n)
  (if (< n 2)
      n
      (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))


(define (suma-llista llista)
  (if (null? llista)
      0
      (+ (car llista) (suma-llista (cdr llista)))))

(define (main)
  (display "Prova de recursivitat amb factorial:")
  (newline)
  (display "Factorial de 5: ")
  (display (factorial 5))
  (newline)

  (display "Prova de recursivitat amb fibonacci:")
  (newline)
  (display "Fibonacci de 6: ")
  (display (fibonacci 6))
  (newline)

  (display "Prova de recursivitat amb suma-llista:")
  (newline)
  (display "Suma de '(1 2 3 4 5): ")
  (display (suma-llista '(1 2 3 4 5)))
  (newline)

  (display "Totes les proves de recursivitat han finalitzat!")
  (newline)
)