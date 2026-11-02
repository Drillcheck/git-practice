# git-practice

팀에서 git을 쓰다 실제로 막히는 상황을 직접 풀어 보는 실습 저장소입니다.
각 미션은 고장 난 상태로 시작하는 브랜치 하나입니다. 고친 결과는 명령어가 아니라 **저장소의 최종 상태**로 채점합니다.
같은 결과에 이르는 방법이 여러 가지라면 어떤 방법이든 통과입니다.

만든 곳: [DrillCheck](https://drillcheck.app)

## 수업

처음이라면 [lessons/](lessons/README.md)를 순서대로 따라 하세요. 준비부터 팀 협업까지 상황별로 나뉘어 있습니다.
`main` 브랜치의 `kitchen/`은 실습에 쓰는 작은 식당 주문 계산기입니다.

## 미션

| 미션 | 상황 |
|---|---|
| `mission/m01` | 오타 하나를 커밋 1개로 남기기 |
| `mission/m02` | 마지막 커밋에 빠뜨린 파일을 같은 커밋에 넣기 |
| `mission/m03` | 커밋에 들어간 비밀 값을 이력에서 빼기 |
| `mission/m04` | 팀원과 같은 줄을 고쳐 충돌 난 merge 풀기 |

## 시작하기

1. 오른쪽 위 **Fork**를 누릅니다. 이때 **Copy the `main` branch only의 체크를 해제**하세요. 체크되어 있으면 미션 브랜치가 복사되지 않습니다.
2. 내 fork를 clone합니다.

   ```
   git clone https://github.com/<내 아이디>/git-practice.git
   cd git-practice
   ```

3. 미션 브랜치로 이동해서 `MISSION.md`를 읽습니다.

   ```
   git switch mission/m01
   ```

4. 다 풀었으면 채점합니다. Windows에서는 Git Bash에서 실행합니다. Python 3이 필요합니다.

   ```
   ./check
   ```

5. 통과하면 push하고, 이 저장소의 같은 미션 브랜치(예: `mission/m01`)로 Pull Request를 엽니다. PR 화면의 check가 초록색이면 완료입니다.

## 알아 두기

- **Pull Request는 공개됩니다.** 내 GitHub 아이디와 커밋 내용이 누구에게나 보입니다. 원하지 않으면 `./check`로 내 컴퓨터에서만 채점해도 됩니다.
- PR은 merge하지 않습니다. 다른 사람이 같은 미션을 같은 시작 상태에서 풀 수 있어야 하기 때문입니다.
- 채점기는 PR의 코드를 실행하지 않습니다. 커밋과 파일 내용만 읽습니다. 채점기 코드는 `check/check.py`에 있습니다.
- 미션에 나오는 키와 이름은 모두 연습용으로 지어낸 것입니다.
