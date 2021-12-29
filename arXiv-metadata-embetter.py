## When month changes,  change these two lines:    (no other changes needed):
import time
import re
import numpy as np
import sys
y = time.gmtime()[0] ##2020
m = time.gmtime()[1] ##3 for march
if m == 1:
    curr_month = str(y)[-2:] + '01'
    prev_month = str(y-1)[-2:] + '12'
else:
    curr_month = str(y)[-2:] + '0' * (2 - len(str(m))) + str(m)
    prev_month = str(y)[-2:] + '0' * (2 - len(str(m-1))) + str(m-1)
save_to_pkl = True

import pickle
def save_obj(obj, name):
    with open(name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


bad_keywords = {'speech recognition': -0.3, 'speaker recognition': -0.7, 'speech separation': -0.4, 'segmentation': -0.25, 'reverberat': -0.2, 'point cloud': -0.2, 'knn': -0.2, 
               'regression': -0.2, 'Object Detection': -0.3, 'black-box attack': -0.4, 'nearest neighbo': -0.4, 'SQL': -0.5, 'emotion': -0.4, 
               'android': -0.2, 'malware': -0.3, 'knowledge graph': -0.15, 'fake news': -0.5, 'super-resolution': -0.5, 'outlier': -0.5,
               'tracker': -0.25, ' face ': -0.3, ' facial ': -0.3, 'clustering': -0.5, 'anomal': -0.25, 'parsing': -0.4, 'parser': -0.3,
               'e-commerce': -0.5, 'speech enhancement': -0.5, 'fmri': -0.4, 'post-editing': -0.4, 'reservoir': -0.3, 'voice separat': -0.4, ' eeg ': -0.5, ' mri ': -0.4, 
               'bengali': -0.4, 'hindi': -0.4, 'japanese': -0.4, 'vietnamese': -0.4, 'chinese': -0.2, 'restaurant': -0.5, 
               'image denoising': -0.3, 'economic': -0.4, ' POS ': -0.5,  'tracking': -0.35, ' NER ': -0.5, 'sentiment': -0.5, 
               'tomography': -0.4, 'hmdb-51': -0.3, 'interpret': -0.2, 'authorship': -0.2, ' mobile ': -0.15, 'hieroglyph': -0.4, 'weather': -0.3, 'market': - 0.3, 
               ' music ': -0.3, 'ecg': -0.5, 'histolog': -0.5, 'fpga': -0.25, 'federated': -0.2, ' nba ': -0.8, 'climate': -0.2, 'style': -0.2, 
               'cancer': -0.2, 'lightweight': -0.2, 'surveillance': -0.4, 'summarization': -0.3, 'privacy': -0.5, 'private': -0.3, 'low-resource': -0.25, 'retrieval': -0.4, 
               'pedestrian': -0.5, 'financ': -0.4, 'competitive': -0.15, 'spoof': -0.3, 
               'customer': -0.6, 'medic': -0.1, 'clinic': -0.2, 'patient': -0.5, 'diseas': -0.2, 'disorder': -0.5, 'random forest': -0.5, 'k-mean': -0.5, 
               'svm': -0.5, 'kernel': -0.5, 'bandit': -0.5, 'boltzmann': -0.5, 'inpainting': -0.3, 'odometry': -0.25, 'gender bias': -0.5, 'retrieval': -0.4, 'deraining': -0.5, 
               'deblur': -0.5, 
                'magnetic resonance': -0.5, 'theor': -0.5, 'gaussi': -0.5, 'mammogra': -0.5, 'diagnos': -0.2, 'patholog': -0.3, 'adversarial att': -0.5, 
                'bayes': -0.5, 'recommendat': -0.5, 'named entity': -0.5, 'anatomy': -0.5, 'lidar': -0.5, 'high-energy': -0.5, 're-identification': -0.5,
                'pose estimation': -0.5}
good_keywords = {'state-of-the-art': 1, 'state of the art': 1, 'github': 1, 'source code': 1, 'alphazero': 1,
               'reinforcement learning': 0.65, 'curriculum learning': 0.1, 'general intelligence': 0.25, 'general artificial' : 0.25, 'general ai': 0.25,
               'lifelong': 0.2, 'MuJoCo': 0.1, 'hierarchical': 0.2, 'zero-shot': 0.2, 'one-shot': 0.15, 'few-shot': 0.2, 
               'sparse reward': 0.3, 'publicly available': 0.3, 'architecture search': 0.3, 'sample efficien': 0.4, 
               'google': 3.0, 'openai': 3.0, 'brain': 0.25, 'curiosity': 0.2, 'human-level': 0.3, ' bert ':0.25, ' gpt': 0.25, 'surprisin': 0.7, 
               'video generation': 0.3, 'http': 0.1, 'russia': 0.3, 'outperform': 0.2, 
               'real-world': 0.15, 'real world': 0.15, 'transformer':0.65, 'molecule': 0.3, 'drug': 0.3}
good_keywords_thresh = {'mathemati': [3.0, 3]}
good_authors = ['Bengio, Yoshua', 'Quoc', 'Vinyals', 'Salakhutdinov', 'Freitas', 'Kyunghyun', 'Schulman, J', 
                  'Hinton', 'Schmidhuber', 'Ng, Andr', 'LeCun', 'Hassabis', 'Goodfellow', 'Lee, Honglak', 
                  'Oord, A', 'Pascanu, R', 'Lillicrap', 'Nøkland', 'Sutskever', 'Yuille', 'Zisserman, A', 'Weston, Jason', 'Mordatch', 
                  'Sukhbaatar', 'Joulin, A', 'Ranzato, Ma', 'Simonyan, Ka', 'Malik, J', 'Fei-Fei, Li', 'Zaremba, W', 'Levine, Sergey', 
                  'Batra, Dhruv', 'Parikh, Devi', 'Sutton, Rich', 'Courville', 'Tatsuya', 'Amodei, Dario', 'Radford, Alec',
                  'Christiano, Paul', 'Botvinick, M', 'Silver, David', 'van Hasselt, Hado']
good_subjects = ['cs:CL', 'cs:NE', 'cs:RO']
subjects_to_follow = {'Computer Science - Robotics' : 'cs:RO', 'Computer Science - Sound' : 'cs:SD', 
                      'Computer Science - Artificial Intelligence' : 'cs:AI', 
                      'Computer Science - Neural and Evolutionary Computing' : 'cs:NE', 
                      'Statistics - Machine Learning' : 'stat:ML', 'Computer Science - Machine Learning' : 'cs:ML', 
                      'Computer Science - Emerging Technologies' : 'cs:ET', 
                      'Computer Science - Computation and Language' : 'cs:CL', 
                      'Computer Science - Computer Vision and Pattern Recognition' : 'cs:CV'}                  

def process(text, dictionary, colorFunc):
    t = text
    d = dictionary
    if_good = 0
    for keyword in d.keys():
        if t.lower().find(keyword.lower()) > -1:
            ci = t.lower().find(keyword.lower()) #ci - color_index
            font_color = colorFunc(d[keyword])
            t = t[:ci] + '<font color="' + font_color + '">' + t[ci: ci + len(keyword)] \
            + '</font>' + t[ci + len(keyword) :]
            if_good += d[keyword]
    return t, if_good

def process_thresh(text, dictionary, colorFunc):
    t = text
    d = dictionary
    if_good = 0
    for keyword in d.keys():
        if len(re.findall(keyword.lower(), description.lower())) >= d[keyword][1]:
            ci = t.lower().find(keyword.lower()) #ci - color_index
            font_color = colorFunc(d[keyword][0])
            t = t[:ci] + '<font color="' + font_color + '">' + t[ci: ci + len(keyword)] \
            + '</font>' + t[ci + len(keyword) :]
            if_good += d[keyword][0]
    return t, if_good

def colorFuncRed(x):
    color = hex(    min(190, int(abs(x) * 1000))    )[2:]   ## 0.5 as ~255
    color = '#' + color + '00' + color
    return color

def colorFuncGreen(x):
    color = hex(    min(190, int(abs(x) * 1000))    )[2:]   ## 0.5 as ~255
    color = '#00' + color + '00'
    return color

def colorFuncBlue(x):
    color = hex(    min(190, int(abs(x) * 1000))    )[2:]   ## 0.5 as ~255
    color = '#00' + color + 'a0'
    return color


f = open("arXiv-articles.xml", "r")
fW = open("arXiv-articles.html", "w+")
articles = {}
a = f.read()

indices_beg = [x.end() for x in re.finditer('<record>', a)]
indices_end = [x.start() for x in re.finditer('</record>', a)]
records = [a[i:j] for [i,j] in np.transpose([indices_beg, indices_end])]

indBeg = 0;   indEnd = 0
while indBeg > -1:
    indBeg = a.find('<record>', indEnd)
    indEnd = a.find('</record>', indBeg)
    b = a[indBeg:indEnd] ## current record ab. some article    
    i1 = b.find('<identifier>')
    i2 = b.find('</identifier>')
    identifier = b[i1+26:i2]  ## 26 = len("<identifier>oai:arXiv.org:")
    articles[identifier] = {}
    articles[identifier]['if-good'] = 0
    
    i1 = b.find('<dc:title>')
    i2 = b.find('</dc:title>')
    title = b[i1+10:i2]
    articles[identifier]['title'] = title
    
    i1 = 0;   i2 = 0
    creators = ''
    while i1 > -1:
        i1 = b.find('<dc:creator>', i2)
        i2 = b.find('</dc:creator>', i1)
        if i2 > -1:
            creator = b[i1+12:i2]
            creators += ", " + creator
            
    for good_author in good_authors:
        if creators.lower().find(good_author.lower()) > -1:
            # gives false positives on many "...ng A..."  like "Cheung Ang"
            red_idx = creators.lower().find(good_author.lower())
            creators = creators[:red_idx] + '<font color="green">' + creators[red_idx: red_idx + len(good_author)] \
            + '</font>' + creators[red_idx + len(good_author) :]
            articles[identifier]['if-good'] += 10
    articles[identifier]['creators'] = creators
    
    i1 = 0;   i2 = 0
    articles[identifier]['subjects-to-follow'] = 0
    articles[identifier]['subject'] = '('
    while i1 > -1:
        i1 = b.find('<dc:subject>', i2)
        i2 = b.find('</dc:subject>', i1)
        if i2 > -1:
            subject = b[i1+12:i2]
            if subject in subjects_to_follow:
                articles[identifier]['subjects-to-follow'] = 1
                articles[identifier]['subject'] += subjects_to_follow[subject] + ", "  ## brief name
    articles[identifier]['subject'] = articles[identifier]['subject'][:-2] + ")"
    for good_subject in good_subjects:
        if articles[identifier]['subject'].find(good_subject) > -1:
            articles[identifier]['if-good'] += 0.1
    
    i1 = b.find('<dc:description>')
    i2 = b.find('</dc:description>')
    description = b[i1+16:i2]
    description = description.replace('\\n'," ")
    articles[identifier]['if-good'] -= 0.0001 * len(description)
    
    description, if_good1 = process(description, bad_keywords, colorFuncRed)
    description, if_good2 = process(description, good_keywords, colorFuncGreen)
    description, if_good3 = process_thresh(description, good_keywords_thresh, colorFuncBlue)
    articles[identifier]['if-good'] += if_good1 + if_good2 + if_good3
    articles[identifier]['description'] = description
    
    title, if_good1 = process(title, bad_keywords, colorFuncRed)
    title, if_good2 = process(title, good_keywords, colorFuncGreen)
    articles[identifier]['if-good'] += if_good1 + if_good2
    articles[identifier]['title'] = title

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        fW.write(sys.argv[i] + " ")
    fW.write("</br></br>\n")

nummer = 1
for currID in sorted(articles, key=lambda x: (articles[x]['if-good']), reverse=True):
    if (articles[currID]['subjects-to-follow'] == 1) and ((currID.find(prev_month) > -1) or (currID.find(curr_month) > -1)):
        fW.write("<a href='http://arxiv.org/pdf/" + currID + ".pdf'>" + currID + "</a> &nbsp&nbsp ")
        fW.write(articles[currID]['subject'])
        fW.write(" &nbsp&nbsp " + "{:.4f}".format(articles[currID]['if-good']) + "баллов, №" + str(nummer) + "</br>\n")
        fW.write("<b>" + articles[currID]['title'] + "</b></br>\n")
        fW.write("Authors: " + articles[currID]['creators'] + "</br>\n")
        fW.write(articles[currID]['description'] + "</br></br>\n\n")
        nummer += 1

f.close()
fW.close()

if save_to_pkl:
    save_obj(articles, 'articles.pkl')
