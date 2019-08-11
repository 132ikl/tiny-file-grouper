# tiny-file-grouper
A simple HTTP server with digest auth that allows you to PUT files into groups. Then you can download the group as gz compressed tar archive, which will also delete the group.

Example:
    
    curl -T file1.txt -c /dev/null --digest -u user:password http://localhost:5000/testgroup/
    curl -T file2.txt -c /dev/null --digest -u user:password http://localhost:5000/testgroup/
    curl -c /dev/null --digest -u user:password http://localhost:5000/download/testgroup --output test.tar.gz

The file test.tar.gz will contain a folder called "testgroup", which contains all files added to the group previously.
