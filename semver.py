class version:
	major = 0
	minor = 0
	patch = 0
	def __init__(self, version):
		try:
			versions = version.split('.', 3)
			self.major = int(versions[0])
			self.minor = int(versions[1])
			self.patch = int(versions[2])
		except ValueError as e:
			raise RuntimeError("Versions must be in the form of X.Y.Z") from e
		except IndexError as e:
			raise RuntimeError("Versions must be in the form of X.Y.Z") from e
			
def equals(v1, v2):
	version1 = version(v1)
	version2 = version(v2)
	if version1.major != version2.major:
		return False
	if version1.minor != version2.minor:
		return False
	if version1.patch != version2.patch:
		return False
	return True

def gt(v1, v2):
	version1 = version(v1)
	version2 = version(v2)
	if version1.major > version2.major:
		return True
	elif version1.major == version2.major:
		if version1.minor > version2.minor:
			return True
		elif version1.minor == version2.minor:
			if version1.patch > version2.patch:
				return True
			else:
				return False
		else:
			return False
	else:
		return False

def gte(v1, v2):
	version1 = version(v1)
	version2 = version(v2)
	if version1.major > version2.major:
		return True
	elif version1.major == version2.major:
		if version1.minor > version2.minor:
			return True
		elif version1.minor == version2.minor:
			if version1.patch > version2.patch:
				return True
			elif version1.patch == version2.patch:
				return True
			else:
				return False
		else:
			return False
	else:
		return False

def satisfies(v1, v2):
	version1 = version(v1)
	version2 = version(v2)
	if version1.major != version2.major:
		return False
	if version1.minor != version2.minor:
		return False
	if version2.patch >= version1.patch:
		return True
	else:
		return False

def lt(v1, v2):
	version1 = version(v1)
	version2 = version(v2)
	if version1.major < version2.major:
		return True
	elif version1.major == version2.major:
		if version1.minor < version2.minor:
			return True
		elif version1.minor == version2.minor:
			if version1.patch < version2.patch:
				return True
			else:
				return False
		else:
			return False
	else:
		return False

def lte(v1, v2):
	version1 = version(v1)
	version2 = version(v2)
	if version1.major < version2.major:
		return True
	elif version1.major == version2.major:
		if version1.minor < version2.minor:
			return True
		elif version1.minor == version2.minor:
			if version1.patch < version2.patch:
				return True
			elif version1.patch == version2.patch:
				return True
			else:
				return False
		else:
			return False
	else:
		return False
