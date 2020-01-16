# tiny-file-grouper
A simple HTTP server with digest auth that allows you to PUT files into groups. Then, you can download the group as gz compressed tar archive, which will also delete the group. tiny-file-grouper has digest authentication (credentials configurable at the top of server.py) no one can touch your groups.

You can also use the `+` symbol to indicate adding a file to multiple groups.

Example:
    
    curl -T file1.txt -c /dev/null --digest -u user:password http://localhost/group1/
    curl -T file2.txt -c /dev/null --digest -u user:password http://localhost/group2/
    curl -T file3.txt -c /dev/null --digest -u user:password http://localhost/group1+group2/
    curl -o g1.tar.gz -c /dev/null --digest -u user:password http://localhost/download/group1 

The file test.tar.gz will all files added to the group previously. No traces of group1 will be left after this point, however group2 is still available.
