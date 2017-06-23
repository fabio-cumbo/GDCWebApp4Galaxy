#!/usr/bin/env python
import json_collect_data_source as jcds
import optparse

__version__ = "1.0.0"

def __main__():
    """ Read the JSON return from a data source. Parse each line and request
    the data, download to "newfilepath", and write metadata.

    Schema
    ------

        [ {"url":"http://url/to/file.tar.gz",
           "name":"My Archive",
           "extension":"tar.gz",
           "organize":"true",
           "metadata":{"db_key":"hg38"},
           "extra_data":[ {"url":"http://url_of_ext_file",
                           "path":"rel/path/to/ext_file"}
                        ]
          }
        ]

    """
    # Parse the command line options
    usage = "Usage: jcds_wrapper.py max_size --json_param_file filename [options]"
    parser = optparse.OptionParser(usage = usage)
    parser.add_option("-j", "--json_param_file", type="string",
                    action="store", dest="json_param_file", help="json schema return data")
    parser.add_option("-p", "--path", type="string",
                    action="store", dest="path", help="new file path")
    # set appdata: temporary directory in which the archives will be decompressed
    parser.add_option("-a", "--appdata", type="string",
                    action="store", dest="appdata", help="appdata folder name")
    parser.add_option("-v", "--version", action="store_true", dest="version",
                    default=False, help="display version and exit")

    (options, args) = parser.parse_args()
    if options.version:
        print __version__
    else:
        jcds.download_from_json_data( options, args )


if __name__ == "__main__": __main__()
