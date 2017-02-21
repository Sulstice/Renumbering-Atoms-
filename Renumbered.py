import time

def main():

    #Initialize Variables
    wroteLine = False
    secondOxygenExists = False
    replacementDone = False
    secondOxygenNoExists = False

    t0 = time.time()

    print("Program Started")
    f = open('FileTest.txt', "r")
    newf = open('NewHello.txt', "w")

    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i]

        if len(line) == 64: # Lines without BackBone

            if line[1:3] == " 7":
                line1 = line
            elif line[1:3] == " 8":
                line2 = line
            else:
                newf.write(line)

        elif len(line) == 73: #Lines with BackBone


            if line[1:3] == " 7":
                line1 = line
            elif line[1:3] == " 8":
                line2 = line

            #Follow the pattern of the Data

            H = lines[i + 1]
            H2 = lines[i + 2]
            O = lines[i + 3]

            # Used to prevent repeats

            previousLine = lines[i - 1]
            previousLine2 = lines[i - 2]
            previousLine3 = lines[i - 3]

            if line[4] == "O" and H[4] == "H" and H2[4:6] == "H2" and O[4] == "O":

                #Remember the line numbers to change the latter half what they are attached to

                lineNumberOfFirstOxygen = line[1:3]
                lineNumberCheckSystem = H2[1:3]
                lineNumberOfSecondOxygen = O[1:3]
                secondOxygenExists = True

                #Relace the lines
                newf.write(line.replace(line[1:3], " 7", 1))
                newf.write(O.replace(O[1:3], " 8", 1))
                newf.write(line1.replace(" 7", line[1:3], 1))
                newf.write(line2.replace(" 8", O[1:3], 1))

            else:

                # Prevent repeats

                if secondOxygenExists:
                    if line[1:3] == lineNumberOfSecondOxygen:
                        continue
                        secondOxygenExists = False
                    else:
                        newf.write(line)
                else:
                    newf.write(line)

        elif len(line) == 26 or len(line) == 15 or len(line) == 16:

            if line[1:3] == " 7":
                bondLine1 = line
            elif line[1:3] == " 8":
                bondLine2 = line

            bondSecondO = lines[i + 3]

            if line[1:3] == lineNumberOfFirstOxygen:
                if bondSecondO[1:3] != lineNumberOfSecondOxygen:
                    secondOxygenNoExists = True

            if secondOxygenNoExists:
                newf.write(line.replace(line[1:3], ' 7').replace(lineNumberOfFirstOxygen, " 7").replace(lineNumberOfSecondOxygen, " 8"))
                newf.write(bondLine1.replace(' 7', line[1:3]).replace(" 8", lineNumberOfSecondOxygen))
                newf.write(bondLine2.replace(' 8', lineNumberOfSecondOxygen).replace(" 7", line[1:3]))
                secondOxygenNoExists = False

            elif line[1:3] == lineNumberOfFirstOxygen and bondSecondO[1:3] == lineNumberOfSecondOxygen:

                newf.write(line.replace(line[1:3], ' 7').replace(lineNumberOfFirstOxygen, " 7").replace(lineNumberOfSecondOxygen, " 8"))
                newf.write(bondSecondO.replace(bondSecondO[1:3], ' 8').replace(lineNumberOfFirstOxygen, " 7").replace(lineNumberOfSecondOxygen, " 8"))
                newf.write(bondLine1.replace(' 7', line[1:3]).replace(" 8", bondSecondO[1:3]))
                newf.write(bondLine2.replace(' 8', bondSecondO[1:3]).replace(" 7", line[1:3]))

            else:

                if line[1:3] == " 7" or line[1:3] == " 8" or line[1:3] == lineNumberOfFirstOxygen or line[1:3] == lineNumberOfSecondOxygen:
                    continue
                else:

                    lettersInLine = line.split()

                    for j in range(0, len(lettersInLine)):

                        if lettersInLine[j] == lineNumberOfFirstOxygen:
                            newf.write(line.replace(lettersInLine[j], " 7"))
                            wroteLine = True
                        elif lettersInLine[j] == lineNumberOfSecondOxygen:
                            newf.write(line.replace(lettersInLine[j], " 8"))
                            wroteLine = True
                        elif lettersInLine[j] == "7" and lettersInLine[j + 1] == "8":
                            newf.write(line.replace(" 7", lineNumberOfFirstOxygen).replace(" 8", lineNumberOfSecondOxygen))
                            wroteLine = True
                        elif lettersInLine[j] == "8" and lettersInLine[j - 1] == "7":
                            wroteLine = True
                        elif lettersInLine[j] == "7" and not replacementDone:
                            newf.write(line.replace(" 7", lineNumberOfFirstOxygen).replace(" 8", lineNumberOfSecondOxygen))
                            wroteLine = True
                        elif lettersInLine[j] == "8" and not replacementDone:
                            newf.write(line.replace(" 8", lineNumberOfSecondOxygen).replace(" 7", lineNumberOfFirstOxygen))
                            wroteLine = True

                    if wroteLine:
                        wroteLine = False
                        continue
                    else:
                        newf.write(line)

        else:

            if line[1:3] == " 7" or line[1:3] == " 8" and len(line) >= 64:
                continue
            else:
                newf.write(line)


    f.close()
    t1 = time.time()
    total = t1 - t0
    print("Time to complete program: " + str(total))

main()