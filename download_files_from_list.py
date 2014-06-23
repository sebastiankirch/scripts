import urllib2

def download():
	lines = [line.strip() for line in open('urls.txt')]
	for url in lines:
		print("downloading " + url)
		video = urllib2.urlopen(url)
		file_name = url.split('/')[-1]
		output = open(file_name,'wb')
		output.write(video.read())
		output.close()

if __name__ == '__main__':
    download()