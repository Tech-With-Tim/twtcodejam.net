import requests

def run_py(code: str, compiler: str="cpython-head", options: dict=None) -> dict:
  if options is None:
    options = {}
  task = {
    "code": code,
    "compiler": compiler,
    "options": options,
  }
  resp = requests.post('https://wandbox.org/api/compile.json', json=task)
  if resp.status_code != 200:
    raise Exception('POST /tasks/ {}'.format(resp.status_code))
  return resp.json()

print(run_py("""
print("true")
"""))
