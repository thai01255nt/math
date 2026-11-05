# Agent Manager (WSL2 + tmux)
[agent-manager](https://github.com/wainmann/agent-manager): run many agent CLIs (Claude Code, Codex, ...) side by side in tmux.

## Install
Requires tmux 3.1+ and git (the script checks and offers to install them). Binary goes to `~/.local/bin`.
```
curl -fsSL -o install.sh https://raw.githubusercontent.com/wainmann/agent-manager/main/install.sh && sh install.sh
rm install.sh
# update later
agent-manager update
```

## Settings
Change in the UI (`s` -> Settings) or from a shell:
```
agent-manager settings list
agent-manager settings set theme paper
agent-manager settings set theme_auto on
agent-manager settings set background theme
agent-manager settings set worktree_default on
agent-manager settings set notify_finished on
```
Backup / restore settings (incl. custom keybindings and `notify_command`) as JSON, saved in [dotfiles/agent-manager.settings.json](../agent-manager.settings.json):
```
agent-manager export --settings dotfiles/agent-manager.settings.json
agent-manager import --settings dotfiles/agent-manager.settings.json
```
Import merges by key; `notify_command` has the Windows user (`thai0`) hard-coded. Do not commit a full export / `--connections` (may contain secrets).

## Keybindings
UI: Settings -> Keybindings (press a key to rebind, `Reset keys` for defaults).
They are not available via `settings set`; edit them through export/import (`keybindings.list` = session list, `keybindings.session` = inside a session):
```
"keybindings.list": "{\"filter\":[\"ctrl+f\"],\"step_in\":[\"ctrl+l\"],\"step_out\":[\"ctrl+h\"]}",
"keybindings.session": "{\"detach\":[\"ctrl+h\"]}"
```
- `filter` (default `w`): attention filter, show only sessions that are waiting / finished / errored
- `/`: search by text (only backspace works in the search box; ctrl+w / alt+backspace / ctrl+u do nothing in v0.46)

## Worktree
With `worktree_default on`, every new session (quick prompt included) gets its own git worktree and branch:
```
<parent of repo>/<repo>-worktrees/<session-name>   # branch: am/<session-name>
```
- Toggle per spawn in the new session / quick prompt form with `alt+w`
- Groups can have their own worktree default
- Branches stay local (no push); clean up leftovers with `git worktree list` / `git worktree remove <path>` / `git branch -D am/<name>`

## Alert sound (WSL)
agent-manager runs `notify_command` on every notification. Play a custom wav through Windows:

1. Download a sound into the Windows Music folder (Mixkit, free, no attribution).
   Others: https://mixkit.co/free-sound-effects/notification/ , direct wav = `https://assets.mixkit.co/active_storage/sfx/<id>/<id>.wav`
```
WINUSER=$(cmd.exe /c "echo %USERNAME%" 2>/dev/null | tr -d '\r')
D=/mnt/c/Users/$WINUSER/Music/agent-sounds
mkdir -p $D
# 931 = Service bell, 2320 = Guitar notification alert
curl -sSf -o $D/service-bell.wav https://assets.mixkit.co/active_storage/sfx/931/931.wav
```
2. (optional) Lower the volume, `SoundPlayer` has no volume option so make a quieter copy (0.2 = 20%, about -14 dB; 0.5 still sounds loud):
```
python3 - $D/service-bell.wav $D/service-bell-20.wav 0.2 <<'EOF'
import sys, wave, array
src, dst, factor = sys.argv[1], sys.argv[2], float(sys.argv[3])
with wave.open(src) as w:
    p = w.getparams(); assert p.sampwidth == 2
    a = array.array('h', w.readframes(p.nframes))
for i, v in enumerate(a):
    a[i] = max(-32768, min(32767, int(v * factor)))
with wave.open(dst, 'wb') as w:
    w.setparams(p); w.writeframes(a.tobytes())
EOF
```
3. Install the notify scripts from [dotfiles/agent-manager](../agent-manager) (paths inside use the Windows user `thai0`, change if different):
   - `am-notify`: the `notify_command`; shows a **silent** Windows toast (title/body from agent-manager) and plays the wav
   - `am-notify.ps1`: the PowerShell part (lives on the Windows side next to the sounds)
   - `powershell.exe`: wrapper that drops agent-manager's built-in toast (it always plays `Notification.Default`, no setting to turn it off); every other `powershell.exe` call passes through. Works because `~/.local/bin` comes before the Windows dirs in PATH
```
cp dotfiles/agent-manager/am-notify dotfiles/agent-manager/powershell.exe ~/.local/bin/
cp dotfiles/agent-manager/am-notify.ps1 $D/
agent-manager settings set notify_command "$HOME/.local/bin/am-notify"
# test (should show 1 toast + 1 bell)
AM_TITLE="agent-manager test" AM_BODY="hello" ~/.local/bin/am-notify
# debug: log AM_* env and PowerShell output
agent-manager settings set notify_command "AM_NOTIFY_LOG=$HOME/.cache/am-notify.log $HOME/.local/bin/am-notify"
# other sound: AM_NOTIFY_SOUND='C:\Users\thai0\Music\agent-sounds\xxx.wav' in front of the command
# undo
agent-manager settings set notify_command ''
rm ~/.local/bin/powershell.exe
```
Env passed to `notify_command`: `AM_NOTIFY_KIND` (waiting / finished / ...), `AM_TITLE`, `AM_BODY`, `AM_SESSION_NAME`, `AM_SESSION_ID`, `AM_TOOL`, `AM_CWD`, `AM_BRANCH`.
Keep `notifications on` in agent-manager, otherwise `notify_command` does not run either.
In Windows Settings -> System -> Notifications: keep **Windows PowerShell** banners on (the toast comes from there).

### Remove the default Windows beep
The default "ding" is the terminal bell (tmux passes bells from every session, `bell-action any`), not the toast.
agent-manager uses the default tmux server, so stop tmux from forwarding bells (already in `dotfiles/tmux/tmux.conf`):
```
set -g bell-action none
# apply now without restarting tmux
tmux set -g bell-action none
```
Only affects tmux; bells outside tmux still beep.
Alternative (all Windows Terminal tabs): Settings -> Defaults -> Advanced -> Bell notification style -> uncheck Audible (`"bellStyle": ["window", "taskbar"]`).
