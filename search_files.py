import os

def search_files(query):
    cmd = "locate -i --regex '^.*{}.*$'".format(query)
    results = os.popen(cmd).read().splitlines()
    return [{"Name": os.path.basename(file), "Path": file} for file in results]
