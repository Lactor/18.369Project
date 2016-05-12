(define-param h 1.5)
(define-param w 0.45)
(define-param sz 10)
(define-param sx 1)

(use-output-directory [Results/])
(set filename-prefix [YOUSHOULNAMEYOURFILE])

(define-param air 1)
(define-param epshi 2.1)

(define-param dPML 1.0)

(set! geometry-lattice (make lattice (size sx no-size sz)))


(set! geometry (list
                (make block (center 0 0 0) (size w infinity h) 
		      (material (make dielectric (epsilon epshi)))
		      )
		)
      )

(set-param! resolution 40)

(set! pml-layers (list (make pml (direction Z) (thickness dPML))))

(set! symmetries (list (make mirror-sym (direction Y) (phase 1))))

; false = transmission spectrum, true = resonant modes:                         
(define-param single-mode? false)

(if single-mode?	    
    (begin		    

      (define-param fcen 0.15) ; pulse center frequency                               
      (define-param df 0.04)  ; pulse width (in frequency)                             

      (define-param targetkx 0.2)
      (define-param targetky 0.0) ; Define Point in Bz to study

      (set! sources (list
		     (make source
		       (src (make gaussian-src (frequency fcen) (fwidth df)))
		       (component Hz) (center 0.1234 0.1234))))
      
      (run-k-point 30 (vector3 0.2 0 0))
      (run-until (/ 1 fcen)
		 (at-beginning output-epsilon)
		 (at-every (/ 1 fcen 20) output-hfield-x)
		 (at-every (/ 1 fcen 20) output-hfield-y)
		 (at-every (/ 1 fcen 20) output-hfield-z)
		 (at-every (/ 1 fcen 20) output-efield-x)
		 (at-every (/ 1 fcen 20) output-efield-y)
		 (at-every (/ 1 fcen 20) output-efield-z)
		 )
    )
    (begin
      

      (define-param fcen 0.3) ; pulse center frequency                               
      (define-param df 0.3)  ; pulse width (in frequency)                             
      (set! sources (list
		     (make source
		       (src (make gaussian-src (frequency fcen) (fwidth df)))
		       (component Hz) (center 0.1234 0.1234))))


      (define-param k-interp 5)
      (run-k-points 20 (interpolate k-interp (list (vector3 0 0 0) (vector3 0.5 0 0 ))))
      
      
      )
    )





