# m01 첫 커밋

## 상황

작은 식당의 주문 계산기 `kitchen`을 함께 만들고 있습니다.
README 마지막 줄을 읽다가 오타를 발견했습니다. `recieve`가 아니라 `receive`가 맞습니다.

고치는 것 자체는 한 글자지만, 팀에서는 이 수정이 **커밋 하나**로 남아야 합니다.
나중에 누가 `git log`를 봐도 "무엇을 왜 바꿨는지" 알 수 있어야 하기 때문입니다.

## 목표

- `README.md`의 오타를 고칩니다.
- 그 수정을 커밋 **1개**로 만듭니다. 다른 파일은 건드리지 않습니다.
- 커밋 메시지 첫 줄에 무엇을 고쳤는지 씁니다. 72자 이내로 씁니다.

## 확인

```
./check
```

통과하면 이 브랜치를 내 fork에 push하고, `Drillcheck/git-practice`의 `mission/m01`로 Pull Request를 엽니다.
PR 화면의 check가 초록색이 되면 끝입니다.

<details>
<summary>힌트</summary>

`git status`, `git diff`, `git add`, `git commit` 순서로 진행합니다.
`git diff`로 무엇이 바뀌었는지 커밋 전에 꼭 확인하세요.

</details>
