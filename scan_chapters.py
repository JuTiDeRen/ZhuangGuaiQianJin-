import os
import re
import glob

def scan_chapters(directory):
    files = sorted(glob.glob(os.path.join(directory, "*.md")))
    results = []
    
    sensitive_words = ["血腥", "自杀", "毒品", "色情", "强暴", "滥交", "赌博", "高利贷", "恐怖", "邪教"]
    emotional_markers = ["！", "？"]
    
    print("| 章节 | 字数 | 敏感词命中 | 情绪标点密度 | 场景切换次数 |")
    print("|---|---|---|---|---|")
    
    for file_path in files:
        filename = os.path.basename(file_path)
        chapter_match = re.search(r"第(\d+)章", filename)
        if not chapter_match:
            continue
            
        chapter_num = chapter_match.group(1)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        word_count = len(content)
        
        sensitive_hits = []
        for word in sensitive_words:
            if word in content:
                sensitive_hits.append(word)
        
        emotional_count = sum(content.count(m) for m in emotional_markers)
        emotional_density = round((emotional_count / word_count) * 1000, 2) if word_count > 0 else 0
        
        scene_breaks = content.count("---") + content.count("——")
        
        sensitive_str = ", ".join(sensitive_hits) if sensitive_hits else "无"
        
        print(f"| {chapter_num} | {word_count} | {sensitive_str} | {emotional_density} | {scene_breaks} |")
        
        results.append({
            "chapter": chapter_num,
            "word_count": word_count,
            "sensitive": sensitive_hits,
            "emotional_density": emotional_density,
            "scene_breaks": scene_breaks
        })
        
    return results

if __name__ == "__main__":
    directory = r"d:\workspace\小说\装乖千金：病娇大佬他自我攻略了\装乖千金：病娇大佬他自我攻略了\正文"
    scan_chapters(directory)
