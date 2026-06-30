import json

data = json.load(open("validation_outputs/comparison.json"))

if data["chi2_rll"] > data["chi2_lcdm"]:
    raise Exception("❌ RLL REJECTED (ΛCDM superior)")
else:
    print("✅ RLL SURVIVES CURRENT TEST")
