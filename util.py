def sortContent(fileName):
    try:
        print("File open for reading")
        f = open(fileName, "r")

        arr = f.readlines()

        arr.sort()

        f.close()
        print("File close")
    except FileNotFoundError:
        print("File not found")
        return False

    return arr


def writeToFile(fileName, content: list):
    try:
        print("File open for writing")
        f = open(fileName, "w+")
        for w in content:
            f.write(w)
            if w[len(w) - 1] != "\n":
                f.write("\n")
        f.close()
        print("File close")
    except FileNotFoundError:
        print("File not found")
        return False

    return True


def formatter(content: list):
    print("Formatter start")

    htmlContent = \
    """<div style='text-align: center;'><span style='font-size: xx-large;'>{}</span></div><div style='text-align: left;'>""" \
        .format(content[0][:len(content[0]) - 1])

    for pair in content[1:]:
        if pair[len(pair) - 1] == '\n':
            htmlContent += """<div style='text-align: left;'><font size='6'>{}</font></div>""".format(
                pair[:len(pair) - 1])
        else:
            htmlContent += """<div style='text-align: left;'><font size='6'>{}</font></div>""".format(pair[:len(pair)])

    htmlContent = "\"" + htmlContent + "</div>" + "\""

    print("Formatter finish")

    return htmlContent
