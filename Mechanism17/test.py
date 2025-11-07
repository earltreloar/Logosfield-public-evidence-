python\nfrom predict import predict_h0\nobs_tdc = 72.1; obs_jwst = 73.17\npred = predict_h0()\nprint(f"Predicted H₀ = {pred:.1f}  (vs TDC {obs_tdc}, JWST {obs_jwst})")\n
