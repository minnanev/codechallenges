def group_by_owners(files):
    # YOUR CODE GOES HERE
    result = {}
    for file, owner in files.items():
        result[owner] = result.get(owner, []) + [file]
    return result


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))
