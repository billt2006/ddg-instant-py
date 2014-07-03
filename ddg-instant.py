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

# Debugging info
# print(r.url)
# print(r.status_code)
# print(r.text)

# Parse the API response for display
if r.status_code == requests.codes.ok:
  results = r.json()

  if results['Redirect']:
    str_buffer = '<' + results['Redirect'] + '>\n'
  else:
    str_buffer = ''
    if results['Heading']:
      str_buffer += results['Heading'] + ': '

    if results['Answer']:
      str_buffer += results['Answer'] + '\n'

    if results['Definition']:
      str_buffer += results['Definition'] + ' <' + results['DefinitionURL'] + '>\n'

    if results['AbstractText']:
      str_buffer += results['AbstractText'] + ' <' + results['AbstractURL'] + '>\n'

    if results['Type'] == 'C' or results['Type'] == 'D':
      for t in results['RelatedTopics']:
        if 'Text' in t and 'FirstURL' in t:
          str_buffer += '\n* ' + t['Text'] + ' <' + t['FirstURL'] + '>'
        elif 'Name' in t and 'Topics' in t:
          str_buffer += '\n* ' + t['Name']
          for sub_t in t['Topics']:
            str_buffer += '\n** '+sub_t['Text']+' <'+sub_t['FirstURL']+'>'
      str_buffer += '\n'

  print(str_buffer + '\nResults from DuckDuckGo <https://duckduckgo.com>.')
