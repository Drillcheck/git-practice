# 수업 순서

각 장은 팀에서 실제로 마주치는 상황 하나입니다. 앞 장에서 익힌 명령을 다음 장에서 다시 씁니다.
실습은 내 컴퓨터에서 합니다. Windows는 Git Bash, macOS와 Linux는 기본 터미널을 씁니다.

| 장 | 상황 | 주로 쓰는 명령 | 미션 |
|---|---|---|---|
| [00](00-setup.ipynb) | 준비: git 설치, GitHub 로그인, 내 이름 등록, fork와 clone | `gh auth login`, `git config`, `git clone` | |
| [01](01-reading-history.ipynb) | 처음 받은 프로젝트의 이력 읽기 | `git log`, `git show`, `git blame`, `git tag` | |
| [02](02-first-pr.ipynb) | 내 첫 변경을 올리고 Pull Request 열기 | `git switch -c`, `git add`, `git commit`, `git push` | m01 |
| [03](03-undo.ipynb) | 실수 되돌리기 | `git restore`, `git stash`, `git reset`, `git commit --amend` | m02, m03 |
| [04](04-tidy-commits.ipynb) | 리뷰 요청대로 커밋 다듬기 | `git rebase -i` | |
| [05](05-sync-with-team.ipynb) | 팀의 최신 변경과 맞추기 | `git fetch`, `git rebase`, `git merge`, `git push --force-with-lease` | m04 |
| [06](06-team-project.ipynb) | 팀 프로젝트: 여러 사람의 PR을 한 repo에 모으기 | 지금까지의 전부 | |
| [07](07-open-source-contribution.ipynb) | 오픈소스 방식으로 기여하기: fork에서 PR 보내기 | `git remote add upstream`, `git commit -s`, `git range-diff`, `git pull --ff-only upstream main` | |
