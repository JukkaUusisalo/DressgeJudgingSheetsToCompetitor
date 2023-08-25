
import argparse
import importmodule



ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,	help="path to input csv")
ap.add_argument("-c", "--command", required=False,default="import",	help="Import tool commands")
ap.add_argument("-k","--keep",required=False, help="keep existing data in database", action='store_true')
args = vars(ap.parse_args())

command = args.get('command')
csvFile = args.get('input')
keep = args.get('keep')

if(command =='import'): 

    if(args.get('keep') is False):
        print ('Clear db')
        importmodule.clearDB()
    else:
        print ('Keep existing data in db')

    print (command + ' / ' + csvFile)
    competitors = importmodule.readCvs(csvFile)
    for licenseNo in competitors:
        competitor = competitors[licenseNo]
        print(competitor.licenseNo + ' ' + competitor.name + ' ' + competitor.email )
else:
    print ('command ' + command + ' is not supported')


