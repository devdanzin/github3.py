from base import BaseTest, expect, str_test
from datetime import datetime
from github3.legacy import LegacyIssue


class TestLegacyIssue(BaseTest):
    def __init__(self, methodName='runTest'):
        super(TestLegacyIssue, self).__init__(methodName)
        issues = self.g.search_issues(self.sigm, self.todo, 'closed',
                'iter_todos')
        self.issue = issues[0]

    def test_legacy_issue(self):
        expect(self.issue).isinstance(LegacyIssue)
        expect(repr(self.issue)).isinstance(str_test)
        expect(repr(self.issue)) != ''

    def test_body(self):
        expect(self.issue.body).isinstance(str_test)
        expect(self.issue.body) != ''

    def test_comments(self):
        expect(self.issue.comments) == 2

    def test_created_at(self):
        expect(self.issue.created_at).isinstance(datetime)

    def test_gravatar_id(self):
        expect(self.issue.gravatar_id).isinstance(str_test)
        expect(self.issue.gravatar_id) == 'c148356d89f925e692178bee1d93acf7'

    def test_html_url(self):
        expect(self.issue.html_url).isinstance(str_test)
        expect(self.issue.html_url) == ('https://github.com/sigmavirus24/'
                'Todo.txt-python/issues/1')

    def test_labels(self):
        expect(self.issue.labels) == ['Enhancement']

    def test_number(self):
        expect(self.issue.number) == 1

    def test_position(self):
        expect(self.issue.position) == 1.0

    def test_state(self):
        expect(self.issue.state).isinstance(str_test)
        expect(self.issue.state) == 'closed'

    def test_title(self):
        expect(self.issue.title).isinstance(str_test)
        expect(self.issue.title) == 'Change get_todos()?'

    def test_updated_at(self):
        expect(self.issue.updated_at).isinstance(datetime)

    def test_user(self):
        expect(self.issue.user).isinstance(str_test)
        expect(self.issue.user) == 'sigmavirus24'

    def test_votes(self):
        expect(self.issue.votes) == 0


class TestLegacyRepo(BaseTest):
    def __init__(self, methodName='runTest'):
        super(TestLegacyRepo, self).__init__(methodName)
        repos = self.g.search_repos('Todo.txt-python', language='python')
        for r in repos:
            if r.owner == 'sigmavirus24':
                self.repo = r
                break

    def test_created(self):
        expect(self.repo.created).isinstance(datetime)

    def test_created_at(self):
        expect(self.repo.created_at).isinstance(datetime)

    def test_description(self):
        expect(self.repo.description).isinstance(str_test)
        expect(self.repo.description) == ("Python version of Gina "
                "Trapani's popular bash script.")

    def test_followers(self):
        expect(self.repo.followers) >= 0

    def test_forks(self):
        expect(self.repo.forks) >= 0

    def test_has_downloads(self):
        expect(self.repo.has_downloads()).is_False()

    def test_has_issues(self):
        expect(self.repo.has_issues()).is_False()

    def test_has_wiki(self):
        expect(self.repo.has_wiki()).is_False()

    def test_homepage(self):
        expect(self.repo.homepage).isinstance(str_test)

    def test_is_fork(self):
        expect(self.repo.is_fork()).is_False()

    def test_language(self):
        expect(self.repo.language).isinstance(str_test)
        expect(self.repo.language) == 'Python'

    def test_name(self):
        expect(self.repo.name) == self.todo

    def test_open_issues(self):
        expect(self.repo.open_issues) >= 0

    def test_owner(self):
        expect(self.repo.owner) == self.sigm

    def test_is_private(self):
        expect(self.repo.is_private()).is_False()

    def test_pushed(self):
        expect(self.repo.pushed).isinstance(datetime)

    def test_pushed_at(self):
        expect(self.repo.pushed_at).isinstance(datetime)

    def test_score(self):
        expect(self.repo.score) == 0.0

    def test_size(self):
        expect(self.repo.size) >= 1

    def test_type(self):
        expect(self.repo.type) == 'repo'

    def test_user(self):
        expect(self.repo.user) == self.sigm

    def test_url(self):
        expect(self.repo.url).isinstance(str_test)

    def test_watchers(self):
        expect(self.repo.watchers) >= 0


class TestLegacyUser(BaseTest):
    def __init__(self, methodName='runTest'):
        super(TestLegacyUser, self).__init__(methodName)
