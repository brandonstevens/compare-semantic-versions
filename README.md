# compare-semantic-versions

A Python library that compares two semantic version strings. See [semver.org](http://semver.org/) for more information on semantic versioning.

Supports the following comparators:

* Equal ( == )
* Greater than ( > )
* Greater than or equal to ( >=)
* Pessimistic ( ~> )
* Less than ( < )
* Less than or equal to (<= )

Note: full version strings (e.g. X.Y.Z) are only supported.

Tested with:

* Python 3.5.1

Note: the library uses [exception chaining](https://www.python.org/dev/peps/pep-3134/) which is only available in Python 3.

## Usage

```python
from semver import version

print(version('1.0.0').equals(version('1.0.0')))
```

## Testing

```bash
python3 compare-semantic-versions-test.py
```

```
docker run -it --rm --name compare-semantic-versions-test -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python compare-semantic-versions-test.py
```
