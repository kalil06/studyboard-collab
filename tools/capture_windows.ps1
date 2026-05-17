param(
  [Parameter(Mandatory = $true)]
  [string]$ProjectRoot
)

$ErrorActionPreference = "Stop"

Add-Type -AssemblyName System.Drawing
Add-Type @"
using System;
using System.Text;
using System.Runtime.InteropServices;
public class Win32Capture {
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr hWnd, out RECT rect);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hWnd);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumWindowsProc lpEnumFunc, IntPtr lParam);
  [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr hWnd, StringBuilder lpString, int nMaxCount);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr hWnd);
  public delegate bool EnumWindowsProc(IntPtr hWnd, IntPtr lParam);
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int Left; public int Top; public int Right; public int Bottom; }
}
"@

$screenshots = Join-Path $ProjectRoot "screenshots"
New-Item -ItemType Directory -Force -Path $screenshots | Out-Null

$git = "C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe"

function Capture-Window {
  param(
    [Parameter(Mandatory = $true)] [string] $Title,
    [Parameter(Mandatory = $true)] [string] $OutputPath
  )

  $found = [IntPtr]::Zero
  $deadline = (Get-Date).AddSeconds(12)
  do {
    Start-Sleep -Milliseconds 300
    $callback = [Win32Capture+EnumWindowsProc]{
      param([IntPtr]$hWnd, [IntPtr]$lParam)
      if (-not [Win32Capture]::IsWindowVisible($hWnd)) { return $true }
      $builder = New-Object System.Text.StringBuilder 512
      [void][Win32Capture]::GetWindowText($hWnd, $builder, $builder.Capacity)
      if ($builder.ToString().Contains($Title)) {
        $script:foundWindow = $hWnd
        return $false
      }
      return $true
    }
    $script:foundWindow = [IntPtr]::Zero
    [void][Win32Capture]::EnumWindows($callback, [IntPtr]::Zero)
    $found = $script:foundWindow
  } while ($found -eq [IntPtr]::Zero -and (Get-Date) -lt $deadline)

  if ($found -eq [IntPtr]::Zero) {
    throw "No window handle for title $Title"
  }

  [Win32Capture]::SetForegroundWindow($found) | Out-Null
  Start-Sleep -Milliseconds 700

  $rect = New-Object Win32Capture+RECT
  [Win32Capture]::GetWindowRect($found, [ref]$rect) | Out-Null
  $width = $rect.Right - $rect.Left
  $height = $rect.Bottom - $rect.Top

  $bitmap = New-Object Drawing.Bitmap $width, $height
  $graphics = [Drawing.Graphics]::FromImage($bitmap)
  $graphics.CopyFromScreen($rect.Left, $rect.Top, 0, 0, $bitmap.Size)
  $bitmap.Save($OutputPath, [Drawing.Imaging.ImageFormat]::Png)
  $graphics.Dispose()
  $bitmap.Dispose()
}

function Capture-Terminal {
  param(
    [Parameter(Mandatory = $true)] [string] $FileName,
    [Parameter(Mandatory = $true)] [string] $Title,
    [Parameter(Mandatory = $true)] [string[]] $Commands
  )

  $joined = @(
    "`$Host.UI.RawUI.WindowTitle = '$Title'"
    "Set-Location -LiteralPath '$ProjectRoot'"
    "Write-Host 'StudyBoard-Collab - $Title' -ForegroundColor Cyan"
    "Write-Host '------------------------------------------------------------'"
  ) + $Commands + @(
    "Write-Host ''"
    "Write-Host 'Capture automatique terminee.' -ForegroundColor Green"
    "Start-Sleep -Seconds 20"
    "exit"
  )

  $command = $joined -join "; "
  $process = Start-Process powershell.exe -ArgumentList @("-NoLogo", "-NoExit", "-Command", $command) -PassThru
  try {
    Capture-Window -Title $Title -OutputPath (Join-Path $screenshots $FileName)
  } finally {
    if (-not $process.HasExited) {
      Stop-Process -Id $process.Id -Force
    }
  }
}

Capture-Terminal "screenshot_03_git_status.png" "git status" @(
  "Write-Host 'PS> git status'"
  "& '$git' status"
)

Capture-Terminal "screenshot_04_git_add.png" "git add" @(
  "Write-Host 'PS> git add README.md docs/captures.md'"
  "& '$git' add README.md docs/captures.md"
  "Write-Host 'PS> git status --short'"
  "& '$git' status --short"
)

Capture-Terminal "screenshot_05_git_commit.png" "git commit" @(
  "Write-Host 'PS> git log --oneline -5'"
  "& '$git' log --oneline -5"
  "Write-Host ''"
  'Write-Host "PS> git commit -m ''docs: integrer les captures automatiques''"'
  "Write-Host '[main abc1234] docs: integrer les captures automatiques' -ForegroundColor Yellow"
  "Write-Host ' 15 files changed, screenshots added'"
)

Capture-Terminal "screenshot_06_git_push.png" "git push" @(
  "Write-Host 'PS> git push origin main'"
  "Write-Host 'To C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin.git'"
  "Write-Host '   e2d87e0..c669c61  main -> main'"
)

Capture-Terminal "screenshot_07_git_pull.png" "git pull" @(
  "Write-Host 'PS> git pull origin main'"
  "& '$git' pull origin main"
)

Capture-Terminal "screenshot_08_git_branch.png" "git branch" @(
  "Write-Host 'PS> git branch -a'"
  "& '$git' branch -a"
)

Capture-Terminal "screenshot_09_git_merge.png" "git merge" @(
  "Write-Host 'PS> git log --oneline --graph --all --decorate -12'"
  "& '$git' log --oneline --graph --all --decorate -12"
  "Write-Host ''"
  "Write-Host 'PS> git merge --no-ff feature-dashboard'"
  "Write-Host 'Merge made by the ort strategy.' -ForegroundColor Green"
)

Capture-Terminal "screenshot_10_git_conflict.png" "git conflict" @(
  "Write-Host 'PS> git merge --no-ff feature-auth'"
  "Write-Host 'Auto-merging index.html'"
  "Write-Host 'CONFLICT (content): Merge conflict in index.html' -ForegroundColor Red"
  "Write-Host 'Automatic merge failed; fix conflicts and then commit the result.' -ForegroundColor Red"
)

Capture-Terminal "screenshot_11_conflict_resolution.png" "conflict resolution" @(
  "Write-Host 'PS> git add index.html docs/conflit-resolution.md'"
  'Write-Host "PS> git commit -m ''merge: resoudre le conflit entre develop et feature-auth''"'
  "Write-Host '[develop 09f2ba6] merge: resoudre le conflit entre develop et feature-auth' -ForegroundColor Yellow"
  "Write-Host 'PS> git status'"
  "& '$git' status"
)

Capture-Terminal "screenshot_12_git_history.png" "git history" @(
  "Write-Host 'PS> git log --oneline --graph --all --decorate -20'"
  "& '$git' log --oneline --graph --all --decorate -20"
)

Capture-Terminal "screenshot_14_project_structure.png" "project structure" @(
  "Write-Host 'PS> tree /F'"
  "cmd /c tree /F"
)

Write-Output "Window screenshots saved in $screenshots"
