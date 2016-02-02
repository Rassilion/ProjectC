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


def ensure_dir(f):
    try:
        os.makedirs(f)
    except OSError:
        if not os.path.isdir(f):
            raise


# File Read/Write Functions
def file_read(filename):
    if not os.path.exists(filename): return ""
    f = codecs.open(filename, "r", "utf-8")
    d = f.read()
    f.close()
    return d.replace("\r", "")


def file_write(filename, data):
    f = codecs.open(filename, "w", "utf-8")
    f.write(data.replace("\r", ""))
    f.close()


def outputFormatter(out):
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
    cmd = "gcc -o " + exe + " -x c -"
    p = subprocess.Popen(cmd, stdin=PIPE, stdout=None, stderr=PIPE, bufsize=1, shell=True)
    o, e = p.communicate(code)
    if e:
        print e
        raise CompileError


def execute(exe, inp, out):
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
