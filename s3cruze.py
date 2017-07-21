#!/usr/bin/env python
# -*- coding: utf-8 -*-

print """
 ____ ____                     _____
/ ___|___ / ____  _ __  _   _ /__   /_____
\___ \ |_ \|  __|| '__|| | | |   / /| ____|
 ___) ___) | |__ | |   | |_| | / /_ | ____|
|____/____/|____||_|    \__,_|/____/|_____|

Release v1.2
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
delete = ""
acl = ""
policy = ""

def wordMixing(target, word):
    wordList = ["{0}{1}".format(target, word)]
    wordList.append("{0}-{1}".format(target, word))
    wordList.append("{1}-{0}".format(target, word))
    wordList.append("{1}{0}".format(target, word))
    return wordList

file = open(uploadFile, 'w+')
file.write("This is a file upload test for bug bounty purposes")
file.close()

parser = ArgumentParser()
parser.add_argument("-t", "--target", dest="targetBucket", help="Select a target bucket name (e.g. 'shopify')", metavar="targetBucket", required="True")
parser.add_argument("-f", "--file", dest="inputFile", help="Select a bucket brute-forcing file (default: bucket-names.txt)", default="bucket-names.txt", metavar="inputFile")
parser.add_argument("-u", "--upload", dest="upload", help="File to upload will be automatically generated (e.g. 'BugBounty-[######].txt')", default=False, action="store_true")
parser.add_argument("-d", "--delete", dest="delete", help="Delete file from bucket after uploading it", default=False, action="store_true")
parser.add_argument("-a", "--acl", dest="acl", help="View bucket ACL", default=False, action="store_true")
parser.add_argument("-p", "--policy", dest="policy", help="View bucket policy", default=False, action="store_true")
parser.add_argument("-c", "--cors", dest="cors", help="View bucket CORS configuration", default=False, action="store_true")
parser.add_argument("-r", "--replication", dest="replication", help="View bucket replication configuration", default=False, action="store_true")
parser.add_argument("-w", "--website", dest="website", help="View bucket website configuration", default=False, action="store_true")
parser.add_argument("--all", dest="all", help="View all bucket configuration", default=False, action="store_true")
args = parser.parse_args()

with open(args.inputFile, 'r') as f:
    bucketName = [line.strip() for line in f]
    lineCount = len(bucketName)

for name in bucketName:
    wordList = wordMixing(args.targetBucket, name)
    for word in wordList:
        r = requests.head("http://%s.s3.amazonaws.com" % (word))
        if r.status_code != 404 and r.status_code != 503:
                print "\n [+] Checking potential match: %s --> %s." % (word, r.status_code)
                ls = commands.getoutput("/usr/bin/aws s3 ls s3://%s" % (word))
                print ls

                if args.all:
                        print "[+] Checking %s bucket configuration." % (word)
                        acl = commands.getoutput("/usr/bin/aws s3api get-bucket-acl --bucket %s" % (word))
                        policy = commands.getoutput("/usr/bin/aws s3api get-bucket-policy --bucket %s" % (word))
                        cors = commands.getoutput("/usr/bin/aws s3api get-bucket-cors --bucket %s" % (word))
                        replication = commands.getoutput("/usr/bin/aws s3api get-bucket-replication --bucket %s" % (word))
                        website = commands.getoutput("/usr/bin/aws s3api get-bucket-website --bucket %s" % (word))
                        print "%s %s %s %s %s"% (acl, policy, cors, replication, website)

                else:
                        sys.stdout.write('')


                if args.acl:
                        print "[+] Checking %s bucket ACL." % (word)
                        acl = commands.getoutput("/usr/bin/aws s3api get-bucket-acl --bucket %s" % (word))
                        print "%s \n" % (acl)
                else:
                        sys.stdout.write('')

                if args.policy:
                        print "[+] Checking %s bucket policy." % (word)
                        policy = commands.getoutput("/usr/bin/aws s3api get-bucket-policy --bucket %s" % (word))
                        print "%s \n" % (policy)

                else:
                        sys.stdout.write('')

                if args.cors:
                        print "[+] Checking %s bucket CORS configuration." % (word)
                        cors = commands.getoutput("/usr/bin/aws s3api get-bucket-cors --bucket %s" % (word))
                        print "%s \n" % (cors)

                else:
                        sys.stdout.write('')

                if args.replication:
                        print "[+] Checking %s bucket replication configuration." % (word)
                        replication = commands.getoutput("/usr/bin/aws s3api get-bucket-replication --bucket %s" % (word))
                        print "%s \n" % (replication)

                else:
                        sys.stdout.write('')

                if args.website:
                        print "[+] Checking %s bucket website configuration." % (word)
                        website = commands.getoutput("/usr/bin/aws s3api get-bucket-website --bucket %s" % (word))
                        print "%s \n" % (website)

                else:
                        sys.stdout.write('')


                if args.upload:
                        print "[+] Uploading file: %s." % (uploadFile)
                        cp = commands.getoutput("/usr/bin/aws s3 cp %s s3://%s" % (uploadFile, word))
                        print "%s \n" % (cp)

                        if args.delete:
                            print "[+] Delete file: %s." % (uploadFile)
                            rm = commands.getoutput("/usr/bin/aws s3 rm s3://%s/%s" % (word, uploadFile))
                            print "%s \n" % (rm)

                        else:
                            sys.stdout.write('')
                else:
                        sys.stdout.write('')
        else:
                sys.stdout.write('')


os.remove("%s" % (uploadFile))

print "\n [*] S3Cruze is now complete on %s." % (args.targetBucket)
