import os
import time
import requests
import pathlib

LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")
LEETCODE_CSRF_TOKEN = os.environ.get("LEETCODE_CSRF_TOKEN")

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://leetcode.com",
    "x-csrftoken": LEETCODE_CSRF_TOKEN,
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={LEETCODE_CSRF_TOKEN}",
}

EXTENSIONS = {
    "java": "java",
    "python": "py",
    "python3": "py",
    "cpp": "cpp",
    "c": "c",
    "javascript": "js",
    "typescript": "ts",
    "kotlin": "kt",
    "swift": "swift",
    "go": "go",
    "rust": "rs",
}

def get_accepted_submissions():
    submissions = []
    offset = 0
    while True:
        query = {
            "query": """
            query submissionList($offset: Int!, $limit: Int!) {
                submissionList(offset: $offset, limit: $limit) {
                    submissions {
                        id
                        title
                        titleSlug
                        statusDisplay
                        lang
                        timestamp
                    }
                }
            }
            """,
            "variables": {"offset": offset, "limit": 20}
        }
        response = requests.post("https://leetcode.com/graphql", json=query, headers=headers)
        data = response.json()
        try:
            batch = data["data"]["submissionList"]["submissions"]
        except:
            print("Failed to fetch submissions:", data)
            break
        if not batch:
            break
        for s in batch:
            if s["statusDisplay"] == "Accepted":
                submissions.append(s)
        offset += 20
        time.sleep(1)
    return submissions

def get_submission_code(submission_id):
    query = {
        "query": """
        query submissionDetails($submissionId: Int!) {
            submissionDetails(submissionId: $submissionId) {
                code
            }
        }
        """,
        "variables": {"submissionId": int(submission_id)}
    }
    response = requests.post("https://leetcode.com/graphql", json=query, headers=headers)
    data = response.json()
    try:
        return data["data"]["submissionDetails"]["code"]
    except:
        return None

def main():
    print("Fetching accepted submissions...")
    submissions = get_accepted_submissions()
    print(f"Found {len(submissions)} accepted submissions")

    seen = set()
    for sub in submissions:
        slug = sub["titleSlug"]
        if slug in seen:
            continue
        seen.add(slug)

        lang = sub["lang"]
        ext = EXTENSIONS.get(lang, lang)
        folder = f"Java-Solutions/{slug}"
        filepath = f"{folder}/{slug}.{ext}"

        if os.path.exists(filepath):
            print(f"Skipping {slug} (already exists)")
            continue

        print(f"Syncing {sub['title']} ({lang})...")
        code = get_submission_code(sub["id"])
        if not code:
            print(f"Could not get code for {slug}")
            continue

        pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(code)
        print(f"Saved {filepath}")
        time.sleep(1)

if __name__ == "__main__":
    main()
