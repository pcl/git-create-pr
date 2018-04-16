## Introduction

Generate GitHub pull requests for the current branch without leaving the
command line!

It is common to use git + GitHub in a pull-request-focused manner, in which 
the master branch is in a central team-accessible repository, and day-to-day
development happens in personal forks of that repository. In this model, the
developers push their code to their personal forks and then use the GitHub
UI to create a pull request (PR) for those changes.

GitHub provides the `hub` CLI tool to help facilitate this workflow, by making
it simple to fork a central repository into your personal workspace. However,
the `hub` tool does not provide any means to create a PR from the command
line. So, after pushing changes to a new personal branch, developers must 
open a browser window, navigate to their personal fork, and then click the 
'create PR' link that appears after they push.

`git create-pr` automates this process by analyzing your local branch and
personal fork and using the GitHub APIs to generate a PR against the origin
repository.


## Usage

    $ <make changes with $EDITOR>
    $ git commit -m "awesomeness here"
    $ git push $USER HEAD:awesomeness
    $ git create-pr


## Requirements and Limitations

This is nascent code. It doesn't handle errors very well, and doesn't
do much precondition analysis. Use at your own risk; YMMV; etc.

The code assumes that your upstream is named `origin` and that your 
remote URLs conform to the `git@...` protocol format.


## Contributing

Contributions are welcome! I suggest that you create a PR if you've 
got any improvements. Or even better, if you want to set up a test 
harness!

See the [issues list](https://github.com/pcl/git-create-pr/issues)
if you're looking for inspiration.