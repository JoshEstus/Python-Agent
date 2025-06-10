from functions.write_file_content import write_file


def test():
    # result = get_file_content("calculator", "main.py")
    # print("Result for 'main.py'")
    # print(result)

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print("Result for 'pkg/calculator.py'")
    # print(result)

    # result = get_file_content("calculator", "/bin/cat")
    # print("Result for '/bin/cat'")
    # print(result)

    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print('Result for write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum")')
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for 'pkg/morelorem.txt'")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for '/tmp/text.txt'")
    print(result)


if __name__ == "__main__":
    test()
