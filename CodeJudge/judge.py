#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import subprocess32 as subprocess
import os
import config
import sys
from subprocess32 import PIPE
from CodeJudge import p, db
from CodeJudge.models import Submission
import time
from CodeJudge.exceptions import CompileError


def ensure_dir(path):
    """
    create dir if not exist
    :type path: str
    """
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise


def file_read(path):
    """
    read file from given path
    :param path: path string
    :return:
    """
    if not os.path.exists(path): return ""
    f = codecs.open(path, "r", "utf-8")
    d = f.read()
    f.close()
    return d


def file_write(path, data):
    """
    write data to given filename
    :param path: path string
    :param data:
    :return:
    """
    f = codecs.open(path, "w", "utf-8")
    f.write(data)
    f.close()


def outputFormatter(out):
    """
    normalizes given string
    :type out: unicode | str
    :param out:
    :return: formatted output
    """
    out = out.replace("\n", " ")
    out = out.replace("\r", " ")
    out = out.replace("\t", " ")
    outputList = out.split(" ")
    i = 0
    while i < len(outputList):
        if outputList[i] == "":
            outputList.pop(i)
            continue
        i += 1

    return " ".join(outputList)


def compile(code, exe):
    """
    compile given code to exe
    :type exe: str
    :type code: str
    :param code: code string
    :param exe: path string
    :return:
    """
    cmd = "gcc -o " + exe + " -x c -"
    p = subprocess.Popen(cmd, stdin=PIPE, stdout=None, stderr=PIPE, bufsize=1, shell=True)
    o, e = p.communicate(code)
    if e:
        print e
        raise CompileError


def execute(exe, inp, out):
    """
    execute given exe with given inputs and save output to out
    :type exe: str
    :type inp: str
    :type out: str
    :param exe: 
    :param inp: 
    :param out: 
    :return: 
    """
    # run exe using gnu coreutils timeout
    cmd = "timeout 5s " + exe + " 1>" + out
    start = time.time()
    # pipe input
    p = subprocess.Popen(cmd, stdin=PIPE, stdout=None, stderr=None, bufsize=1, shell=True)
    p.communicate(inp)
    stop = time.time()
    ti = stop - start
    return p.returncode, ti


def test(testcases, code):
    """
    compiles code and tests it with given test cases
    :param testcases: test case array
    :param code: code string
    :return: error code and time tuple
    :rtype: (str,int)
    """
    try:
        # compile code
        compile(code, exe)
        count = 1
        error_name = ""
        # start test
        time = 0
        for test in testcases:
            # define output file
            output_file = exe + ".txt"
            # ? flush pipe
            sys.stdout.flush()
            exit_code, ti = execute(exe, test[0], output_file)
            # if error not known return exit code
            error_name = exit_code
            if exit_code == 124:
                error_name = "TLE"
                break
            elif exit_code == 139:
                error_name = "SIGSEGV"
                break
            elif exit_code == 136:
                error_name = "SIGFPE"
                break
            elif exit_code == 134:
                error_name = "SIGABRT"
                break
            elif exit_code == 0:
                # limit output to 5 mb
                if os.path.getsize(output_file) > 5000000:
                    error_name = "Big Output" + str(count)
                    break
                else:
                    # read output file from disk
                    out = file_read(output_file)
                    # format outputs and compare them
                    if outputFormatter(out) == outputFormatter(test[1]):
                        error_name = "SUCCESS"
                        time += ti
                    else:
                        error_name = "TE" + str(count)
            count += 1
        return error_name, "%.3f" % time
    except CompileError:
        return "COMPILER", 0


# TODO: better listener
print "start"
ensure_dir("submissions")
while True:
    # get new submission id from redis
    message = p.get_message()
    if message:
        sid = message['data']
        print sid
        # get submission data from database
        submission = db.query(Submission).filter_by(id=sid).first()
        testcases = submission.problem.test_cases
        s = submission.code.encode('utf-8')
        dir = os.path.join(config.submissiondir, sid)
        exe = dir
        err, ti = test(testcases, s)
        submission.error = err
        submission.time = ti
        print ti
        # TODO: db error handling
        db.commit()
    time.sleep(1)  # be nice to the system :)
