# S3Cruze
[![Python |2.7](https://img.shields.io/badge/python-2.7-yellow.svg)](https://www.python.org/) [![Twitter](https://img.shields.io/badge/twitter-@JR0ch17-blue.svg)](https://twitter.com/JR0ch17)

This tool is based off of the Sandcastle projet from @yasinS. Using a word list, it will enumerate buckets and list files (if allowed). You can also choose to try to upload a test file, or attempt to view a bucket's ACL, policy, CORS configuration, replication configuration, website configuration and bucket location. You also have the option to check a single bucket that you have already found elsewhere. 



## AWS-CLI
- For this tool to work properly, you need to have **AWS-CLI** installed (http://docs.aws.amazon.com/cli/latest/userguide/installing.html). - Once installed, you need to run `$ aws configure` to configure your AWS Access Keys.



## How to use S3Cruze
1. Clone this repo
2. Run s3cruze.py with your target name. You can also specify your own dictionnary file if you'd like and you can also select if you want to try to upload a file or not. The default behavior will only enumerate buckets.

```
usage: s3cruze.py [-h] -t targetBucket [-f inputFile] [-u] [-d] [-a] [-p]
                   [-c] [-r] [-w] [-l] [--all] (-b | -s)

optional arguments:
  -h, --help            show this help message and exit
  -t targetBucket, --target targetBucket
                        Select a target bucket name (e.g. 'shopify')
  -f inputFile, --file inputFile
                        Select a bucket brute-forcing file (default: bucket-
                        names.txt)
  -u, --upload          File to upload will be automatically generated (e.g.
                        'BugBounty-[######].txt')
  -d, --delete          Delete file from bucket after uploading it
  -a, --acl             View bucket ACL
  -p, --policy          View bucket policy
  -c, --cors            View bucket CORS configuration
  -r, --replication     View bucket replication configuration
  -w, --website         View bucket website configuration
  -l, --location        View bucket location
  --all                 View all bucket configuration
  -b, --bruteforce      Bruteforce buckets names. By default it will try to
                        list files from the buckets.
  -s, --single          Check a single bucket only

  
```



## Contributions
I'm just beginning to code in Python so if you feel it could work better by coding it in a certain way, please feel free to create pull requests, it would be greatly appreciated. Honestly, please do. 

If needed, I can also be reached via Twitter @JR0ch17.
