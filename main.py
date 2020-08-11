#!/usr/bin/env python

import os


def executeCommand(command):
    stream = os.popen(command)
    output = list(map(lambda x: x.strip(), stream.readlines()))#.split("\n")
    return output

def getPackages():
    command ='dnf history | grep install | cut -d"|" -f1 | head -n1 | xargs dnf history info | grep Install | sed -r "s/.*Install (.*) .*/\\1/"'
    return executeCommand(command)

def getBinaries(package):
    command = "rpm -qi --filesbypkg " + package + " | grep -Eo /.*bin/.*"
    return executeCommand(command)

def installPackage(packageName, category = "Default"):
    command = "podman container list -all | sed -r 's/.*\s([[:alnum:]]+)\s*$/\\1/'"
    toolboxes = executeCommand(command)
    categories = toolboxes[1:]

    if category not in categories:
        print("Creating container " + container)
        executeCommand("toolbox create -c " + category )

    executeCommand("toolbox run -c " + category + " sudo dnf install -y " + package)

print(getPackages())
