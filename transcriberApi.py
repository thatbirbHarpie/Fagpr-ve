import sys
import requests

if len(sys.argv) < 2:
    sys.exit(1)


LYDFILEN=sys.argv[1]
OUTPUTFILE="tekst.py"
f = open(LYDFILEN, "rb")
url = "https://gpt-dev.uio.no/api/gpt-gateway/audio-stt"
res = requests.post(
    url, 
    files={
        "file": f
    },
    headers= {
        "domain":"uio.no",
        "model":"gpt-4o-transcribe",
        "x-secret-backdoor-key": "YWtzZWxteTo4YTM2NGZjNy03MDhjLTRlMzUtYjk3Zi1mMjg4MGY5MzEzNDc",
    }
)
f.close()
print(res.text)



with open(OUTPUTFILE, "w") as text_file:
    text_file.write(res.text)
