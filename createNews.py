import glob
import os

imagePath = r'assets\img\News'
moveImageTo = r'assets\img'
mdPath = r'_posts'

for image in glob.glob(imagePath + '\*.jpg'):
    filename = os.path.basename(image)
    title = filename[10:].replace('-', ' ')[:-4]
    # newName = filename.replace(' ', '-')
    # print(newName)
    # os.rename(imagePath + '\\' + filename, imagePath + '\\' + newName)
    destPath = mdPath + '\\' + filename[:-4] + '.md'

#####################################################################
    mdContent = '\
---\n\
layout: post\n\
title: \"' + title + '\"\n\
author: \"Z. Kang\"\n\
categories: news\n\
tags: [news]\n\
image: ' + filename + '\n\
---\n\
\n' + '#' + title
#####################################################################

    with open (destPath, 'w') as mdFile:
        mdFile.writelines(mdContent)

    os.rename(image, moveImageTo + '\\' + filename)
