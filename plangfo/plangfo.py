# plangfo is a module with some tools. It only has the blob languages detection thing right now tho :P

import os
import sys
try:
    from .data import languages
except ModuleNotFoundError:
    from data import languages

class Detect(object):
    def __init__(self, directory):
        self.directory = directory
        self.languages = languages
        self.all = set()
        self.file_sizes = {}
        self.file_percentages = {}
        self.all_bytes = 0

    def get_all_files(self):
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                relDir = os.path.relpath(root, self.directory)
                relFile = os.path.join(relDir, file)
                self.all.add(relFile)
        return(self.all)

    def get_bytes(self):
        for file in self.all:
            for name, extension in self.languages.items():
                for ext in extension:
                    if file.endswith(ext):
                        fbytes = os.path.getsize(file)
                        if fbytes != 0:
                            self.all_bytes += fbytes
                            try:
                                self.file_sizes[name] += fbytes
                            except KeyError:
                                self.file_sizes[name] = fbytes
                        else:
                            pass
        return(self.file_sizes)


    def get_percentage(self):
        for filesize in self.file_sizes:
            equation = (self.file_sizes[filesize] / self.all_bytes) * 100
            equation = round(equation, 1)
            if equation != 0.0:
                self.file_percentages[filesize] = equation
            else:
                pass
        return(self.file_percentages)

    def detect(self, **kwargs):
        all_files = self.get_all_files()
        bytes_ = self.get_bytes()
        sorted_bytes = sorted(bytes_.items(), key=lambda x: x[1], reverse=True)
        sb_result = {}
        for key, val in sorted_bytes:
            sb_result[key] = val
        percentage = self.get_percentage()
        sorted_percentage = sorted(percentage.items(), key=lambda x: x[1], reverse=True)
        sp_result = {}
        for key, val in sorted_percentage:
            sp_result[key] = val
        if len(kwargs.items()) == 1:
            for parm, value in kwargs.items():
                if parm == "all_files" and value is True: return(all_files)
                elif parm == "bytes" and value is True: return(bytes_)
                elif parm == "sorted_bytes" and value is True: return(sb_result)
                elif parm == "percentage" and value is True: return(percentage)
                elif parm == "sorted_percentage" and value is True: return(sp_result)

                else: return(False)

        else:
            return(False)

def main():
    direc = "."
    if len(sys.argv) >= 3:
        direc = sys.argv[2]
        detect = Detect(direc)
        if "--ignore" in sys.argv:
            pass
        if sys.argv[1] == "-a" or sys.argv[1] == "--all-files":
            output = detect.detect(all_files=True)
        elif sys.argv[1] == "-b" or sys.argv[1] == "--bytes":
            output = detect.detect(bytes=True)
        elif sys.argv[1] == "-p" or sys.argv[1] == "--percentage":
            output = detect.detect(percentage=True)
        elif sys.argv[1] == "-sp" or sys.argv[1] == "--sorted-percentage":
            output = detect.detect(sorted_percentage=True)
        elif sys.argv[1] == "-sb" or sys.argv[1] == "--sorted-bytes":
            output = detect.detect(sorted_bytes=True)
        else:
            output = "\rThat's an argument I don't recognize. :("
        print(output)

    else:
        detect = Detect(direc)
        output = detect.detect(sorted_percentage=True)
        print(output)


if __name__ == '__main__':
    main()
