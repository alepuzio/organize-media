# Organize Media (photos and videos)
--------
Questa applicazione crea, in una directory esistente passata come argomento, una lista di directory dove sono memorizzati file video e foto in base all'anno e al mese di creazione.

Più precisamente:
* Passo un path dove ci sono le mie fotografie divise per soggetto ('topic') e un path dove scrivere le copie organizzate
* Il programma crea le directory se già non eistono, altrimenti le lascia invariate
* La struttura delle directory finali si basa sull'estensione e il soggetto dei file


## Evolutive

* Quando i file sono stati copiati, in ogni directory sarà creato un file CSV adatto (in funzione del Media) con la lista dei file e i dati da caricare su Pond5
* Preparare sistemare di pacchettizzazione

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

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Alessandro Puzielli** - *creator* - [Alepuzio](https://github.com/alepuzio)

See also the list of [contributors](https://github.com/alepuzio/organize-media/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **PurpleBooth** - to publish an [excellent template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) of README that I used in this project 
* **Yegor256** - to write the post [Elegant READMEs](https://www.yegor256.com/2019/04/23/elegant-readme.html) about the README file and the [An Open Code Base Is Not Yet an Open Source Project](https://www.yegor256.com/2018/05/08/open-source-attributes.html) for the Open Source projects
