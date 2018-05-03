import json
import responses
import requests
import unittest

# Currently, the source is all in one file for ease of deployment.
# And the file is named according to the git tool conventions. So,
# some voodoo is necessary.
import types
import importlib.machinery
import os
path = os.path.abspath(os.path.dirname(__file__) + "/../git-pr")
loader = importlib.machinery.SourceFileLoader('git_pr', path)
git_pr = types.ModuleType(loader.name)
loader.exec_module(git_pr)


class TestGitPRCreate(unittest.TestCase):

    def graphql_callback(self, request):
        payload = json.loads(request.body)
        if payload['query'] == self.prc.suggested_reviewers_query(7):
            return (200, {}, '{"data": {"repository": {"pullRequest": '
                    '{ "suggestedReviewers": [ { "reviewer": { "login": "pcl" } } ] } } } }')
        else:
            return (404, {}, "Un-tested graphql")
                                                                  
    def setUp(self):
        responses.add(responses.POST, 'https://api.github.com/repos/pcl/git-pull-request/pulls',
                      json={'number': 7}, status=200)
        responses.add_callback(responses.POST, 'https://api.github.com/graphql', self.graphql_callback)
        responses.add(responses.POST, 'https://api.github.com/repos/pcl/git-pull-request/pulls/7/requested_reviewers',
                      json={'html_url': 'https://api.github.com/pcl/git-pull-request/pulls/7'}, status=200)

        self.prc = git_pr.PullRequestController()
        self.prc.interactive = False

    @responses.activate
    def test_create_pr(self):
        self.prc.configure()

        self.assertEqual('https://api.github.com', self.prc.rest_api)
        self.assertEqual('https://api.github.com/graphql', self.prc.graphql_api)
        self.assertEqual('https://github.com', self.prc.web_url)
        self.assertEqual('pcl', self.prc.origin_org)
        self.assertEqual('git-pull-request', self.prc.origin_repo)

        self.assertEqual(0, self.prc.create_pr('origin', 'branch', 'pcl'))
        
