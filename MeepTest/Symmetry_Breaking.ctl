;; Define the params of the Geometry

(define-param air 1)
(define-param epshi 2.1)
(define-param dPML 1.0)

(define-param h 1.5)
(define-param w 0.45)
(define-param sz 10)
(define-param sx 1)
(define-param Deps 1.05)


;; Define the params of the computation

(set-param! resolution 20)

(define-param targetkx 0.25)	
(define-param targetky 0.02) ; Define Point in Bz to study
(define-param k-interp 5)


(define-param kxmin 0)
(define-param kymin 0)
(define-param kxmax 0.1)
(define-param kymax 0.1)
(define-param k-interpx 6)
(define-param k-interpy 6)


(define-param fcen 0.655) ; pulse center frequency                               
(define-param df 0.01)  ; pulse width (in frequency)   

(define-param sourcex 0.1)
(define-param sourcey 0)
(define-param sourcez 0.15)

(define-param runtime 300)

(define-param Ez? true)
(define-param strField "Ez")
(if Ez?
    (begin
      (set! strField "Ez")
      )
    (begin
      (set! strField "Hz")
      )
)

(define-param strPrefix "SHOULDNTBETHIS")

(define-param single-mode? false)
(define-param strType "Single")
(if single-mode?
    (begin
      (set! strType "Single")
      (set! strPrefix (string-append "SYM" strField strType "_fcen" (number->string fcen) "_df" (number->string df) "_kx" (number->string targetkx) "_ky" (number->string targetky) "_h" (number->string h) "_res" (number->string resolution)))
      )
    (begin
      (set! strType "Band")
      (set! strPrefix (string-append  "SYM" strField strType "_fcen" (number->string fcen) "_df" (number->string df)  "_h" (number->string h) "_res" (number->string resolution)))
      )
)

;; Defines where the output is going to be placed
(display strPrefix)
(newline)
(use-output-directory "Results")
(set! filename-prefix strPrefix)



;; Make geometry
(set! geometry-lattice (make lattice (size sx no-size sz)))
(set! geometry (list
      	       ( make block (center 0 0 (/ (* -1 sz) 4)) (size sx infinity (/ sz 2))
	              (material (make dielectric (epsilon Deps)))
		      )
		      
                (make block (center 0 0 0) (size w infinity h) 
		      (material (make dielectric (epsilon epshi)))
		      )
		)
      )
(set! pml-layers (list (make pml (direction Z) (thickness dPML))))

;(set! symmetries (list (make mirror-sym (direction Y) (phase 1))))

(if single-mode?	    
    (begin		    
      (display "SINGLE MODE CALCULATION\n\n")                          

       (if Ez?
	   (begin 
	     (display "Adding Ez Source\n")
	     (set! sources (list
			    (make source
			      (src (make gaussian-src (frequency fcen) (fwidth df)))
			      (component Ez) (center sourcex sourcey sourcez))))
	     )
	   (begin
	     (display "Adding Hz Source\n")
	     (set! sources (list
			    (make source
			      (src (make gaussian-src (frequency fcen) (fwidth df)))
			      (component Hz) (center sourcex sourcey sourcez))))
	     )
	   )
       (run-k-point runtime (vector3 targetkx targetky))

       (print pi "\n")
       (define (CX r fx)
	 (* (exp (* -1i (vector3-x r) targetkx 2 pi)) fx )
	 )
       (define (CY r fy)
	 (* (exp (* -1i (vector3-x r) targetkx 2 pi)) fy )
	 )
  
     (run-until (/ 2 fcen)
		  ;(at-beginning output-epsilon )
		  ;(at-every (/ 1 fcen 20) output-hfield-x)
		  ;(at-every (/ 1 fcen 20) output-hfield-y)
		  ;(at-every (/ 1 fcen 20) output-hfield-z)
		  ;(at-every (/ 1 fcen 20) output-efield-x)
		  ;(at-every (/ 1 fcen 20) output-efield-y)
		  ;(at-every (/ 1 fcen 20) output-efield-z)
		  )

     (output-efield-x)
     (output-efield-y)
     (print "CX_E_TOP: " (integrate-field-function (list Ex) CX (volume (size 1 0 0) (center 0 0 (- (/ sz 2) (* dPML 2)) ) )) "\n")
     (print "CY_E_TOP: " (integrate-field-function (list Ey) CY (volume (size 1 0 0) (center 0 0  (- (/ sz 2) (* dPML 2))) ) ) "\n")

     (print "CX_E_BOT: " (integrate-field-function (list Ex) CX (volume (size 1 0 0) (center 0 0 (-  (* dPML 2) (/ sz 2)) ) )) "\n")
     (print "CY_E_BOT: " (integrate-field-function (list Ey) CY (volume (size 1 0 0) (center 0 0  (- (* dPML 2) (/ sz 2) )) ) ) "\n")

     ;(output-field-function "weird-function" (list Ex) CX)


     (print "CX_H: " (integrate-field-function (list Hx) CX (volume (size 1 0 0) (center 0 0 (- (/ sz 2) (* dPML 2))) ) ) "\n")
     (print "CY_H: " (integrate-field-function (list Hy) CY (volume (size 1 0 0) (center 0 0 (- (/ sz 2) (* dPML 2))) ) ) "\n")

       )

    (begin
      
      (display "BAND CALCULATION\n\n")
      
      
      (if Ez?
	  (begin 
	    (set! sources (list
			   (make source
			     (src (make gaussian-src (frequency fcen) (fwidth df)))
			     (component Ez) (center sourcex sourcey))))
	    )
	  (begin

	    (set! sources (list
			   (make source
			     (src (make gaussian-src (frequency fcen) (fwidth df)))
			     (component Hz) (center sourcex sourcey))))
	    )
	  )
      
      (define kpoints '())
      (define kxpoints (interpolate k-interpx (list (vector3 kxmin 0 0) (vector3 kxmax 0 0))))
      (for-each (lambda (x)
		  (define t (interpolate k-interpy (list (vector3+ x (vector3 0 kymin 0))  (vector3+ x (vector3 0 kymax 0 ) ) ) ) )
		  ;(display t)
		  ;(newline)
		  (set! kpoints (append kpoints t))
		  ;(append( kpoints (interpolate k-interp (list x (vector3+ x (vector3 0 0.2 0))))))
		  )
		kxpoints)
      (display kpoints)
      ;(newline)
      (run-k-points runtime kpoints)
      
      
      )

    )





