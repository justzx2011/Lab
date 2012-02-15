#coding: utf8

import ConfigParser,urlparse,os.path

try:
	import cStringIO as StringIO
except:
	import StringIO

def urljoin(base,url):
	"""
		连接2个URL -> 一个URL
	"""
	join = urlparse.urljoin(base,url)
	url = urlparse.urlsplit(join)
	path = os.path.normpath(url.path)
	return urlparse.urlunsplit((url.scheme,url.netloc,path,url.query,url.fragment))
	
def getConfig(configfile,section,includesection="include"):
	"""
		返回某个配置文件的某个section的内容，以dict形式返回.
		增加一个include的内容区域，这样可以进行包含.
		[include]
		files : included_file_path(绝对路径/configfile的相对路径)
	"""
	conf = ConfigParser.ConfigParser()
	conf.readfp(open(configfile))

	isections = []
	try:
		i = dict(conf.items(includesection))
		ied = i.get('files','')
		for x in StringIO.StringIO(ied):
			if os.path.isabs(x):
				d = x
			else:
				d = os.path.join(os.path.dirname(configfile),x)
			v = getConfig(d,section,includesection)
			if v:
				isections.append(v)
	except ConfigParser.NoSectionError:
		pass
	v = {}
	try:
		v = dict(conf.items(section))
	except ConfigParser.NoSectionError:
		pass
	for d in isections:
		for x in d:
			if x not in v:
				v[x] = d[x]
	return v

if __name__=="__main__":
	print test()
