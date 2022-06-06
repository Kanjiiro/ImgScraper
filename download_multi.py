#!/usr/bin/python3
from multiprocessing import Process
import urllib.request
from tqdm import tqdm


def splitter(filename):
    # open file
    file = open(filename, "r")
    # read file
    lines = file.readlines()
    # close file
    file.close()
    # add all links to main list and splits into 6 lists
    links = []
    for line in lines:
        links.append(line)
    # create 6 lists
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    # split links into 6 lists
    for i in range(len(links)):
        if i % 6 == 0:
            list1.append(links[i])
        elif i % 6 == 1:
            list2.append(links[i])
        elif i % 6 == 2:
            list3.append(links[i])
        elif i % 6 == 3:
            list4.append(links[i])
        elif i % 6 == 4:
            list5.append(links[i])
        elif i % 6 == 5:
            list6.append(links[i])

    return list1, list2, list3, list4, list5, list6


def downloader(listname):

    name = ""
    url = ""
    for line in tqdm(listname):
        ...
        url = line
        name = line.split('/')[4]+'.jpg'
        req = urllib.request.Request(
            url, headers={'User-Agent': 'Mozilla/5.0'})
        with open('imgs/'+name, "wb") as f:
            with urllib.request.urlopen(req) as r:
                f.write(r.read())


if __name__ == "__main__":
    proc1, proc2, proc3, proc4, proc5, proc6 = splitter("links.txt")

    p1 = Process(target=downloader, args=(proc1,))
    p2 = Process(target=downloader, args=(proc2,))
    p3 = Process(target=downloader, args=(proc3,))
    p4 = Process(target=downloader, args=(proc4,))
    p5 = Process(target=downloader, args=(proc5,))
    p6 = Process(target=downloader, args=(proc6,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    print("We're done")
