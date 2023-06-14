from substrateinterface import SubstrateInterface
from substrateinterface.utils.ss58 import ss58_decode, ss58_encode
import datetime
import pandas as pd
pd.set_option('display.max_columns', None)
pd.options.display.max_colwidth = 100
from wasmer import wasm2wat
import re

def get_search(url, tag):
  substrate = SubstrateInterface(url)
  result = substrate.query_map(module="Contracts", storage_function="CodeStorage", block_hash = None, page_size = 100)
      
  data = []
  for (a, b) in result:
    code = b.value['code']
    code = code.replace("0x","")
    hexcode = bytes.fromhex(code)
    text = wasm2wat(hexcode)
    out = re.search(tag, text)
    if out != None:
      data.append({'url':url, 'code_hash':a.value, 'search term':out, 'code_text':text})
    
  # df = pd.DataFrame(data)
  return data

def main():
  tag = "delegate"
  tag = "delegate_call"
  
  urls = ['wss://ws.azero.dev','wss://astar.public.curie.radiumblock.co/ws','wss://shiden.api.onfinality.io/public-ws']
  # Select which url to search
  url = urls[2]
  # this function extracts all the contracts from the storage function and searches them for the supplied term
  v = get_search(url, tag)
  # Show all matches
  pd.DataFrame(v)


  
if __name__ == "__main__":
    main()
