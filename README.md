## Latex-merge
> A simple script for removing all comments and merging all ```tex``` files in a single file


Usage:
```bash
$ python3 latex-merge.py main.tex output-merge.tex
```

---
**Example**

Input:
```bash
$ cat main.tex

%% bare_jrnl_compsoc.tex
%% V1.4b
%% 2015/08/26
%% by Michael Shell
%% See:
%% http://www.michaelshell.org/
%% for current contact information.
%%

\documentclass[10pt,journal,compsoc]{IEEEtran}
%
...
\input{sections/Intro}
...
```

```bash
$ python3 latex-merge.py main.tex output-merge.tex
```

Output:
```bash
$ cat output-merge.tex

\documentclass[10pt,journal,compsoc]{IEEEtran}
...
\section{Introduction}\label{sec:intro}
...
```
