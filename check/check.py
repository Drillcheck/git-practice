#!/usr/bin/env python3
"""Grade a git-practice mission by reading the commit graph.

Only git objects are read. Nothing from the learner's commits is executed,
so this is safe to run on pull requests from forks.

    python3 check/check.py --mission m01 --head HEAD --main-ref origin/main
"""
import argparse
import json
import subprocess
import sys

MARKERS = ("<<<<<<<", "=======", ">>>>>>>")


def git(*args, ok=False):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if ok:
        return r.returncode == 0
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} 실패: {r.stderr.strip()}")
    return r.stdout


def is_ancestor(a, b):
    return git("merge-base", "--is-ancestor", a, b, ok=True)


def commits(base, head):
    """Commits reachable from head but not from base, oldest first."""
    out = git("rev-list", "--reverse", f"{base}..{head}")
    return out.split()


def parents(sha):
    return git("rev-list", "--parents", "-n", "1", sha).split()[1:]


def subject(sha):
    return git("log", "-1", "--format=%s", sha).strip()


def files(sha):
    return set(git("ls-tree", "-r", "--name-only", sha).split("\n")) - {""}


def read(sha, path):
    return git("show", f"{sha}:{path}")


def changed(a, b):
    return set(git("diff", "--name-only", a, b).split("\n")) - {""}


def blob(sha, path):
    return git("rev-parse", f"{sha}:{path}").strip()


class Report:
    def __init__(self):
        self.failed = 0

    def check(self, ok, good, bad):
        print(("  통과  " + good) if ok else ("  실패  " + bad))
        if not ok:
            self.failed += 1
        return ok

    def stop(self, msg):
        print("  실패  " + msg)
        self.failed += 1


def m01(head, spec, r):
    base = spec["base"]
    if not r.check(is_ancestor(base, head), "시작 커밋 위에서 작업했습니다.",
                   "이 브랜치가 mission/m01에서 시작하지 않았습니다. git switch mission/m01 로 다시 시작하세요."):
        return
    new = commits(base, head)
    if not r.check(len(new) == 1, "커밋이 정확히 1개 추가되었습니다.",
                   f"추가된 커밋이 {len(new)}개입니다. 오타 수정은 커밋 1개여야 합니다."):
        return
    c = new[0]
    r.check(len(parents(c)) == 1, "merge 커밋이 아닙니다.", "merge 커밋이 아닌 일반 커밋이어야 합니다.")
    diff = changed(base, c)
    r.check(diff == {"README.md"}, "README.md만 바뀌었습니다.",
            f"README.md 외의 파일도 바뀌었습니다: {', '.join(sorted(diff - {'README.md'})) or '(없음)'}"
            if diff else "README.md가 바뀌지 않았습니다.")
    text = read(c, "README.md")
    r.check("recieve" not in text and "receive" in text, "오타가 고쳐졌습니다.",
            "README.md에 아직 recieve가 있거나 receive가 없습니다.")
    s = subject(c)
    r.check(0 < len(s) <= 72, f"커밋 메시지 첫 줄: \"{s}\"",
            f"커밋 메시지 첫 줄이 비었거나 72자를 넘습니다 ({len(s)}자).")


def m02(head, spec, r):
    base, parent = spec["base"], spec["base_parent"]
    if not r.check(is_ancestor(parent, head), "시작 커밋의 이전 이력이 그대로입니다.",
                   "이 브랜치가 mission/m02에서 시작하지 않았거나, 마지막 커밋보다 앞의 이력이 바뀌었습니다."):
        return
    new = commits(parent, head)
    if not r.check(len(new) == 1, "세금 추가가 커밋 1개로 남았습니다.",
                   f"마지막 커밋 자리에 커밋이 {len(new)}개 있습니다. 새 커밋을 만들지 말고 마지막 커밋을 고치세요."):
        return
    c = new[0]
    r.check(c != base, "마지막 커밋이 새 커밋으로 바뀌었습니다.", "마지막 커밋이 그대로입니다. tax.py가 아직 커밋에 없습니다.")
    r.check(subject(c) == subject(base), "커밋 메시지 첫 줄이 그대로입니다.",
            f"커밋 메시지 첫 줄이 바뀌었습니다: \"{subject(c)}\"")
    has = "kitchen/tax.py" in files(c)
    r.check(has and "def apply" in read(c, "kitchen/tax.py"), "kitchen/tax.py가 커밋에 들어갔습니다.",
            "kitchen/tax.py가 커밋에 없거나 apply 함수가 없습니다.")
    r.check(blob(c, "kitchen/order.py") == blob(base, "kitchen/order.py"), "order.py는 그대로입니다.",
            "kitchen/order.py가 바뀌었습니다. 이 미션은 빠진 파일만 넣으면 됩니다.")


