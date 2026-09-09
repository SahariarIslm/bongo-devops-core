import urllib.request, json

url = "https://api.github.com/zen"
req = urllib.request.Request(url, headers={"User-Agent": "Python"})
with urllib.request.urlopen(req) as response:
    print(f"GitHub Zen: {response.read().decode('utf-8')}")