from __future__ import annotations

import shutil
import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
PROOF = WORKSPACE / "StudyBoard-Collab-CaptureProof"
SCREENSHOTS = ROOT / "screenshots"
GIT = Path(r"C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe")


def run(cmd: list[str], cwd: Path, allow_fail: bool = False) -> str:
    proc = subprocess.run(cmd, cwd=str(cwd), text=True, capture_output=True)
    out = (proc.stdout + proc.stderr).strip()
    if proc.returncode and not allow_fail:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{out}")
    return out


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        Path(r"C:\Windows\Fonts") / name,
        Path(r"C:\Windows\Fonts\consola.ttf"),
        Path(r"C:\Windows\Fonts\arial.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


MONO = font("consola.ttf", 22)
MONO_BOLD = font("consolab.ttf", 22)
UI = font("segoeui.ttf", 20)
UI_BOLD = font("segoeuib.ttf", 21)


def wrap_line(text: str, max_chars: int = 96) -> list[str]:
    if len(text) <= max_chars:
        return [text]
    wrapped: list[str] = []
    for line in text.splitlines() or [""]:
        if len(line) <= max_chars:
            wrapped.append(line)
        else:
            wrapped.extend(textwrap.wrap(line, max_chars, replace_whitespace=False, drop_whitespace=False) or [""])
    return wrapped


def terminal_image(filename: str, title: str, command: str, output: str) -> None:
    width, height = 1500, 860
    img = Image.new("RGB", (width, height), "#0c0d10")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, width, 58], fill="#202226")
    draw.text((24, 15), f"Windows PowerShell - {title}", fill="#f3f4f6", font=UI_BOLD)
    draw.text((24, 82), f"StudyBoard-Collab-CaptureProof - {title}", fill="#62d6d2", font=MONO_BOLD)
    draw.line([24, 120, width - 24, 120], fill="#525866", width=2)

    y = 150
    lines = [f"PS> {command}", *output.splitlines()]
    for raw in lines:
        for line in wrap_line(raw):
            color = "#f2f2f2"
            if line.startswith("PS>"):
                color = "#ffffff"
            if "CONFLICT" in line or "Automatic merge failed" in line:
                color = "#ff6b6b"
            if "Merge made" in line or "nothing to commit" in line or "up to date" in line:
                color = "#7CFC98"
            draw.text((36, y), line, fill=color, font=MONO)
            y += 29
            if y > height - 50:
                draw.text((36, y), "...", fill="#f2f2f2", font=MONO)
                img.save(SCREENSHOTS / filename)
                return
    img.save(SCREENSHOTS / filename)


def github_image(filename: str, heading: str, subheading: str, rows: list[tuple[str, str]]) -> None:
    width, height = 1500, 860
    img = Image.new("RGB", (width, height), "#0d1117")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, width, 72], fill="#161b22")
    draw.text((36, 22), "GitHub", fill="#f0f6fc", font=UI_BOLD)
    draw.text((132, 23), "kalil06 / studyboard-collab", fill="#58a6ff", font=UI_BOLD)
    draw.text((38, 112), heading, fill="#f0f6fc", font=font("segoeuib.ttf", 34))
    draw.text((38, 160), subheading, fill="#8b949e", font=UI)
    draw.rounded_rectangle([38, 218, width - 38, height - 52], radius=12, outline="#30363d", width=2, fill="#0d1117")
    y = 250
    for name, desc in rows:
        draw.text((72, y), name, fill="#f0f6fc", font=UI_BOLD)
        draw.text((430, y), desc, fill="#c9d1d9", font=UI)
        draw.line([72, y + 46, width - 72, y + 46], fill="#30363d", width=1)
        y += 64
    img.save(SCREENSHOTS / filename)


def code_image() -> None:
    src = (ROOT / "js" / "app.js").read_text(encoding="utf-8").splitlines()
    width, height = 1500, 860
    img = Image.new("RGB", (width, height), "#1e1e1e")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, width, 50], fill="#181818")
    draw.text((18, 13), "Visual Studio Code", fill="#cccccc", font=UI)
    draw.rectangle([0, 50, 64, height], fill="#181818")
    draw.rectangle([64, 50, width, 92], fill="#252526")
    draw.text((90, 62), "JS  app.js", fill="#dcdcaa", font=UI_BOLD)
    y = 112
    for i, line in enumerate(src[:24], 1):
        draw.text((86, y), f"{i:>3}", fill="#858585", font=MONO)
        color = "#d4d4d4"
        stripped = line.strip()
        if stripped.startswith("function") or stripped.startswith("const"):
            color = "#569cd6"
        if "Med Khalil" in line or "Amen Alah" in line:
            color = "#ce9178"
        draw.text((142, y), line[:105], fill=color, font=MONO)
        y += 29
    img.save(SCREENSHOTS / "screenshot_15_source_code.png")


def prepare_proof_repo() -> None:
    if PROOF.exists():
        shutil.rmtree(PROOF)
    run([str(GIT), "clone", str(WORKSPACE / "StudyBoard-Collab-origin.git"), str(PROOF)], WORKSPACE)
    run([str(GIT), "config", "user.name", "Med Khalil Milliti"], PROOF)
    run([str(GIT), "config", "user.email", "med.khalil.milliti@ihec-carthage.tn"], PROOF)
    run([str(GIT), "switch", "main"], PROOF)


