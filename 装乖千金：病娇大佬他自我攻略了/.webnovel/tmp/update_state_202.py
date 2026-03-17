import json
import datetime

# 读取state.json
with open("D:/workspace/小说/装乖千金：病娇大佬他自我攻略了/装乖千金：病娇大佬他自我攻略了/.webnovel/state.json", "r", encoding="utf-8") as f:
    state = json.load(f)

# 1. 更新progress
state["progress"]["current_chapter"] = 202
state["progress"]["total_written_words"] = 324400  # 322200 + 2200
state["progress"]["total_words"] = 312400  # 310200 + 2200
state["progress"]["last_updated"] = "2026-03-17 22:30:00"

# 2. 更新protagonist_state
state["protagonist_state"]["abilities"]["微表情洞察"]["used_today"] = 2
state["protagonist_state"]["abilities"]["微表情洞察"]["remaining"] = 1
state["protagonist_state"]["current_date"] = "2026-11-15"
state["protagonist_state"]["location"] = "城郊疗养院"

# 3. 新增intel
new_intel = [
    "王护士愿意出面作证，已获取证词",
    "沈家二房给沈婉清送黑色药丸导致中毒",
    "获得关键证物：黑色药丸（沈家二房送的'补品'）",
    "威胁王护士的是沈家二房管家",
    "祭祖大典倒计时D-10"
]
for intel in new_intel:
    if intel not in state["protagonist_state"]["intel"]:
        state["protagonist_state"]["intel"].append(intel)

# 4. 添加chapter_meta for 0202
chapter_meta_202 = {
    "hook": {
        "type": "悬念钩",
        "content": "黑色药丸的真相是什么？沈家二房的毒药阴谋即将揭露",
        "strength": "strong"
    },
    "pattern": {
        "opening": "场景描写开场",
        "hook": "悬念钩+信息爽点",
        "emotion_rhythm": "紧张→真诚→突破→震撼",
        "info_density": "high",
        "strand_type": "Quest"
    },
    "ending": {
        "time": "2026年11月15日下午",
        "location": "城郊疗养院",
        "emotion": "获得关键证物和证词，真相即将大白"
    }
}

# 修复0201的格式（如果是嵌套格式）
if "0201" in state["chapter_meta"]:
    if "0201" in state["chapter_meta"]["0201"]:
        # 修复嵌套格式
        state["chapter_meta"]["0201"] = state["chapter_meta"]["0201"]["0201"]

# 添加202章的meta
state["chapter_meta"]["0202"] = chapter_meta_202

# 保存更新后的state.json
with open("D:/workspace/小说/装乖千金：病娇大佬他自我攻略了/装乖千金：病娇大佬他自我攻略了/.webnovel/state.json", "w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

print("state.json updated successfully!")
print(f"Current chapter: {state['progress']['current_chapter']}")
print(f"Total words: {state['progress']['total_written_words']}")
print(f"Abilities used today: {state['protagonist_state']['abilities']['微表情洞察']['used_today']}")
print(f"Chapter 202 meta added: {'0202' in state['chapter_meta']}")
