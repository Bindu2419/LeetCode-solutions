import os
import time
import requests
import pathlib

LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")
LEETCODE_CSRF_TOKEN = os.environ.get("LEETCODE_CSRF_TOKEN")

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://leetcode.com",
    "x-csrftoken": LEETCODE_CSRF_TOKEN,
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={LEETCODE_CSRF_TOKEN}",
}

EXTENSIONS = {
    "java": "java", "python": "py", "python3": "py",
    "cpp": "cpp", "c": "c", "javascript": "js",
    "typescript": "ts", "kotlin": "kt", "swift": "swift",
    "go": "go", "rust": "rs",
}

os.system('git config user.name "Bindu2419"')
os.system('git config user.email "binduchinta0@gmail.com"')

def get_solved_problems():
    response = requests.get(
        "https://leetcode.com/api/problems/all/",
        headers=headers,
        timeout=15
    )
    data = response.json()
    pairs = data.get("stat_status_pairs", [])
    print(f"Total problems fetched: {len(pairs)}")
    solved = []
    for p in pairs:
        if p.get("status") == "ac":
            solved.append({
                "id": p["stat"]["frontend_question_id"],
                "title": p["stat"]["question__title"],
                "slug": p["stat"]["question__title_slug"],
            })
    return solved

def get_submission_code(slug):
    query = {
        "query": """
        query ($slug: String!, $offset: Int!, $limit: Int!) {
            questionSubmissionList(questionSlug: $slug, offset: $offset, limit: $limit, status: 10) {
                submissions {
                    id
                    lang
                }
            }
        }
        """,
        "variables": {"slug": slug, "offset": 0, "limit": 5}
    }
    r = requests.post("https://leetcode.com/graphql", json=query, headers=headers, timeout=15)
    data = r.json()
    try:
        subs = data["data"]["questionSubmissionList"]["submissions"]
        if not subs:
            return None, None
        sub_id = subs[0]["id"]
        lang = subs[0]["lang"]
    except Exception as e:
        print(f"  Error: {e}, response: {data}")
        return None, None

    query2 = {
        "query": """
        query ($id: Int!) {
            submissionDetails(submissionId: $id) {
                code
            }
        }
        """,
        "variables": {"id": int(sub_id)}
    }
    r2 = requests.post("https://leetcode.com/graphql", json=query2, headers=headers, timeout=15)
    data2 = r2.json()
    try:
        return data2["data"]["submissionDetails"]["code"], lang
    except Exception as e:
        print(f"  Error getting code: {e}")
        return None, None

def main():
    print("Fetching solved problems...")
    solved = get_solved_problems()
    print(f"Found {len(solved)} solved problems")

    for problem in solved:
        slug = problem["slug"]
        folder = f"Java-Solutions/{slug}"
        if os.path.exists(folder) and os.listdir(folder):
            print(f"Skipping {slug} (already exists)")
            continue
        print(f"Syncing: {problem['title']}...")
        code, lang = get_submission_code(slug)
        if not code:
            print(f"  Could not get code for {slug}")
            time.sleep(1)
            continue
        ext = EXTENSIONS.get(lang, lang)
        pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
        filepath = f"{folder}/{slug}.{ext}"
        with open(filepath, "w") as f:
            f.write(code)
        os.system(f'git add -A')
        os.system(f'git commit -m "Sync LeetCode: {problem["title"]}"')
        print(f"  Saved and committed {filepath} ({lang})")
        time.sleep(2)
    
    os.system('git push origin main')
    print("Done!")

if __name__ == "__main__":
    main()
