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
the `hub` tool has only basic support for creating and managing PRs from the
command line. So, after pushing changes to a new personal branch, developers 
end up opening a browser window, navigating to their personal fork, and then 
interacting with the PR management web UI

`git pr` simplifies this process by analyzing your local branch and
personal fork and using the GitHub APIs to generate and manage PRs against
the origin repository.


## Installation

The easiest way to install `git pr` on a Mac is to use `brew`:

    $ brew install https://raw.githubusercontent.com/pcl/homebrew-git-pull-request/master/git-pull-request.rb

If you're using Windows or Linux, download the `git-pr`
[script](https://raw.githubusercontent.com/pcl/git-pull-request/master/git-pr)
and put it somewhere in your path.

## Usage

    $ <make changes with $EDITOR>
    $ git commit -m "awesomeness here"
    $ git push $USER HEAD:awesomeness
    $ git pr create


## Requirements and Limitations

This is nascent code. It doesn't handle errors very well, and doesn't do 
much precondition analysis. Use at your own risk; YMMV; etc.

The code assumes that your upstream is named `origin` and that your remote
URLs conform to the `git@...` protocol format.


## Contributing

Contributions are welcome! I suggest that you create a PR if you've got
any improvements. 

See the [issues list](https://github.com/pcl/git-create-pr/issues) if 
you're looking for inspiration.


## Other Command-Line Pull Request Tools

There are a number of other CLI tools for interacting with GitHub PRs
from the command line, none of which did quite what I was looking
for. Here are some others that I've found:

- https://github.com/vitorgalvao/tiny-scripts/blob/master/climergebutton
- https://github.com/jd/git-pull-request
- https://pypi.org/project/git-pr/