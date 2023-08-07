import sys
import os
import timeit

import cProfile

def filename_without_extension(full_filename):
    base_name = os.path.basename(full_filename)  # Get the base filename from the full path
    filename_without_ext, _ = os.path.splitext(base_name)  # Split filename and extension
    return filename_without_ext

class Solution:
    def __init__(self, N = 0, abstract = None, profile = False):
        self.N = N
        self.abstract = abstract
        self.profile = profile

    def log(self, text):
        print("[ParadOEIS] {}".format(text), flush = True)

    def logic(self) -> list:
        self.log("Please overwrite the logic function...")
        return None

    def run(self):
        #self.log("Executing ParadOEIS Solution '{}' where N = {}".format(sys.argv[0].replace(".py", ""), self.N))
        self.log("Executing Solution {} where N = {}".format(filename_without_extension(sys.argv[0]), self.N))
        if self.abstract is not None:
            self.log("Abstract: {}".format(self.abstract))

        # [TODO] Get this to actually time things and run value check
        if self.profile:
            # It may be possible for the subclass to rename the logic function, here we address that
            name = self.logic.__name__
            cProfile.run("{}()".format(name))
            return

        beg = timeit.default_timer()
        value = self.logic()
        fin = timeit.default_timer()

        self.log("Finished executing in {:.4f} seconds".format(fin - beg))

        if value is not None:
            self.log("The resulting value(s) are as follows\n{}".format(value))

        # Kept so that I don't have to go back to my ProjectEuler project
        # [TODO] To be removed eventually
        """
        if self.value == None:
            if value == None: self.log("The correct value is not known, and no value was discovered")
            else: self.log("The correct value is not known, however the value {} was discovered".format(value))
        else:
            if value != self.value: self.log("The correct value is {}, however an incorrect value of {} was discovered".format(self.value, value))
            else: self.log("Congratulations, the correct value of {} was discovered!".format(value))
        """
