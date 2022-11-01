import csv

result = []

with open("./parser/read.txt", "r") as csvFile:
    reader = csv.reader(csvFile, delimiter="$")

    counter = 0
    validCounter = 0
    
    for line in reader:
        counter += 1
        if (len(line) == 3):
            validCounter += 1
            if ("Closed" not in line[2]):
                result.append(line)
        else:
            print("Error", counter)

    # print(counter)
    # print(validCounter)
    # print(len(result))
    # print(result)
print("read.txt: Success")

with open("./parser/output.csv", "w", newline="") as outputFile:
    writer = csv.writer(outputFile, delimiter="$")
    for element in result:
        writer.writerow(element)

print("output.csv: Success")

with open("./parser/outputName.txt", "w", newline="") as outputNameFile:
    for element in result:
        outputNameFile.write(element[0] + "\n")
print("outputName.txt: Success")

with open("./parser/outputSName.txt", "w", newline="") as outputSNameFile:
    for element in result:
        if ("sponsorship" in element[0] or "sponsorship" in element[1] 
        or "sponsorship" in element[2] or "Sponsorship" in element[0] 
        or "Sponsorship" in element[1] or "Sponsorship" in element[2]):
            outputSNameFile.write(element[0] + "$ " + element[2] + "\n")
print("outputSName.txt: Success")