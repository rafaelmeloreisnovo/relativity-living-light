import json

with open("validation_outputs/comparison.json") as f:
    data = json.load(f)

if data["chi2_rll"] > data["chi2_lcdm"]:
    raise Exception("❌ RLL rejeitado: ΛCDM superior no ajuste estatístico")
else:
    print("✅ RLL sobrevive ao teste atual")
