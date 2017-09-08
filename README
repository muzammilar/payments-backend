 

Payment Backend
===============

 

##### Muzammil Andul Rehman

 

Instructions:
-------------

 

-   The source code is written in Python2. The main file in the program is
    `main.py` that can be made a executable using `chmod +x` command in linux.
    The `main.py` file can be run as follows:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
usage: python main.py [-h] [--log LOG] [--logfile LOGFILE]

optional arguments:
  -h, --help         show this help message and exit
  --log LOG          INFO, WARNING, ERROR
  --logfile LOGFILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

-   `log` and `logfile` are optional arguments and the program runs with the
    default filename specified in `config.py` with `INFO` level log if no
    arguments are specified.

 

 

### Was the question/problem clear? Did you feel like something was missing or not explained correctly?

-   The question was relatively generic. The rules were a little ambigous with
    words. The words  “shorter than”, “over”, and “under”  could easily have
    included the number under considerations. I used “greater than” as the
    meaning of “over” instead of “greater than equals to”.

-   It would have been helpful to know about the level of structure that was
    required. Things like files being empty, the respective behavior, malformed
    input in one of the files was not defined. Although, my solution should
    cater for those cases but the implementation depends on how I saw things
    fit. Example, my program should parse the exchange rates file even if one of
    the entries is corrupt.

 

### What makes your solution awesome? 

While there’s always something more that could be done, Ii's tailored to my
understanding of the problem. That’s what makes it unique. Apart from the good
programming practices that I try to follow, here are a few things:

-   **Config File:** I use a config file over command line arguments for the
    filenames, although I can add more code to update the config file to handle
    both (updating config when you get command line arguments). That might be
    too much of over-engineering. Both have a different trade-offs and depends
    on the need. A config file provides ease of use while command-line
    arguements allow other programs to call this program without modifying the
    source code. There was no specific requirement for either except "any
    exceptions that may be thrown based on what rules or files are specified on
    the command line should be handled appropriately" which doesn't forces a
    developer to use either.

-   **Logging:** My solution uses a logger with different *log* levels for the
    program and it can be run as per the requirement. The output *log* file can
    be used with `grep` command to look for specific log values if the program
    is running in `INFO` mode.

-   **Command Line arguments:** The command line can be used to specify the log
    level.

-   **Package, Modules and Structure:** The primary portion of the code is
    written in the `payments` package that is imported in the main file. This
    type of structure allows the package to be moved easily and deployed on
    demand. Moreover each file in the package has a different purpose. The
    `rules.py` file deals with rules alone, `payments.py` contains the main code
    execution, `exchange.py` handles loading the exchange rates, `fhandler.py`
    is for reading writing files, and `functions.py` file implements some binary
    functions (greater than, less than) to be used for the rules.

-   **Reading/Writing Key-Value objects:** The code reads each column as a
    key-value pair instead of structured data. This means that we can
    dynamically add new columns in the file and easily add rules for then since
    things are not hard-coded.

-   **Rules for Complex Queries:** The rules in the system are a list of list.
    The rules are defined as `[[rule1 OR rule2 OR ...] AND [rule3 OR rule4] AND
    ...]` where `rule1`, `rule2`, `rule3` and `rule4` are different rules in the
    system. This allows more complex rules to be specified in the system.

 

### Did you have to make any trade-offs in your design? If so, what? 

-   **Threading, Server-Worker Model, Google MapReduce, Spark:** Due to GIL in
    Python, and relatively smaller file sizes, I chose not to implement
    multi-threading. Had I gone that route, I would have split the file at
    different ID ranges and given given each chunk to a different thread, then
    create multiple temporary files and combined them at the end. A better
    solution would have been a scalable server-worker model that I implemented a
    few years ago as in my undergraduate
    [here](https://github.com/MuzammilAR/Assignments/tree/master/Distributed%20File%20Searcher)
    [link=https://github.com/MuzammilAR/Assignments/tree/master/Distributed%20File%20Searcher].
    A better solution than that would have been to use Google MapReduce model
    with each filtration rule being a Map job and then a single reduce job to
    combine all the files. MapReduce is ideal with each rule as a map job then a
    reduce job to combine all the files with the same name. Although, I've not
    used Spark, but in my limited understanding the RDDs of Spark will be better
    than MapReduce as they provide loops as well.

-   **Structure vs No Structure (Dict vs Class):** Due to dynamic nature of the
    columns (as they can increase later) we use dict (key-value store) instead
    of a class variable for the data. Class would be for more structured data
    (with hard-coded columns), I had more unstructured data in mind. There was
    no specification in the question.

-   **Memory usage:** The currency exchange is expected to be a
    constant(*O(1)*), so we keep it in memory since reading it from disk is
    expensive. We also auto-remove duplicates. Due to space constraints we
    *parse* the *videos.csv *file instead of completely loading it into the
    memory.

-   **Command Line vs Config File:** We hard-coded filenames in the config file
    not as command line arguments. We had *logging* as a command-line argument.
    It’s a trade-off between easy and usability.

-   **Output files: **We assume that only two file types are going to be present
    for output. Otherwise, we create a mapping for each rule. The rules class
    already has a *filename* and *precedence* fields that can be used for more
    complex file decisions (eg. writing to multiple files, etc)

-   **Global variable: **Although, using global generally is not recommended but
    I have only used only one global variable for read-only exchange rates. In
    Python, global variables are limited to that specific module.

-   **Rule Lookup: **Currently, the rule lookup looks at all the rules before
    adding the row to valid. It can be made faster by maybe using some other
    data structure, like decision trees.

 

 

### Is there anything else you want to share about your solution or the problem?

 

-   We assume that none of the column headers in the videos file will be the
    same as currency code in the exchange_rates file.

-   Due the program requirement, I used a second class for rules, while the job
    could have been done by a single class and a few functions in the module.
