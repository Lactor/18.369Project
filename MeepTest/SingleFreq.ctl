(define-param h 1.5)
(define-param w 0.45)
(define-param sz 10)
(define-param sx 1)

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


(define-param fcen 0.15) ; pulse center frequency                               
(define-param df 0.04)  ; pulse width (in frequency)                             
(set! sources (list
               (make source
                 (src (make gaussian-src (frequency fcen) (fwidth df)))
                 (component Ey) (center 0.1234 0.1234))))

;(set! symmetries (list (make mirror-sym (direction Y) (phase -1))))
					; Position of the source means only odd TE modes


i
;(define-param k-interp 5)
;(run-k-points 20 (interpolate k-interp (list (vector3 0 0 0) (vector3 0.5 0 0 ))))


