import os
from os import listdir
from os.path import isfile, join

# Pfade für Labels und Bilder angeben
path_to_images = './63%/images/'
path_to_labels = './63%/labels/'

blacklisted_images = {}
blacklisted_labels = {}

# erlaubte Klassen der Verkehrszeichen
whitelist = [ '0', '1', '2', '3', '4', '5', '7', '8', '11', '12', '13', '14', '15', '17', '25', '26', '27', '29', '32', '33', '34', '35', '36', '37', '38', '39', '40' ]

# Listen für Unterordner erstellen um diese später zu iterieren
paths_to_images = []
paths_to_images.append( path_to_images + 'test/' )
paths_to_images.append( path_to_images + 'train/' )
paths_to_images.append( path_to_images + 'val/' )

paths_to_labels = []
paths_to_labels.append( path_to_labels + 'test/' )
paths_to_labels.append( path_to_labels + 'train/' )
paths_to_labels.append( path_to_labels + 'val/' )

# Die Label Textdateien einlesen und deren Klasse herausbekommen
def getBlacklistedFiles(dir_path):
    blacklist = []
    files = [ f for f in listdir( dir_path ) if isfile( join( dir_path, f ) ) ]

    for file in files:
        with open( dir_path + file ) as f:
            lines = f.readlines()
            lines_splitted = lines[ 0 ].split()
            if lines_splitted[ 0 ] not in whitelist:
                blacklist.append( file )

    return blacklist

# Löscht alle Dateien, die in der Blacklist enthalten sind
def deleteBlacklistedFiles(sub_dir, files):
    for file in files:
        a = sub_dir + file
        if os.path.exists( sub_dir + file ):
            os.remove( sub_dir + file )
        else:
            print( "Datei existiert nicht!" )

for sub_dir in paths_to_labels:
    blacklistedFiles = getBlacklistedFiles( sub_dir )
    blacklisted_images[ sub_dir.replace( 'label', 'image') ] = [ element.replace( '.txt', '.png' ) for element in blacklistedFiles]
    blacklisted_labels[ sub_dir ] = blacklistedFiles

for sub_dir in blacklisted_images:
    deleteBlacklistedFiles( sub_dir, blacklisted_images.get( sub_dir ) )

for sub_dir in blacklisted_labels:
    deleteBlacklistedFiles( sub_dir, blacklisted_labels.get( sub_dir ) )