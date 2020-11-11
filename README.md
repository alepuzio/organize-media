# Organize Media (photos and videos)
--------
This application writes, inside an input existing directory , one directory list where the videos and photos are copied and organized in subdirectories following the year of creation, month of creation and topic.
In detail:
* I declared a ( relative or absolute) path where there are the videos and photos organized in subdirectories ('topic') and another path where writing the copied files
* The application writes the directories and subdirectories of they don't exist, otherwise they are not modified
* The structure of the final directories is based on the extension and the topic of the files


## Features

### Future
* In copying the files, every directory also will have a CSV file (different from media type) with the list of the files and the data (this feature will remove the -w flag in input)
* Package the project
* use the internal logging in python
* add the control that _draft-tag_ must has'nt not more than 100 row
* create the specific file for Shutterstock: ( I put the filename, description and tags in different rows)
* Using _chain of command_ desing pattern
* Create one file _draft-tag-_ for every image or video, in the list I create the _selected-tags_ and after, into _join_ phase, for every file I'm looking for the specific file tag, I read this and I join in the final file
* Before writing the tags, I control that the rows have'nt it
* When I create the final file CSV to upload, I have to create more than 1, so I can upload in batch way
* Create directroy _realtime_ and _timelapse_ in directory di _copy_ phase

### Next
* write the file _Contribuing_ like  [this](https://gist.github.com/PurpleBooth/b24679402957c63ec426/forks)

### Running


### Past

* Organize the code: there are classes into directory test ( sistemare gli import nella directory organizemedia )
* use travis for CI
* delete class _AsString_
* fix the style in the modules
* put classes with the tests in _tests_ and importo _test classes_ in package _organizedmedia_, where there are only the classes withou test


## Bug

### Future
* Fix the unit test
* fix the Test Suite
* Resolve the TODO in the code
* Organize the structure following the guidelines in[The Hitchhiker's Guide to Python!] (https://docs.python-guide.org/)
* Delete the test classes where it s _import date_ or _import datetime_
* Create directories _exported_ and _original_ in _topic_ in _copy_ command
* review the system of the calculation of the more important tags

### Next
* Write defensive class to manage the input parameters

### Running

### Past




## Status CI Integration
 
 I use [Travis](https://travis-ci.org/)
 [![Build Status](https://travis-ci.org/alepuzio/organize-media.svg?branch=master)](https://travis-ci.org/alepuzio/organize-media)

## Getting started

### Prerequisites

- Python 3.0+
- pip
- unittest 

### Installing

- Clone the project with _git-clone_ (or download directly it)
- Have fun!


## Running the tests

 - Run __python -m unittest TestSuiteProject-A-L.py__ and __python -m unittest TestSuiteProject-M-Z.py__ : the letter indicates the first letter of the module in the current TestSuite

### Break down into to end to end tests

No indications

	
### Coding styles sheets

Please read the file [CONTRIBUTING.md](http://github.com/alepuzio/organize-media/CONTRIBUTING.md)

## Deployment
 
 - No package built (sorry, I'm a beginner in Python :) )
 - Run    __>>> python Main.py $ABSOLUTE-PATH-WHERE-IT-READS-THE-EXISTING-IMG $ABSOLUTE-PATH-WHERE-IT-COPIES-TH-IMG__
 
### Built with:

* [ViM](http://www.vim.org) - one of the best text editor I know
* [unittest](https://docs.python.org/3/library/unittest.html) - most famous library about the unit testing in Python

## Contributing

Please read the [Contributing.md](http://github.com/alepuzio/organize-media/CONTRIBUTING.md) for the details about the code of conduct and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/alepuzio/organize-media/tags). 

## Authors

* **Alessandro Puzielli** - *creator* - [Alepuzio](https://github.com/alepuzio)

See also the list of [contributors](https://github.com/alepuzio/organize-media/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **PurpleBooth** - to publish an [excellent template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) of README that I used in this project 
* **Yegor256** - to write the post [Elegant READMEs](https://www.yegor256.com/2019/04/23/elegant-readme.html) about the README file and the [An Open Code Base Is Not Yet an Open Source Project](https://www.yegor256.com/2018/05/08/open-source-attributes.html) for the Open Source projects
