from .file_to_write import FileToWrite
from .final_data_tag import FinalDataTag

from GroupTags import FailFirst
from GroupTags import GroupTags

from NameFile import NameSelected

from .personal_logging import PersonalLogging
from ReadFileTag import ReadFileTag
from .unsafe_file import UnsafeFile
from .write import Write


    #TODO mettere controllo che il path passato deve avere il sepratore os.sep corretto
    # altrimenti ci saranno problemi con i file


class ListTag:
    """@overview: class to list the tags in one row"""
    def __init__(self, new_args ):
        self.directory = new_args[0]

    def __repr__(self):
        return 'ListTag(%s)' % (self.directory)

    def __str__(self):
        return "ListTag(%s)" % (self.directory)

    def __eq__(self, other):
        return self.directory == other.directory
    
    def run(self):
        """run the list 
        - reading the file draft
        - building TagList
        - print the tags in a row
        """
        print("run")
        FinalDataTag(
            UnsafeFile(
                FileToWrite ( 
                    NameSelected(self.directory).name(), 
                    )
                )
                , 
                FailFirst(
                    GroupTags ( 
                        ReadFileTag(
                            self.directory
                            ).read()
                        )
                    ).calculate( ) 
            ).data()

