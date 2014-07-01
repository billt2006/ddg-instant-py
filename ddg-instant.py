import argparse
import requests

APP_NAME = 'ddg-instant-py'
SEARCH_URL = 'https://api.duckduckgo.com/'

# Set up the argument parser
parser = argparse.ArgumentParser(description='Get an Instant Answer from the DuckDuckGo API.')
parser.add_argument('query', help='the query string')
args = parser.parse_args()

# Query the API
query_params = {
  't': APP_NAME,
  'q': args.query,
  'format': 'json',
  # 'pretty': '1',
  'no_redirect': '1',
  'no_html': '1',
  'skip_disambig': '1'
}
r = requests.get(SEARCH_URL, params=query_params)
# print(r.url)
# print(r.status_code)
# print(r.text)

# Parse the API response for display
if r.status_code == requests.codes.ok:
  results = r.json()

  if results['Heading']:
    print(results['Heading'])
    underline = ''
    for c in results['Heading']:
      underline += '='
    print(underline+'\n')

  if results['Redirect']:
    print('<'+results['Redirect']+'>')

  if results['Answer']:
    print(results['Answer'])

  if results['Definition']:
    print(results['Definition'])+' <'+results['DefinitionURL']+'>'

  if results['AbstractText']:
    print(results['AbstractText']+' <'+results['AbstractURL']+'>')

  if results['Type'] == 'C' or results['Type'] == 'D':
    for t in results['RelatedTopics']:
      if 'Text' in t and 'FirstURL' in t:
        print('* '+t['Text']+' <'+t['FirstURL']+'>')
      elif 'Name' in t and 'Topics' in t:
        print('* '+t['Name'])
        for sub_t in t['Topics']:
          print('** '+sub_t['Text']+' <'+sub_t['FirstURL']+'>')

  print("\nResults from DuckDuckGo <https://duckduckgo.com>.")
