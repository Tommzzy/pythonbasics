echo "# javascriptbasics" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Tommzzy/javascriptbasics.git
git push -u origin main




cd /D-change directory
 
mkdir -make directory

USER@Tomzzy MINGW64 /d/School Work
$ cd  Tutor_Work/

USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$ ls
'Lab 1'  'echo # javascriptbasics  README.md.txt'   main.py

USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$ touch calculator.py

USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$ ls
'Lab 1'   calculator.py  'echo # javascriptbasics  README.md.txt'   main.py

USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$ code .

USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$ ls
'Lab 1'   calculator.py  'echo # javascriptbasics  README.md.txt'   main.py

USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$ git init
Reinitialized existing Git repository in D:/School Work/Tutor_Work/.git/

USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   echo # javascriptbasics  README.md.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        calculator.py

no changes added to commit (use "git add" and/or "git commit -a")

USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$ git add .

USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   calculator.py
        modified:   echo # javascriptbasics  README.md.txt


USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$ git commit -m "second commit"
[master d34576a] second commit
 2 files changed, 51 insertions(+), 1 deletion(-)
 create mode 100644 calculator.py

USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$ git pull origin master
From https://github.com/Tommzzy/pythonbasics
 * branch            master     -> FETCH_HEAD
Already up to date.

USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$ git push -u origin master
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 820 bytes | 820.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Tommzzy/pythonbasics.git
   ae8d594..d34576a  master -> master
branch 'master' set up to track 'origin/master'.

USER@Tomzzy MINGW64 /d/School Work/Tutor_Work (master)
$

 