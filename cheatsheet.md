
# Talon HUD Voice Command Cheatsheet

A quick reference for all voice commands and available values in the Talon HUD repository. Optimized for wide screens.

---

## General HUD Commands

| Command               | Description       | Command                       | Description        |
| --------------------- | ----------------- | ----------------------------- | ------------------ |
| head up show / open   | Show the HUD      | head up hide / close          | Hide the HUD       |
| head up theme {theme} | Switch theme      | head up drop / stop / confirm | Confirm/stop setup |
| head up cancel        | Cancel setup mode |                               |                    |


## Widget Control (replace `{widget}` with a widget name)

**Available widgets:**

| ability_bar | choices        | context_menu | cursor_tracker | documentation |
| ----------- | -------------- | ------------ | -------------- | ------------- |
| event_log   | screen_overlay | status_bar   | text_panel     | walkthrough   |

| Command                                             | Description      | Command                        | Description     |
| --------------------------------------------------- | ---------------- | ------------------------------ | --------------- |
| head up show/open {widget}                          | Show a widget    | head up hide/close {widget}    | Hide a widget   |
| head up resize {widget}                             | Resize widget    | head up expand {widget}        | Expand widget   |
| head up text scale {widget}                         | Change text size | head up drag {widget}          | Drag widget     |
| head up basic {widget}                              | Basic animation  | head up fancy {widget}         | Fancy animation |
| head up hide {widget} on sleep                      | Hide on sleep    | head up show {widget} on sleep | Show on sleep   |
| head up align {widget} right/left/center/top/bottom | Align widget     |                                |                 |

## Widget Content

| Command            | Description         | Command                | Description           |
| ------------------ | ------------------- | ---------------------- | --------------------- |
| {widget} show/open | Show widget         | {widget} hide/close    | Hide widget           |
| {widget} minimize  | Minimize widget     | {widget} maximize      | Maximize widget       |
| {widget} next      | Next page/content   | {widget} back/previous | Previous page/content |
| {widget} options   | Show widget options |                        |                       |

## Focus Commands

| Command                       | Description       | Command                    | Description        |
| ----------------------------- | ----------------- | -------------------------- | ------------------ |
| head up focus / focus head up | Focus the HUD     | head up blur               | Remove focus       |
| head up enable auto focus     | Enable auto focus | head up disable auto focus | Disable auto focus |

## Development/Debug

| Command                   | Description    | Command                  | Description   |
| ------------------------- | -------------- | ------------------------ | ------------- |
| head up development start | Start dev mode | head up development stop | Stop dev mode |

---


## Lists and Captures

### Themes (`{theme}`)

| dark | light | (custom themes) |
| ---- | ----- | --------------- |

### Numerical Choices (for options, e.g. "option one", "option twenty three")

| one | two | three | ... | one hundred |
| --- | --- | ----- | --- | ----------- |

---

**Tip:**
- You can use the command **toolkit lists** to see all available lists in your Talon environment.
- For more advanced or custom commands, check your `.talon` files or the documentation in the repo.

### Themes (`{theme}`)
- dark
- light
- (any custom themes you have added)

### Numerical Choices (for options, e.g. "option one", "option twenty three")
- one, two, three, ... up to one hundred

---

**Tip:**
- You can use the command **toolkit lists** to see all available lists in your Talon environment.
- For more advanced or custom commands, check your `.talon` files or the documentation in the repo.
