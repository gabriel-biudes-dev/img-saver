import io, os
from PIL import Image

class ImageData:
  def __init__(self, name, content):
    self.name = name
    self.content = content

def showMenu():
    print('[MENU]')
    print('\t1)Save image')
    print('\t2)Restore image')
    return int(input('Option: '))

def readimage(path):
    with open(path, "rb") as f:
        return bytearray(f.read())

#bytess = readimage('tucano.jpg')
#img = Image.open(io.BytesIO(bytess))
#img.save('kkskzq.jpg')

def saveImage(name):
    f = open('data.txt', 'a')
    image = readimage(name)
    f.write('START\n')
    f.write(name + '\n')
    for x in image:
        f.write(str(x) + ' ')
    f.write('\nEND\n')
    f.close()

def getContent(index):
    f = open('data.txt')
    lines = f.readlines()
    data = lines[index]

def getImage():
    f = open('data.txt')
    byt = bytearray()
    lines = f.readlines()
    filelist = []
    for index, line in enumerate(lines):
        if line.startswith('START'):
            filename = lines[index + 1].split('\n')[0]
            filedata = lines[index + 2].split(' ')
            filedata.remove('\n')
            for x in filedata:
                byt.append(int(x))
            image = ImageData(filename, byt)
            filelist.append(image)
    print('\n[FILES SAVED]')
    for index,x in enumerate(filelist):
        print(f'\t{index + 1}){x.name}')
    option = int(input('Choose the number of the file to be recovered: '))
    filerecovered = filelist[option - 1]
    #img = Image.open(io.BytesIO(filerecovered.content))
    #img.save(filerecovered.name)
    #print(f'{filerecovered.name} recovered successfully!')
    #print(filerecovered.content)


def main():
    answer = showMenu()
    while answer != 9:
        if answer == 1: saveImage(input('Image name: '))
        if answer == 2: getImage()
        answer = showMenu()
main()


