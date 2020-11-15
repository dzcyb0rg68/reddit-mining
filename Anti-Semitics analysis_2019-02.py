
# coding: utf-8

import nltk
import json
import re
import zstandard as zstd
import json
import lzma
import datetime

def convert_sectodate(sec):
    ndate = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=(sec))
    return ndate.isoformat().replace('T',' ')

sample_dict = {'all_awardings': [],
#  'author': 'ragenukem',
 'author_created_utc': 1343369985,
 'author_flair_background_color': None,
 'author_flair_css_class': None,
 'author_flair_richtext': [],
 'author_flair_template_id': None,
 'author_flair_text': None,
 'author_flair_text_color': None,
 'author_flair_type': 'text',
 'author_fullname': 't2_8gva8',
 'author_patreon_flair': False,
#  'body': 'I get to do the thing! /r/beetlejuicing',
 'can_gild': True,
 'can_mod_post': False,
 'collapsed': False,
 'collapsed_reason': None,
 'controversiality': 0,
 'created_utc': 1559347203,
 'distinguished': None,
 'edited': False,
 'gilded': 0,
 'gildings': {},
 'id': 'epom0fx',
 'is_submitter': False,
 'link_id': 't3_bv9v53',
 'locked': False,
 'no_follow': True,
 'parent_id': 't1_epobwr9',
 'permalink': '/r/Wellthatsucks/comments/bv9v53/ball_boy_meet_wall_boy/epom0fx/',
 'quarantined': False,
 'removal_reason': None,
 'retrieved_on': 1568677948,
#  'score': 2,
#  'send_replies': True,
 'steward_reports': [],
 'stickied': False,
#  'subreddit': 'Wellthatsucks',
 'subreddit_id': 't5_2xcv7',
 'subreddit_name_prefixed': 'r/Wellthatsucks',
 'subreddit_type': 'public',
 'total_awards_received': 0}

def remove_key(target_dict, source_dict):
    for key in source_dict:
        try:
            del target_dict[key]
        except KeyError:
            pass

antisemitics_words = ['libel', 'clannish', 'conspiracy', 'cowardice', 'goyim', 'globalist', 'greed', 'holocaust', 'jew', 'jewish', 'illuminati', 'khazars', 'kosher', 'zionish', 'scapegoat', 'silencing', 'smirking', 'merchant']
antisemitics_set = set(antisemitics_words)

filenames = ["/l/research/social-media-mining/reddit/comments/RC_2019-02.zst"
    # "/l/research/social-media-mining/reddit/comments/RC_2019-03.zst",
    # "/l/research/social-media-mining/reddit/comments/RC_2019-04.zst",
    # "/l/research/social-media-mining/reddit/comments/RC_2019-05.zst",
    # "/l/research/social-media-mining/reddit/comments/RC_2019-06.zst"
            ]

for filename in filenames:
    date = filename.replace('.xz','').replace('.zst','')
    if filename.split('.',1)[1] == 'xz':
        with lzma.open(filename, mode='rt', encoding='utf-8') as redditfile:
            for line in redditfile:
                line = json.loads(line)
                words = re.findall(r'\w+', line['body'].lower())
                words_set = set(words)
                common_elements = words_set.intersection(antisemitics_set)
                score = len(common_elements)
                antisemitics_list = []
                if score >= 4:
                    for w in words:
                        for a in antisemitics_words:
                            if w == a:
                                antisemitics_list.append(w)
                                
                    ndate = convert_sectodate(line['created_utc'])
                    line['date_year_month'] = date[-7:]
                    line['created_utc_converted'] = ndate
                    line['score_overall'] = len(antisemitics_list)
                    line['words'] = ' '.join([str(elem) for elem in antisemitics_list])
                    line['shared_words'] = ' '.join([str(elem) for elem in list(dict.fromkeys(antisemitics_list))])
                    line['socre_distint'] = score
                    remove_key(line, sample_dict)
                    with open('antisemitics_2019-02.json', 'a') as outfile:
                        json.dump(line, outfile)
                        outfile.write('\n')
                        outfile.close()
                        
    elif filename.split('.',1)[1] == 'zst':
        with open(filename, 'rb') as fh:
            dctx = zstd.ZstdDecompressor()
            stream_reader = dctx.stream_reader(fh)
            text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
            z = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
            for line in text_stream:
                line = json.loads(line.translate(z))
                words = re.findall(r'\w+', line['body'].lower())
                words_set = set(words)
                common_elements = words_set.intersection(antisemitics_set)
                score = len(common_elements)
                antisemitics_list = []
                if score >= 4:
                    for w in words:
                        for a in antisemitics_words:
                            if w == a:
                                antisemitics_list.append(w)
                                
                    ndate = convert_sectodate(line['created_utc'])
                    line['date_year_month'] = date[-7:]
                    line['created_utc_converted'] = ndate
                    line['score_overall'] = len(antisemitics_list)
                    line['words'] = ' '.join([str(elem) for elem in antisemitics_list])
                    line['shared_words'] = ' '.join([str(elem) for elem in list(dict.fromkeys(antisemitics_list))])
                    line['socre_distint'] = score
                    remove_key(line, sample_dict)
                    with open('antisemitics_2019-02.json', 'a') as outfile:
                        json.dump(line, outfile)
                        outfile.write('\n')
                        outfile.close()
