#!/usr/bin/env python
# -*- coding: utf-8 -*-

print """
 ____ ____                     _____
/ ___|___ / ____  _ __  _   _ /__   /_____
\___ \ |_ \|  __|| '__|| | | |   / /| ____|
 ___) ___) | |__ | |   | |_| | / /_ | ____|
|____/____/|____||_|    \__,_|/____/|_____|

S3 bucket enumeration and file upload
Release v1.0 
By JR0ch17
"""


import sys, os, commands, requests, random
from argparse import ArgumentParser
from random import randrange

randomNumber = randrange(100000, 999999)
uploadFile = "BugBounty-%s.txt" % randomNumber
inputFile = ""
targetBucket = ""
upload = ""

file = open(uploadFile, 'w+')
file.write("This is a file upload test for bug bounty purposes")
file.close()

parser = ArgumentParser()
parser.add_argument("-t", "--target", dest="targetBucket", help="Select a target bucket name (e.g. 'shopify')", metavar="targetBucket", required="True")
parser.add_argument("-f", "--file", dest="inputFile", help="Select a bucket brute-forcing file (default: bucket-names.txt)", default="bucket-names.txt", metavar="inputFile")
parser.add_argument("-u", "--upload", dest="upload", help="File to upload will be automatically generated (e.g. 'BugBounty-[######].txt')", default=False, action="store_true") 

args = parser.parse_args()

with open(args.inputFile, 'r') as f:
    bucketName = [line.strip() for line in f]
    lineCount = len(bucketName)

print "[*] Starting enumeration of the '%s' bucket, reading %i lines from '%s'. \n" % (args.targetBucket, lineCount, f.name)

for name in bucketName:
        r = requests.head("http://%s%s.s3.amazonaws.com" % (args.targetBucket, name))
        if r.status_code != 404:
                print "\n [+] Checking potential match: %s%s --> %s." % (args.targetBucket, name, r.status_code)
                ls = commands.getoutput("/usr/local/bin/aws s3 ls s3://%s%s" % (args.targetBucket, name))
                print ls
		
		if args.upload:
				    print "[+] Uploading file: %s." % (uploadFile)	
				    cp = commands.getoutput("/usr/local/bin/aws s3 cp %s s3://%s%s" % (uploadFile, args.targetBucket, name))
                		    print "%s \n" % (cp)
		else:
				    sys.stdout.write('')
        else:
                sys.stdout.write('')


os.remove("%s" % (uploadFile))

print "\n [*] S3Cruze is now complete on %s." % (args.targetBucket)

