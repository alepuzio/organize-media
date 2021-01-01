# Organize Media (photos and videos)

---------------

This application writes, inside an input existing directory , one directory list where the videos and photos are copied and organized in subdirectories following the year of creation, month of creation and topic.
In detail:
* I declared a ( relative or absolute) path where there are the videos and photos organized in subdirectories ('topic') and another path where writing the copied files
* The application writes the directories and subdirectories of they don't exist, otherwise they are not modified
* The structure of the final directories is based on the extension and the topic of the files


## Features and Bugs

This is the list of the future issues

  | Requirement | type | Delivered | Working | Next |
  | ----------- |----- | --------- |---------|------|
  |  In copying the files, every directory also will have a CSV file (different from media type) with the list of the files and the data (this feature will remove the **-w** flag in input) | Feature | [O] | [O] | [O] |
| Package the project| Feature | [O] | [O] | [O] | 
  | use the internal logging in python | Feature | [O] | [O] | [O] | 
  | add the control that *draft-tag* must has'nt not more than 1OO rows | Feature| [O] | [O] | [O] | 
  | create the specific file for Shutterstock: ( I put the filename, description and tags in different rows) | Feature | [O] | [O] | [O] |
  | Using *chain of command* design pattern | Feature | [O] | [O] | [O] | 
  | Create one file *draft-tag-* for every image or video, in the list I create the *selected-tags* and after, into *join* phase, for every file I'm looking for the specific file tag, I read this and I join in the final file | Feature | [O] | [O] | [O] |
  | Before writing the tags, I control that the rows have'nt it | Feature | [O] | [O] | [O] | 
  | When I create the final file CSV to upload, I have to create more than 1, so I can upload in batch way| Feature | [O] | [O] | [O] | 
  | Create directroy *realtime* and *timelapse* in directory di *copy* phase| Feature| [O] | [O] | [O] | 
  | write the file *Contribuing* like [this](https://gist.github.com/PurpleBooth/b246794O2957c63ec426/forks) | Feature | [O]| [O] | [O] |
| Organize the code: there are classes into directory test ( sistemare gli import nella directory organizemedia ) | Feature | [X] | [X] | [X] |
| use travis for CI | Feature | [X] | [X] | [X] |
| delete class *AsString* | Feature | [X] | [X] | [X] |
| fix the style in the modules | Feature | [X] | [X] | [X] |
| put classes with the tests in *tests* package and classes with no tests in *src* package, where there are only the classes without the tests | Feature | [X] | [X] | [X] |
| Write defensive class to manage the input parameters | Bug | [O] | [O] | [X]
| Fix the OOP desing as suggested by [Yegor Bugayenko](http://www.yegor256.com) | Bug | [O] | [X] | [X]
| Fix the unit test | Bug | [O] | [O] | [O]
| Fix the Test Suite | Bug | [O] | [O] |[O]
| Resolve the TODO in the code | Bug | [O] | [O] | [O]
| Organize the structure following the guidelines in[The Hitchhiker's Guide to Python!](https://docs.python-guide.org/) | Bug | [O] | [O] | [O]
| Delete the test classes where it s *import date* or *import datetime* | Bug | [O] | [O] | [O]
| Create directories *exported* and *original* in *topic* in *copy* command | Bug | [O] | [O] | [O]
| Review the system of the calculation of the more important tags | Bug | [O] | [O] | [O]



## Status CI Integration
 
 I use [Travis](https://travis-ci.org/)
 [![Build Status](https://travis-ci.org/alepuzio/organize-media.svg?branch=master)](https://travis-ci.org/alepuzio/organize-media)

## Getting started

### Prerequisites

- Python 3.0+
- pip
- pytest 

### Installing

- Clone the project with *git-clone* (or download directly it)
- Have fun!


## Running the tests

 - Run **scripts/unit_testing.sh (or bat)** 

### Break down into to end to end tests

No indications

	
### Coding styles sheets

Please read the file [CONTRIBUTING.md](http://github.com/alepuzio/organize-media/CONTRIBUTING.md)

## Deployment
 
 - No package built (sorry, I'm a beginner in Python :) )
 - Run    **>>> python Main.py $ABSOLUTE-PATH-WHERE-IT-READS-THE-EXISTING-IMG $ABSOLUTE-PATH-WHERE-IT-COPIES-TH-IMG**
 
### Built with:

* [ViM](http://www.vim.org) - one of the best text editor I know
* [pytest](https://docs.pytest.org/en/stable/) - most famous library about the unit testing in Python

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
