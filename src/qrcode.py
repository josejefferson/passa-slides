import pyqrcode

# QR Code (https://gist.github.com/eduardomazolini/2466eda91ff8cff379ad83031c334e58)
def qrCode(url):
    def halfChar(a, b):
        halfMatrix = {
            ('0', '0'): '█',
            ('1', '1'): ' ',
            ('1', '0'): '▄',
            ('0', '1'): '▀'
        }
        return halfMatrix[(a, b)]

    lines = pyqrcode.create(url).text().split('\n')[3:-4]
    lines = list(map(lambda l: l[3:-3], lines))

    i = 0
    result = ''
    while i < len(lines):
        line1 = lines[i]
        i += 1
        if i == len(lines):
            result += ' ' + '▀' * len(lines[0])
        else:
            line2 = lines[i]
            if (line2 < line1):
                line2 += '1' * len(line1)
            i += 1
            result += ' ' + ''.join(map(halfChar, list(line1), list(line2))) + '\n'

    return result.strip('\n')
