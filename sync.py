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

def get_solved_problems():
    query = {
        "query": """
        query {
            allQuestionsCount { difficulty count }
            matchedUser(username: "") {
                submitStats {
                    acSubmissionNum { difficulty count }
                }
            }
        }
        """
    }
    # Get list of AC problems via problems/all API
    response = requests.get(
        "https://leetcode.com/api/problems/all/",
        headers=headers,
        timeout=15
    )
    print("First problem raw:", data["stat_status_pairs"][0])
    print(f"Total problems fetched: {len(data.get('stat_status_pairs', []))}")
    statuses = set(p.get("status") for p in data.get("stat_status_pairs", []))
    print(f"Statuses found: {statuses}")
    solved = []
    for p in data.get("stat_status_pairs", []):
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
                    timestamp
                    statusDisplay
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
        print(f"  Error getting submission list: {e}, response: {data}")
        return None, None

    # Get code
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
        code = data2["data"]["submissionDetails"]["code"]
        return code, lang
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

        # Check if any file already exists for this problem
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
        print(f"  Saved {filepath} ({lang})")
        time.sleep(2)

if __name__ == "__main__":
    main()
