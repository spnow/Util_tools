import urllib2
import sys


def main():
	"""
	"""

	if len(sys.argv) < 4:
		print "sniff_back: sniff_back.py [url] [filename] [extension]"
		return

	list_ = [".backup",".bck",".old",".save",".bak",".sav","~",".copy",".old",".orig",".tmp",".txt",".back",".bkp",".bac",".tar",".gz",".tar.gz",".zip",".rar", ".ini", ".inc.php", ".php"]
	hote = sys.argv[1] #url

	fichier = sys.argv[2] #file name ex: index

	ext = sys.argv[3] #.php .html ...
	 
	for item in list_:
	 
	   try:
	        url = hote + "" + fichier + "" + ext + item
	        result = urllib2.urlopen(url)
	        print "\033[32m" + url + " Code : "+str(result.getcode()) + "\033[39m"
	 
	   except urllib2.HTTPError as e:
	            print "\033[31m" + url+" Code :  " + str(e) + "\033[39m"

if __name__ == '__main__':
	main()
