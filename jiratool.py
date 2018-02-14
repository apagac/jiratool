#!/usr/bin/python

# version 0.0

# NOTES:
# these really are just excerpts from ipython with some comments
# try to work with summary where possible for better human readability


from jira import JIRA as JiraClient


# First, here is a workaround by bsquizz to make kerberos auth work
"""
Requires pykerberos, NOT kerberos!
Make sure you have the right kerb package installed. If 'kerberos' was installed it needs to be
removed and pykerberos re-installed.
"""
class JiraClientOverride(JiraClient):
    def _create_kerberos_session(self, *args, **kwargs):
        """
        Little hack to get auth cookies from JIRA when using kerberos, otherwise
        queries to other URLs hit a 401 and are not handled properly for some
        reason
        https://stackoverflow.com/questions/21578699/jira-rest-api-and-kerberos-authentication
        """
        super(JiraClientOverride, self)._create_kerberos_session(*args, **kwargs)
        self._session.get("{}/step-auth-gss".format(self._options['server']))
        # added by apagac
        # TODO this is a workaround, investigate?
        from requests_kerberos import HTTPKerberosAuth, DISABLED
        self._session.auth = HTTPKerberosAuth(mutual_authentication=DISABLED)


# Initialize jira client, make it connect to the server
# TODO hardcoded url
jira = JiraClientOverride("https://projects.engineering.redhat.com", kerberos=True,
                          options={"verify": False})   


"""
Follows a chunk of code you can use while looking around jira and searching for stuff
"""

# get all sprints from the board
# "CloudForms QE Sprints" board.id == 1651
sprints = jira.sprints("1651")

# a number of the current sprint
sprint_number = 22

# find our sprint
def find_sprint_by_number(sprints, num):
    for sprint in sprints:
        if str(num) in sprint.name:
            return sprint

# get our current sprint
sprint = find_sprint_by_number()


"""
An easy way to get all your stories from the current sprint
""" 

myissues = jira.search_issues('project = RHCFQE and assignee = currentUser() and sprint in openSprints()')

# print summaries of stories
for issue in myissues:
    print issue.fields.summary
