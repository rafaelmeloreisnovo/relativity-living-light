import json

data = json.load(open("validation_outputs/comparison.json"))

if data["chi2_rll"] > data["chi2_lcdm"]:
    raise Exception("❌ RLL rejeitado pelo teste atual")
else:
    print("✅ RLL sobrevive ao teste")
