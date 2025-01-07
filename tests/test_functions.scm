(define (power base exponent)
  ;; Calcula base^exponent recursivament
  (if (= exponent 0)
      1
      (* base (power base (- exponent 1)))))

(define (apply-twice f val)
  ;; Exemple de funció d'ordre superior
  (f (f val)))

(define (is-even? n)
  (if (= n 0)
      #t
      (if (= n 1)
          #f
          (is-even? (- n 2)))))

(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(define (fibonacci n)
  (if (< n 2)
      n
      (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))

(define (main)
  (display "Prova de la potència: 2^5 = ")
  (display (power 2 5))
  (newline)

  (display "Prova de la funció d'ordre superior 'apply-twice' (factorial 3 dues vegades): ")
  (display (apply-twice factorial 3))
  (newline)

  (display "Prova de 'is-even?' amb 10: ")
  (display (is-even? 10))
  (newline)

  (display "Prova de 'factorial' amb 5: ")
  (display (factorial 5))
  (newline)

  (display "Prova de 'fibonacci' amb 8: ")
  (display (fibonacci 8))
  (newline)

  (display "Proves de funcions finalitzades!")
  (newline)
)