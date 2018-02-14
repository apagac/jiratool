# jiratool
A jira wrapper written in python

Link to original kerberos workaround by bsquizz:
https://gist.github.com/bsquizz/119b1c98b8f8670f0768e1d046b602c2

Follows a updated copy of the original draft document:

# Purpose

jiratool is a command-line tool written in python and designed to ease and shorten tasks that we engineers have to do when working with jira. This includes logging work, adding comments, watching status of PR requests, moving cards to different columns, creating new cards etc. For a full list of proposed functionality see Examples of use.


# Used technologies

This program will be leveraging kerberos (kinit) to authenticate user against server, so seamless operation is expected. For communicating with jira the program will be using Jira python library [1], for communicating with github it will be using most probably PyGithub [2].


# Examples of use

Here is proposed usage of the new tool. This should present an overview of what can be expected.

jiratool alias RHCFQE-6112 mystory
 - creates a local alias for the ugly jira story ID and enables to use this as a unique card name

jiratool id mystory
 - prints the ugly jira ID for an alias mystory

jiratool time log mystory 1 -m "worked on this"
 - using simple 'jira log' I want to be able to log time to my cards without using the UI
 - the number ‘1’ would be probably default, in hours, otherwise any sane number in hours
 - 'mystory' is an alias previously created from the ugly RHCFQE-xyzn jira story ID
 - message is a string preceeded with '-m' that will be saved as a comment to work log

jiratool time remains mystory
 - how much time remains to be logged in mystory

jiratool time set 0 all
 - sets the remaining time to 0 on all cards that are in "DONE"

jiratool time estimate 5 mystory
 - set new estimate to mystory, in this case 5 hours

jiratool time show mystory
 - show time log
 - usefull when tracking time logging
 - show timestap when the last time log was performed AND the time log

jiratool time today
 - show how many hours are logged for today, maybe also with comments and card aliases

jiratool watch mystory 5432
 - creates a link between the PR #5432 and the story mystory
 - watches opened PR and sets the summary of associated jira story accordingly
 - prepends the summary with [WIP], [WIPTEST], [RFR] - depends on the PR state
 - moves the card between "IN PROGRESS" to "AWAITING REVIEW" and "DONE" - depends on the PR state

jiratool move mystory done|inprogress|new|onhold -m ""
 - moves jira card to appropriate column with optional comment

jiratool edit mystory -m "comment"
 - Add a comment to story mystory

jiratool edit mystory --component "component"
 - Add a component to story mystory

jiratool edit mystory --label "label"
 - Add a label to story mystory


# Experimental features

status emails
 - provide an interface to status emails
 - define a template to be used
 - enable repeating chosen tasks over the period of multiple days
 - enable input of a BZ or a PR hosted externally

email view today|yesterday

email send

email log "did a draft of a super crazy idea"


# Design notes

 - verbose mode
   - In case of slow response times
   - make people angry at jira, not at my program
 - Be aware of current sprint
 - Command line interface
 - Save all data to disk and work with that
 - Proposal: generate status emails from scratch
   - take comments made to the jira cards and generate and send the status email from that
   - look also at status changes like moving the card to DONE
 - Proposal: enable saving a template as an email
   - when there's something being worked at for mutliple days
 - Proposal: calendar integration
 - know what day it is
 - able to detect meetings?


Sources
[1] https://github.com/pycontribs/jira
[2] https://github.com/PyGithub/PyGithub

