import os, json, sys, requests
token = os.environ.get("META_ACCESS_TOKEN") or open(".env").read().split("META_ACCESS_TOKEN=")[1].split("\n")[0].strip()
me = requests.get(f"https://graph.facebook.com/v21.0/me?access_token={token}").json()
perms = requests.get(f"https://graph.facebook.com/v21.0/me/permissions?access_token={token}").json()
debug = requests.get(f"https://graph.facebook.com/v21.0/debug_token?input_token={token}&access_token={token}").json()
out = {
  "me": me,
  "permissions_granted": [p["permission"] for p in perms.get("data", []) if p.get("status") == "granted"],
  "expires_at": debug.get("data", {}).get("expires_at", 0),
  "type": debug.get("data", {}).get("type", "unknown"),
}
json.dump(out, open("token_info.json", "w"), indent=2)
print(json.dumps(out, indent=2))
