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
  (display "Prova de funció d'ordre superior 'apply-twice' amb 'factorial':")
  (newline)
  (display "apply-twice factorial 3: ")
  (display (apply-twice factorial 3))
  (newline)


  (display "Prova de passatge de funcions com a paràmetres:")
  (newline)
  (display "Cridant 'apply-twice' amb 'is-even?' i 4: ")
  (display (apply-twice is-even? 4))
  (newline)

  (display "Totes les proves de funcions d'ordre superior han finalitzat!")
  (newline)
)