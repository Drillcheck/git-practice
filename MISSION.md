# m02 빠뜨린 파일을 같은 커밋에 넣기

## 상황

방금 "Add tax to the order total" 커밋을 만들었습니다. 아직 push하지 않았습니다.
그런데 테스트를 돌려 보니 실패합니다.

```
python3 -m unittest
```

`kitchen/order.py`는 `kitchen/tax.py`를 불러오는데, 정작 `tax.py`를 커밋에 넣지 않았습니다.
새 커밋을 하나 더 만들면 "세금 추가"가 커밋 2개로 쪼개지고, 그 사이 커밋은 깨진 상태로 남습니다.

## 목표

- 아래 내용으로 `kitchen/tax.py`를 만듭니다.

  ```python
  RATE = 0.1


  def apply(amount):
      return round(amount * (1 + RATE), 2)
  ```

- 이 파일을 **마지막 커밋 안에** 넣습니다. 커밋 수는 늘어나지 않아야 합니다.
- 커밋 메시지 첫 줄은 그대로 `Add tax to the order total`로 둡니다.
- 테스트가 통과하는지 확인합니다.

## 확인

```
./check
```

통과하면 push하고 `mission/m02`로 Pull Request를 엽니다.

<details>
<summary>힌트</summary>

`git commit --amend`는 마지막 커밋을 새 커밋으로 바꿉니다. 커밋 해시도 바뀝니다.
이미 push해서 다른 사람이 받아 간 커밋이라면 amend하기 전에 한 번 더 생각해야 하는 이유가 여기에 있습니다.

</details>