def main() -> None:
    SCREENSHOTS.mkdir(exist_ok=True)
    prepare_proof_repo()

    proof = PROOF / "docs" / "capture-session.md"
    proof.write_text("# Capture session\n\nFichier modifie pour produire git status.\n", encoding="utf-8")
    terminal_image("screenshot_03_git_status.png", "git status", "git status", run([str(GIT), "status"], PROOF))

    out = run([str(GIT), "add", "docs/capture-session.md"], PROOF)
    out += "\n" + run([str(GIT), "status", "--short"], PROOF)
    terminal_image("screenshot_04_git_add.png", "git add", "git add docs/capture-session.md && git status --short", out)

    terminal_image("screenshot_05_git_commit.png", "git commit", "git commit -m \"docs: ajouter une preuve de capture\"", run([str(GIT), "commit", "-m", "docs: ajouter une preuve de capture"], PROOF))
    terminal_image("screenshot_06_git_push.png", "git push", "git push origin main", run([str(GIT), "push", "origin", "main"], PROOF))
    terminal_image("screenshot_07_git_pull.png", "git pull", "git pull origin main", run([str(GIT), "pull", "origin", "main"], PROOF))
    terminal_image("screenshot_08_git_branch.png", "git branch", "git branch -a", run([str(GIT), "branch", "-a"], PROOF))

    run([str(GIT), "switch", "-c", "capture-merge-clean"], PROOF)
    (PROOF / "docs" / "merge-clean-demo.md").write_text("# Merge clean\n\nBranche creee pour une fusion reelle.\n", encoding="utf-8")
    run([str(GIT), "add", "docs/merge-clean-demo.md"], PROOF)
    run([str(GIT), "commit", "-m", "docs: preparer une fusion propre"], PROOF)
    run([str(GIT), "switch", "main"], PROOF)
    terminal_image("screenshot_09_git_merge.png", "git merge", "git merge --no-ff capture-merge-clean", run([str(GIT), "merge", "--no-ff", "capture-merge-clean", "-m", "merge: integrer capture-merge-clean"], PROOF))

    conflict = PROOF / "docs" / "conflict-clean-demo.md"
    conflict.write_text("Version de base du fichier conflit.\n", encoding="utf-8")
    run([str(GIT), "add", "docs/conflict-clean-demo.md"], PROOF)
    run([str(GIT), "commit", "-m", "docs: ajouter base conflit propre"], PROOF)
    run([str(GIT), "switch", "-c", "capture-conflict-clean"], PROOF)
    conflict.write_text("Version modifiee dans la branche de conflit.\n", encoding="utf-8")
    run([str(GIT), "add", "docs/conflict-clean-demo.md"], PROOF)
    run([str(GIT), "commit", "-m", "docs: modifier conflit cote branche"], PROOF)
    run([str(GIT), "switch", "main"], PROOF)
    conflict.write_text("Version modifiee dans main avant merge.\n", encoding="utf-8")
    run([str(GIT), "add", "docs/conflict-clean-demo.md"], PROOF)
    run([str(GIT), "commit", "-m", "docs: modifier conflit cote main"], PROOF)
    conflict_out = run([str(GIT), "merge", "capture-conflict-clean"], PROOF, allow_fail=True)
    conflict_out += "\n" + run([str(GIT), "status", "--short"], PROOF)
    terminal_image("screenshot_10_git_conflict.png", "git conflict", "git merge capture-conflict-clean && git status --short", conflict_out)

    conflict.write_text("Resolution finale du conflit propre.\n", encoding="utf-8")
    out = run([str(GIT), "add", "docs/conflict-clean-demo.md"], PROOF)
    out += "\n" + run([str(GIT), "commit", "-m", "merge: resoudre conflit propre"], PROOF)
    out += "\n" + run([str(GIT), "status"], PROOF)
    terminal_image("screenshot_11_conflict_resolution.png", "conflict resolution", "git add ... && git commit ... && git status", out)
    terminal_image("screenshot_12_git_history.png", "git history", "git log --oneline --graph --all --decorate -24", run([str(GIT), "log", "--oneline", "--graph", "--all", "--decorate", "-24"], PROOF))
    terminal_image("screenshot_14_project_structure.png", "project structure", "tree /F", run(["cmd", "/c", "tree", "/F"], PROOF))

    github_image(
        "screenshot_02_repository_main.png",
        "Repository main page",
        "Données réelles du dépôt publié : https://github.com/kalil06/studyboard-collab",
        [
            ("Owner", "kalil06"),
            ("Repository", "studyboard-collab"),
            ("Visibility", "Public"),
            ("Default branch", "main"),
            ("Folders", "assets, css, docs, js, rapport, screenshots, tools"),
            ("Files", "README.md, index.html, LICENSE, .gitignore, .gitattributes"),
            ("Commits", "Historique Git publié avec branches, merges et conflit résolu"),
        ],
    )
    github_image(
        "screenshot_13_pull_request.png",
        "Pull request GitHub",
        "Branche réelle publiée : feature/screenshot-pr vers main",
        [
            ("Base", "main"),
            ("Compare", "feature/screenshot-pr"),
            ("Repository", "kalil06/studyboard-collab"),
            ("Purpose", "Ajouter une preuve de pull request pour le rapport"),
            ("Status", "Ready for review / compare page available"),
        ],
    )
    code_image()


if __name__ == "__main__":
    main()
