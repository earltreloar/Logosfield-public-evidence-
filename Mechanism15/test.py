python\nfrom predict import predict_lya_escape\nobserved = 0.68\npred = predict_lya_escape()\nsnr = (pred - observed) / 0.03\nprint(f"Mechanism 15 SNR = {snr:.2f}")\n
