import getopt
import sys
import requests
import os

def get_group(base_url, token_segment, namespace):
    final_url = base_url + 'groups?' + token_segment + "search=" + namespace
    r = requests.get(final_url)
    results = r.json()
    
    if not results:
        print("Group " + namespace + " not found.")
        return
    
    i = 0
    if len(results) > 1:
        print("Multiple group candidates found. Select the required candidate: ")
        for i, result in enumerate(results):
            print("\t" + str(i) + ') '  + result['web_url'])
    
        i = int(input())

    return results[i]


def main(argv):
    opts = []
    args = []
    try:
        opts, args = getopt.getopt(argv, "ht:", ["help", "token"])
    except getopt.GetoptError as err:
        print("Error:" + str(err))
    
    access_token = None
    base_url =  'https://gitlab.com/api/v4/'
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print_usage()
        elif opt == '-t' or opt == '--token':
            access_token = arg

    if not args:
        print("Group namespace not provided. Exiting...")
        return

    token_segment = ""
    if access_token is not None:
        token_segment = "private_token=" + access_token + "&"

    namespace = args[0]
    
    group = get_group(base_url, token_segment, namespace)
    print(group)    
    
    clone_group(base_url, token_segment, group)

    
    

if __name__ == "__main__":
    main(sys.argv[1:])

