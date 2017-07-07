# S3Cruze
This tool is based off of the Sandcastle projet from @yasinS. It will look for bucket names using a dictionnary and try to upload a file to the identified buckets.

## AWS-CLI
- For this tool to work properly, you need to have [AWS-CLI] installed (http://docs.aws.amazon.com/cli/latest/userguide/installing.html). - Once installed, you need to run `aws configure` to configure your AWS Access Keys.

### How to use S3Cruze
1. Clone this repo
2. Run s3cruze.py with your target name and dictionnary file and upload file if needed

```
usage: test.py [-h] -t targetBucket [-f inputFile] [-u uploadFile]

optional arguments:
  -h, --help            show this help message and exit
  -t targetBucket, --target targetBucket
                        Select a target bucket name (e.g. 'shopify')
  -f inputFile, --file inputFile
                        Select a bucket brute-forcing file (default: bucket-
                        names.txt)
  -u uploadFile, --upload  uploadFile
                        File to upload will be automatically generated (e.g.
                        'BugBounty-[######].txt')
```
