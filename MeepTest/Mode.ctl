;; Define the params of the Geometry

(define-param air 1)
(define-param epshi 2.1)
(define-param dPML 1.0)

(define-param h 1.5)
(define-param w 0.45)
(define-param sz 10)
(define-param sx 1)


;; Define the params of the computation

(set-param! resolution 20)

(define-param targetkx 0.25)	
(define-param targetky 0.02) ; Define Point in Bz to study
(define-param k-interp 5)


(define-param fcen 0.655) ; pulse center frequency                               
(define-param df 0.01)  ; pulse width (in frequency)   

(define-param sourcex 0.1)
(define-param sourcey 0)
(define-param sourcey 0.15)

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
      (set! strPrefix (string-append strField strType "_fcen" (number->string fcen) "_df" (number->string df) "_kx" (number->string targetkx) "_ky" (number->string targetky) "_res" (number->string resolution)))
      )
    (begin
      (set! strType "Band")
      (set! strPrefix (string-append strField strType "_fcen" (number->string fcen) "_df" (number->string df)"_res" (number->string resolution)))
      )
)

;; Defines where the output is going to be placed
(display strPrefix)
(use-output-directory "Results")
(set! filename-prefix strPrefix)



;; Make geometry
(set! geometry-lattice (make lattice (size sx no-size sz)))
(set! geometry (list
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
       (run-until (/ 2 fcen)
		  (at-beginning output-epsilon )
		  (at-every (/ 1 fcen 20) output-hfield-x)
		  (at-every (/ 1 fcen 20) output-hfield-y)
		  (at-every (/ 1 fcen 20) output-hfield-z)
		  (at-every (/ 1 fcen 20) output-efield-x)
		  (at-every (/ 1 fcen 20) output-efield-y)
		  (at-every (/ 1 fcen 20) output-efield-z)
		  )
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

      (run-k-points runtime (interpolate k-interp (list (vector3 0 0 0) (vector3 0.1 0 0 ))))
      
      
      )
    )





