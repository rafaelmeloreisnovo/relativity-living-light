import json

data = json.load(open("validation_outputs/comparison.json"))

if data["chi2_rll"] > data["chi2_lcdm"]:
    status = "RLL rejected under current dataset"
    winner = "LCDM"
else:
    status = "RLL survives"
    winner = "RLL"

result = {
    "status": status,
    "winner": winner,
    "chi2_lcdm": data["chi2_lcdm"],
    "chi2_rll": data["chi2_rll"]
}

print("FINAL RESULT:", result)
