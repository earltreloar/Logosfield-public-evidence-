python\nimport numpy as np, random\nfrom predict import predict_h0\nnulls = [predict_h0(random.gauss(0.005,0.001)) for _ in range(1000)]\nprint(f"Null H₀ mean = {np.mean(nulls):.2f}")\n
