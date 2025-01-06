(define (sumar-dos-valors)
  (display "Introdueix dos valors: ")
  (let ((val1 (read))
        (val2 (read)))
     (display "La suma és: ")
     (display (+ val1 val2))
     (newline)))

(sumar-dos-valors)