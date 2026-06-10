# PythonPro - Python Learning Repository

A structured collection of Python learning examples from basics to advanced topics, including a complete standard library reference with real-time use cases.

## Structure

```
PythonPro/
├── 01_Basics/
│   ├── 01_variables_and_datatypes.py   # Variables, types, strings, numbers
│   ├── 02_control_flow.py             # If/else, loops, match statement
│   └── 03_functions.py                # Functions, lambda, map/filter, decorators, generators
│
├── 02_DataStructures/
│   ├── 01_lists.py                    # Lists, comprehensions, operations
│   ├── 02_dictionaries.py            # Dicts, defaultdict, Counter
│   └── 03_tuples_sets_more.py        # Tuples, sets, deque, heap
│
├── 03_OOP/
│   ├── 01_classes_and_objects.py      # Classes, inheritance, encapsulation, polymorphism
│   └── 02_advanced_oop.py            # ABC, dataclasses, magic methods, descriptors
│
├── 04_FileHandling/
│   └── 01_files_and_exceptions.py     # Files, JSON, CSV, exceptions, pathlib
│
├── 05_Advanced/
│   ├── 01_iterators_generators_decorators.py  # Custom iterators, generators, decorators
│   ├── 02_concurrency_async.py                # Threading, async/await, queues
│   └── 03_patterns_and_tricks.py              # Type hints, protocols, functools, itertools, enum
│
└── 06_StandardLibrary/                        # ★ COMPLETE STDLIB REFERENCE ★
    ├── 01_os_system_modules.py        # os, pathlib, sys, shutil, subprocess, platform, tempfile, glob, signal, atexit
    ├── 02_data_math_algorithms.py     # math, statistics, decimal, fractions, random, collections, itertools, functools, operator, bisect, heapq
    ├── 03_networking_web.py           # urllib, http, json, socket, email, xmlrpc, socketserver, ipaddress, ftplib, webbrowser, wsgiref
    ├── 04_text_fileformats.py         # re, string, textwrap, csv, configparser, xml, html, sqlite3, pickle, zipfile, struct, base64
    ├── 05_devtools_testing.py         # unittest, doctest, logging, pdb, timeit, cProfile, traceback, inspect, typing, dataclasses, abc, argparse
    ├── 06_concurrency_ipc.py          # threading, multiprocessing, concurrent.futures, asyncio, queue, sched, selectors, contextvars
    ├── 07_security_datetime.py        # hashlib, secrets, hmac, ssl, datetime, time, calendar, uuid, copy, enum, weakref, getpass
    └── 08_complete_index.py           # ALL 200+ modules indexed + Decision Guide (which module for which task)
```

## How to Run

Each file is self-contained and can be run independently:

```bash
python 01_Basics/01_variables_and_datatypes.py
python 06_StandardLibrary/08_complete_index.py
```

## Standard Library Coverage

Every module includes:
- **WHERE** — What domain/industry uses it
- **WHEN** — What triggers you to use it
- **HOW** — Working code examples with real-world context

## Requirements

- Python 3.10+ (for match statements and modern features)
- Python 3.11+ (for tomllib)
- No external packages required (all stdlib)
