# pyfiledb

## Simple mark on a file
Do you find yourself searching for files in your daily work?
I am one of them.
This pyfiledb is a simple way to mark a file path with an arbitrary hashtag, just like YouTube or Instagram.
You can search for files by adding any hashtag to the file's path.

It has three interfaces (API, CLI, and GUI), and all of them are completely free.(MIT License)

## Using API
Install pyfiledb.
```bash
>python setup.py install
```

append adds file information, and search allows hash searches.
```python
>>> from pyfiledb import pyfiledb
>>>> filedb = pyfiledb()
>>> filedb.append('xxx/yyy/zzz.txt', '#hash1#hash2')
>>>> filedb.search('#hash2')
{'xxx/yyy/zzz.txt': '#hash1#hash2'}
>>> filedb.close()
```

## Using CLI
INSTALL pyfiledb.
````bash
>python setup.py install
```

Add file information with append.
```bash
> pyfiledb-cli add
path: xxx/yyyy/zzz.txt  
hashs: #hash1#hash2
````

search to search for hashes
```bash
> pyfiledb-cli search
hashs: #hash1 
-[0]-------------
path: xxx/yyyy/zzz.txt
hashs: #hash1#hash2
```

## Using GUI
Install kivy.
```bash
>pip install kivy
```

Start the GUI application is the following code.
```bash
>python -m pyfiledb.gui
```


## Future improvements.
* Ability to delete profiles of registered files.
* Ahead-Of-Time compilation of CLI and GUI
* Optimization of search algorithm
* Support for with statements
