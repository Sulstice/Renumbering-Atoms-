import time


def main():

    t0 = time.time()
    atomCount = 0
    bondCount = 0


    print ("Program Started")
    f = open('NewHello.txt', 'r')
    newf = open('SortedNewHello.txt', 'w')
    lines = f.readlines()

    startAtomAppending = False
    startBondAppending = False

    sortedAtomData = []
    sortedBondData = []

    #Know the count of atoms in the file to make a list of lists

    count = 0

    for i in range(0, len(lines)):
        line = lines[i]
        if line == "@<TRIPOS>MOLECULE\n":
            count = count + 1
        else:
            continue

    print (count)

    atomData = [[] for _ in range(count)]
    bondData = [[] for _ in range(count)]

    #Grab each atom and bond data in the lists of lists and chronogically add them

    for i in range(0, len(lines)):

        line = lines[i]

        if line == "@<TRIPOS>BOND\n":
            startAtomAppending = False
            startBondAppending = True
            continue

        elif startAtomAppending:
            atomData[atomCount].append(line)

        elif startBondAppending:
            bondData[bondCount].append(line)

        if line == "@<TRIPOS>ATOM\n":
            startAtomAppending = True
            continue

        elif line == "@<TRIPOS>BOND\n":
            startAtomAppending = False
            startBondAppending = True

        elif line == "@<TRIPOS>SUBSTRUCTURE\n":
            startAtomAppending = False
            startBondAppending = False
            atomCount = atomCount + 1
            bondCount = bondCount + 1

        elif len(line) == 64 or len(line) == 73 or len(line) == 26 or len(line) == 15 or len(line) == 16:
            continue

    #Sort the elements into a list of lists

    atomCount = 0
    bondCount = 0

    for i in range(0, len(atomData)):
        sortData = sorted(atomData[i])
        sortedAtomData.append(sortData)

    for i in range(0, len(bondData)):
        sortBondData = sorted(bondData[i])
        sortedBondData.append(sortBondData)


    for i in range(0, len(lines)):
        line = lines[i]

        if line == "@<TRIPOS>ATOM\n":
            newf.write(line)
            for i in sortedAtomData[atomCount]:
                for j in i:
                    newf.write(j)
        elif line == "@<TRIPOS>BOND\n":
            newf.write(line)
            for i in sortedBondData[bondCount]:
                for j in i:
                    newf.write(j)

        elif line == "@<TRIPOS>SUBSTRUCTURE\n":
            newf.write(line)
            atomCount = atomCount + 1
            bondCount = bondCount + 1

        elif len(line) == 64 or len(line) == 73 or len(line) == 26 or len(line) == 15 or len(line) == 16:
            continue
        else:
            newf.write(line)

    t1 = time.time()
    tf = t1 - t0
    print ("Time to complete program: " + str(tf))


main()