def m03(head, spec, r):
    base, parent = spec["base"], spec["base_parent"]
    if not r.check(is_ancestor(parent, head), "시작 커밋의 이전 이력이 그대로입니다.",
                   "이 브랜치가 mission/m03에서 시작하지 않았거나, 마지막 커밋보다 앞의 이력이 바뀌었습니다."):
        return
    new = commits(parent, head)
    if not new:
        r.stop("마지막 커밋이 사라졌습니다. payment.py는 커밋에 남아 있어야 합니다.")
        return
    leaked = [c for c in new if ".env" in files(c)]
    r.check(not leaked, "어떤 커밋에도 .env가 없습니다.",
            ".env가 들어 있는 커밋이 남아 있습니다: " + ", ".join(c[:7] for c in leaked)
            + ". 지우는 커밋을 새로 만들어도 이전 커밋에는 키가 남습니다.")
    tip = files(head)
    r.check("kitchen/payment.py" in tip, "kitchen/payment.py가 남아 있습니다.", "kitchen/payment.py가 사라졌습니다.")
    ignore = read(head, ".gitignore").splitlines() if ".gitignore" in tip else []
    r.check(any(line.strip() in (".env", "/.env") for line in ignore), ".gitignore에 .env가 있습니다.",
            ".gitignore에 .env 줄이 없습니다.")


def m04(head, spec, r):
    base, mate = spec["base"], spec["teammate"]
    ps = parents(head)
    if not r.check(len(ps) == 2, "마지막 커밋이 merge 커밋입니다.",
                   "마지막 커밋이 merge 커밋이 아닙니다. teammate/m04를 merge하세요. (rebase나 cherry-pick이 아니라 merge입니다)"):
        return
    r.check(ps[0] == base, "첫 번째 부모가 내 커밋입니다.",
            "첫 번째 부모가 mission/m04의 시작 커밋이 아닙니다. mission/m04 위에서 merge하세요.")
    r.check(ps[1] == mate, "두 번째 부모가 Emily의 커밋입니다.", "두 번째 부모가 teammate/m04의 커밋이 아닙니다.")
    text = read(head, "kitchen/order.py")
    r.check(not any(m in text for m in MARKERS), "충돌 표시가 남아 있지 않습니다.",
            "kitchen/order.py에 충돌 표시(<<<<<<< ======= >>>>>>>)가 남아 있습니다.")
    r.check("1.1" in text, "봉사료(내 변경)가 살아 있습니다.", "봉사료 10%(내 변경)가 사라졌습니다.")
    r.check("round(" in text, "반올림(Emily의 변경)이 살아 있습니다.", "반올림(Emily의 변경)이 사라졌습니다.")


MISSIONS = {"m01": m01, "m02": m02, "m03": m03, "m04": m04}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mission", required=True)
    ap.add_argument("--head", default="HEAD")
    ap.add_argument("--main-ref", default="origin/main")
    a = ap.parse_args()
    if a.mission not in MISSIONS:
        raise SystemExit(f"없는 미션입니다: {a.mission}")
    spec = json.loads(read(a.main_ref, "check/missions.json"))[a.mission]
    head = git("rev-parse", "--verify", f"{a.head}^{{commit}}").strip()
    print(f"{a.mission} 채점 ({head[:7]})")
    if a.head == "HEAD" and git("status", "--porcelain", "--untracked-files=no").strip():
        print("  참고  커밋하지 않은 변경이 있습니다. 채점은 커밋된 내용만 봅니다.")
    r = Report()
    MISSIONS[a.mission](head, spec, r)
    print("결과: 통과" if r.failed == 0 else f"결과: {r.failed}개 항목 실패")
    sys.exit(0 if r.failed == 0 else 1)


if __name__ == "__main__":
    main()
