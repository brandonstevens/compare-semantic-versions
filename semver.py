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
			
	def equals(self, v2):
		if self.major != v2.major:
			return False
		if self.minor != v2.minor:
			return False
		if self.patch != v2.patch:
			return False
		return True

	def lt(self, v2):
		if self.major > v2.major:
			return True
		elif self.major == v2.major:
			if self.minor > v2.minor:
				return True
			elif self.minor == v2.minor:
				if self.patch > v2.patch:
					return True
				else:
					return False
			else:
				return False
		else:
			return False

	def lte(self, v2):
		if self.major > v2.major:
			return True
		elif self.major == v2.major:
			if self.minor > v2.minor:
				return True
			elif self.minor == v2.minor:
				if self.patch > v2.patch:
					return True
				elif self.patch == v2.patch:
					return True
				else:
					return False
			else:
				return False
		else:
			return False

	def satisfies(self, v2):
		if self.major != v2.major:
			return False
		if self.minor != v2.minor:
			return False
		if v2.patch >= self.patch:
			return True
		else:
			return False

	def gt(self, v2):
		if self.major < v2.major:
			return True
		elif self.major == v2.major:
			if self.minor < v2.minor:
				return True
			elif self.minor == v2.minor:
				if self.patch < v2.patch:
					return True
				else:
					return False
			else:
				return False
		else:
			return False

	def gte(self, v2):
		if self.major < v2.major:
			return True
		elif self.major == v2.major:
			if self.minor < v2.minor:
				return True
			elif self.minor == v2.minor:
				if self.patch < v2.patch:
					return True
				elif self.patch == v2.patch:
					return True
				else:
					return False
			else:
				return False
		else:
			return False
