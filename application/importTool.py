
import argparse
import importmodule



ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,	help="path to input csv")
ap.add_argument("-c", "--command", required=True,	help="Import tool commands")
args = vars(ap.parse_args())

command = args.get('command')
csvFile = args.get('input');

print (command + ' / ' + csvFile)

competitors = importmodule.readCvs(csvFile)
for licenseNo in competitors:
    competitor = competitors[licenseNo]
    print(competitor.licenseNo + ' ' + competitor.name + ' ' + competitor.email )


