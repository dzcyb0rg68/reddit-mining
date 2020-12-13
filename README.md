# Antisemitic Tracing on Reddit: An Intersectional Approach Toward Dissecting Ideologies

The   domain-specific   communities   thatform in subreddits may seem at first glanceto  cohere  around  the  topical  label  withwhich each subgroup is named.  However,such  a  surface-level  orientation  may  notbe as transparent in framing what is dis-cussed and how.  Particularly in detectinghate speech and other potentially harmfuldiscussions,  such  analysis  requires  morerobust  methods  to  detect  and  understandthe emergence of ideologies. In this study,we present an intersectional method of de-termining  likelihood  of  harmful  discus-sions.    Our  methodology  replicates  suc-cessful  detection  methods  from  previousstudies and suggests opportunity for morediscrete analysis.

# Data Source

The data we used are already extracted and saved in the data folder. The origianl data were the compressed files on the linux sever **gh.luddy.indiana.edu**. To replicate the extracting, login to the server and run **Anti-Semitics_data_extract.py**.

**How-to**

Environment
```
python3 -m venv <env_name>
source <env_name>/bin/activate
pip install -r requirements.txt
```

Execution
```
git clone https://github.com/dzcyb0rg68/reddit-mining.git
cd reddit-mining
python Anti-Semitics_data_extract.py
```

Please note that the original data files have 204.4GB and contain 793,326,999 reddit posts. The extracting may take a up to 24 hours to complete. To speed up, please contract the authors for parallel extracting support. 


# Questions?

Please reach out to the author at cc93@iu.edu

# Paper Preview

<object data="https://github.com/dzcyb0rg68/reddit-mining/raw/master/report/Final%20Project%20-%20Antisemitic%20Tracing%20on%20Reddit%20(Chang-Han%20and%20Michalek).pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/dzcyb0rg68/reddit-mining/raw/master/report/Final%20Project%20-%20Antisemitic%20Tracing%20on%20Reddit%20(Chang-Han%20and%20Michalek).pdf">
        <p>Your browser does not support PDFs. Please download the PDF to view it: <a href="https://github.com/dzcyb0rg68/reddit-mining/raw/master/report/Final%20Project%20-%20Antisemitic%20Tracing%20on%20Reddit%20(Chang-Han%20and%20Michalek).pdf">Download PDF</a>.</p>
    </embed>
</object>
