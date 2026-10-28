import hashlib,json,pathlib
p=pathlib.Path('public')
for name,digest in json.loads(pathlib.Path('checksums.json').read_text()).items():
 assert hashlib.sha256((p/name).read_bytes()).hexdigest()==digest,name
print('All deployment file checksums verified')
