# Multiple contexts in single with

with(
    open('file1.txt') as f1,# DNE
    open('file2.txt') as f2# DNE
):
    print(f1.read())
    print(f2.read())


    # ....... file processes