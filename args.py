from argparse import ArgumentParser

parser = ArgumentParser()
sp = parser.add_subparsers()

# jiratool alias *
p_alias = sp.add_parser('alias')
p_alias.add_argument('story_id')
p_alias.add_argument('story_alias')
# jiratool edit *
# TODO add default to comment
p_edit = sp.add_parser('edit')
p_edit.add_argument('story')
p_edit.add_argument('-m', '--comment')
p_edit.add_argument('-c', '--component')
p_edit.add_argument('-l', '--label')
# jiratool id <story>
p_id = sp.add_parser('id')
p_id.add_argument('story')
# jiratool move *
p_move = sp.add_parser('move')
p_move.add_argument('story')
p_move.add_argument('action', choices=('done', 'inprogress', 'onhold', 'new'))
p_move.add_argument('-m', '--message')
# jiratool time *
p_time = sp.add_parser('time')
ps_time = p_time.add_subparsers()
# jiratool time log *
p_time_log = ps_time.add_parser('log')
p_time_log.add_argument('story')
p_time_log.add_argument('hours')
p_time_log.add_argument('-m', '--message')
# jiratool time remains <story>
p_time_remains = ps_time.add_parser('remains')
p_time_remains.add_argument('story')
# jiratool time set *
p_time_set = ps_time.add_parser('set')
p_time_set.add_argument('hours')
p_time_set.add_argument('cards')
# jiratool time estimate *
p_time_estimate = ps_time.add_parser('estimate')
p_time_estimate.add_argument('hours')
p_time_estimate.add_argument('story')
# jiratool time show <story>
p_time_show = ps_time.add_parser('show')
p_time_show.add_argument('story')
# jiratool time today
p_time_today = ps_time.add_parser('today')
# jiratool watch *
p_watch = sp.add_parser('watch')
p_watch.add_argument('story')
p_watch.add_argument('pr')

args = parser.parse_args()
