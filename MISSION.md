# m04 충돌 난 merge 풀기

## 상황

나는 이 브랜치에서 봉사료 10%를 더하는 커밋 "Add a 10% service charge"를 만들었습니다.
같은 시간에 팀원 Emily는 `teammate/m04` 브랜치에서 합계를 센트 단위로 반올림하는 커밋 "Round the total to cents"를 만들었습니다.

두 사람 모두 `kitchen/order.py`의 같은 줄을 고쳤습니다.
그래서 Emily의 브랜치를 merge하면 git이 어느 쪽을 남길지 정하지 못하고 멈춥니다. 이것이 충돌(conflict)입니다.

## 목표

- `teammate/m04`를 이 브랜치에 merge합니다. merge 커밋이 생겨야 합니다.
- 충돌을 풀 때 **두 사람의 변경을 모두 살립니다.** 봉사료를 더한 합계를 반올림해야 합니다.
- 충돌 표시(`<<<<<<<`, `=======`, `>>>>>>>`)가 파일에 남아 있으면 안 됩니다.
- 테스트가 통과하는지 확인합니다.

  ```
  python3 -m unittest
  ```

## 확인

```
./check
```

통과하면 push하고 `mission/m04`로 Pull Request를 엽니다.

<details>
<summary>힌트</summary>

`git merge origin/teammate/m04`를 실행하면 충돌이 난 파일이 표시됩니다.
파일을 열어 `<<<<<<<`와 `>>>>>>>` 사이를 직접 고친 뒤 `git add`, `git commit`으로 merge를 마칩니다.
한 쪽만 고르는 것(`--ours`, `--theirs`)으로는 이 미션을 통과할 수 없습니다.

</details>
