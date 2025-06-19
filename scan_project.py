import os

ESSENTIAL_FILES = {
    "app.py",
    "mexc_liquidation_fetcher.py",
    "core/ai/recovery_flow.py",
    "templates/quantum_dashboard.html",
    "templates/recovery_flow.html",
    "templates/liquidation-tracker.html"
}

def scan_project(base_path="."):
    all_files = []
    netfa = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            full_path = os.path.relpath(os.path.join(root, file), base_path)
            if "__pycache__" in full_path or file.endswith(".pyc") or file.endswith(".log"):
                netfa.append(full_path)
            elif full_path not in ESSENTIAL_FILES:
                netfa.append(full_path)
            all_files.append(full_path)

    print("✅ جميع الملفات:")
    for f in all_files:
        print("-", f)

    print("\n🗑️ ملفات يُحتمل حذفها (نتفة):")
    for f in netfa:
        print("🗑️", f)

if __name__ == "__main__":
    scan_project()
